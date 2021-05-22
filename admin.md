# System and Network Administration
# This will be where I post tools, tricks, and solutions to help me run servers

# School specific
The school's nameserver is not super great, so adding google's nameserver helps
resolve IP addresses more regularly.
Symptoms: can ping IP, can't ping web address
Solution: nano /etc/resolv.conf, add `nameserver 8.8.8.8`

