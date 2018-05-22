from argparse import Namespace

from locust import runners

import mystic as locustfile


options = Namespace()
options.host = "http://localhost"
options.num_clients = 10
options.hatch_rate = options.num_clients
options.num_requests = options.num_clients * 10

runners.locust_runner = runners.LocalLocustRunner([locustfile.MysticLocust], options)
runners.locust_runner.start_hatching(wait=True)
runners.locust_runner.greenlet.join()

for name, value in runners.locust_runner.stats.entries.items():
    print(name,
          value.min_response_time,
          value.median_response_time,
          value.max_response_time,
          value.total_rps)