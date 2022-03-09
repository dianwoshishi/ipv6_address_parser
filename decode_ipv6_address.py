#!/usr/bin/env python   
# This file is convert from the addr6 of ipv6toolkit, 
# can be used to classify IPv6 address into `type, subtype,
# scope, iidtype, iidsubtype`, which is defined in addr6's
# manual(https://manpages.ubuntu.com/manpages/bionic/man1/addr6.1.html).
# 

from IPy import IPint
from dataclasses import dataclass

@dataclass
class IPType():
    ipv6_type = {
    "IPV6_UNKNOWN": ["IPV6_UNKNOWN", (1 << 0)], 
    "IPV6_UNSPEC": ["IPV6_UNSPEC", (1 << 1)],
    "IPV6_MULTICAS": ["IPV6_MULTICAS", (1 << 2)],
    "IPV6_UNICAST": ["IPV6_UNICAST", (1 << 3)],

    "UCAST_V4MAPPE": ["UCAST_V4MAPPE", (1 << 1)],
    "UCAST_V4COMPA": ["UCAST_V4COMPA", (1 << 2)],
    "UCAST_LINKLOCA": ["UCAST_LINKLOCA", (1 << 3)],
    "UCAST_SITELOCA": ["UCAST_SITELOCA", (1 << 4)],
    "UCAST_UNIQUELOCA": ["UCAST_UNIQUELOCA", (1 << 5)],
    "UCAST_6TO4": ["UCAST_6TO4", (1 << 6)], 
    "UCAST_TEREDO": ["UCAST_TEREDO", (1 << 7)],
    "UCAST_GLOBAL": ["UCAST_GLOBAL", (1 << 8)],
    "UCAST_LOOPBACK": ["UCAST_LOOPBACK", (1 << 9)],
                                        
    "MCAST_PERMANENT": ["MCAST_PERMANENT", (1 << 1)],
    "MCAST_NONPERMANENT": ["MCAST_NONPERMANENT", (1 << 2)],
    "MCAST_INVALID": ["MCAST_INVALID", (1 << 3)],
    "MCAST_UNICASTBASED": ["MCAST_UNICASTBASED", (1 << 4)],
    "MCAST_EMBEDRP": ["MCAST_EMBEDRP", (1 << 5)],
    "MCAST_UNKNOWN": ["MCAST_UNKNOWN", (1 << 6)],
                                        
    "SCOPE_RESERVED": ["SCOPE_RESERVED", (1 << 1)],
    "SCOPE_INTERFACE": ["SCOPE_INTERFACE", (1 << 2)],
    "SCOPE_LINK": ["SCOPE_LINK", (1 << 3)] ,
    "SCOPE_ADMIN": ["SCOPE_ADMIN", (1 << 4)],
    "SCOPE_SITE": ["SCOPE_SITE", (1 << 5)] ,
    "SCOPE_ORGANIZATION": ["SCOPE_ORGANIZATION", (1 << 6)],
    "SCOPE_GLOBAL": ["SCOPE_GLOBAL", (1 << 7)],
    "SCOPE_UNASSIGNED": ["SCOPE_UNASSIGNED", (1 << 8)],
    "SCOPE_UNSPECIFIED": ["SCOPE_UNSPECIFIED"],
                                        
    "IID_MACDERIVED": ["IID_MACDERIVED", (1 << 1)],
    "IID_ISATAP": ["IID_ISATAP", (1 << 2)],
    "IID_EMBEDDEDIPV4": ["IID_EMBEDDEDIPV4", (1 << 3)],
    "IID_EMBEDDEDPORT": ["IID_EMBEDDEDPO", (1 << 4)],
    "IID_EMBEDDEDPORTREV": ["IID_EMBEDDEDPORTRE", (1 << 5)],
    "IID_LOWBYTE": ["IID_LOWBYTE", (1 << 6)],
    "IID_EMBEDDEDIPV4_64": ["IID_EMBEDDEDIPV4_64", (1 << 7)],
    "IID_PATTERN_BYTES": ["IID_PATTERN_BYTES", (1 << 8)],
    "IID_RANDOM": ["IID_RANDOM", (1 << 9)],
    "IID_TEREDO_RFC4380": ["IID_TEREDO_RFC4380", (1 << 10)],
    "IID_TEREDO_RFC5991": ["IID_TEREDO_RFC5991", (1 << 11)],
    "IID_TEREDO_UNKNOWN": ["IID_TEREDO_UNKNOWN", (1 << 12)],
    "IID_TEREDO": ["IID_TEREDO", (1 << 13)],
    "IID_UNSPECIFIED": ["IID_UNSPECIFIED", (1 << 14)],
    "IID_EMBEDDEDIPV4_32": ["IID_EMBEDDEDIPV4_32", (1 << 15)],
    }

class IPv6ParseError:
    def __init__(self, msg):
        self.msg = msg
    def error_msg(self):
        return self.msg

class IPv6Address:
    def __init__(self, ipv6):
        self.ipv6_address = IPint(ipv6).ip
        self.ipv6_type = IPType.ipv6_type["IPV6_UNKNOWN"]
        self.ipv6_subtype = IPType.ipv6_type["IPV6_UNKNOWN"]
        self.ipv6_scope = IPType.ipv6_type["IPV6_UNKNOWN"]
        self.ipv6_iidtype = IPType.ipv6_type["IPV6_UNKNOWN"]
        self.ipv6_iidsubtype = IPType.ipv6_type["IPV6_UNKNOWN"]

class IPstat(object):
    def __init__(self, ipv6):
        self.ipv6address = IPv6Address(ipv6)


    def get_int64(self, _nth):
        _nth -= 1
        if _nth < 0 or _nth >= 2:
            raise IPv6ParseError("the _nth should be 1-2, your input is {}".format(_nth + 1))
        return (self.ipv6address.ipv6_address >> ((1 - _nth) * 64) ) & 0xffffffffffffffff
    def get_int32(self, _nth):
        _nth -= 1
        if _nth < 0 or _nth >= 4:
            raise IPv6ParseError("the _nth should be 1-4, your input is {}".format(_nth + 1))
        return (self.ipv6address.ipv6_address >> ((3 - _nth) * 32) ) & 0xffffffff 
    def get_int16(self, _nth):
        _nth -= 1
        if _nth < 0 or _nth >= 8:
            raise IPv6ParseError("the _nth should be 1-8, your input is {}".format(_nth + 1))
        return (self.ipv6address.ipv6_address >> ((7 - _nth) * 16) ) & 0xffff
    def get_int8(self, _nth): 
        _nth -= 1
        if _nth < 0 or _nth >= 16:
            raise IPv6ParseError("the _nth should be 1-16, your input is {}".format(_nth + 1))
        return (self.ipv6address.ipv6_address >> ((15 - _nth) * 8) ) & 0xff


    def IN6_IS_ADDR_UNIQUELOCAL(self):
        return self.get_int32(1) & 0xfe000000 == 0xfc000000
        
    def IN6_IS_ADDR_6TO4(self):
        return self.get_int32(1) & 0xffff0000 == 0x20020000

    def IN6_IS_ADDR_TEREDO(self):
        return self.get_int32(1)  == 0x20010000

    def IN6_IS_ADDR_TEREDO_LEGACY(self):
        return self.get_int32(1)  == 0x3ffe831f

#  * Unspecified
    def IN6_IS_ADDR_UNSPECIFIED(self):
        if  self.get_int32(1) == 0 and \
            self.get_int32(2) == 0 and \
            self.get_int32(3) == 0 and \
            self.get_int32(4) == 0:
            return True
        else:
            return False
#  * Loopback
    def IN6_IS_ADDR_LOOPBACK(self):
        if  self.get_int32(1) == 0 and \
            self.get_int32(2) == 0 and \
            self.get_int32(3) == 0 and \
            self.get_int32(4) == 1:
            return True
        else:
            return False
#  * IPv4 compatible
    def IN6_IS_ADDR_V4COMPAT(self):
        if  self.get_int32(1) == 0 and \
            self.get_int32(2) == 0 and \
            self.get_int32(3) == 0 and \
            self.get_int32(4) != 0 and \
            self.get_int32(4) != 1:
            return True
        else:
            return False    
#  Mappe    
    def IN6_IS_ADDR_V4MAPPED(self):
        if  self.get_int32(1) == 0 and \
            self.get_int32(2) == 0 and \
            self.get_int32(3) == 0x0000ffff:
            return True
        else:
            return False  
#  * 6to4
    def IN6_IS_ADDR_6TO4(self):
        if  self.get_int16(1) == 0x2002:
            return True
        else:
            return False
#  * Unicast Scope
#  * Note that we must check topmost 10 bits only, not 16 bits (see RFC2373)
    def IN6_IS_ADDR_LINKLOCAL(self):
        if  self.get_int8(1) == 0xfe and \
            self.get_int8(2) & 0xc0 == 0x80:
            return True
        else:
            return False
    def IN6_IS_ADDR_SITELOCAL(self):
        if  self.get_int8(1) == 0xfe and \
            self.get_int8(2) & 0xc0 == 0xc0:
            return True
        else:
            return False   

# Multicast       
    def IN6_IS_ADDR_MULTICAST(self):
        if  self.get_int8(1) == 0xff:
            return True
        else:
            return False   
    def IPV6_ADDR_MC_FLAGS(self):
        if  self.get_int8(2) == 0xf0:
            return True
        else:
            return False   
    IPV6_ADDR_MC_FLAGS_TRANSIENT = 0x10
    IPV6_ADDR_MC_FLAGS_PREFIX    = 0x20
    IPV6_ADDR_MC_FLAGS_UNICAST_BASED = IPV6_ADDR_MC_FLAGS_TRANSIENT | IPV6_ADDR_MC_FLAGS_PREFIX
    def IN6_IS_ADDR_UNICAST_BASED_MULTICAST(self):
        if  self.IN6_IS_ADDR_MULTICAST() and \
            self.IPV6_ADDR_MC_FLAGS() == self.IPV6_ADDR_MC_FLAGS_UNICAST_BASED:
            return True
        else:
            return False    
# Unique Local IPv6 Unicast Addresses (per RFC 4193)
    def IN6_IS_ADDR_UNIQUE_LOCAL(self):
        if  self.get_int8(1) == 0xfc or \
            self.get_int8(1) == 0xfd:
            return True
        else:
            return False

    def __IPV6_ADDR_MC_SCOPE(self):
        return self.get_int8(2) & 0x0f


 #* Multicast Scope
#   * KAME Scope Values
    __IPV6_ADDR_SCOPE_NODELOCAL     = 0x01
    __IPV6_ADDR_SCOPE_INTFACELOCAL  = 0x01
    __IPV6_ADDR_SCOPE_LINKLOCAL     = 0x02
    __IPV6_ADDR_SCOPE_SITELOCAL     = 0x05
    __IPV6_ADDR_SCOPE_ORGLOCAL      = 0x08    #/* just used in this file */
    __IPV6_ADDR_SCOPE_GLOBAL        = 0x0e
    def IN6_IS_ADDR_MC_NODELOCAL(self):
        if  self.IN6_IS_ADDR_MULTICAST() and \
            self.__IPV6_ADDR_MC_SCOPE() ==  __IPV6_ADDR_SCOPE_NODELOCAL:
            return True
        else:
            return False
    def IN6_IS_ADDR_MC_LINKLOCAL(self):
        if  self.IN6_IS_ADDR_MULTICAST() and \
            self.IPV6_ADDR_MC_FLAGS() !=  IPV6_ADDR_MC_FLAGS_UNICAST_BASED and \
            self.__IPV6_ADDR_MC_SCOPE() == __IPV6_ADDR_SCOPE_LINKLOCAL:
            return True
        else:
            return False
    def IN6_IS_ADDR_MC_SITELOCAL(self):
        if  self.IN6_IS_ADDR_MULTICAST() and \
            self.__IPV6_ADDR_MC_SCOPE() ==  __IPV6_ADDR_SCOPE_SITELOCAL:
            return True
        else:
            return False
    def IN6_IS_ADDR_MC_ORGLOCAL(self):
        if  self.IN6_IS_ADDR_MULTICAST() and \
            self.__IPV6_ADDR_MC_SCOPE() ==  __IPV6_ADDR_SCOPE_ORGLOCAL:
            return True
        else:
            return False
    def IN6_IS_ADDR_MC_GLOBAL(self):
        if  self.IN6_IS_ADDR_MULTICAST() and \
            self.__IPV6_ADDR_MC_SCOPE() ==  __IPV6_ADDR_SCOPE_GLOBAL:
            return True
        else:
            return False   
    def is_service_port(self, port):
        service_ports_hex=[0x21, 0x22, 0x23, 0x25, 0x49, 0x53, 0x80, 0x110, 0x123, 0x179, 0x220, 0x389, \
						                 0x443, 0x547, 0x993, 0x995, 0x1194, 0x3306, 0x5060, 0x5061, 0x5432, 0x6446, 0x8080]
	    
        service_ports_dec=[21, 22, 23, 25, 49, 53, 80, 110, 123, 179, 220, 389, \
						                 443, 547, 993, 995, 1194, 3306, 5060, 5061, 5432, 6446, 8080]
        if port in service_ports_hex:
            return True
        if port in service_ports_dec:
            return True
        return False
    def zero_byte_iid(self):
        zero_count = 0
        for i in range(8,16):
            if self.get_int8(i + 1) == 0x0:
                zero_count += 1
        return zero_count


    def __parseType(self):
        if self.IN6_IS_ADDR_UNSPECIFIED():
            self.ipv6address.ipv6_type = IPType.ipv6_type["IPV6_UNSPEC"]
            self.ipv6address.ipv6_subtype =IPType.ipv6_type["IPV6_UNSPEC"] 
            self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_UNSPECIFIED"]
        elif self.IN6_IS_ADDR_MULTICAST():
            self.ipv6address.ipv6_type = IPType.ipv6_type["IPV6_MULTICAST"]
            self.ipv6address.ipv6_subtype =IPType.ipv6_type["IID_UNSPECIFIED"] 
            self.ipv6address.ipv6_scope = IPType.ipv6_type["IID_UNSPECIFIED"]
            if  self.get_int32(1) & 0xff000000 == 0xff000000:
                if self.get_int32(1) & 0xfff00000 == 0xff000000:
                    self.ipv6address.ipv6_subtype =IPType.ipv6_type["MCAST_PERMANENT"] 
                elif self.get_int32(1) & 0xfff00000 == 0xff100000:
                    self.ipv6address.ipv6_subtype =IPType.ipv6_type["MCAST_NONPERMANENT"] 
                elif self.get_int32(1) & 0xfff00000 == 0xff200000:
                    self.ipv6address.ipv6_subtype =IPType.ipv6_type["MCAST_INVALID"] 
                elif self.get_int32(1) & 0xfff00000 == 0xff300000:
                    self.ipv6address.ipv6_subtype =IPType.ipv6_type["MCAST_UNICASTBASED"] 
                elif self.get_int32(1) & 0xfff00000 == 0xff400000:
                    self.ipv6address.ipv6_subtype =IPType.ipv6_type["MCAST_INVALID"] 
                elif self.get_int32(1) & 0xfff00000 == 0xff500000:
                    self.ipv6address.ipv6_subtype =IPType.ipv6_type["MCAST_INVALID"] 
                elif self.get_int32(1) & 0xfff00000 == 0xff600000:
                    self.ipv6address.ipv6_subtype =IPType.ipv6_type["MCAST_INVALID"] 
                elif self.get_int32(1) & 0xfff00000 == 0xff700000:
                    self.ipv6address.ipv6_subtype =IPType.ipv6_type["MCAST_EMBEDRP"] 
                
                scope = ( self.get_int32(1) & 0x000f0000 ) >> 16
                if scope == 0:
                    self.ipv6address.ipv6_scope =IPType.ipv6_type["SCOPE_RESERVED"] 
                elif scope == 1:
                    self.ipv6address.ipv6_scope =IPType.ipv6_type["SCOPE_INTERFACE"] 
                elif scope == 2:
                    self.ipv6address.ipv6_scope =IPType.ipv6_type["SCOPE_LINK"]
                elif scope == 3:
                    self.ipv6address.ipv6_scope =IPType.ipv6_type["SCOPE_RESERVED"]
                elif scope == 4:
                    self.ipv6address.ipv6_scope =IPType.ipv6_type["SCOPE_ADMIN"]
                elif scope == 5:
                    self.ipv6address.ipv6_scope =IPType.ipv6_type["SCOPE_SITE"]
                elif scope == 8:
                    self.ipv6address.ipv6_scope =IPType.ipv6_type["SCOPE_ORGANIZATION"]
                elif scope == 0xe:
                    self.ipv6address.ipv6_scope =IPType.ipv6_type["SCOPE_GLOBAL"]
                else:
                    self.ipv6address.ipv6_scope =IPType.ipv6_type["SCOPE_UNASSIGNED"]
            else:
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["MCAST_UNKNOWN"] 
        else:
            self.ipv6address.ipv6_type = IPType.ipv6_type["IPV6_UNICAST"]
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_UNSPECIFIED"] 
            self.ipv6address.ipv6_iidsubtype = IPType.ipv6_type["IID_UNSPECIFIED"]
            if self.IN6_IS_ADDR_LOOPBACK():
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["UCAST_LOOPBACK"] 
                self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_INTERFACE"]
            elif self.IN6_IS_ADDR_V4MAPPED():
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["UCAST_V4MAPPED"] 
                self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_UNSPECIFIED"]
            elif self.IN6_IS_ADDR_V4COMPAT():
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["UCAST_V4COMPAT"] 
                self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_UNSPECIFIED"]
            elif self.IN6_IS_ADDR_LINKLOCAL():
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["UCAST_LINKLOCAL"] 
                self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_LINK"]
            elif self.IN6_IS_ADDR_SITELOCAL():
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["UCAST_SITELOCAL"] 
                self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_SITE"]
            elif self.IN6_IS_ADDR_UNIQUELOCAL():
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["UCAST_UNIQUELOCAL"] 
                self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_GLOBAL"]
            elif self.IN6_IS_ADDR_6TO4():
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["UCAST_6TO4"] 
                self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_GLOBAL"]
            elif self.IN6_IS_ADDR_TEREDO() or self.IN6_IS_ADDR_TEREDO_LEGACY():
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["UCAST_UNIQUELOCAL"] 
                self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_GLOBAL"]
                self.ipv6address.ipv6_iidtype = IPType.ipv6_type["IID_TEREDO"]
                if self.get_int32(3) & 0x03000000:
                    self.ipv6address.ipv6_iidsubtype = IPType.ipv6_type["IID_TEREDO_UNKNOWN"]
                elif self.get_int32(3) & 0x3cff0000:
                    self.ipv6address.ipv6_iidsubtype = IPType.ipv6_type["IID_TEREDO_RFC5991"]
                else:
                    self.ipv6address.ipv6_iidsubtype = IPType.ipv6_type["IID_TEREDO_RFC4380"]
            else:
                self.ipv6address.ipv6_subtype =IPType.ipv6_type["UCAST_GLOBAL"] 
                self.ipv6address.ipv6_scope = IPType.ipv6_type["SCOPE_GLOBAL"] 
        
        if  self.get_int32(3) & 0x020000ff == 0x020000ff and \
            self.get_int32(4) & 0xff000000 == 0xfe000000:
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_MACDERIVED"] 
            self.ipv6address.ipv6_iidsubtype = (self.get_int32(3) >> 8) & 0xfffdffff 
        elif self.get_int32(3) & 0xfdffffff == 0x00005efe:
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_ISATAP"] 
        elif    self.get_int32(3) == 0 and \
                self.get_int32(4) & 0xff000000 != 0 and\
                self.get_int32(4) & 0x0000ffff != 0:
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_EMBEDDEDIPV4"] 
            self.ipv6address.ipv6_iidsubtype = IPType.ipv6_type["IID_EMBEDDEDIPV4_32"]  
        elif    self.get_int32(3) == 0 and \
                self.get_int32(4) & 0xff000000 == 0 and\
                self.is_service_port(self.get_int32(4) & 0x0000ffff):
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_EMBEDDEDPORT"] 
            self.ipv6address.ipv6_iidsubtype = IPType.ipv6_type["IID_EMBEDDEDPORT"]   
        elif    self.get_int32(3) == 0 and \
                self.get_int32(4) & 0x0000ff00 == 0 and\
                self.is_service_port(self.get_int32(4) >> 16):
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_EMBEDDEDPORT"] 
            self.ipv6address.ipv6_iidsubtype = IPType.ipv6_type["IID_EMBEDDEDPORTREV"] 
        elif    self.get_int32(3) == 0 and \
                self.get_int32(4) & 0xff000000 == 0 and\
                self.get_int32(4) & 0x0000ffff != 0:
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_LOWBYTE"] 
        elif    self.get_int32(3) >> 16 <= 0x255 and\
                self.get_int32(3) & 0x0000ffff <= 0x255 and\
                self.get_int32(4) >> 16 <= 0x255 and\
                self.get_int32(4) & 0x0000ffff <= 0x255:
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_EMBEDDEDIPV4"] 
            self.ipv6address.ipv6_iidsubtype = IPType.ipv6_type["IID_EMBEDDEDIPV4_64"] 
        elif self.zero_byte_iid() > 2:
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_PATTERN_BYTES"]
        else:
            self.ipv6address.ipv6_iidtype =IPType.ipv6_type["IID_RANDOM"]

    def get_ipstat(self):
        return self.ipv6address
             
    nullstring=""
    unspecified="unspecified"
    iidsubtypebuffer=""
    ipv6unspec="unspecified"
    ipv6multicast="multicast";
    ipv6unicast="unicast";
    
    ucastloopback="loopback";
    ucastv4mapped="ipv4-mapped";
    ucastv4compat="ipv4-compatible";
    ucastlinklocal="link-local";
    ucastsitelocal="site-local";
    ucastuniquelocal="unique-local";
    ucast6to4="6to4";
    ucastteredo="teredo";
    ucastglobal="global";
    
    mcastpermanent="permanent";
    mcastnonpermanent="non-permanent";
    mcastinvalid="invalid";
    mcastunicastbased="unicast-based";
    mcastembedrp="embedded-rp";
    mcastunknown="unknown";
    
    iidmacderived="ieee-derived";
    iidisatap="isatap";
    iidmbeddedipv4="embedded-ipv4";
    iidembeddedport="embedded-port";
    iidembeddedportfwd="port-fwd";
    iidembeddedportrev="port-rev";
    iidlowbyte="low-byte";
    iidembeddedipv4_32="embedded-ipv4-32";
    iidembeddedipv4_64="embedded-ipv4-64";
    iidpatternbytes="pattern-bytes";
    iidrandom="randomized";
    iidteredo="teredo";
    iidteredorfc4380="rfc4380";
    iidteredorfc5991="rfc5991";
    iidteredounknown="unknown";
    
    scopereserved="reserved";
    scopeinterface="interface";
    scopelink="link";
    scopeadmin="admin";
    scopesite="site";
    scopeorganization="organization";
    scopeglobal="global";
    scopeunassigned="unassigned";
    scopeunspecified="unspecified";
    def get_ip_type(self):
        
        self.__parseType()
        ipstat = self.get_ipstat()
        type_str = self.nullstring
        subtype_str = self.nullstring
        iidtype_str = self.nullstring
        iidsubtype_str = self.nullstring
        if ipstat.ipv6_type == IPType.ipv6_type["IPV6_UNSPEC"]:
            type_str = self.ipv6unspec
            subtype_str = self.unspecified
            iidtype_str = self.unspecified
            iidsubtype_str = self.unspecified
        elif ipstat.ipv6_type == IPType.ipv6_type["IPV6_UNICAST"]:
            type_str = self.ipv6unicast
            iidtype_str = self.unspecified
            iidsubtype_str = self.unspecified
            if ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_LOOPBACK"]:
                subtype_str = self.ucastloopback
                iidtype_str = self.iidlowbyte
            elif ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_GLOBAL"]:
                subtype_str = self.ucastglobal
            elif ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_V4MAPPE"]:
                subtype_str = self.ucastv4mapped
            elif ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_V4COMPA"]:
                subtype_str = self.ucastv4compat
            elif ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_LINKLOCA"]:
                subtype_str = self.ucastlinklocal
            elif ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_SITELOCA"]:
                subtype_str = self.ucastsitelocal
            elif ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_UNIQUELOCA"]:
                subtype_str = self.ucastuniquelocal  
            elif ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_6TO4"]:
                subtype_str = self.ucast6to4
            elif ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_TEREDO"]:
                subtype_str = self.ucastteredo


            if ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_GLOBAL"] or\
                ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_V4MAPPED"] or\
                ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_V4COMPAT"] or\
                ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_LINKLOCA"] or\
                ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_SITELOCA"] or\
                ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_UNIQUELOCA"] or\
                ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_6TO4"] or\
                ipstat.ipv6_subtype == IPType.ipv6_type["UCAST_TEREDO"]:

                if ipstat.ipv6_iidtype == IPType.ipv6_type["IID_MACDERIVED"]:
                    iidtype_str =   self.iidmacderived
                    

                    iidsubtype_str = "{:0>2x}-{:0>2x}-{:0>2x}".format((ipstat.ipv6_iidsubtype >> 16)&0xff,
                                                                        (ipstat.ipv6_iidsubtype >> 8)&0xff,     
                                                                        (ipstat.ipv6_iidsubtype >> 0    )&0xff)


                elif ipstat.ipv6_iidtype == IPType.ipv6_type["IID_ISATAP"]:
                    iidtype_str = self.iidisatap
                elif ipstat.ipv6_iidtype == IPType.ipv6_type["IID_EMBEDDEDIPV4"]:
                    iidtype_str = self.iidmbeddedipv4
                    if ipstat.ipv6_iidsubtype == IPType.ipv6_type["IID_EMBEDDEDIPV4_32"]:
                        iidsubtype_str = self.iidembeddedipv4_32
                    elif ipstat.ipv6_iidsubtype == IPType.ipv6_type["IID_EMBEDDEDIPV4_64"]:
                        iidsubtype_str = self.iidembeddedipv4_64
                elif ipstat.ipv6_iidtype == IPType.ipv6_type["IID_EMBEDDEDPORT"]:
                    iidtype_str = self.iidembeddedport
                    if ipstat.ipv6_iidsubtype == IPType.ipv6_type["IID_EMBEDDEDPORT"]: 
                        iidsubtype_str = self.iidembeddedportfwd
                    elif ipstat.ipv6_iidsubtype == IPType.ipv6_type["IID_EMBEDDEDPORTREV"]: 
                        iidsubtype_str = self.iidembeddedportrev
                elif ipstat.ipv6_iidtype == IPType.ipv6_type["IID_LOWBYTE"]:
                    iidtype_str = self.iidlowbyte
                elif ipstat.ipv6_iidtype == IPType.ipv6_type["IID_PATTERN_BYTES"]:
                    iidtype_str = self.iidpatternbytes
                elif ipstat.ipv6_iidtype == IPType.ipv6_type["IID_RANDOM"]:
                    iidtype_str = self.iidrandom
                elif ipstat.ipv6_iidtype == IPType.ipv6_type["IID_TEREDO"]:
                    iidtype_str = self.iidteredo
                    if ipstat.ipv6_iidsubtype == IPType.ipv6_type["IID_TEREDO_RFC4380"]: 
                        iidsubtype_str = self.iidteredorfc4380
                    elif ipstat.ipv6_iidsubtype == IPType.ipv6_type["IID_TEREDO_RFC5991"]: 
                        iidsubtype_str = self.iidteredorfc5991
                    elif ipstat.ipv6_iidsubtype == IPType.ipv6_type["IID_TEREDO_UNKNOWN"]: 
                        iidsubtype_str = self.iidteredounknown
        
        elif ipstat.ipv6_type == IPType.ipv6_type["IPV6_MULTICAST"]:
            type_str = self.ipv6multicast
            iidtype_str = self.unspecified
            iidsubtype_str = self.unspecified
            if ipstat.ipv6_subtype == IPType.ipv6_type["MCAST_PERMANENT"]: 
                subtype_str = self.mcastpermanent
            elif ipstat.ipv6_subtype == IPType.ipv6_type["MCAST_NONPERMANENT"]: 
                subtype_str = self.mcastnonpermanent
            elif ipstat.ipv6_subtype == IPType.ipv6_type["MCAST_INVALID"]: 
                subtype_str = self.mcastinvalid
            elif ipstat.ipv6_subtype == IPType.ipv6_type["MCAST_UNICASTBASED"]: 
                subtype_str = self.mcastunicastbased
            elif ipstat.ipv6_subtype == IPType.ipv6_type["MCAST_EMBEDRP"]: 
                subtype_str = self.mcastembedrp
            elif ipstat.ipv6_subtype == IPType.ipv6_type["MCAST_UNKNOWN"]: 
                subtype_str = self.mcastunknown

        if ipstat.ipv6_scope == IPType.ipv6_type["SCOPE_RESERVED"]:
            scope = self.scopereserved
        elif ipstat.ipv6_scope == IPType.ipv6_type["SCOPE_INTERFACE"]:
            scope = self.scopeinterface
        elif ipstat.ipv6_scope == IPType.ipv6_type["SCOPE_LINK"]:
            scope = self.scopelink
        elif ipstat.ipv6_scope == IPType.ipv6_type["SCOPE_ADMIN"]:
            scope = self.scopeadmin
        elif ipstat.ipv6_scope == IPType.ipv6_type["SCOPE_SITE"]:
            scope = self.scopesite
        elif ipstat.ipv6_scope == IPType.ipv6_type["SCOPE_ORGANIZATION"]:
            scope = self.scopeorganization
        elif ipstat.ipv6_scope == IPType.ipv6_type["SCOPE_GLOBAL"]:
            scope = self.scopeglobal
        elif ipstat.ipv6_scope == IPType.ipv6_type["SCOPE_UNSPECIFIED"]:
            scope = self.scopeunspecified
        else:
            scope = self.scopeunassigned 
        
        type_str = "{}={}={}={}={}".format(type_str,\
                                        subtype_str,\
                                        scope,\
                                        iidtype_str,\
                                        iidsubtype_str)
        return type_str

