import HiwonderSDK.Board as Board
import time

Board.setBuzzer(1) #启动蜂鸣器
time.sleep(1)
Board.setBuzzer(0) #停止蜂鸣器
time.sleep(0.5)

for i in range(10):
    Board.setBuzzer(1) #启动蜂鸣器
    time.sleep(0.05)
    Board.setBuzzer(0)
    time.sleep(0.5)

