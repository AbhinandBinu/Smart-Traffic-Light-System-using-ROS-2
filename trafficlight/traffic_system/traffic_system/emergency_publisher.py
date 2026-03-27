# emergency_publisher.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class EmergencyPublisher(Node):

    def __init__(self):
        super().__init__('emergency_publisher')

        self.publisher_ = self.create_publisher(String, '/emergency', 10)

        self.timer = self.create_timer(10.0, self.send_emergency)

    def send_emergency(self):
        msg = String()
        msg.data = "EMERGENCY"

        self.publisher_.publish(msg)
        self.get_logger().warn("🚑 Emergency triggered!")


def main():
    rclpy.init()
    node = EmergencyPublisher()
    rclpy.spin(node)
    rclpy.shutdown()
