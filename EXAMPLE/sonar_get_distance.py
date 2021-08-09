import HiwonderSDK.Sonar
import time

sonar = HiwonderSDK.Sonar.Sonar()

while True:
    print(sonar.getDistance(), 'mm')
    time.sleep(1)
