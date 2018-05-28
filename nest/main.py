from optparse import OptionParser
from configure import make_config, save_config
from nest import collect_tasksets
from locust import TaskSet, HttpLocust, run_locust, parse_options
import sys


def create_parser():
    """Create parser object used for defining all options for Locust.

    Returns:
        OptionParser: OptionParser object used in *parse_options*.
    """

    # Initialize
    parser = OptionParser(usage="nest [options] Locust options")

    parser.add_option(
        '--configure',
        action='store_true',
        dest='configure',
        default=False,
        help="Generate config file using helper."
    )

    parser.add_option(
        '--config_file',
        action='store',
        dest='config_file',
        default='config.json',
        help="Specify config file location."
    )

    parser.add_option(
        '-T', '--taskset_dir',
        action='store',
        dest='taskset_dir',
        default=None,
        help="Specify directory containing TaskSets."
    )

    # Version number (optparse gives you:version but we have to do it
    # ourselves to get -V too. sigh)
    parser.add_option(
        '-V', '--version',
        action='store_true',
        dest='show_version',
        default=False,
        help="show program's version number and exit"
    )
    return parser


def parse_nest_options(args=sys.argv):
    """
    Handle command-line options with optparse.OptionParser.

    Return list of arguments, largely for use in `parse_arguments`.
    """
    parser = create_parser()
    # Return tuple of the output from parse_args (opt obj, args)
    opts, args = parser.parse_args(args)
    return opts, args


def main(sys_args):
    nest_opts, nest_args = parse_nest_options(sys_args[1:])
    if nest_opts.configure:
        save_config(make_config(nest_opts.taskset_dir), nest_opts.config_file)

    class NestTaskSet(TaskSet):
        """TaskSet containing all the sub-tasksets contained
        in the specified directory.

        Arguments:
            TaskSet {class} -- TaskSet class from Locust.

        """
        tasks = collect_tasksets(dir_path=nest_opts.taskset_dir)

    class NestLocust(HttpLocust):
        """HttpLocust using the NestTaskSet.

        Arguments:
            HttpLocust {class} -- HttpLocust from Locust.

        """
        task_set = NestTaskSet

    _, locust_opts, locust_args = parse_options(nest_args)
    locust_opts.locust_classes = [NestLocust]
    run_locust(locust_opts, locust_args)

if __name__ == "__main__":
    main(sys.argv)
