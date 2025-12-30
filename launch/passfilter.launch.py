import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    config = os.path.join(get_package_share_directory('id_parampkg'), 'config', 'params.yaml')

    id_param_talker = launch_ros.actions.Node(
        package='id_parampkg',
        executable='id_talker',
        parameters=[config],
        )
    id_param_listener = launch_ros.actions.Node(
        package='id_parampkg',
        executable='id_listener',
        parameters=[config],
        output='screen'
        )
    
    return launch.LaunchDescription([id_param_talker, id_param_listener])
