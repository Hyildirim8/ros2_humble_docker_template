#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from simple_interfaces_pkg.msg import ComponentsStatus


class ComponentStatusPublisher(Node):
    def __init__(self):
        super().__init__("component_status_publisher")
        # create publisher (fixed typo and parenthesis)
        self.components_status_publisher_ = self.create_publisher(
            ComponentsStatus, "components_status", 10
        )
        # timer to publish periodically
        self.timer_ = self.create_timer(1.0, self.publish_status)

        self.get_logger().info("Component Status Publisher Node has been started.")
        # initialize simulated component readiness states
        self.counter = 0
        self.camera_is_ready = True
        self.lidar_is_ready = True
        self.motor_is_ready = True

    def publish_status(self):
        # update simulated readiness (simple pattern to vary values over time)
        self.counter += 1
        self.camera_is_ready = (self.counter % 4) != 0
        self.lidar_is_ready = (self.counter % 6) != 0
        self.motor_is_ready = (self.counter % 10) != 0

        # populate message
        msg = ComponentsStatus()
        msg.camera_is_ready = bool(self.camera_is_ready)
        msg.lidar_is_ready = bool(self.lidar_is_ready)
        msg.motor_is_ready = bool(self.motor_is_ready)

        # assemble debug message based on readiness
        not_ready = []
        if not msg.camera_is_ready:
            not_ready.append("camera")
        if not msg.lidar_is_ready:
            not_ready.append("lidar")
        if not msg.motor_is_ready:
            not_ready.append("motor")

        if not_ready:
            msg.debug_message = "Not ready: " + ", ".join(not_ready)
        else:
            msg.debug_message = "All components ready"

        # publish and log
        self.components_status_publisher_.publish(msg)
        self.get_logger().info(f"Published status: {msg.debug_message}")


def main(args=None):
    rclpy.init(args=args)
    node = ComponentStatusPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()