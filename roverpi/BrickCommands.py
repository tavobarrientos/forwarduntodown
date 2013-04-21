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
	
	def ExecuteCommand(self, cmd):
		if cmd == "fwd":
			self.forward(self.nxtbrick, 360)
		elif cmd == "rwd":
			self.backwards(self.nxtbrick, 360)
		elif cmd == "lft":
			self.left(self.nxtbrick, 360)
		elif cmd == "rgt":
			self.right(self.nxtbrick, 360)
				
	def forward(self, brick, duration):
		self.MovementCmd(100, 100, duration)
	
	def backwards(self, brick, duration):
		self.MovementCmd(-100, -100, duration)
	
	def left(self, brick, duration):
		self.MovementCmd(-100, 100, duration)
	
	def right(self, brick, duration):
		self.MovementCmd(100, -100, duration)

	def MovementCmd(self, directionl, directionr, duration):
		try:
			self.LeftMotor.update(directionl, duration)
			self.RightMotor.update(directionr, duration)
		except nxt.locator.BrickNotFoundError:
			return '=('
		return 'OK'


class BrickHelper:
	def GetAvailableBrick(self):
		brick = nxt.locator.find_one_brick()
		return brick.connect()
	
	def CloseBrick(self, brick):
		brick.close()
	
	def GetBrikName(self, brick):
	    name, host, signal, flash = brick.get_device_info()
	    return name
