import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from basic_interface.action import Random

class Randomactionclient(Node):
    def __init__(self):
        super().__init__('random_action_client')
        self.action_client = ActionClient(self,Random,'random')

    def send_goal(self,order):
        goal_msg = Random.Goal()
        goal_msg.order = order

        self.action_client.wait_for_server()
        self.send_goal_future = self.action_client.send_goal_async(goal_msg,feedback_callback=self.feedback_callback)
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self,future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :')
            return
        self.get_logger().info('Goal accepted')
        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self,future):
        result = future.result().result
        if result.sequence == 5:
            self.get_logger().info('Result: {0}'.format(result.sequence))
            rclpy.shutdown()

    def feedback_callback(self,feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))

def main(args=None):
    rclpy.init(args=args)
    action_client = Randomactionclient()
    action_client.send_goal(5)
    rclpy.spin(action_client)

if __name__ == '__main__':
    main()