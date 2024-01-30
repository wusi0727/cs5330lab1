import os
import cv2
import numpy as np
from gradient_methods import detect_sky_area


def detect_sky(image):
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range for sky color blue
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # Create a mask that captures areas in the range
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Apply the mask to get the sky region
    sky_region = cv2.bitwise_and(image, image, mask=mask)

    return sky_region


def process_and_compare(image_paths, output_dir=None):
    for i, path in enumerate(image_paths):
        img = cv2.imread(path)
        if img is None:
            print(f"Failed to load image: {path}")
            continue

        result1 = detect_sky(img)
        result2 = detect_sky_area(img)

        # Combine the original image with the results side by side
        combined = np.concatenate((img, result1, result2), axis=1)

        if output_dir:
            # Save combined image
            output_path = os.path.join(output_dir, f"combined_{i}.jpg")
            cv2.imwrite(output_path, combined)
        else:
            # Or display them
            cv2.imshow(f"Combined Result {i}", combined)
            cv2.waitKey(0)

    cv2.destroyAllWindows()


# List of image paths
image_paths = ['skyImages/1.jpg', 'skyImages/2.jpg', 'skyImages/3.jpg', 'skyImages/4.jpg', 'skyImages/5.jpg',
               'skyImages/6.jpg', 'skyImages/7.jpg', 'skyImages/8.jpg', 'skyImages/9.jpg',
               'skyImages/10.jpg', 'skyImages/11.jpg', 'skyImages/12.jpg',
               'skyImages/13.jpg', 'skyImages/14.jpg', 'skyImages/15.jpg',
               'skyImages/16.jpg', 'skyImages/17.jpg', 'skyImages/18.jpg',
               'skyImages/19.jpg', 'skyImages/20.jpg']

# Directory to save the output images
output_dir = 'output_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process and compare
process_and_compare(image_paths, output_dir)
