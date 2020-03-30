
# Problems enabling the 3.5mm jack (on-board sound card)
I finally managed to get it to work.

Just add “dtparam=audio=on” to /boot/config.txt. 

It also helps to choose the default sound device for ALSA because sometimes the wrong default card is chosen. 

In my case the Roland UM-ONE was chosen as a default, which obviously cannot play PCM data :slight_smile:

##Edit the ALSA config:
```
sudo nano /usr/share/alsa/alsa.conf
defaults.ctl.card “ALSA”
defaults.pcm.card “ALSA”
```

# Audio set up

https://discourse.zynthian.org/t/audio-setup/2647/6  

In partic  
```
The issue was with dbus, I had to change the file /etc/dbus-1/system-local.conf to

<policy user="root">
     <allow own="org.freedesktop.ReserveDevice1.Audio1"/>
</policy>
```

# Debug ?

play audio
```
# aplay -l

# amixer -c1
```

“pstree” command?
qjackctl ?

https://discourse.zynthian.org/t/audio-stops-working/2717/14

# general sites
https://discourse.zynthian.org/
https://wiki.zynthian.org/index.php/Zynthian_FAQ



# and for the hifberry dac + adc

https://github.com/zynthian/zynthian-webconf/commit/27705ca76e67467c61be792584849ef886494ca9

