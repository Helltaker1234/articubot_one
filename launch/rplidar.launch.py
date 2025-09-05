import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    # 필터 설정 파일 경로
    filter_params_file = os.path.join(
        get_package_share_directory('articubot_one'),
        'config',
        'my_laser_filter.yaml'
    )

    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/serial/by-path/pci-0000:00:14.0-usb-0:2.3:1.0-port0',
                'serial_baudrate': 115200,
                'frame_id': 'laser_frame',
                'angle_compensate': True
            }]
        ),

        # Laser Filter 노드
        Node(
            package='laser_filters',
            executable='scan_to_scan_filter_chain',
            parameters=[filter_params_file]
            # remappings=[('/scan', '/scan_filtered')] # 필터링된 토픽 이름을 /scan_filtered로 변경
        ),

    ])


# 우리가 쓰는 rplidar 정보
# 포트파일명 = ttyUSB0
# Bus 003 Device 008: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
# 
# /dev/serial/by-path/pci-0000:00:14.0-usb-0:2:1.0-port0
 