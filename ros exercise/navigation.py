#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt

class TurtleBot:
    
    def __init__(self):
        rospy.init_node('motioncontroller')
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose,self.New_pose)
        self.goal_pose_subscriber = rospy.Subscriber('/cmd/goal_pose',Pose,self.destination_pose)
        
        self.goal_pose = Pose()
        self.pose = Pose()
        self.rate = rospy.Rate(10)
    def destination_pose(self,msg):
        self.goal_pose = msg
        
    def New_pose(self,msg):
        self.pose = msg
        
    def distance(self,goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x),2)+pow((goal_pose.y-self.pose.y),2))
    def linear_vel(self,goal_pose):
        return 1.5*self.distance(goal_pose)
    def angular_vel(self,goal_pose,):
        return 6 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)
    
    def move_goal(self):
        vel_msg = Twist()
        while not rospy.is_shutdown():
            vel_msg.linear.x = self.linear_vel(self.goal_pose)
            vel_msg.angular.z = self.angular_vel(self.goal_pose)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        rospy.spin()
        
x = TurtleBot()
x.move_goal()