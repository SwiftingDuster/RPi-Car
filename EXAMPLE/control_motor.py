import HiwonderSDK.Board as Board
import time

Board.setMotor(1, 50) #马达1,50速度正转, 速度为 100~-100
time.sleep(3)
Board.setMotor(1, 0)
time.sleep(1)
Board.setMotor(1, -50) #马达可以是1、2、3、4
time.sleep(3)
Board.setMotor(1, 0)
