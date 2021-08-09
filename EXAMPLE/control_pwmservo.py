import HiwonderSDK.Board as Board
import time

Board.setPWMServoPulse(1, 1500, 100) #控制1号pwm舵机用100ms时间转到1500位置
                                     #位置范围为500 ～ 2500对应0～180度
time.sleep(1)
Board.setPWMServoPulse(1, 500, 1000)
time.sleep(2)
Board.setPWMServoPulse(1, 2500, 2000)
time.sleep(3)
Board.setPWMServoPulse(1, 1500, 1000)
time.sleep(2)
