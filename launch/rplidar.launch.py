import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/serial/by-path/pci-0000:00:14.0-usb-0:2:1.0-port0',
                'serial_baudrate': 115200,
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard',
                'angle_min': -2.094,
                'angle_max': 2.094
                # 에스뽀 로봇 뒷면 막혀서 스캔 범위 지정
            }]
        )
    ])


# 우리가 쓰는 rplidar 정보
# 포트파일명 = ttyUSB0
# Bus 003 Device 008: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
# 
# /dev/serial/by-path/pci-0000:00:14.0-usb-0:2:1.0-port0
 