# traffic_monitor.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TrafficMonitor(Node):

    def __init__(self):
        super().__init__('traffic_monitor')

        self.subscription = self.create_subscription(
            String,
            '/traffic_signal',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f"📊 Current Signal: {msg.data}")


def main():
    rclpy.init()
    node = TrafficMonitor()
    rclpy.spin(node)
    rclpy.shutdown()
