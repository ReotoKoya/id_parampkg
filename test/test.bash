#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Reoto Koya
# SPDX-License-Identifier: BSD-3-Clause

set -e

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# テスト1: 許可リストにあるID全てがログに出力されるか検証.
timeout 1m ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log || [ $? -eq 124 ]
cat /tmp/id_parampkg.log | grep  'pass: 3$'
cat /tmp/id_parampkg.log | grep  'pass: 5$'
cat /tmp/id_parampkg.log | grep  'pass: 8$'
cat /tmp/id_parampkg.log | grep  'pass: 10$'
cat /tmp/id_parampkg.log | grep  'pass: 13$'
cat /tmp/id_parampkg.log | grep  'pass: 20$'
cat /tmp/id_parampkg.log | grep  'pass: 24$'
cat /tmp/id_parampkg.log | grep  'pass: 33$'
cat /tmp/id_parampkg.log | grep  'pass: 36$'
cat /tmp/id_parampkg.log | grep  'pass: 37$'
cat /tmp/id_parampkg.log | grep  'pass: 38$'
cat /tmp/id_parampkg.log | grep  'pass: 39$'
cat /tmp/id_parampkg.log | grep  'pass: 40$'
cat /tmp/id_parampkg.log | grep  'pass: 43$'
cat /tmp/id_parampkg.log | grep  'pass: 47$'
cat /tmp/id_parampkg.log | grep  'pass: 49$'
cat /tmp/id_parampkg.log | grep  'pass: 54$'
cat /tmp/id_parampkg.log | grep  'pass: 55$'
