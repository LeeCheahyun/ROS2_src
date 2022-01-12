import rclpy
from rclpy.node import Node

from basic_interface.srv import AddTwoInts


class Rptkssub(Node):

    def __init__(self):
        super().__init__('rptks_sub')
        self.srv = self.create_service(AddTwoInts, 'rptks', self.service_callback)

    def service_callback(self, request, response):
        response.sum = request.a + request.b
        response.min = request.a - request.b
        response.mul = request.a * request.b
        response.div = request.a / request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response

def main(args=None):
    rclpy.init(args=args)

    custom_service_server = Rptkssub()

    rclpy.spin(custom_service_server)

    rclpy.shutdown()


if __name__ == '__main__':
    main()