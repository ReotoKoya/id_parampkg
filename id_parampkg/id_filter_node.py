#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Reoto Koya
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()

node.declare_parameter("allowed_id_param", [3, 8])
id_param = node.get_parameter("allowed_id_param").value

node = Node("id_talker")

node.declare_parameter("all_id_param", [1, 2])
id_param = node.get_parameter("all_id_param").value

pub = node.create_publisher(Int16, "input_id", 10)
n = 0

def cb(msg):
    global node

    if msg.data in id_param:
        node.get_logger().info("pass: %s" % msg.data)

    else:
        pass

def main():
    sub = node.create_subscription(Int16, "filtered_id", cb, 10)
    rclpy.spin(node)


