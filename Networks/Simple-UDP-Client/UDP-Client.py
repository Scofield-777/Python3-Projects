import argparse
import socket

# Setting UP Argument Parsing
parser = argparse.ArgumentParser(description="-----Simple UDP Client-----")
parser.add_argument('--host', type=str, required=True, help="The target host to connect.")
parser.add_argument('--port', type=str, required=True, help="The target port to connect.")
args = parser.parse_args()

target_host = args.host
target_port = args.port

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    client.sendto(b"Hello",(target_host, target_port))
    data, addr = client.recvfrom(4096)
    print(data.decode())
except socket.error as error0:
    print(f"\n[-] Data Transmission Failed: {error0}\n")
except Exception as error9:
    print("\n[-] Unexpected Error occurred.\n")
finally:
    client.close()

