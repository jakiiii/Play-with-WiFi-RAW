# Configure Monitor Mode

```
root@kali:~# python3 monitor-mode.py
Operating System: Linux
You are running this script as root
Monitor mon0 exists! Continue
Your mon0 MAC address: 81:74:7f:3c:1C:96
```

If you see all interface in your machine: `ifconfig`

```
lo: ...

mon0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        unspec 81:74:7f:3c:1C:96-3C-3B-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 72935  bytes 62752189 (59.8 MiB)
        RX errors 0  dropped 111488  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: ....

wlan1: ....
```
