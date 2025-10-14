from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit
from MCLab.robocar import Robocar
import time

screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

robo = Robocar()
robo.init_motor_module()
if not robo.select_lego:
  robo.encoder4.set_all_motors_mode(0x00)

def normal_mode():
  if not robo.select_lego:
    robo.select_normal_mode()
    for i in range(4):
      robo.encoder4.set_motor_pwm_dutycycle(i, 0)

def MotorsStopAll():
  global _Direction, _For, _Type, _Speed, Distance_test, initial_ticks, required_ticks, revolutions_required
  robo.motor_stop(1)
  robo.motor_stop(2)
  robo.motor_stop(3)
  robo.motor_stop(4)

robo.ow_line_port_init(unit.PORTB)
robo.ow_multi_line_led(1)

screen.set_screen_bg_color(0xff0000)

def Mission1P1():
    Count = 0
    Flag = False
    Pattern = False
    while not Flag:
        (L, _, C, _, R) = robo.ow_multi_line_get_sensor_values()
        if (not L) and C and (not R):
            robo.set_motor_speed(1, 1, 70)
            robo.set_motor_speed(2, 0, 72)
            Pattern = False

        elif L and C and (not R):
            if not Pattern:
                Count += 1
                Pattern = True
            if Count == 1:
                robo.set_motor_speed(1, 1, 40)
                robo.set_motor_speed(2, 0, 42)
            elif Count == 2:
                robo.set_motor_speed(1, 1, 0)
                robo.set_motor_speed(2, 0, 0)
                Flag = True

        else:
            robo.set_motor_speed(1, 1, 70)
            robo.set_motor_speed(2, 0, 72)
            Pattern = False

        wait_ms(10)

def Mission1P2():
    robo.set_motor_speed(1, 0, 70)
    robo.set_motor_speed(2, 0, 72)
    wait_ms(1400)
    MotorsStopAll()

    robo.set_motor_speed(1, 1, 70)
    robo.set_motor_speed(2, 0, 72)
    wait_ms(1000)

    Flag = False
    while not Flag:
        (L, _, C, _, R) = robo.ow_multi_line_get_sensor_values()
        if L and C and R:
            robo.set_motor_speed(1, 1, 0)
            robo.set_motor_speed(2, 0, 0)
            Flag = True
        else:
            robo.set_motor_speed(1, 1, 70)
            robo.set_motor_speed(2, 0, 72)
        wait_ms(10)

def Mission1P3():
    screen.set_screen_bg_color(0x333333)

    label0 = MCLabel('label0', x=129, y=133, color=0x000, font=FONT_MONT_18, parent=None)
    label0.set_text_color(0xffffff)
    label0.set_hidden(False)
    label0.set_text(str("Fueling"))

    slider0 = MCSlider(x=115, y=179, w=70, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0xFFFF00, parent=None)
    slider0.set_value(0)

    Time = 0
    while Time < 4000:
        rgb.setColorAll(0xff0000)
        wait_ms(250)
        rgb.setColorAll(0x000000)
        wait_ms(250)
        slider0.set_value(int((Time / 4000) * 100))
        Time += 500

    slider0.set_value(100)
    label0.set_text(str("Done Fueling"))
    wait_ms(1000)

    slider0.delete()
    label0.set_hidden(True)

Mission1P1()
Mission1P2()
Mission1P3()
