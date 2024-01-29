import os
from color_thresholding import *
from gradient_methods import *


def process_and_compare(image_paths, output_dir=None):
    for i, path in enumerate(image_paths):
        img = cv2.imread(path)
        if img is None:
            print(f"Failed to load image: {path}")
            continue

        result1 = detect_sky(img)
        result2 = detect_sky_area(img)

        # Combine results side by side
        combined = np.concatenate((result1, result2), axis=1)

        if output_dir:
            # Save combined image
            output_path = os.path.join(output_dir, f"combined_{i}.jpg")
            cv2.imwrite(output_path, combined)
        else:
            # Or display them
            cv2.imshow(f"Combined Result {i}", combined)
            cv2.waitKey(0)

    cv2.destroyAllWindows()

# List of 20 image paths
image_paths = ['skyImages/1.jpg', 'skyImages/2.jpg', 'skyImages/3.jpg']

# Directory to save the output images
output_dir = 'output_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process and compare
process_and_compare(image_paths, output_dir)
