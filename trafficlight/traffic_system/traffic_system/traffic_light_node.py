# traffic_light_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TrafficLight(Node):

    def __init__(self):
        super().__init__('traffic_light_node')

        self.publisher_ = self.create_publisher(String, '/traffic_signal', 10)
        self.subscriber_ = self.create_subscription(
            String,
            '/emergency',
            self.emergency_callback,
            10
        )

        self.signals = ["RED", "GREEN", "YELLOW"]
        self.index = 0

        self.timer = self.create_timer(3.0, self.publish_signal)

        self.emergency = False


    def publish_signal(self):
        msg = String()

        if self.emergency:
            msg.data = "GREEN"
            self.get_logger().warn("🚑 EMERGENCY MODE: GREEN SIGNAL")
        else:
            msg.data = self.signals[self.index]
            self.index = (self.index + 1) % len(self.signals)

        self.publisher_.publish(msg)
        self.get_logger().info(f"🚦 Signal: {msg.data}")


    def emergency_callback(self, msg):
        if msg.data == "EMERGENCY":
            self.emergency = True


def main():
    rclpy.init()
    node = TrafficLight()
    rclpy.spin(node)
    rclpy.shutdown()
