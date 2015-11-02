# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import with_statement

from libcloud.common.cloudstack import CloudStackDriverMixIn
from libcloud.common.cloudstack import CloudStackConnection
from libcloud.compute.providers import Provider
from libcloud.compute.drivers.cloudstack import CloudStackNodeDriver
from urlparse import urlparse

__all__ = [
    'InterouteNodeDriver'
]


class InterouteConnection(CloudStackConnection):
    def add_default_params(self, params):
        params['apiKey'] = self.user_id
        params['response'] = 'json'
        params['region'] = InterouteDriverMixIn.region
        super(InterouteConnection, self).add_default_params(params=params)
        return params


class InterouteDriverMixIn(CloudStackDriverMixIn):
    host = None
    path = None
    region = None

    connectionCls = InterouteConnection

    def __init__(self, key, secret=None,
                 secure=True, host=None,
                 port=None, region=None):
        host = host or self.host
        InterouteDriverMixIn.region = region or self.region
        super(InterouteDriverMixIn, self).__init__(key, secret, secure, host,
                                                   port)

    def _sync_request(self, command, action=None, params=None, data=None,
                      headers=None, method='GET'):
        return self.connection._sync_request(command=command, action=action,
                                             params=params, data=data,
                                             headers=headers, method=method)

    def _async_request(self, command, action=None, params=None, data=None,
                       headers=None, method='GET', context=None):
        return self.connection._async_request(command=command, action=action,
                                              params=params, data=data,
                                              headers=headers, method=method,
                                              context=context)


class InterouteNodeDriver(CloudStackNodeDriver, InterouteDriverMixIn):
    type = 'interoute'
    name = 'interoute'
    api_name = 'interoute'
    website = 'http://www.interoute.com/'

    def __init__(self, key, secret=None, secure=True, host=None,
                 path=None, port=None, url=None, *args, **kwargs):
        if url:
            parsed = urlparse.urlparse(url)

            path = parsed.path

            scheme = parsed.scheme
            split = parsed.netloc.split(':')

            if len(split) == 1:
                # No port provided, use the default one
                host = parsed.netloc
                port = 443 if scheme == 'https' else 80
            else:
                host = split[0]
                port = int(split[1])
        else:
            host = host if host else self.host
            path = path if path else self.path

        if path is not None:
            self.path = path

        if host is not None:
            self.host = host

        if (self.type == Provider.CLOUDSTACK) and (not host or not path):
            raise Exception('When instantiating CloudStack driver directly '
                            'you also need to provide url or host and path '
                            'argument')

        region = kwargs.get('region', None)
        if region is not None:
            self.region = region

        super(InterouteNodeDriver, self).__init__(key=key,
                                                  secret=secret,
                                                  secure=secure,
                                                  host=host,
                                                  port=port)
