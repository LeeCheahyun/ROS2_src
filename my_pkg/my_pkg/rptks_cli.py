import sys
import rclpy
from rclpy.node import Node

from basic_interface.srv import AddTwoInts

class Rptkscli(Node):

    def __init__(self):
        super().__init__('rptkscli')
        self.client = self.create_client(AddTwoInts, 'rptks') # Client builder 패턴
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for custom service server...')
        self.req = AddTwoInts.Request()

    def send_request(self):
        self.req.c = str(sys.argv[2])
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[3])
        self.future = self.client.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    custom_service_client = Rptkscli()
    custom_service_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(custom_service_client)
        # future가 done 상태가 되면 다음 if문을 실행합니다
        if custom_service_client.future.done():
            try:
                response = custom_service_client.future.result()
            except Exception as e:
                custom_service_client.get_logger().info(
                    'Service call failed: %r' % (e,))
            else:
                if custom_service_client.req.c == '+' :
                    custom_service_client.get_logger().info(
                        'Result: %d + %d = %d' %
                        (custom_service_client.req.a, custom_service_client.req.b, response.sum))
                
                elif custom_service_client.req.c == '-' :
                    custom_service_client.get_logger().info(
                        'Result: %d - %d = %d' %
                        (custom_service_client.req.a, custom_service_client.req.b, response.min))
                
                elif custom_service_client.req.c == 'x' :
                    custom_service_client.get_logger().info(
                        'Result: %d x %d = %d' %
                        (custom_service_client.req.a, custom_service_client.req.b, response.mul))
        
                elif custom_service_client.req.c == '/' :
                    custom_service_client.get_logger().info(
                        'Result: %d / %d = %f' %
                        (custom_service_client.req.a, custom_service_client.req.b, response.div))
            break

    custom_service_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()