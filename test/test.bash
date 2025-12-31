#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Reoto Koya
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# テスト1: 許可リストにあるものが全て通過するか.
timeout 3 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log | 
grep 'pass: 3'

timeout 5 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log |
grep 'pass: 5'

timeout 8 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log |
grep 'pass: 8'

#テスト2: 許可リスト外のものを通過させていないかのテスト.
timeout 1 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log |
grep 'pass: 1'

timeout 2 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log |
grep 'pass: 2'

timeout 4 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log |
grep 'pass: 4'

timeout 6 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log |
grep 'pass: 6'


timeout 7 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log |
grep 'pass: 7'


timeout 9 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log |
grep 'pass: 9'

timeout 10 ros2 launch id_parampkg passfilter.launch.py > /tmp/id_parampkg.log
cat /tmp/id_parampkg.log |
grep 'pass: 10'
