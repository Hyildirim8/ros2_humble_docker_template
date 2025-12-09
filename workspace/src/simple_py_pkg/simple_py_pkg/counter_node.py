#!/usr/bin/env python3

# 1.library imports
import rclpy
from rclpy.node import Node

# 2. Node class definition

class CounterNode(Node):
    def __init__(self):
        super().__init__("counter_node")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info(f"Hello World {self.counter_}")



def main(args=None):
    rclpy.init(args=args)
    node = CounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()