#!/usr/bin/env python3
# kutuphane eklem
import rclpy
from rclpy.node import Node

# node oluşturma
def main(args=None):
    rclpy.init(args=args)
    node = Node("sample_node")
    for i in range(5):
        node.get_logger().info("Sample Node Başlatıldı")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()