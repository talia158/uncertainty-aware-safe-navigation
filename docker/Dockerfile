FROM osrf/ros:humble-desktop

ENV DEBIAN_FRONTEND=noninteractive
ENV TURTLEBOT3_MODEL=burger

RUN apt-get update && apt-get install -y \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-robot-localization \
    ros-humble-slam-toolbox \
    ros-humble-turtlebot3* \
    tigervnc-standalone-server \
    xterm \
    x11-apps \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*


# Some Python libs for log/AI 
RUN pip3 install \
    numpy \
    pandas \
    matplotlib

# Create a ROS 2 workspace
RUN mkdir -p /root/ros2_ws/src
WORKDIR /root/ros2_ws

# Use bash and always source ROS in bashrc
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# Copy VNC startup script
COPY docker/start_vnc.sh /root/start_vnc.sh
RUN chmod +x /root/start_vnc.sh

# Default command: start VNC server + desktop
CMD ["/root/start_vnc.sh"]

