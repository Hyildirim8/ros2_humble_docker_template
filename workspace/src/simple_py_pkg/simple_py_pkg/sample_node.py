#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)

    node = Node("sample_node")
    for i in range(5):
        node.get_logger().info(f"Sample node has started {i}.")

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.get_logger().info("Shutting down sample node.")
        node.destroy_node()
        try:
            rclpy.shutdown()
        except:
            # ROS zaten shutdown etmişse burası çalışır, hata engellenir
            pass

if __name__ == "__main__":
    main()
