import socket
from concurrent.futures import ThreadPoolExecutor

# ================= CONFIG =================
BASE_IP = "192.168.0"   # ajuste para sua rede
PORTS = [21, 22, 23, 53, 80, 443, 8080, 7547]
TIMEOUT = 1
MAX_THREADS = 100

active_hosts = set()

# ================= CORE =================
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)

    try:
        s.connect((ip, port))

        try:
            s.send(b"GET / HTTP/1.0\r\n\r\n")
            banner = s.recv(100)
        except:
            banner = b""

        print(f"[OPEN] {ip}:{port} -> {banner}")
        active_hosts.add(ip)

    except:
        pass

    finally:
        s.close()


def scan_ip(ip):
    for port in PORTS:
        scan_port(ip, port)


def scan_network():
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for i in range(1, 255):
            ip = f"{BASE_IP}.{i}"
            executor.submit(scan_ip, ip)


# ================= MAIN =================
if __name__ == "__main__":
    print("Iniciando scan...\n")
    
    scan_network()

    print("\nScan finalizado.\n")

    print("Hosts ativos encontrados:")
    for host in active_hosts:
        print(host)