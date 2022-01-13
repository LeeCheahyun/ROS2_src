import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from basic_interface.action import Random



class RandomActionServer(Node):

    def __init__(self):
        super().__init__('random_action_server')
        self._action_server = ActionServer(
            self,
            Random,
            'random',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')


        feedback_msg = Random.Feedback()
        feedback_msg.partial_sequence = [0, 1]


        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1]) # 피보나치 리스트에 데이터 추가
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)


        goal_handle.succeed()
        result = Random.Result()
        result.sequence = feedback_msg.partial_sequence

        return result


def main(args=None):
    rclpy.init(args=args)
    fibonacci_action_server = RandomActionServer()
    rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
    main()