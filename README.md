# 数値フィルタパッケージ

![test](https://github.com/ReotoKoya/id_parampkg/actions/workflows/test.yml/badge.svg)

## 概要
- 入力される数値から, 許可リストにある数値のみを出力するフィルタパッケージです.\
  許可リストの数値はyamlファイルを編集すれば書き換えられます.

## 各ノード説明
### id_talker
- yamlファイルの全体リストとして設定した, 1から60の数値を読み込んで, 繰り返し送信します.
  - 出力トピック名: input_id
  - メッセージ型: std_msgs/msg/Int16

### id_filter
- input_idに流れた数値をフィルタリングし, yamlファイルの許可リストにある数値のみfiltered_idに出力する.
  - 入力トピック名: input_id
  - 出力トピック名: filtered_id
  - メッセージ型: std_msgs/msg/Int16

### id_listener
- filtered_idからフィルタリングされて通過した数値を受け取り, ログに出力する.
  - 入力トピック名: filtered_id
  - メッセージ型: std_msgs/msg/Int16

## 実行例
- yamlファイルに記述した1から60の数値リストの中から\
  許可リストにある数値のみを"pass:"としてログに出力する例です.

  ```
  $ ros2 launch id_parampkg passfilter.launch.py
  [INFO] [launch]: All log files can be found below /home/reoto/.ros/log/2026-01-08-13-27-55-969009-reotokoya-30269
  [INFO] [launch]: Default logging verbosity is set to INFO
  [INFO] [id_talker-1]: process started with pid [30272]
  [INFO] [id_listener-2]: process started with pid [30274]
  [INFO] [id_filter-3]: process started with pid [30276]
  [id_talker-1] [INFO] [1767846477.643190580] [id_talker]: sent: 1
  [id_talker-1] [INFO] [1767846478.625400323] [id_talker]: sent: 2
  [id_talker-1] [INFO] [1767846479.625326523] [id_talker]: sent: 3
  [id_listener-2] [INFO] [1767846479.646180518] [id_listener]: pass: 3
  [id_talker-1] [INFO] [1767846480.625402098] [id_talker]: sent: 4
  [id_talker-1] [INFO] [1767846481.626199690] [id_talker]: sent: 5
  [id_listener-2] [INFO] [1767846481.628827372] [id_listener]: pass: 5
  [id_talker-1] [INFO] [1767846482.625760644] [id_talker]: sent: 6
  [id_talker-1] [INFO] [1767846483.626435285] [id_talker]: sent: 7
  [id_talker-1] [INFO] [1767846484.626278768] [id_talker]: sent: 8
  [id_listener-2] [INFO] [1767846484.628686818] [id_listener]: pass: 8
  [id_talker-1] [INFO] [1767846485.625710960] [id_talker]: sent: 9
  ```

### 補足
実行例では1から60の数値しか送信していませんが, 1から60までの数値でなくても, 構いません.\ 
launchファイルの実行を止めたい場合は, キーボードで「Ctrl + C　」を押してください.
テストで使用しているyqコマンドは, 「sudo snap install yq」でインストールできます.

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
- [【yqコマンド活用】yqコマンドでYAMLファイルを自由自在に操作する](https://deep.tacoskingdom.com/blog/203)
