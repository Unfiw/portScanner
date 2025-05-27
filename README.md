
# TCP Port Scanner

Advanced multi-threaded TCP port scanner with banner grabbing capabilities.

----------

## Description

This script allows you to scan a specified range of TCP ports on a target IP address. It utilizes multi-threading to speed up the scanning process, captures basic service banners, and displays open ports in real-time. Graceful termination is supported via `Ctrl+C`.

> [!NOTE]  
This script scans a specified range of TCP ports on a target IP address.  
It uses multi-threading for speed, captures basic service banners, and supports graceful shutdown with `Ctrl+C`.


----------

## Features

-  Multi-threaded scanning using `ThreadPoolExecutor` for high performance
-  Accepts single port, list of ports, or port range
-  Banner grabbing via `HEAD / HTTP/1.0` request
-  Graceful shutdown on `SIGINT` (`Ctrl+C`)
-  Colored output for better readability
-  Robust error handling for timeouts and refused connections

----------

## Usage

### Command Line Arguments:

> [!IMPORTANT]  
The following arguments are required for execution:

- `-t`, `--target` — Target IP address to scan.
- `-p`, `--port` — Port range to scan. Accepted formats:
  - A range (e.g., `1-100`)
  - A comma-separated list (e.g., `22,80,443`)
  - A single port (e.g., `8080`)

### Example:

```bash
python3 scanner.py -t 192.168.1.1 -p 20-80
python3 scanner.py -t 192.168.1.1 -p 22,80,443
python3 scanner.py -t 192.168.1.1 -p 8080
```

## Output

-   Open ports are displayed in **green**:

`[+] Port 80  is  open` 

-   Basic banners (HTTP headers or responses) are printed in **blue** when available:
    


`[+] Port 80  is  open  Server: Apache/2.4.41 (Ubuntu) Date: Mon, 27 May 2025  10:00:00 GMT` 

-   Closed/filtered ports are silently ignored to reduce output clutter.

## How It Works

1.  **Argument Parsing:**
    
    -   Uses `argparse` to retrieve the target IP and port(s).
        
2.  **Port Parsing:**
    
    -   Interprets ranges (`start-end`), comma-separated values (`p1,p2,...`), or single port.
        
3.  **Threaded Scanning:**
    
    -   Executes scans concurrently via `ThreadPoolExecutor` (up to 50 workers).
        
4.  **Connection Attempt:**
    
    -   Sends a basic `HEAD` request if connection is successful.
        
5.  **Banner Grabbing:**
    
    -   Reads and displays the response if available.
        
6.  **Graceful Exit:**
    
    -   On `Ctrl+C`, all open sockets are closed before exit.
 
 
## Dependencies

Install required module:

```bash
pip install termcolor` 
```

----------

## Author

Developed by **Marco Becerra**
