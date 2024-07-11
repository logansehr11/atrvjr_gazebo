from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(
        ExecuteProcess(
            cmd=[
                'gazebo',
                '--verbose',
                '-s',
                'libgazebo_ros_factory.so'
            ],
            output='screen'
        )
    )

    return ld