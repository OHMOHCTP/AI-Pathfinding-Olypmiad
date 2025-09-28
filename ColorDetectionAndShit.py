from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from MCLab.ai_tools import *
import unit
from datetime import datetime


# Custom libs -- Azaan
import threading

screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
color_0 = unit.get(unit.COLOR, unit.PORTA)
servo_0 = unit.get(unit.SERVO, unit.PORTC)
servo_1 = unit.get(unit.SERVO, unit.PORTD)

class ObjectStatus:
  def __init__(self):
    self.color = "Nil"
    self.picked = False
    self.goal = "Ignore"

GreenObject = ObjectStatus()
GreenObject.color = "Green"
RedObject = ObjectStatus()
RedObject.color = "Red"
BlueObject = ObjectStatus()
BlueObject.color = "Blue"
YellowObject = ObjectStatus()
YellowObject.color = "Yellow"

Goal = "Blue"

for obj in [GreenObject, RedObject, BlueObject, YellowObject]:
  if obj.color == Goal:
    obj.goal = "Pick"
  else:
    obj.goal = "Ignore"
  
unitv_base = UnitVBase()
color_track = ColorTrack(unitv_base)

label0 = MCLabel('label0', x=16, y=46, color=0x000, font=FONT_MONT_14, parent=None)
label1 = MCLabel('label1', x=76, y=46, color=0x000, font=FONT_MONT_14, parent=None)
label2 = MCLabel('label2', x=133, y=43, color=0x000, font=FONT_MONT_14, parent=None)
label3 = MCLabel('label3', x=16, y=8, color=0x000, font=FONT_MONT_14, parent=None)
label4 = MCLabel('label4', x=72, y=6, color=0x000, font=FONT_MONT_14, parent=None)
label5 = MCLabel('label5', x=126, y=7, color=0x000, font=FONT_MONT_14, parent=None)
label6 = MCLabel('label6', x=138, y=151, color=0x000, font=FONT_MONT_14, parent=None)
slider0 = MCSlider(x=125, y=204, w=70, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)

DetectionTest = "Nil"

color_track.init()
label3.set_text('R')
label4.set_text('G')
label5.set_text('B')
def ColorDetector():
  while True:
    BlueLabel = color_0.blue
    GreenLabel = color_0.green
    RedLabel = color_0.red
    label0.set_text(str(color_0.red))
    label1.set_text(str(color_0.green))
    label2.set_text(str(color_0.blue))
    slider0.set_color((color_0.red << 16) | (color_0.green << 8) | color_0.blue)
    if RedLabel >= 175 and GreenLabel > BlueLabel:
      label6.set_text("Yellow Yellow Dirty Fellow")
      DetectionTest = "Yellow"
    elif RedLabel > BlueLabel and RedLabel > GreenLabel:
      label6.set_text("Roses are Red")
      DetectionTest = "Red"
    elif BlueLabel > GreenLabel:
      label6.set_text("Violets are Blue")
      DetectionTest = "Blue"
    elif GreenLabel >= 45:
      label6.set_text("Green")
      DetectionTest = "Green"
    else:
      label6.set_text("I cant identify ts cuh 💔")
      DetectionTest = "Nil"
    wait_ms(2)

def PickUpObject():
  #One servo goes up and down, other opens and closes claw
  if  DetectionTest != "Nil":
    servo_1.write_angle(0)
    servo_0.write_angle(180)
    wait_ms(500)
    servo_0.write_angle(50)
    wait_ms(500)
    servo_1.write_angle(180)
    wait_ms(500)

def DropObject():
  servo_1.write_angle(0)
  servo_0.write_angle(180)
  wait_ms(500)
  servo_0.write_angle(50)
  wait_ms(500)


ColorDetectorThread = threading.Thread(target=ColorDetector)
ColorDetectorThread.start()
ColorDetectorThread.join()
