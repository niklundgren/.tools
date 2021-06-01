# System and Network Administration
# This will be where I post tools, tricks, and solutions to help me run servers

# School specific
# Symptoms: can ping IP, can't ping web address
Solution: nano /etc/resolv.conf, add `nameserver <ip addr>`
The problem:
	Nameservers change web addresses to ips to help guide web connection.
The school's nameserver is not super great, so adding google's nameserver helps
resolve IP addresses more regularly and quickly. Nameservers can be assesed wth 
namebench (currently installed on amdryz).
	Best for UCDavis: 8.8.8.8, 169.237.250.250, 169.237.1.250


