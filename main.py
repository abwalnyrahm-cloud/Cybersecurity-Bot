import socket
import requests
from cryptography.fernet import Fernet

# فحص المنافذ
def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            else:
                print(f"Port {port} is CLOSED ❌")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# فحص الروابط
def check_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"{url} is reachable ✅")
            else:
                print(f"{url} returned status {response.status_code}")
        except Exception as e:
            print(f"{url} is not reachable ❌ - {e}")

# تشفير وفك تشفير
def encrypt_decrypt_demo(message):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    decrypted = cipher.decrypt(encrypted).decode()
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    # فحص منافذ
    target_host = "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443]
    scan_ports(target_host, ports_to_scan)

    # فحص روابط
    urls = ["http://example.com", "http://testphp.vulnweb.com"]
    check_urls(urls)

    # تجربة التشفير
    encrypt_decrypt_demo("Cyber Security Bot")
import socket
import requests
from cryptography.fernet import Fernet

# فحص المنافذ
def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            else:
                print(f"Port {port} is CLOSED ❌")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# فحص الروابط
def check_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"{url} is reachable ✅")
            else:
                print(f"{url} returned status {response.status_code}")
        except Exception as e:
            print(f"{url} is not reachable ❌ - {e}")

# تشفير وفك تشفير
def encrypt_decrypt_demo(message):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    decrypted = cipher.decrypt(encrypted).decode()
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    # فحص منافذ
    target_host = "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443]
    scan_ports(target_host, ports_to_scan)

    # فحص روابط
    urls = ["http://example.com", "http://testphp.vulnweb.com"]
    check_urls(urls)

    # تجربة التشفير
    encrypt_decrypt_demo("Cyber Security Bot")
import socket
import requests
from cryptography.fernet import Fernet

# فحص المنافذ
def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            else:
                print(f"Port {port} is CLOSED ❌")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# فحص الروابط
def check_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"{url} is reachable ✅")
            else:
                print(f"{url} returned status {response.status_code}")
        except Exception as e:
            print(f"{url} is not reachable ❌ - {e}")

# تشفير وفك تشفير
def encrypt_decrypt_demo(message):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    decrypted = cipher.decrypt(encrypted).decode()
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    # فحص منافذ
    target_host = "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443]
    scan_ports(target_host, ports_to_scan)

    # فحص روابط
    urls = ["http://example.com", "http://testphp.vulnweb.com"]
    check_urls(urls)

    # تجربة التشفير
    encrypt_decrypt_demo("Cyber Security Bot")
import socket
import requests
from cryptography.fernet import Fernet

# فحص المنافذ
def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            else:
                print(f"Port {port} is CLOSED ❌")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# فحص الروابط
def check_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"{url} is reachable ✅")
            else:
                print(f"{url} returned status {response.status_code}")
        except Exception as e:
            print(f"{url} is not reachable ❌ - {e}")

# تشفير وفك تشفير
def encrypt_decrypt_demo(message):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    decrypted = cipher.decrypt(encrypted).decode()
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    # فحص منافذ
    target_host = "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443]
    scan_ports(target_host, ports_to_scan)

    # فحص روابط
    urls = ["http://example.com", "http://testphp.vulnweb.com"]
    check_urls(urls)

    # تجربة التشفير
    encrypt_decrypt_demo("Cyber Security Bot")
import socket
import requests
from cryptography.fernet import Fernet

# فحص المنافذ
def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            else:
                print(f"Port {port} is CLOSED ❌")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# فحص الروابط
def check_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"{url} is reachable ✅")
            else:
                print(f"{url} returned status {response.status_code}")
        except Exception as e:
            print(f"{url} is not reachable ❌ - {e}")

# تشفير وفك تشفير
def encrypt_decrypt_demo(message):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    decrypted = cipher.decrypt(encrypted).decode()
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    # فحص منافذ
    target_host = "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443]
    scan_ports(target_host, ports_to_scan)

    # فحص روابط
    urls = ["http://example.com", "http://testphp.vulnweb.com"]
    check_urls(urls)

    # تجربة التشفير
    encrypt_decrypt_demo("Cyber Security Bot")
import socket
import requests
from cryptography.fernet import Fernet

# فحص المنافذ
def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            else:
                print(f"Port {port} is CLOSED ❌")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# فحص الروابط
def check_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"{url} is reachable ✅")
            else:
                print(f"{url} returned status {response.status_code}")
        except Exception as e:
            print(f"{url} is not reachable ❌ - {e}")

# تشفير وفك تشفير
def encrypt_decrypt_demo(message):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    decrypted = cipher.decrypt(encrypted).decode()
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    # فحص منافذ
    target_host = "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443]
    scan_ports(target_host, ports_to_scan)

    # فحص روابط
    urls = ["http://example.com", "http://testphp.vulnweb.com"]
    check_urls(urls)

    # تجربة التشفير
    encrypt_decrypt_demo("Cyber Security Bot")
import socket
import requests
from cryptography.fernet import Fernet

# فحص المنافذ
def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            else:
                print(f"Port {port} is CLOSED ❌")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# فحص الروابط
def check_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"{url} is reachable ✅")
            else:
                print(f"{url} returned status {response.status_code}")
        except Exception as e:
            print(f"{url} is not reachable ❌ - {e}")

# تشفير وفك تشفير
def encrypt_decrypt_demo(message):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    decrypted = cipher.decrypt(encrypted).decode()
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    # فحص منافذ
    target_host = "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443]
    scan_ports(target_host, ports_to_scan)

    # فحص روابط
    urls = ["http://example.com", "http://testphp.vulnweb.com"]
    check_urls(urls)

    # تجربة التشفير
    encrypt_decrypt_demo("Cyber Security Bot")
import socket
import requests
from cryptography.fernet import Fernet

# فحص المنافذ
def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN ✅")
            else:
                print(f"Port {port} is CLOSED ❌")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# فحص الروابط
def check_urls(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"{url} is reachable ✅")
            else:
                print(f"{url} returned status {response.status_code}")
        except Exception as e:
            print(f"{url} is not reachable ❌ - {e}")

# تشفير وفك تشفير
def encrypt_decrypt_demo(message):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    decrypted = cipher.decrypt(encrypted).decode()
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    # فحص منافذ
    target_host = "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443]
    scan_ports(target_host, ports_to_scan)

    # فحص روابط
    urls = ["http://example.com", "http://testphp.vulnweb.com"]
    check_urls(urls)

    # تجربة التشفير
    encrypt_decrypt_demo("Cyber Security Bot")
