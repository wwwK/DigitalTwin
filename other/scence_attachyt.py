#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    moveit_obstacles_demo.py - Version 0.1 2014-01-14
    
    Move the gripper to a target pose while avoiding simulated obstacles.
    
    Created for the Pi Robot Project: http://www.pirobot.org
    Copyright (c) 2014 Patrick Goebel.  All rights reserved.

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.5
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details at:
    
    http://www.gnu.org/licenses/gpl.html
"""

import rospy, sys
import moveit_commander
from moveit_commander import MoveGroupCommander, PlanningSceneInterface
from moveit_msgs.msg import  PlanningScene, ObjectColor
from geometry_msgs.msg import PoseStamped, Pose

class MoveItDemo:
    def __init__(self):
        # Initialize the move_group API
        moveit_commander.roscpp_initialize(sys.argv)
        
        rospy.init_node('moveit_demo')
        # Construct the initial scene object，实例化planningscenceinterface实例
        scene = PlanningSceneInterface()
        
        # Create a scene publisher to push changes to the scene，发布场景信息到规划场景中
        self.scene_pub = rospy.Publisher('planning_scene', PlanningScene, queue_size=10)
        
        # Create a dictionary to hold object colors
        self.colors = dict()
        
        # Pause for the scene to get ready
        rospy.sleep(1)
                        
        # Initialize the move group for the right arm
        right_arm = MoveGroupCommander('manipulator')
        
        # Get the name of the end-effector link
        end_effector_link = right_arm.get_end_effector_link()
        
        # Allow some leeway in position (meters) and orientation (radians)
        right_arm.set_goal_position_tolerance(0.1)
        right_arm.set_goal_orientation_tolerance(0.5)
       
        # Allow replanning to increase the odds of a solution
        right_arm.allow_replanning(True)
        
        # Set the reference frame for pose targets，设置物体的位姿参考系
        reference_frame = 'base_link'
        
        # Set the right arm reference frame accordingly
        right_arm.set_pose_reference_frame(reference_frame)
        
        # Allow 5 seconds per planning attempt
        right_arm.set_planning_time(5)
        
        # Give each of the scene objects a unique name，设置场景中物体的名称
        #table_id = 'table'
        box1_id = 'box1'
        box2_id = 'box2'
        box3_id = 'box3'
	box4_id = 'box4'
	box5_id = 'box5'
	box6_id = 'box6'
	box7_id = 'box7'
        # Remove leftover objects from a previous run，移除前一次运行过程中添加的场景物体
        #scene.remove_world_object(table_id)
        scene.remove_world_object(box1_id)
        scene.remove_world_object(box2_id)
        scene.remove_world_object(box3_id)
        scene.remove_world_object(box4_id)
        scene.remove_world_object(box5_id)
        scene.remove_world_object(box6_id)
        scene.remove_world_object(box7_id)

        # Give the scene a chance to catch up，给场景时间添加
        rospy.sleep(3)
	
        '''# Set the height of the table off the ground，设置桌面距地面高度
        table_ground = 0.75
        
        # Set the length, width and height of the table and boxes设置桌子、盒子的尺寸
        table_size = [0.2, 0.7, 0.01]'''
        box1_size = [3.00*42/35, 1.60*42/35, 0.050*42/35]
        box2_size = [ 0.050*42/35,1.60*42/35, 0.40*42/35]
        box3_size = [0.40*42/35,0.025*42/35,0.30*42/35 ]
        box4_size = [0.40*42/35,0.025*42/35,0.30*42/35 ]

        box5_size = [ 0.050*42/35,1.60*42/35, 0.40*42/35]
        box6_size = [ 0.050*42/35,1.60*42/35, 0.40*42/35]
        box7_size = [ 0.050*42/35,1.60*42/35, 0.40*42/35]
        #设置位姿
        box1_pose = PoseStamped()
        box1_pose.header.frame_id = reference_frame
        box1_pose.pose.position.x = (0.30-2)*42/35
        box1_pose.pose.position.y = (0.60-1)*42/35
        box1_pose.pose.position.z = 0.0*42/35
        box1_pose.pose.orientation.w = 1.0   
	#将立方体加到规划场景中
        scene.add_box(box1_id, box1_pose, box1_size)
        
        box2_pose = PoseStamped()
        box2_pose.header.frame_id = reference_frame
        box2_pose.pose.position.x = (0.05-1+0.2)*42/35
        box2_pose.pose.position.y = (0.60-1)*42/35
        box2_pose.pose.position.z = 0.20*42/35
        box2_pose.pose.orientation.w = 1.0   
        scene.add_box(box2_id, box2_pose, box2_size)
        
        box3_pose = PoseStamped()
        box3_pose.header.frame_id = reference_frame
	#-0.185        
	box3_pose.pose.position.x = (0.05-1+0.225+0.2)*42/35
        box3_pose.pose.position.y = (0.60-1+0.4)*42/35
        box3_pose.pose.position.z = 0.125*42/35
        box3_pose.pose.orientation.w = 1.0   
        scene.add_box(box3_id, box3_pose, box3_size)

        box4_pose = PoseStamped()
        box4_pose.header.frame_id = reference_frame
	#-0.185        
	box4_pose.pose.position.x = (0.05-1+0.225+0.2)*42/35
        box4_pose.pose.position.y = (0.60-1-0.4)*42/35
        box4_pose.pose.position.z = 0.125*42/35
        box4_pose.pose.orientation.w = 1.0   
        scene.add_box(box4_id, box4_pose, box4_size)

        
        box5_pose = PoseStamped()
        box5_pose.header.frame_id = reference_frame
        box5_pose.pose.position.x = (0.05-1+0.2-0.5)*42/35
        box5_pose.pose.position.y = (0.60-1)*42/35
        box5_pose.pose.position.z = 0.20*42/35
        box5_pose.pose.orientation.w = 1.0   
        scene.add_box(box5_id, box5_pose, box5_size)

        
        box6_pose = PoseStamped()
        box6_pose.header.frame_id = reference_frame
        box6_pose.pose.position.x = (0.05-1+0.2-0.5-0.5)*42/35
        box6_pose.pose.position.y = (0.60-1)*42/35
        box6_pose.pose.position.z = 0.20*42/35
        box6_pose.pose.orientation.w = 1.0   
        scene.add_box(box6_id, box6_pose, box6_size)


        
        box7_pose = PoseStamped()
        box7_pose.header.frame_id = reference_frame
        box7_pose.pose.position.x = (0.05-1+0.2-0.5-0.5-0.5)*42/35
        box7_pose.pose.position.y = (0.60-1)*42/35
        box7_pose.pose.position.z = 0.20*42/35
        box7_pose.pose.orientation.w = 1.0   
        scene.add_box(box7_id, box7_pose, box7_size)


        # Make the table red and the boxes orange设置物体颜色
        self.setColor(box1_id, 0.8, 0.4, 0, 1.0)
        self.setColor(box2_id, 0.5, 0.5, 0.5, 1.0)
	self.setColor(box3_id, 0.5, 0.5, 0.5, 1.0)
	self.setColor(box4_id, 0.5, 0.5, 0.5, 1.0) 
	self.setColor(box5_id, 0.5, 0.5, 0.5, 1.0) 
	self.setColor(box6_id, 0.5, 0.5, 0.5, 1.0) 
	self.setColor(box7_id, 0.5, 0.5, 0.5, 1.0) 
        # Send the colors to the planning scene发送颜色信息到场景中
        self.sendColors()    
        # Pause for a moment...
        rospy.sleep(2)
        
        # Exit MoveIt cleanly
        moveit_commander.roscpp_shutdown()
        
        # Exit the script        
        moveit_commander.os._exit(0)
        
    # Set the color of an object设置物体颜色
    def setColor(self, name, r, g, b, a = 0.9):
        # Initialize a MoveIt color object
        color = ObjectColor()
        
        # Set the id to the name given as an argument
        color.id = name
        
        # Set the rgb and alpha values given as input
        color.color.r = r
        color.color.g = g
        color.color.b = b
        color.color.a = a
        
        # Update the global color dictionary
        self.colors[name] = color

    # Actually send the colors to MoveIt!发送颜色信息到moveit
    def sendColors(self):
        # Initialize a planning scene object
        p = PlanningScene()

        # Need to publish a planning scene diff，is_diff为true，则总的规划空间会被更新而不是替代        
        p.is_diff = True
        
        # Append the colors from the global color dictionary将颜色添加到物体
        for color in self.colors.values():
            p.object_colors.append(color)
        
        # Publish the scene diff发布话题信息
        self.scene_pub.publish(p)

if __name__ == "__main__":
    try:
        MoveItDemo()
    except KeyboardInterrupt:
        raise
    

    
