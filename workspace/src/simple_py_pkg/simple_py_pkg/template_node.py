#!/usr/bin/env python3

# 1.library imports
import rclpy
from rclpy.node import Node

# 2. Node class definition

class CustomNodeName(Node):
    def __init__(self):
        super().__init__("custom_node_name")
    

def main(args=None):
    rclpy.init(args=args)
    node = CustomNodeName()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()