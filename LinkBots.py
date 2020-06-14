
import linkbot
import math
import time

#initialize bots
robots = [
   linkbot.Linkbot("D7DQ"),
   linkbot.Linkbot("PRNL"),
   linkbot.Linkbot("D3H3"),
   linkbot.Linkbot("7C6R")
]
#small bots
smallBots = [
   robots[1],
   robots[2]
]
#big bots
bigBots = [
   robots[0],
   robots[3]
]

#assign size
SMALLBOT_90 = 1
BIGBOT_90 = 1.6/2

# Small wheels: 1.45 = 180 degrees at 1-speed

for i in robots:
   i.stop()

time.sleep(3)

#add moves
for i in smallBots:
   i.wheel_diameter = 3.5
   i.track_width = 3.7
   i.set_led_color_rgb('#FFFF00');

for i in bigBots:
   i.wheel_diameter = 5
   i.track_width = 3.7
   i.set_led_color_rgb('#FFFF00');

bigBots[0].set_joint_states(1, 0, 1)
bigBots[1].set_joint_states(-1, 0, -1)

time.sleep(BIGBOT_90*2)

for i in smallBots:
   i.set_joint_states(1, 0, -1)

for i in bigBots:
   i.set_joint_states(1, 0, -1)

time.sleep(2)

for i in robots:
   i.stop()

smallBots[0].set_joint_states(-1, 0, -1)
smallBots[1].set_joint_states(1, 0, 1)

time.sleep(SMALLBOT_90*2)

for i in smallBots:
   i.stop()

bigBots[0].set_joint_states(1, 0, 1)
bigBots[1].set_joint_states(-1, 0, -1)

time.sleep(BIGBOT_90*2)

for i in smallBots:
   i.set_joint_states(1, 0, -1)

for i in bigBots:
   i.set_joint_states(1, 0, -1)

time.sleep(2)

for i in robots:
   i.stop()

for i in smallBots:
   i.set_joint_states(1, 0, -1)

time.sleep(2)

smallBots[0].set_joint_states(-1, 0, -1)
smallBots[1].set_joint_states(1, 0, 1)
time.sleep(SMALLBOT_90*0.35)

for i in robots:
   i.stop()

for i in bigBots:
   i.set_joint_states(1, 0, -1)

time.sleep(1.5)

bigBots[0].set_joint_states(1, 0, 1)
bigBots[1].set_joint_states(-1, 0, -1)

time.sleep(BIGBOT_90*0.35)

for i in bigBots:
   i.set_joint_states(-1, 0, 1)

time.sleep(1.25)

for i in robots:
   i.stop()

time.sleep(2)

for i in robots:
   i.set_joint_states(1, 0, -1)

time.sleep(2)

for i in robots:
   i.stop()
  
for i in bigBots:
    bigBots[0].set_joint_states(1,0,1)
    bigBots[1].set_joint_states(1,0,1)
    
    time.sleep(5)
    
    bigBots[0].set_joint_states(-1,0,-1)
    bigBots[1].set_joint_states(-1,0,-1)
    
    
for i in smallBots:
    time.sleep(5)
    smallBots[0].set_joint_states(-1,0,-1)
    smallBots[1].set_joint_states(-1,0,-1)
    
    time.sleep(3)
    
    smallBots[0].set_joint_states(1,0,1)
    smallBots[1].set_joint_states(1,0,1)
    
for i in robots:
    time.sleep(2)
    i.stop()
    
for i in robots:
    i.set_joint_states(1,0,1)
    time.sleep(1)
    i.stop()
    
for i in smallBots:
    smallBots[0].set_joint_states(1,0,-1)
    smallBots[1].set_joint_states(1,0,-1)
    time.sleep(1)

for i in robots:
    i.stop()
    
for i in bigBots:
    bigBots[0].set_joint_states(1,0,1)
    bigBots[1].set_joint_states(1,0,1)
    time.sleep(1)
    
for i in robots:
    i.stop()
    
for i in robots:
    i.set_joint_states(1,0,1)
    i.set_joint_states(1,0,-1)
    time.sleep(2)

for i in robots:
    i.stop()

