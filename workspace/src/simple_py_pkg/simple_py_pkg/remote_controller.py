#!/usr/bin/env python3

# 1.library imports
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
# 2. Node class definition

class RemoteControllerNode(Node):
    def __init__(self):
        super().__init__("remote_controller_node")
        self.subscriber_ = self.create_subscription(
            String,
            "tv_channel",
            self.channel_callback,
            10
        )
        self.get_logger().info("RemoteControllerNode has been started.")
    def channel_callback(self, msg):
        self.get_logger().info(f"RemoteController received channel: {msg.data}")
        

def main(args=None):
    rclpy.init(args=args)
    node = RemoteControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()