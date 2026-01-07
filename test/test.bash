#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Reoto Koya
# SPDX-License-Identifier: BSD-3-Clause

set -e

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# テスト1: 許可リストの数値とログに出力される数値が一致しているかのテスト.
timeout 1m ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log || [ $? -eq 124 ]
cat /tmp/id_parampkg.log | grep "pass:" | sed 's/.*pass: //' > log.txt

yq '.id_filter.ros__parameters.allowed_id_param[]' $dir/ros2_ws/src/id_parampkg/config/params.yaml > id_list.txt

diff id_list.txt log.txt

# テスト2: 許可リストにないIDがログに出力されていないかテスト.
timeout 1m ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log || [ $? -eq 124 ]
















