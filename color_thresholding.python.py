import cv2
import numpy as np


def detect_sky(image_path):
    # Load an image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from {image_path}. Check the file path.")
        return

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range for sky color blue
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # Create a mask that captures areas in the range
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Apply the mask to get the sky region
    sky_region = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image and the sky region
    cv2.imshow('Original Image', image)
    cv2.imshow('Sky Region', sky_region)

    # Wait indefinitely until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # Path to your image
    image_path = 'skyImages/10.jpg'

    # Detect and display sky region
    detect_sky(image_path)


if __name__ == "__main__":
    main()
