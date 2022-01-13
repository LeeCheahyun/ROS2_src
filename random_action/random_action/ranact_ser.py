import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from basic_interface.action import Random
import random
import time

class Randomactionserver(Node):
    def __init__(self):
        super().__init__('random_server')
        self.action_server = ActionServer(self,Random,'random',self.execute_callback)

    def execute_callback(self,goal_handle):
        self.get_logger().info('executing goal,,')
        feedback_msg = Random.Feedback()

        while True:
            feedback_msg.partial_sequence = random.randrange(1,11)
            self.get_logger().info('Feedback : {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

            if feedback_msg.partial_sequence == goal_handle.request.order:
                break

        goal_handle.succeed()
        result = Random.Result()
        result.sequence = feedback_msg.partial_sequence
        return result

def main(args=None):
    rclpy.init(args=args)
    random_action_server = Randomactionserver()
    rclpy.spin(random_action_server)

if __name__ == '__main__':
    main()