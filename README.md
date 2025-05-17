
# TCP Port Scanner

> A simple and fast multi-threaded TCP Port Scanner built with Python.

----------

## Description

This script allows you to scan a specified range of TCP ports on a target IP address. It utilizes multi-threading to speed up the scanning process and displays open ports in real-time.

----------

## Usage

### Command Line Arguments:

-   `-t`, `--target` — Target IP address to scan.
    
-   `-p`, `--port` — Port range to scan. This can be:
    
    -   A range (e.g., `1-100`)
        
    -   A list of ports separated by commas (e.g., `22,80,443`)
        
    -   A single port (e.g., `8080`)
        

### Example:

```
python3 scanner.py -t 192.168.1.1 -p 1-100
```

> This will scan ports from 1 to 100 on the target `192.168.1.1`.

----------

## Output

-   Open ports are displayed in green with the format:
    

```
[+] Port 22 open
[+] Port 80 open
```

-   Closed or filtered ports are ignored to reduce clutter.
    

----------

## How It Works

1.  **Argument Parsing:**
    
    -   Uses `argparse` to parse the target IP and port range from command line arguments.
        
2.  **Socket Creation:**
    
    -   A TCP socket is created for each port to check its status.
        
3.  **Multi-threading:**
    
    -   Each port scan runs in its own thread for faster results.
        
4.  **Port Scanning:**
    
    -   If the connection is successful, the port is marked as **open**.
        
5.  **Output Display:**
    
    -   Results are displayed in real-time as the scan progresses.
        

----------

## Dependencies

-   `termcolor` for colored terminal output:
    

```
pip install termcolor
```

----------

## Author

Developed by **Marco Becerra**
