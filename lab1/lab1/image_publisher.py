#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageFlipper(Node):

    def __init__(self):
        super().__init__('image_flipper')

        self.bridge = CvBridge()

        # subscriber: leggi immagine sorgente
        self.subscription = self.create_subscription(
            Image,
            '/head_front_camera/rgb/image_raw',   # ← cambia se necessario
            self.image_callback,
            10
        )

        # publisher: pubblica immagine modificata
        self.publisher = self.create_publisher(
            Image,
            '/head_front_camera/rgb/image_flipped',   # nuovo topic
            10
        )

        self.get_logger().info("Image flipper node started.")

    def image_callback(self, msg):
        try:
            # ROS → OpenCV
            img_cv = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Flip verticale (0 = asse verticale)
            img_flipped = cv2.flip(img_cv, 0)

            # OpenCV → ROS
            flipped_msg = self.bridge.cv2_to_imgmsg(
                img_flipped, encoding='bgr8'
            )

            flipped_msg.header = msg.header  # mantiene timestamp e frame_id

            # Publish
            self.publisher.publish(flipped_msg)

        except Exception as e:
            self.get_logger().error(f"Error processing image: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = ImageFlipper()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
