from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit
from MCLab.robocar import Robocar
import _thread

# ------- UI -------
screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

switch0 = MCSwitch(x=0,   y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
switch1 = MCSwitch(x=50,  y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
switch2 = MCSwitch(x=93,  y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
switch3 = MCSwitch(x=140, y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
switch4 = MCSwitch(x=186, y=105, w=70, h=30, bg_c=0xCCCCCC, color=0x0288FB, parent=None)
label0  = MCLabel('label0', x=125, y=35, color=0x000, font=FONT_MONT_14, parent=None)

# ------- Robot setup -------
robo = Robocar()
robo.init_motor_module()

if not robo.select_lego:
    robo.encoder4.set_all_motors_mode(0x00)  # DC mode for all 4 channels

def normal_mode():
    if not robo.select_lego:
        robo.select_normal_mode()
        for i in range(4):
            robo.encoder4.set_motor_pwm_dutycycle(i, 0)

robo.ow_line_port_init(unit.PORTB)  # init 5x IR array on PORTB

# ------- Motor helpers (adjust directions if your wiring is flipped) -------
def motors_forward(speed=70):
    # Assuming motor channel 4 = left (dir 0 forward), channel 2 = right (dir 1 forward)
    robo.set_motor_speed(4, 0, speed)
    robo.set_motor_speed(2, 1, speed)

def motors_backward(speed=90):
    robo.set_motor_speed(4, 1, speed)
    robo.set_motor_speed(2, 0, speed)

def motors_stop():
    robo.set_motor_speed(4, 0, 0)
    robo.set_motor_speed(2, 1, 0)

# ------- UI update -------
def update_switches(LF1, LF2, LF3, LF4, LF5):
    (switch0.set_on() if LF1 else switch0.set_off())
    (switch1.set_on() if LF2 else switch1.set_off())
    (switch2.set_on() if LF3 else switch2.set_off())
    (switch3.set_on() if LF4 else switch3.set_off())
    (switch4.set_on() if LF5 else switch4.set_off())

# ------- Main behavior loop -------
def behavior_loop():
    state = "WAIT_FOR_LINE"   # other states: "FORWARD_ON_LINE", "REVERSING"

    while True:
        # Read 5 IR sensors as booleans
        LF1, LF2, LF3, LF4, LF5 = robo.ow_multi_line_get_sensor_values()
        update_switches(LF1, LF2, LF3, LF4, LF5)

        if state == "WAIT_FOR_LINE":
            label0.set_text("Waiting")
            motors_stop()
            # Start moving only when center sees line and sides don't
            if LF3 and not (LF2 or LF4):
                motors_forward(70)
                label0.set_text("Forward")
                state = "FORWARD_ON_LINE"

        elif state == "FORWARD_ON_LINE":
            # Keep rolling as long as we're still centered (LF3 True & sides not both true)
            if LF3 and not (LF2 and LF4):
                # continue forward
                pass
            else:
                # We just lost center (end of line or drifted off) -> reverse
                label0.set_text("Reverse")
                motors_backward(90)
                wait_ms(650)          # back up 1.75s
                motors_stop()
                state = "WAIT_FOR_LINE"

        # loop cadence
        wait_ms(10)

# Optional: run on a thread if your UI needs the main thread free
# _thread.start_new_thread(behavior_loop, ())
# Or just call directly (blocks):
behavior_loop()
