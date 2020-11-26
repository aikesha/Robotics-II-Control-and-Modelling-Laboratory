import gym
import rospy
import tf
import roslaunch
import time
import numpy as np
import tf


from gym import utils, spaces
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from std_srvs.srv import Empty
from sensor_msgs.msg import JointState
from gym.utils import seeding

def callback(data):
	angle = data.position

def rad2deg(ang):
    return ang*180/3.14

def deg2rad(ang):
    return ang*3.14/180


class GazeboPlanar5DofEnv(gym.Env):
	def __init__(self):
		print("Created an environment")
		rospy.init_node('rl_gym')
		self.unpause = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
		self.pause = rospy.ServiceProxy('/gazebo/pause_physics', Empty)
		self.reset_proxy = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
		self.motor1_pub = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=5) # Subscribing to each topic, to control the robot
		self.motor2_pub = rospy.Publisher('/robot/joint2_position_controller/command', Float64, queue_size=5)
		self.motor3_pub = rospy.Publisher('/robot/joint3_position_controller/command', Float64, queue_size=5)
		self.motor4_pub = rospy.Publisher('/robot/joint4_position_controller/command', Float64, queue_size=5)
		self.motor5_pub = rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=5)
		self.listener = tf.TransformListener() # Transformation plugin

		self.action_space = spaces.Discrete(10) #F,L,R
		self.reward_range = (-np.inf, np.inf)

		self._seed()
        # Launch the simulation with the given launchfile name




	def coord(self,x,y):
		self.xcord = x
		self.ycord = y



	def _seed(self, seed=None):
		self.np_random, seed = seeding.np_random(seed)
		return [seed]


	def step(self, action):

		angles = None
		while angles is None:
			try:
				angles = rospy.wait_for_message('/robot/joint_states', JointState, timeout=5) # joint states or angle of each motor
			except:
				pass
		rate = rospy.Rate(50)
		if action == 0: #Base motor left
			msg = angles.position[4] - deg2rad(5) # You can change the sample angle
			while True:
				self.motor1_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[4] - msg) < 0.01):
					break
				rate.sleep()


		elif action == 1: #Base motor right
			msg = angles.position[4] + deg2rad(5)
			while True:
				self.motor1_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[4] - msg) < 0.01):
					break
				rate.sleep()

		elif action == 2: #Second motor left
			msg = angles.position[1] - deg2rad(5)
			while True:
				self.motor2_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[1] - msg) < 0.01):
					break
				rate.sleep()

		elif action == 3: #Second motor right
			msg = angles.position[1] + deg2rad(5)
			while True:
				self.motor2_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[1] - msg) < 0.01):
					break
				rate.sleep()

		elif action == 4: #Third motor left
			msg = angles.position[2] - deg2rad(5)
			while True:
				self.motor3_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[2] - msg) < 0.01):
					break
				rate.sleep()

		elif action == 5: #Third motor right
			msg = angles.position[2] + deg2rad(5)
			while True:
				self.motor3_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[2] - msg) < 0.01):
					break
				rate.sleep()

		elif action == 6: #Fourth motor left
			msg = angles.position[3] - deg2rad(5)
			while True:
				self.motor4_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[3] - msg) < 0.01):
					break
				rate.sleep()

		elif action == 7: #Fourth motor right
			msg = angles.position[3] + deg2rad(5)
			while True:
				self.motor4_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[3] - msg) < 0.01):
					break
				rate.sleep()

		elif action == 8: #Fifth motor left
			msg = angles.position[0] - deg2rad(5)
			while True:
				self.motor5_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[0] - msg) < 0.01):
					break
				rate.sleep()

		elif action == 9: #Fifth motor right
			msg = angles.position[0] + deg2rad(5)
			while True:
				self.motor5_pub.publish(Float64(msg))
				s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				if (abs(s.position[0] - msg) < 0.01):
					break
				rate.sleep()

		angles = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)

		trans = None
		while trans is None:
			try:

				(trans,rot) = self.listener.lookupTransform('/world', '/sensor_frame', rospy.Time(0))
			except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
				continue
		done = False
		reward = -1 # Default reward is -1 to minimize the steps
		if (trans[0] < 0 or abs(angles.position[0]) > 1.57 or abs(angles.position[1]) > 1.57 or abs(angles.position[2]) > 1.57 or abs(angles.position[3]) > 1.57 or abs(angles.position[4]) > 1.57):
			done = True
			reward = -20 # If it fails, then reward is -20
		elif (rospy.wait_for_message('isDone', Bool).data):
			done = True
			reward = 30 # If succeeds then 30
		print("!!!!")

		state = self.states2obs(angles.position) # convert to the states



		return state, reward, done, {}


	def reset(self):

        # Resets the state of the environment and returns an initial observation. Basically moving each motor to the 0 degree. 
		msg = 0
		rate = rospy.Rate(50)
		while True:
			self.motor1_pub.publish(Float64(msg))
			self.motor2_pub.publish(Float64(msg))
			self.motor3_pub.publish(Float64(msg))
			self.motor4_pub.publish(Float64(msg))
			self.motor5_pub.publish(Float64(msg))
			s = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
			if ((abs(s.position[0] - msg) < 0.01) and (abs(s.position[1] - msg) < 0.01) and (abs(s.position[2] - msg) < 0.01) and (abs(s.position[3] - msg)) < 0.01 and (abs(s.position[4] - msg) < 0.01)):
				break
			rate.sleep()

		angles = None
		while angles is None:

			try:
				angles = rospy.wait_for_message('/robot/joint_states', JointState, timeout=5)
			except:
				pass

		state = self.states2obs(angles.position)
		return state

	def states2obs(self,states): # Mapping our state space to integers

		angle1 = int(10 + (round(rad2deg(states[4])) + 90)//5)
		angle2 = int(10 + (round(rad2deg(states[1])) + 90)//5)
		angle3 = int(10 + (round(rad2deg(states[2])) + 90)//5)
		angle4 = int(10 + (round(rad2deg(states[3])) + 90)//5)
		angle5 = int(10 + (round(rad2deg(states[0])) + 90)//5)

		c = str(angle1)+str(angle2)+str(angle3)+str(angle4)+str(angle5)

		result = int(c)

		return result
