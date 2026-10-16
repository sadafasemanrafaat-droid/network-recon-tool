# Network Recon Tool

A Python-based network reconnaissance tool for TCP port scanning and HTTP service detection.

## Description

This project is a simple network reconnaissance tool built with Python.

The tool scans a specified range of TCP ports on a target host, identifies open ports, and checks whether an open port is running an HTTP service.

The project was developed as a practical cybersecurity learning project to understand network reconnaissance, TCP connections, sockets, HTTP requests, and service detection.

## Features

- Target host/IP input
- Custom TCP port range
- TCP port scanning
- Open port detection
- HTTP service detection
- HTTP request sending
- HTTP response inspection
- Scan time calculation
- Simple terminal output

## How to Run

### 1. Start a local HTTP server

For testing in a safe local environment:

```bash
python3 -m http.server 9000 --bind 127.0.0.1
```
### 2. Run the scanner
Open another terminal and run:
```bash
python3 recon.py
```
### 3. Enter the target information

Example:

```text
Enter Target: 127.0.0.1
Enter start port: 8995
Enter end port: 9000
```

### 4.Example Output
```text
NETWORK RECON TOOL
------------------
Service: HTTP
------------------
Open ports: [9000]
----------------------
Scan Time: 5.21 seconds
```

## Technologies Used
Python 3
Socket Programming
TCP
HTTP
Linux / WSL
Git
GitHub
## Project Purpose
The purpose of this project is to practice basic network reconnaissance concepts and Python socket programming in a controlled local environment.
The project demonstrates how a security tool can:
1. Scan TCP ports
2. Identify open ports
3. Connect to an open service
4. Send an HTTP request
5. Inspect the HTTP response
6. Identify an HTTP service
Security Note
This tool is intended for educational purposes and authorized testing only.
Use it only against systems you own or have explicit permission to test.
Future Improvements
- HTTP banner extraction
- Better error handling
- Faster port scanning
- Support for additional services
- Cleaner scan reports
- Command-line arguments
