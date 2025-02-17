import gradio as gr
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


def detect_sky(image):
    # Convert PIL Image to OpenCV format
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Process the image
    processed_image = detect_sky_area(image)

    # Convert back to PIL format
    processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
    return processed_image


iface = gr.Interface(
    fn=detect_sky,
    inputs=gr.Image(),
    outputs=gr.Image(),
    title="Sky Detection",
    description="Upload an image to detect the sky region."
)

iface.launch(share=True)
