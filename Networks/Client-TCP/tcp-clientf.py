import argparse
import socket

# Setting up argument parsing
parser = argparse.ArgumentParser(description="-----Simple Python TCP Client-----")
parser.add_argument('--host', type=str, required=True, help="The Target Host to connect.")
parser.add_argument('--port', type=int, required=True, help="The Target Port to connect.")
args = parser.parse_args()

target_host = args.host
target_port = args.port

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((target_host, target_port))
    print("\n[+] Connected\n")
    try:
        client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
        try:
            response = client.recv(4096)
            if not response:
                print("\n[-] No Response Received\n")
            else:
                print(response.decode())
        except socket.error as error0:
            print(f"\n[-] Data Transmission Failed: {error0}\n")
        except Exception as error9:
            print("\n[-] Unexpected Error occurred while sending data.\n")
    except socket.error as error:
        print(f"\n[-] Connection Failed: {error}\n")
    except Exception as error1:
        print("\n[-] Unexpected Error occurred while sending data.\n")
except socket.herror:
    print("\n[-] Address Related Error\n")
except socket.timeout:
    print("\n[-] Timeout Error\n")
except socket.error as err:
    print(f"\n[-] Connection Failed: {err}\n")
except Exception as e:
    print("\n[-] Unexpected Error Occurred\n")
finally:
    client.close()
