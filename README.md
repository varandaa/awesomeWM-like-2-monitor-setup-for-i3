# awesomeWM-like-2-monitor-setup-for-i3
A Python script that makes it so i3 has per-monitor workspaces like in awesomeWM. 

To use it, remove the instructions related to workspace moving and switching in your i3 config file and add this: 

``` conf
############################
# MONITOR DEFINITIONS
############################
# run 'xrandr --listmonitors' and put your monitor names here 
set $mon1 eDP
set $mon2 HDMI-0

############################
# WORKSPACE DEFINITIONS
############################
# Monitor 1 (eDP)
set $ws1  "1"
set $ws2  "2"
set $ws3  "3"
set $ws4  "4"
set $ws5  "5"
set $ws6  "6"
set $ws7  "7"
set $ws8  "8"
set $ws9  "9"
set $ws10 "10"

# Monitor 2 (HDMI-0)
set $ws11 "11"
set $ws12 "12"
set $ws13 "13"
set $ws14 "14"
set $ws15 "15"
set $ws16 "16"
set $ws17 "17"
set $ws18 "18"
set $ws19 "19"
set $ws20 "20"

############################
# PIN WORKSPACES TO MONITORS
############################
# eDP
workspace $ws1  output $mon1
workspace $ws2  output $mon1
workspace $ws3  output $mon1
workspace $ws4  output $mon1
workspace $ws5  output $mon1
workspace $ws6  output $mon1
workspace $ws7  output $mon1
workspace $ws8  output $mon1
workspace $ws9  output $mon1
workspace $ws10 output $mon1

# HDMI-A-0
workspace $ws11 output $mon2
workspace $ws12 output $mon2
workspace $ws13 output $mon2
workspace $ws14 output $mon2
workspace $ws15 output $mon2
workspace $ws16 output $mon2
workspace $ws17 output $mon2
workspace $ws18 output $mon2
workspace $ws19 output $mon2
workspace $ws20 output $mon2

############################
# MOVE WINDOW BETWEEN MONITORS (AWESOME-LIKE)
############################
# dont forget to 'chmod +x' the file and change the path if you saved the script in a different location 
bindsym $mod+Shift+1 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 1 
bindsym $mod+Shift+2 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 2 
bindsym $mod+Shift+3 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 3 
bindsym $mod+Shift+4 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 4 
bindsym $mod+Shift+5 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 5 
bindsym $mod+Shift+6 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 6 
bindsym $mod+Shift+7 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 7 
bindsym $mod+Shift+8 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 8 
bindsym $mod+Shift+9 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 9 
bindsym $mod+Shift+0 exec --no-startup-id /home/user/.config/i3/smart_switch.py move 10 


# Monitor 1 (eDP) workspaces
bindsym $mod+1 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 1 
bindsym $mod+2 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 2 
bindsym $mod+3 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 3 
bindsym $mod+4 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 4 
bindsym $mod+5 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 5 
bindsym $mod+6 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 6 
bindsym $mod+7 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 7 
bindsym $mod+8 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 8 
bindsym $mod+9 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 9 
bindsym $mod+0 exec --no-startup-id /home/user/.config/i3/smart_switch.py switch 0 

# Monitor 2 (HDMI-A-0) workspaces
# bindsym $mod+Shift+1 workspace $ws11
# bindsym $mod+Shift+2 workspace $ws12
# bindsym $mod+Shift+3 workspace $ws13
# bindsym $mod+Shift+4 workspace $ws14
# bindsym $mod+Shift+5 workspace $ws15
# bindsym $mod+Shift+6 workspace $ws16
# bindsym $mod+Shift+7 workspace $ws17
# bindsym $mod+Shift+8 workspace $ws18
# bindsym $mod+Shift+9 workspace $ws19
# bindsym $mod+Shift+0 workspace $ws20


############################
# QUICK OUTPUT SWITCH
############################
# mod+o to send a window to the other monitor
bindsym $mod+o \
    move container to output right; \
    exec --no-startup-id xdotool mousemove --screen 1 100 10

############################
# AUTO CREATE WORKSPACES ON START
############################
exec --no-startup-id i3-msg workspace 1
exec --no-startup-id i3-msg workspace 11
```