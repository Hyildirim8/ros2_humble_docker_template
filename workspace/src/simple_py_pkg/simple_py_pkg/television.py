#!/usr/bin/env python3

# 1.library imports
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
# 2. Node class definition

class ChannelNode(Node):
    def __init__(self):
        super().__init__("channel_node")
        self.publisher_ = self.create_publisher(String, "tv_channel", 10)
        self.timer = self.create_timer(2.0, self.publish_channel)
        self.get_logger().info("ChannelNode has been started.")
    
    def publish_channel(self):
        channel_name = "Discovery Channel"
        msg = String()
        msg.data = channel_name
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published channel: {channel_name}")

def main(args=None):
    rclpy.init(args=args)
    node = ChannelNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()