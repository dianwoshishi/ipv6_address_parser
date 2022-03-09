# addr6 decode_ipv6_address for python

## introduction
ipv6toolkit is an useful tool set.
addr6 is one of these tools. It can be used to analysis ipv6 addresses.
for example, an ipv6 address can be decode into `type, subtype, scope, iidtype, iidsubtype`, which is defined in addr6's manual.
```
unicast=global=global=pattern-bytes=unspecified
```

this job is a python script, which is impliment the same function of addr6's `decode_ipv6_address()` function that comes from addr6. It can be used in your python project.

## install

```shell
pip install -r requirements.txt
```

```shell
.
├── README.md
├── active_ipv6 #ipv6 test set
├── active_ipv6_addr6 # ipv6 type test set
├── decode_ipv6_address.py # main work
├── requirements.txt # dependencies
└── test_decode_ipv6_address.py  #unit test
```

## how to 
```python

from decode_ipv6_address import IPstat

if __name__ == "__main__":
    ipv6 = "2001:1210:105:34:0:606:a8:31"
    ipv6_type = "unicast=global=global=pattern-bytes=unspecified"
    ipstat = IPstat(ipv6)
    type_str = ipstat.get_ip_type()
    assert type_str == ipv6_type

    print(type_str)
```
the output is:
```
unicast=global=global=pattern-bytes=unspecified
```

## unit test
`active_ipv6` and `active_ipv6_addr6` are files used to test this project.
you can simplely test it use the command below:
```
python test_decode_ipv6_address.py
```
