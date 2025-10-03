from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit
from MCLab.robocar import Robocar


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
color_0 = unit.get(unit.COLOR, unit.PORTA)

def fun__(topic_data):
  # global params
  pass


mcmqtt = MCmqtt('', '', 1883, '', '', 300)
mcmqtt.subscribe(str(''), fun__)
mcmqtt.start()

LF1 = None
LF2 = None
LF3 = None
LF4 = None
LF5 = None



robo = Robocar()

switch0 = MCSwitch(x=0, y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
switch1 = MCSwitch(x=50, y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
switch2 = MCSwitch(x=93, y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
switch3 = MCSwitch(x=140, y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
switch4 = MCSwitch(x=186, y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
label0 = MCLabel('label0', x=125, y=35, color=0x000, font=FONT_MONT_14, parent=None)



robo.init_motor_module()
if not robo.select_lego:
  robo.encoder4.set_all_motors_mode(0x00)
def normal_mode():
  if not robo.select_lego:
    robo.select_normal_mode()
    for i in range(4):
      robo.encoder4.set_motor_pwm_dutycycle(i, 0)



robo.ow_line_port_init(unit.PORTB)
robo.ow_multi_line_led(1)

def Start():
    robo.set_motor_speed(1,1,100)
    robo.set_motor_speed(2, 0, 100)
    wait_ms(190)
    WSens1 = 0
    Bsens = 1
    Wsens2 = 0
    while Bsens and not (Wsens2 and WSens1):
        (LF1, LF2, LF3, LF4, LF5) = robo.ow_multi_line_get_sensor_values()

def Func1():
    while True:
      (LF1, LF2, LF3, LF4, LF5) = robo.ow_multi_line_get_sensor_values()
      if LF5:
        switch4.set_on()
      else:
        switch4.set_off()
      if LF1:
        switch0.set_on()
      else:
        switch0.set_off()
      if LF2:
        switch1.set_on()
      else:
        switch1.set_off()
      if LF3:
        switch2.set_on()
        if LF3 and (not LF4 and not LF2):
          robo.set_motor_speed(1,1,60)
          robo.set_motor_speed(2,0,60)
        else:
          robo.set_motor_speed(1,1,0)
          robo.set_motor_speed(1,1,0)
      else:
        switch2.set_off()
      if LF4:
        switch3.set_on()
      else:
        switch3.set_off()
      wait_ms(2)
