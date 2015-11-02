# libcloud-interoute
Apache Libcloud driver for Interoute (based on Apache CloudStack, but slightly modified)

## Requirements

[Apache Libcloud](https://github.com/apache/libcloud/) 0.18.0 or later

## Install
```
python setup.py install
```

## Usage

```
from libcloud.compute.providers import get_driver
from libcloud.compute.providers import set_driver


set_driver('interoute', 'interoute.libcloud.compute', 'InterouteNodeDriver')

# Your code which uses the driver.
# For example:
Driver = get_driver('interoute')
```
or [RTFM](https://libcloud.readthedocs.org/en/latest/other/registering-a-third-party-driver.html)
