#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Reoto Koya
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("id_listener")

node.declare_parameter("allowed_id_param", [])
id_param = node.get_parameter("allowed_id_param").value


def cb(msg):
    global node
    node.get_logger().info("id_sub: %s" % msg)


def main():
    pub = node.create_subscription(String, "id", cb)
    rclpy.spin(node)
