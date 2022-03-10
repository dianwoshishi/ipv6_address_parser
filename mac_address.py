from OuiLookup import OuiLookup
import macaddress


class MacAddress:
    def __init__(self, _mac):
        try:
            self.mac = macaddress.MAC(_mac)
        except:
            self.mac_str = None
            self.org_str = None
            return 

        try:
            look_up_result = OuiLookup().query(str(self.mac))[0]
            (self.mac_str, self.org_str), = look_up_result.items()
        except Exception as e:
            self.mac_str = str(self.mac)
            self.org_str = None

    def get_mac(self):
        return self.mac_str.upper() if self.mac_str != None else None
    def get_org(self):
        return self.org_str.upper() if self.org_str != None else None
    def get_code(self):
        return self.mac_str.upper()[0:3] if self.mac_str != None else None

    def manual_update(self):
        stat = OuiLookup().update()
        print(stat)
    def get_oui_stat(self):
        stat = OuiLookup().status()
        print(stat)



if __name__ == "__main__":
    mac_address = MacAddress("00AA00AAAAAA")
    mac_address.manual_update()
    mac_address.get_oui_stat()
    print(mac_address.get_mac())
    print(mac_address.get_org())
    
