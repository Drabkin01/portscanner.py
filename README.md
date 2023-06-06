# Network Scanner

This repository contains a Python script for a simple network scanner. The script allows you to scan one or multiple IP addresses for open ports.

## Prerequisites

To run this script, you need to have Python installed on your system. Additionally, you should have the `socket` module available, which is usually included in the Python standard library.

## Usage

To use the network scanner, follow these steps:

1. Clone the repository to your local machine or download the script directly.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Execute the script by running the following command:

   ```
   python network_scanner.py
   ```

4. You will be prompted to enter the targets to scan and the number of ports to scan.
   - For the targets, enter the IP addresses you want to scan, separated by commas. For example: `192.168.0.1, 192.168.0.2`.
   - For the number of ports, enter the desired number of ports to scan on each target.

5. The script will start scanning the specified targets and ports. It will print a message for each open port found.

## Example

Here's an example usage of the script:

```
[*] Enter Targets To Scan (split them by ,): 192.168.0.1, 192.168.0.2
[*] Enter How Many Ports You Want To Scan: 100

Starting Scan For 192.168.0.1
[+] Port Opened 80
[+] Port Opened 443

Starting Scan For 192.168.0.2
[+] Port Opened 22
[+] Port Opened 80
```

In this example, we scan two IP addresses (`192.168.0.1` and `192.168.0.2`) for the first 100 ports. The script finds open ports 80 and 443 on `192.168.0.1`, and ports 22 and 80 on `192.168.0.2`.

## Notes

- The script uses the `socket` module to establish a connection with each target IP address and port. If a connection is successfully established, it indicates that the port is open.
- The script utilizes exception handling to ignore any errors that may occur during the scan, such as connection timeouts or refused connections.

Feel free to customize and modify the script according to your specific needs. Happy scanning!
