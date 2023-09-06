"""my_controller_wave_me controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Keyboard, Motion

# create the Robot instance.
robot = Robot()

timestep=32

keyboard= Keyboard()
keyboard.enable(timestep)


wave= Motion("../../motions/wave.motion")

while robot.step(timestep)!=-1:
    key= keyboard.getKey()
    
    if key==Keyboard.UP:
        wave.play()