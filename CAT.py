import subprocess

# Define the IP address to block
ip_address = "192.168.1.100"

# Run the iptables command to block incoming traffic from the specified IP address
subprocess.run(["iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"])
