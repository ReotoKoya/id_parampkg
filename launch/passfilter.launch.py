import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
        package='id_parampkg',
        executable='id_param_talker',
        )
    listener = launch_ros.actions.Node(
        package='id_parampkg'
        executable='id_param_listener',
        output='screen'
        )
    
    return launch.LaunchDescription([id_param_talker, id_param_listener])
