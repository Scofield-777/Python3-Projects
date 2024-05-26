# Simple Python TCP Client

This Python script is a simple TCP client that connects to a specified host and port, sends an HTTP GET request, and prints the response.

## Prerequisites

- Python 3.x

## Usage

1. Make sure you have Python installed on your system.
2. Save the script to a file, for example, `tcp_client.py`.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using the following command:

   ```bash
   python tcp_client.py --host <target_host> --port <target_port>
   ```
Replace <target_host> with the target hostname or IP address and <target_port> with the target port number.

## Example
Connect to example.com on port 80:

  ```bash
  python tcp_client.py --host example.com --port 80
```

## Script Explanation
The script performs the following steps:

1. Parses command-line arguments for the target host and port using argparse.
2. Creates a TCP socket.
3. Tries to connect to the specified host and port.
4. If the connection is successful, sends an HTTP GET request.
5. Receives and prints the response from the server.
6. Handles various socket errors and exceptions.
7. Closes the socket connection in the finally block.

## Disclaimer
This script is provided for educational purposes only. Ensure that you have permission to connect to the target host and port before running this script. Unauthorized access to computer systems is illegal and unethical.
