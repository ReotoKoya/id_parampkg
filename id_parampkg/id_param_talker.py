#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Reoto Koya
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init() 
node = Node("all_id_pub")

node.declare_parameter("all_id_param", ["1001", "1002"])
id_param = node.get_parameter("all_id_param").value

pub = node.create_publisher(Int16, "id", 10)
n = 0

def cb():
    global n

    if len(id_param) == 0:
        return

    msg = Int16()
    msg.data = id_param[n]
    pub.publish(msg)
    n += 1

def main():
    node.create_timer(0.5 cb)
    rclpy.spin(node)
