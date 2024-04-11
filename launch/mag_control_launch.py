from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mini_tank_ros2',
            executable='v4l2_camera',
            name='camera',
            output='screen',
            parameters=[
                {'video_device': '/dev/video0'},
                {'output_encoding': 'rgb8'},
                {'pixel_format': 'YUYV'},
                {'image_size': [640,480]},
                {'io_method': 'mmap'},
                {'image_raw.jpeg_quality': 40}
            ]
        ),
        Node(
            package = 'mini_tank_ros2',
            executable = 'robot_object_detection_subscriber',
            name = 'robot_object_detection_subscriber',
            output = 'screen'
        ),
        Node(
            package = 'mini_tank_ros2',
            executable='mag_control_node',
            name='mag_control_node',
            output='screen'
        ),
        Node(
            package='mini_tank_ros2',
            executable='magnetometer_node',
            name='magnetometer_node',
            output='screen'
        ),
        Node(
            package='mini_tank_ros2',
            executable='get_goal_heading_node',
            name='get_goal_heading_node',
            output='screen'
        ),
    ])