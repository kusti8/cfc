# Coding for Community - Streetlight - Hansen Ltd.
## by Aruj Jain and Gustav Hansen

## Installation
Installation is simple:
1. Download [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/)
and use it to write the ready made image, available [here]() to a SD card.

2. Put the SD card and Ethernet cable into the Pi. Plug the power in.

3. Wait for it to start up. After a minute, go to http://raspberrypi.local:8080
If that doesn't work, try and find the IP address of the Pi and replace
raspberrypi.local with that.

4. Login using the username "admin" and the password "changeme"
![Login](https://github.com/kusti8/cfc/blob/master/login.png)

5. Change the password under Admin > Account to something secure

6. Go to Admin > Network and change a few things. Change the IP address to
192.168.3.x where X is a unique number for each Pi. Change the SSID if you wish,
but it must be changed on each Pi.
![WiFi](https://github.com/kusti8/cfc/blob/master/wifi.png)

7. To change the Instapush ID, connect the Pi to a monitor and keyboard, login
with "pi" and "raspberry", run `nano checker.py` and edit the AppID and Secret.

8. That's it! Press save and press reboot. Pull the Ethernet cable while it is
rebooting.

9. **For the gateway (the one that connects to the Internet),
there's one extra step. Go to wired and change the IP address to a free
IP address for your own network. Ask IT for a free address. Then, change
DHCP start to 2 and DHCP end to 254. This will be the only Pi wired to the Internet.**
![Wired](https://github.com/kusti8/cfc/blob/master/wired.png)

The Pis will connect automatically and automatically make a mesh. Plug them
in and no further configuration is needed.
