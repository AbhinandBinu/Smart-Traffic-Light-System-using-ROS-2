# vehicle_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Vehicle(Node):

    def __init__(self):
        super().__init__('vehicle_node')

        self.subscription = self.create_subscription(
            String,
            '/traffic_signal',
            self.callback,
            10
        )

    def callback(self, msg):
        signal = msg.data

        if signal == "RED":
            action = "🛑 STOP"
        elif signal == "GREEN":
            action = "🚗 MOVE"
        elif signal == "YELLOW":
            action = "⚠ SLOW DOWN"
        else:
            action = "UNKNOWN"

        self.get_logger().info(f"Vehicle Action: {action}")


def main():
    rclpy.init()
    node = Vehicle()
    rclpy.spin(node)
    rclpy.shutdown()
