import unittest

from ipv6_address_parser import IPstat
from tqdm import tqdm

class TestStringMethods(unittest.TestCase):
    


    def test_get_intxx(self):
        self.ipv6_addresses = [  ("2001:1218:4000:2f0::4a",
                            [0x20011218400002f0, 0x000000000000004a],
                            [0x20011218, 0x400002f0, 0x00000000, 0x0000004a],
                            [0x2001, 0x1218, 0x4000, 0x02f0, 0x0000, 0x0000, 0x0000, 0x004a],
                            [0x20, 0x01, 0x12, 0x18, 0x40, 0x00, 0x02, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x4a])
                            ]
        ipstat = IPstat(self.ipv6_addresses[0][0])
        ipstat_64 = [ipstat.get_int64(i + 1) for i in range(0,2)]
        self.assertListEqual(ipstat_64, self.ipv6_addresses[0][1])
        ipstat_32 = [ipstat.get_int32(i + 1) for i in range(0,4)]
        self.assertListEqual(ipstat_32, self.ipv6_addresses[0][2])
        ipstat_16 = [ipstat.get_int16(i + 1) for i in range(0,8)]
        self.assertListEqual(ipstat_16, self.ipv6_addresses[0][3])
        ipstat_8 = [ipstat.get_int8(i + 1) for i in range(0,16)]
        self.assertListEqual(ipstat_8, self.ipv6_addresses[0][4])

    #@unittest.skip("skipping, for save time")
    def test_address_type(self):
        def test_file(ipv6_set, type_set):
            with open(ipv6_set) as f_ip, open(type_set) as f_type:
                for ip, ip_type in tqdm(zip(f_ip, f_type)):
                    with self.subTest(ip):
                        ip = ip.strip("\n")
                        ip_type = ip_type.strip("\n")
                        ipstat = IPstat(ip)
                        type_str = ipstat.str_types

                        self.assertEqual(type_str,ip_type) 

        test_data_dir = "test_data"
        files = ['active_ipv6']
        for file in files:
            ipv6_set = "{}/{}".format(test_data_dir, file)
            type_set = "{}/{}".format(test_data_dir, "{}_addr6".format(file))
            test_file(ipv6_set, type_set)
    
    def test_get_mac_address(self):
        test_ipv6 = [
                        [ "fe80::2aa:ff:fe3f:2a1c", "00AA003F2A1C", "00AA00", "INTEL CORPORATION"],
                        [ "FE80::24A:DFFF:FE8C:5EC1", "004ADF8C5EC1", "004ADF",  None],
                        ["FE80:0:0:0:02e0:4cFF:fe00:321a", "00E04C00321A", "00E04C", "REALTEK SEMICONDUCTOR CORP."],
                        ["2001:1218:4000:2f0::4a", None, None, None],
                        ["fe80::76d4:35ff:fe4e:39c8","74D4354E39C8", "74D435",  "GIGA-BYTE TECHNOLOGY CO.,LTD."],
                    ]
        for ipv6, mac,code, org in tqdm(test_ipv6):
            with self.subTest(ipv6):
                ipstat = IPstat(ipv6)
                mac_address = ipstat.get_mac_address()
                self.assertEqual( mac , mac_address.get_mac())
                self.assertEqual( org , mac_address.get_org())

if __name__ == '__main__':
    unittest.main(verbosity=2)
