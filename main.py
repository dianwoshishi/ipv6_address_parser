from decode_ipv6_address import IPstat

if __name__ == "__main__":
    ipv6 = "2001:1210:105:34:0:606:a8:31"
    ipv6_type = "unicast=global=global=pattern-bytes=unspecified"
    ipstat = IPstat(ipv6)
    type_str = ipstat.get_ip_type()
    assert type_str == ipv6_type

    print(type_str)

    print(ipstat.get_types())
