import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial
class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.call_add_two_ints(12, 5)  # Initialize future_
       
    def call_add_two_ints(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting again...")
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future_ = client.call_async(request)
        future_.add_done_callback(partial(self.handle_response, a=a, b=b))
        self.future_ = future_
        
    def handle_response(self, future, a, b):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().info(f"Service call failed: {e}")
        else:
            self.get_logger().info(f"Result of {a} + {b} = {response.sum}")

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
  
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()