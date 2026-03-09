# Python Port Scanner

A lightweight, TCP port scanner built in Python. This tool identifies open ports on a target IP address and maps them to common service names (SSH, DNS, HTTP, etc.).

## Project Structure
The project is split into three modules to ensure separation of concerns:
* **`run_scan.py`**: The main entry point. Handles user input and orchestrates the scanning process.
* **`scanner_engine.py`**: The core networking logic using Python's `socket` library.
* **`reporter.py`**: Handles output formatting and logs results to `scan_report.txt`.


### Prerequisites
* Python 3.x
* Basic understanding of networking (IP addresses and Ports)

### Installation
1. Clone or move the files into a single directory:
   ```bash
   mkdir PortScanner
   mv run_scan.py scanner_engine.py reporter.py PortScanner/