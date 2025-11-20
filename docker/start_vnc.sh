#!/bin/bash
set -e

# Set default robot model if not set
export TURTLEBOT3_MODEL=${TURTLEBOT3_MODEL:-burger}

# Set a default VNC password ("ros2")
if [ ! -f /root/.vnc/passwd ]; then
  mkdir -p /root/.vnc
  echo "ros2" | vncpasswd -f > /root/.vnc/passwd
  chmod 600 /root/.vnc/passwd
fi

# Kill any existing VNC server on :1 
/usr/bin/vncserver -kill :1 > /dev/null 2>&1 || true

# Start VNC server on display :1
/usr/bin/vncserver :1 -geometry 1920x1080 -depth 24 \
  -localhost no \
  -xstartup /usr/bin/xterm

echo "VNC server started on :1 (port 5901). Password is 'ros2'."

# Keep the container alive forever
tail -f /dev/null
