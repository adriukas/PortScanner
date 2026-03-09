#Function: display_results(open_ports)
#Logic: Take a list of open ports and print them with their common service names (e.g., if port 80 is open, print "Port 80 (HTTP) is OPEN").
#Tip: Use a dictionary to map common ports like 22 (SSH), 80 (HTTP), and 443 (HTTPS).

def display_results(open_ports):
    port_names = {22:"SSH", 53:"DNS", 80:"HTTP", 443:"HTTPS", 3306:"MySQL", 8080:"HTTP-ALT", 25:"SMTP", 21:"FTP"}

    if not open_ports:
        print("No open ports found.")
    else:
        for port_number in open_ports:
            if port_number in port_names:
                service_name = port_names[port_number]
                print("Port {0} ({1}) is OPEN".format(port_number, service_name))
            else:
                print("Port {0} (Unknown Service) is OPEN".format(port_number))