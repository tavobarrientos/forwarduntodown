"""
	Process Commands for NXT brick
	for my brick configuration.
"""
import nxt.locator
from nxt.motor import *

class BrickCommands:

	def __init__(self, brick):
		self.nxtbrick = brick;
		self.LeftMotor = Motor(brick, PORT_B)
		self.RightMotor = Motor(brick, PORT_C)
		self.BothMotors = Motor(brick, PORT_ALL)
	
	def ExecuteCommand(self, cmd):
		if cmd == "fwd":
			self.forward(self.nxtbrick, 360)
		elif cmd == "rwd":
			self.backwards(self.nxtbrick, 360)
		elif cmd == "lft":
			self.left(self.nxtbrick, 360)
		elif cmd == "rgt":
			self.right(self.nxtbrick, 360)
		elif cmd == "rotatel":
			self.left(self.nxtbrick, 360)
		elif cmd == "rotater":
			self.right(self.nxtbrick, 360)
	
	def forward(self, brick, duration):
		self.MovementCmd(100, 100, duration)
	
	def backwards(self, brick, duration):
		self.MovementCmd(-100, -100, duration)
	
	def left(self, brick, duration):
		self.MovementCmd(100, -100, duration)
	
	def right(self, brick, duration):
		self.MovementCmd(-100, 100, duration)

	def MovementCmd(self, directionl, directionr, duration):
		try:
			self.LeftMotor.update(directionl, duration)
			self.RightMotor.update(directionr, duration)
		except nxt.locator.BrickNotFoundError:
			return '=('
		return 'OK'

	def RunForward(self):
		self.BothMotors.run()

	def RunBackwards(self):
		self.BothMotors.run(-100)
	
	def RunLeft(self):
		self.LeftMotor.run(-100)
		self.RightMotor.run(100)

	def RunRight(self):
		self.LeftMotor.run(100)
		self.RightMotor.run(-100)
	
	def Stop(self):
		self.LeftMotor.stop(1)
		self.RightMotor.stop(1)
		

class BrickHelper:
	def GetAvailableBrick(self):
		brick = nxt.locator.find_one_brick()
		return brick.connect()
	
	def CloseBrick(self, brick):
		brick.close()
	
	def GetBrikName(self, brick):
	    name, host, signal, flash = brick.get_device_info()
	    return name
