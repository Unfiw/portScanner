#!/usr/bin/env python3

import socket
from termcolor import colored
import argparse
import threading

def get_arguments():
    parser = argparse.ArgumentParser(description="TCP Port Scanner")
    parser.add_argument("-t", "--target", help="Target to scan (Example: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", help="Port range to scan (Example: -p 1-100)")
    options = parser.parse_args()
    
    return options.target, options.port

def create_socket():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    return s

def port_scanner(host, port):

    s = create_socket()
    
    try:
        s.connect((host, port))
        print(colored(f"[+] Port {port} open", 'green'))
        
        s.close()

    except (socket.timeout, ConnectionRefusedError):
        s.close()


def parse_ports(ports_str):
    
    if '-' in ports_str:
        start, end = map(int,ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
         return map(int, ports_str.split(','))  
    else:
        return (int(ports_str),)


def scan_ports(target, ports):

    threads = []

    for port in ports:
        thread = threading.Thread(target=port_scanner(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def main():

    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(target, ports)

if __name__ == '__main__':
    main()
    
