#!/bin/bash

if [ ! -f /boot/check ]; then
  sed -i "s/#kernel=kernel7.img/kernel=kernel7.img/" /boot/config.txt
  sed -i "s/#initramfs initrd7.img/initramfs initrd7.img/" /boot/config.txt
  sed -i '$s/$/ boot=overlay/' /boot/cmdline.txt
  touch /boot/check
fi
