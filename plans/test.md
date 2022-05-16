# Test Plan

[v2.1](https://github.com/USDOT-SDC/sdc-dot-gitlab/tree/2.1)

* Prior to deployment, log on into GitLab and capture inventory of existing projects.
* After deployment, log on into GitLab and verify that all projects are present.
* After deployment, verify that GitLab is functioning normally
  * Log into GitLab
  * Ensure navigation works
  * Ensure you can do the following operations:
    * Create own project
    * Create files, edit files, delete files
    * Edit project settings
    * Delete project 

* Verify that iptables firewall rules persist through reboots
  * SSH into GitLab EC2 instance
  * Perform reboot
    * sudo reboot
  * SSH into GitLab EC2 instance again
  * Print out firewall rules
    * sudo iptables-save
  * Verify that the following rules for SSH, HTTP, and BigFix/XDR connections are present
```
    -A IN_public_allow -p tcp -m tcp --dport 22 -m conntrack --ctstate NEW,UNTRACKED -j ACCEPT
    -A IN_public_allow -p tcp -m tcp --dport 80 -m conntrack --ctstate NEW,UNTRACKED -j ACCEPT
    -A IN_public_allow -p tcp -m tcp --dport 52311 -m conntrack --ctstate NEW,UNTRACKED -j ACCEPT
    -A IN_public_allow -p udp -m udp --dport 52311 -m conntrack --ctstate NEW,UNTRACKED -j ACCEPT
```


