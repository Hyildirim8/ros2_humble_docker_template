import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting again...")
        self.request_ = AddTwoInts.Request()

    def send_request(self, a, b):
        self.request_.a = a
        self.request_.b = b
        self.future_ = self.client_.call_async(self.request_)

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    a = 5
    b = 3
    node.send_request(a, b)

    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future_.done():
            try:
                response = node.future_.result()
            except Exception as e:
                node.get_logger().info(f"Service call failed: {e}")
            else:
                node.get_logger().info(f"Result of {a} + {b} = {response.sum}")
            break

    rclpy.shutdown()

if __name__ == "__main__":
    main()