#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class TiagoCameraSubscriber(Node):

    def __init__(self):
        super().__init__('tiago_camera_subscriber')

        self.bridge = CvBridge()

        # Cambia topic se necessario
        self.subscription = self.create_subscription(
            Image,
            '/head_front_camera/rgb/image_raw',
            self.callback_image,
            10
        )

        self.get_logger().info("Camera subscriber started.")

    def callback_image(self, msg):
        try:
            # Convert ROS image → OpenCV
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Show image
            cv2.imshow("TIAGo RGB Camera", cv_image)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f"Image conversion failed: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = TiagoCameraSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
