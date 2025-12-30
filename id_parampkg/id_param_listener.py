#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Reoto Koya
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("id_listener")

node.declare_parameter("allowed_id_param", [1003, 1020])
id_param = node.get_parameter("allowed_id_param").value


def cb(msg):
    global node

    if msg.data in id_param:
        node.get_logger().info("pass: %s" % msg)

    else:
        pass

def main():
    sub = node.create_subscription(Int16, "id", cb, 10)
    rclpy.spin(node)
