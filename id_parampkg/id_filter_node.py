#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Reoto Koya
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node, id_param

    if msg.data in id_param:
        pub.publish(msg)    
    else:
        pass

def main():
    global node, pub, id_param

    rclpy.init()
    node = Node("id_filter")

    node.declare_parameter("allowed_id_param", [])
    id_param = node.get_parameter("allowed_id_param").value

    sub = node.create_subscription(Int16, "input_id", cb, 10)
    pub = node.create_publisher(Int16, "filtered_id", 10)

    rclpy.spin(node)
