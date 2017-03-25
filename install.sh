#!/bin/bash
if [[ $EUID -ne 0 ]]; then
  echo "You must be a root user" 2>&1
  exit 1
fi
mv checker.py /home/pi/
mv lightcheck.service /etc/systemd/system/lightcheck.service
systemctl enable lightcheck
