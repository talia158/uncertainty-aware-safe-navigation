import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_safe_nav = get_package_share_directory('safe_nav')
    
    # Arguments
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # 1. Start the simulation (Gazebo + Robot)
    sim_world_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_safe_nav, 'launch', 'sim_world.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    # 2. Start Robot Localization (EKF)
    ekf_config_path = os.path.join(pkg_safe_nav, 'config', 'ekf.yaml')
    
    ekf_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[
            ekf_config_path, 
            {'use_sim_time': use_sim_time}
        ],
        remappings=[('odometry/filtered', 'odometry/filtered')]
    )

    # 3. Start RViz
    rviz_config_path = os.path.join(pkg_safe_nav, 'rviz', 'default.rviz')
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path],
        parameters=[{'use_sim_time': use_sim_time}]
    )

    ld = LaunchDescription()
    ld.add_action(sim_world_cmd)
    ld.add_action(ekf_node)
    ld.add_action(rviz_node)

    return ld
