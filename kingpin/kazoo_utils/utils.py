#!/usr/bin/python
#
# Copyright 2016 Pinterest, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import socket


hostname = socket.gethostname()


def _escape_path_for_stats_name(path):
    # Do some formatting the file path.
    if path is None:
        return None
    if path.startswith("/"):
        path = path[1:]
    return path.replace("/", "_")


class DummyStatsdClient:
    def __init__(self, *args, **kwargs):
        pass

    def increment(self, stats, sample_rate=1, tags={}):
        pass

    def gauge(self, stats, value, sample_rate=1, tags={}):
        pass


dummy_statsd = DummyStatsdClient()
