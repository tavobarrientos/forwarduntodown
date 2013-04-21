import nxt.sensor

"""
	Get Brick Sensors configured for my current brick
"""

class BrickSensors:

	def __init__(self, brick):
		self.light = LightSensor(brick, PORT_2)
		self.sonic = UltrasonicSensor(brick, PORT_3)

	def GetLightSensorSample(brick):
		return self.light.get_sample()

	def GetUltrasonicSensorSample(brick):
		return self.sonic.get_sample()
	
	