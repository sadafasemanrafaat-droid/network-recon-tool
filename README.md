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
