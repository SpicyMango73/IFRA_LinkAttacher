from launch import LaunchDescription
from launch_ros.actions import Node

package_name = "lab1"

def generate_launch_description():
    
    publisher_node = Node(
        package = package_name,
        executable="publisher",
        output="screen",
        prefix='xterm -title "The Publisher" -fa "Monospace" -fs 12 -hold -e',
    )

    subscriber_node = Node(
        package = package_name,
        executable="subscriber",
        output="screen",
        prefix='xterm -title "The Subscriber" -fa "Monospace" -fs 12 -hold -e',
    )

    
    return LaunchDescription([publisher_node, subscriber_node])