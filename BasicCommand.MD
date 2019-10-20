# BASIC COMMAND


Configuration: `ifconfig`

Interface Down: `ifconfig <interface> down`

Interface Up:  `ifconfig <interface> up`

For Checking WiFi Device: `airmon-ng`

Monitor mood on: `airmon-ng start <interface>`

Monitor mood off: `airmon-ng stop <interface>`

Necessary to run it two or three time consecutively: `airmon-ng check kill`

VAP / VIP (Virtual Interface) will be created *mon0* from the parent *wlan0*. After having the VAP created, 
it is necessary to bring the interface up:

`iw dev wlan0 interface add mon0 type monitor`

`ifconfig <interface> up`

Switch to channel: `iw dev <interface> set channel <number. ex. 6>`

*In some laptops, it is possible that the airplane mode is enabled, disabling any RF transmission. Therefore, 
any wireless card (Wi-Fi, Bluetooth...) would be disabled for transmitting. To force enabling it just execute:*

`rfkill unblock all`

Mac changer: `macchanger -A <interface>`

