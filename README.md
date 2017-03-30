# Coding for Community - Streetlight - Hansen Ltd.
## by Aruj Jain and Gustav Hansen

## Requirements per Pi
 - A Pi3
 - A Power supply (5V at around 1-2A)
 - A LDR (light dependent resistor)
 - A 10 uF capacitor
 - Wires
 - A 4 GB or larger SD card

## Phone notification
Download Instapush to each phone and login to receive notifications.

## Installation
Installation is simple:
1. Download [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/)
and use it to write the ready made image, available [here](https://github.com/kusti8/cfc/releases/download/v1.1/cfc-non-instapush-2.zip) to a SD card.

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

7. Go to Mesh and change the identifier number to a unique number for each Pi.
This is the number you will be given when a streetlight goes out, so it would
be best to make a map corresponding number with streetlight.

8. That's it! Press save and press reboot. Pull the Ethernet cable while it is
rebooting.

9. **For the gateway (the one that connects to the Internet),
there's one extra step. Go to wired and change the IP address to a free
IP address for your own network. Ask IT for a free address. Then, change
DHCP start to 2 and DHCP end to 253. This will be the only Pi wired to the Internet. Also change LAN to WAN!**
![Wired](https://github.com/kusti8/cfc/blob/master/wired.png)

The Pis will connect automatically and automatically make a mesh. Plug them
in and no further configuration is needed.

## The circuit
Built the following circuit diagrammed.
![Circuit](https://github.com/kusti8/cfc/blob/master/circuit.png)
![Schematic](https://github.com/kusti8/cfc/blob/master/schematic.png)

## Custom Instapush
Since the OS has been hardened against power surges, you need to temporarily
reverse that. Boot the Pi up and run `sudo nano /boot/config.txt` and comment,
with `#` out the last two lines:
```
#kernel=kernel7
#initramfs initrd7.img
```
Press [CTRL]+[X] to exit, [ENTER], and then [Y]
Then, run `sudo nano /boot/cmdline.txt`
And remove `boot=overlay`
Exit the same way. Run `sudo reboot` and then edit checker.py by running
`nano checker.py` and changing the instapush credentials.
Undo the changes done before and it should work!
