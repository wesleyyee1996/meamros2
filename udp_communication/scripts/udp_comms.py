#!/usr/bin/env python

import rospy
import socket
UDP_PORT = 2522
UDP_IP = ""
from robot_control.msg import MotorDrive

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("Connected to local IP ", s.getsockname()[0], " on port ", UDP_PORT)
    s.close()

def udp_comms():
    pub = rospy.Publisher('motor_control', MotorDrive, queue_size=10)
    rospy.init_node('udp_communication', anonymous=True)
    rate = rospy.Rate(50)

    get_local_ip()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    print("Now listening!")

    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(1024)
        #print(data)
        

if __name__ == '__main__':
    try:
        udp_comms()
    except rospy.ROSInterruptException:
        pass
