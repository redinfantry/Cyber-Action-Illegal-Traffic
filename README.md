# Cyber-Action-Illegal-Traffic
: This project works in coherence with existing access controls and instantly blocks the suspicious Ip address for a particular time and reports it as cyber incident in logs.

# Additional Information
This code uses the subprocess module to run the iptables command with the necessary parameters to block incoming traffic from the specified IP address. The -A option specifies that the rule should be appended to the INPUT chain, -s specifies the source IP address, and -j specifies that the traffic should be dropped.

Note that the above code assumes that the script is run with root privileges. Also, the iptables command may have different syntax or options depending on the firewall software and hardware used.

# Usage
MAke sure to change the configurations as per your environment like ip address, etc
