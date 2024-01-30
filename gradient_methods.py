import cv2
import numpy as np
from scipy.ndimage import median_filter


def refine_skyline(mask, median_kernel_size=19, threshold=20):
    height, width = mask.shape
    for column in range(width):
        column_data = mask[:, column]
        median_filtered = median_filter(column_data, size=median_kernel_size)
        zero_indices = np.where(median_filtered == 0)[0]
        one_indices = np.where(median_filtered == 1)[0]

        if zero_indices.size > 0 and one_indices.size > 0:
            first_zero = zero_indices[0]
            first_one = one_indices[0]

            if first_zero > threshold:
                mask[first_one:first_zero, column] = 1
                mask[first_zero:, column] = 0
                mask[:first_one, column] = 0

    return mask


def detect_sky_area(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.blur(grayscale, (9, 3))
    blurred = cv2.medianBlur(blurred, 5)
    laplacian = cv2.Laplacian(blurred, cv2.CV_8U)
    gradient_mask = laplacian < 6

    structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
    eroded_mask = cv2.morphologyEx(gradient_mask.astype(np.uint8), cv2.MORPH_ERODE, structuring_element)

    refined_mask = refine_skyline(eroded_mask)
    sky_region = cv2.bitwise_and(image, image, mask=refined_mask)

    return sky_region


def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Unable to load image from {image_path}.")
        return

    sky = detect_sky_area(image)

    cv2.imshow("Original", image)
    cv2.imshow("Sky Region", sky)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    image_path = 'skyImages/1.jpg'
    process_image(image_path)


if __name__ == "__main__":
    main()
