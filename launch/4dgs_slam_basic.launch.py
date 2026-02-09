#!/usr/bin/env python3
"""Launch file for basic 4DGS-SLAM node"""
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Generate launch description for 4DGS-SLAM node"""
    
    return LaunchDescription([
        Node(
            package='4dgs_slam',
            executable='4dgs_slam_node',
            name='4dgs_slam_node',
            output='screen',
            parameters=[],
            remappings=[],
        ),
    ])