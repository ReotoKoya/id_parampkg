#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Reoto Koya
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("id_listener")

def cb(msg):
  
    node.get_logger().info("pass: %s" % msg.data)

def main():
    sub = node.create_subscription(Int16, "filtered_id", cb, 10)
    rclpy.spin(node)
