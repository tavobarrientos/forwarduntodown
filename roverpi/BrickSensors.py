import nxt.sensors

"""
	Get Brick Sensors configured for my current brick
"""

class BrickSensors:

	def __init__(self):
		self.light = LightSensor(brick, PORT_2)
		self.sonic = UltrasonicSensor(brick, PORT_3)
		self.touch = TouchSensor(brick, PORT_1)

	def GetLightSensorSample(brick):
		return self.light.get_sample()

	def GetUltrasonicSensorSample(brick):
		return self.sonic.get_sample()
	
	def GetTouchSensorSample(brick):
		return self.touch.get_sample()
	