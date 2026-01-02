from rclpy.node import Node
from simple_interfaces_pkg.msg import ComponentsStatus
import rclpy

class ComponentsStatusListener(Node):
    def __init__(self):
        super().__init__("components_status_listener")
        # create subscriber
        self.components_status_subscriber_ = self.create_subscription(
            ComponentsStatus,
            "components_status",
            self.listener_callback,
            10,
        )
        self.get_logger().info("Components Status Listener Node has been started.")

    def listener_callback(self, msg):
        # log received status
        self.get_logger().info(f"Received status: {msg.debug_message}") 
        
def main(args=None):
    rclpy.init(args=args)
    node = ComponentsStatusListener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()