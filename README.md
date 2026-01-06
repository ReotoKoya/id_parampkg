# IDフィルタパッケージ

![test](https://github.com/ReotoKoya/id_parampkg/actions/workflows/test.yml/badge.svg)

## 概要
- リストにある全てのIDから, 許可リストにあるIDのみを出力するフィルタパッケージです.

## ノード

- トピック: id
- メッセージ型: std_msgs/msg/Int16
- ノード名: id_talker 
- ノード名: id_listener

## 実行環境
- Ubuntu 22.04 LTS on Windows
- ROS 2 Humble Hawksbill

## 実行方法
-以下のコマンドを任意のディレクトリで実行してください.

  ```
  $ ros2 launch id_parampkg passfilter.launch.py
  ```

### 実行例
- yamlファイルに記述した1から10の数値リストの中から\ 
  許可リストにある3, 5, 8の数値のみをパスする例です.

  ```
  $ ros2 launch id_parampkg passfilter.launch.py
  [INFO] [launch]: All log files can be found below /home/reoto/.ros/log/2025-12-31-23-25-22-996268-reotokoya-50372
  [INFO] [launch]: Default logging verbosity is set to INFO
  [INFO] [id_talker-1]: process started with pid [50378]
  [INFO] [id_listener-2]: process started with pid [50380]
  [id_listener-2] [INFO] [1767191125.123733079] [id_listener]: pass: 3
  [id_listener-2] [INFO] [1767191126.070253071] [id_listener]: pass: 5
  [id_listener-2] [INFO] [1767191127.563359766] [id_listener]: pass: 8

## テスト環境
- Local: Ubuntu 22.04 LTS on Windows 11
- ROS: ROS 2 Humble Hawksbill
- GitHub Actions: Ubuntu 22.04 

## 著作権 ・ライセンス
- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます．
- @ 2025 Reoto Koya

## 参考資料
- [第7回 : GitHub でのテスト](https://ryuichiueda.github.io/slides_marp/robosys2025/lesson7.html)
- [第8回 : Robot Operating System (ROS 2)](https://ryuichiueda.github.io/slides_marp/robosys2025/lesson8.html)
- [第9回 : ROS 2の通信と型](https://ryuichiueda.github.io/slides_marp/robosys2025/lesson9.html)
- [第10回 : ROSシステムのテスト](https://ryuichiueda.github.io/slides_marp/robosys2025/lesson10.html)
