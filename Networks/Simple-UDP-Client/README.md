# Simple UDP Client

This Python script is a simple UDP client that connects to a specified host and port, sends a message, and prints the response.

## Prerequisites

- Python 3.x

## Usage

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Save the script to a file, for example, `udp_client.py`.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using the following command:

   ```bash
   python udp_client.py --host <target_host> --port <target_port>
Replace <target_host> with the target hostname or IP address and <target_port> with the target port number.

## Example
Connect to example.com on port 8080:

  ```bash
  python udp_client.py --host example.com --port 8080
```

## Script Explanation
The script performs the following steps:

1. Parses command-line arguments for the target host and port using argparse.
2. Creates a UDP socket.
3. Sends a "Hello" message to the specified host and port.
4. Receives and prints the response from the server.
5. Handles various socket errors and exceptions.
6. Closes the socket connection in the finally block.

## Disclaimer
This script is provided for educational purposes only. Ensure that you have permission to connect to the target host and port before running this script. Unauthorized access to computer systems is illegal and unethical.
