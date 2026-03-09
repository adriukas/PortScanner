#Import: scanner_engine and reporter.
#ogic: Define a target (like 127.0.0.1 for your own machine) and a range of ports (e.g., 1 to 1024).
#Loop: Call the engine for each port, collect the "Open" ones in a list, and pass that list to the reporter.


   
import reporter
import scanner_engine

target = input("Enter IP address:")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

open_ports = []


for port in range(start_port, end_port + 1):
    if scanner_engine.check_port(target, port):
        open_ports.append(port)

print("Now scanning ports from {0} to {1} on {2}...".format(start_port, end_port, target))
reporter.display_results(open_ports)
