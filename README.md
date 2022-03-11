# IPv6 address parser

## Introduction && Motivation
ipv6toolkit (https://github.com/fgont/ipv6toolkit)is an useful tool set,and 
addr6 is one of these tools, which can be used to analysis ipv6 addresses.

for example,according to IPv6 addressing strategy, an ipv6 address can be decode into 5 types:`type, subtype, scope, iidtype, iidsubtype`. The defination of these types can be found in addr6's manual(such as https://www.venea.net/man/addr6(1)).

But there is no python lib parsing and analysising IPv6 addresses, especially the IID, which is the host part of IPv6 address. So this python script implements the same function as addr6's `decode_ipv6_address()` function did.

Besides, additional features are added, for example:

- when the IID of an IPv6 address is ieee-drived, mac address and corresponding mac vendor are parsed. 

It can be used in your python project easily to classify the IPv6 addresses.

## install
Dependencies:
- `IPy` is used to convert string of ipv6 to int.
- `macaddress,ouilookup` are used to process mac address.

Using `pip`, you can install the dependencies easily:

```shell/
pip install -r requirements.txt
```
## directory && short description
```python
active_ipv6 #ipv6 test set, download from the ipv6hitlist.github.io

active_ipv6_addr6 # ipv6 type test set, generate from active_ipv6 using addr6

icmp.txt, icmp.txt_addr6 # same as above files

decode_ipv6_address.py # main work

requirements.txt # dependencies

test_decode_ipv6_address.py  #unit test

mac_address.py #class MacAddress
```

## how to use it
example can be found in `exmaple.py`
```python

from ipv6_address_parser import IPstat

if __name__ == "__main__":
    ipv6 = "2001:1210:105:34:0:606:a8:31"
    ipv6_type = "unicast=global=global=pattern-bytes=unspecified"
    ipstat = IPstat(ipv6)
    type_str = ipstat.get_ip_type()
    assert type_str == ipv6_type

    print(type_str)
```
the output of the example is:
```
unicast=global=global=pattern-bytes=unspecified
```
or get json output using `ipstat.get_type()`:
```json
{'type': 'unicast', 'subtype': 'global', 'scope': 'global', 'iidtype': 'pattern-bytes', 'iidsubtype': 'unspecified'}
```

## unit test
we use unittest to test this script. To make sure the script works fine, `672673 + 2561265` ipv6 addresses are tested. Another active file, which contains 2561256 ipv6 address, can be found in http://tsinghua-nmgroup-ipv6.cn/sharedfiles/icmp.txt, you can download it from this url.

`active_ipv6` and `active_ipv6_addr6` are files used to test this project.

you can simplely test it use the command below:
```
python test_decode_ipv6_address.py

```

