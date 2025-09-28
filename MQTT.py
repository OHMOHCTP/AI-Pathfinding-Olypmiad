from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from mcmqtt import MCmqtt


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


data = None



label0 = MCLabel('label0', x=104, y=110, color=0x000, font=FONT_MONT_14, parent=None)



def fun_Communications_(topic_data):
  global data
  data = topic_data
  pass


mcmqtt = MCmqtt('RobotTest1', '86.97.118.3', 1883, '', '', 300)
mcmqtt.subscribe(str('Communications'), fun_Communications_)
mcmqtt.start()
while True:
  label0.set_text(str(data))
  wait_ms(2)
