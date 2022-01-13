from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='random_action',
            executable='client',
            name='random',
            output='screen',
            emulate_tty=True,
        ),

        Node(
            package='random_action',
            executable='server',
            name='random',
            output='screen',
            emulate_tty=True,
        )
    ])