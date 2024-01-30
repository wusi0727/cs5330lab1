# Sky Pixel Identification in Images using Two different Methods

# Introduction
Sky detection in images is a crucial task in various applications, 
from weather forecasting to enhancing aerial photography. 
Accurate detection of the sky in different lighting conditions poses a unique challenge due to the variability in sky colors and intensities. 
This report explores two distinct techniques for sky detection - one based on color thresholding in the HSV color space 
and another using gradient-based methods - and compares their effectiveness in different scenarios.

# Technique 1: Color Thresholding in HSV Color Space
## Rational
The first method employs color thresholding within the HSV (Hue, Saturation, Value) color space. 
This approach is grounded in the principle that the sky typically manifests as shades of blue, 
making HSV an ideal color space due to its effective separation of color information from intensity.

## Implementation
The technique involves converting the RGB image to HSV, then defining and applying a blue color range to create a mask. 
This mask is used to isolate the sky region from the rest of the image.
Here is my python implementation: 
[color_thresholding](color_thresholding.python.py)

## Strength and Limitations
The method excels in scenarios with clear blue skies and consistent lighting.
However, it struggles in complex lighting conditions, such as sunsets and clouds, 
where the sky's color deviates significantly from the standard blue.

# Technique 2: Gradient - Based methods and median Filtering
## Rational
The second technique uses gradient-based edge detection and median filtering. 
This method was chosen to address the limitations of the first, 
particularly in handling diverse and challenging lighting conditions like sunsets or overcast skies.

## Implementation
This approach processes the image using the Laplacian operator to detect edges 
(representing changes in intensity) and applies median filtering to refine the sky's boundary. 
The technique emphasizes the structural features of the sky, making it more adaptive to varying sky conditions
Here is my implementation:
[gradient_methods](gradient_methods.py)

## Strength and Limitations
This method shows superior performance in complex scenarios, 
providing a more nuanced and accurate sky detection. 
However, it is more computationally intensive and may require optimization 
for real-time applications. 

## Demo Link
To further showcase the practicality and user-friendliness of my gradient-based sky detection method, 
I have developed an interactive Gradio demo. 
This online application provides a user-friendly interface where you can effortlessly upload your own images and immediately witness the effectiveness of the method in real time. 
The demo serves as an excellent platform for users to experiment with various images, 
particularly those with challenging lighting conditions, 
and observe the robustness and accuracy of our algorithm. 
I invite you to try out the demo and explore its capabilities firsthand at
[Sky Detection Demo](http://127.0.0.1:7860) based the following snippets:

[gradio_demo](gradio_demo.python)

# Comparative Analysis
This section will show the results obtained from applying the two distinct sky detection methods 
on a diverse set of 20 images. This comparative display will provide a straightforward 
and visual representation of the effectiveness of each technique. 
By examining the outcomes side-by-side, we aim to offer a clear and direct understanding of how each method performs 
under various conditions, highlighting their strengths and limitations. 
This visual comparison serves as a critical tool in evaluating the practical applicability and accuracy of 
our color thresholding and gradient-based methods in real-world scenarios. The most left side image is the original, and the second left
is the result from the traditional color thresholding, and the most right is the result from the gradient method.

![images1](output_images/combined_0.jpg)
![images2](output_images/combined_1.jpg)
![images3](output_images/combined_2.jpg)
![images4](output_images/combined_3.jpg)
![images5](output_images/combined_4.jpg)
![images6](output_images/combined_5.jpg)
![images7](output_images/combined_6.jpg)
![images8](output_images/combined_7.jpg)
![images9](output_images/combined_8.jpg)
![images10](output_images/combined_9.jpg)
![images11](output_images/combined_10.jpg)
![images12](output_images/combined_11.jpg)
![images13](output_images/combined_12.jpg)
![images14](output_images/combined_13.jpg)
![images15](output_images/combined_14.jpg)
![images16](output_images/combined_15.jpg)
![images17](output_images/combined_16.jpg)
![images18](output_images/combined_17.jpg)
![images19](output_images/combined_18.jpg)
![images20](output_images/combined_19.jpg)

In conclusion, the comparative analysis of our two sky detection methods clearly demonstrates 
the superior performance of the gradient-based approach, 
especially in complex lighting conditions. 
This method's effectiveness lies in its nuanced understanding of image textures and edges,
which allows for a more accurate differentiation between the sky and other elements in the image. 
Unlike the color thresholding method, which primarily relies on color information and can struggle with varied lighting scenarios like sunsets, 
the gradient-based method adapts more effectively to a range of environmental conditions. 
Its ability to capture subtle changes in light and shadow provides a more robust and consistent detection of the sky, 
making it an inherently more versatile and reliable technique for sky detection tasks.
This project underscores the importance of selecting the right algorithmic approach in image processing,
particularly in applications where lighting conditions can be unpredictable and varied.

# Reflection 
## Effectiveness of the Approach
### Technique 1: Color Thresholding in HSV Color Space
1. Effectiveness: This technique proved effective in environments with clear, uniform skies. It excelled in simplicity and computational efficiency, making it suitable for real-time applications or situations with limited processing power.
2. Limitations: Its effectiveness was limited under varied lighting conditions. For instance, during sunsets or in overcast weather, the technique struggled to accurately detect the sky due to the wide range of colors that these conditions present.
### Technique 2: Gradient-Based Methods and Median Filtering
1. Effectiveness: This approach demonstrated high accuracy in complex lighting scenarios, such as during sunsets or in cloudy conditions. Its use of gradient-based edge detection and median filtering effectively captured the nuances of different sky conditions.
2. Limitations: The primary limitation was its computational intensity. This method may not be ideal for time-sensitive applications or devices with limited processing capabilities.

## Potential Improvements
1. Hybrid Approach: Combining both methods could leverage the speed of color thresholding and the accuracy of gradient-based methods, potentially creating a more robust and versatile solution.
2. Machine Learning Integration: Employing machine learning, particularly deep learning techniques, could offer a more adaptive approach to sky detection, capable of learning from a wide range of scenarios and conditions.

## Learning Outcome
1. Technical Skills: The project enhanced my proficiency in image processing techniques, particularly in working with different color spaces and edge detection methods.
2. Problem-Solving: I developed a deeper understanding of how to approach a problem with multiple solutions and learned to evaluate the effectiveness of each.
3. Adaptability: This project underscored the importance of adaptability in algorithm design, especially in handling real-world variability in data.
4. Future Direction: I gained insights into the potential of machine learning in image processing and am motivated to explore this area further, recognizing its capacity to solve complex, dynamic problems in computer vision.

# Reference
1. Liu, K. (2022). An adaptive median filtering of visual product image based on gradient direction information. International Journal of Product Development, 26(1-4), 206-215.
2. Evans, A. N., & Liu, X. U. (2006). A morphological gradient approach to color edge detection. IEEE Transactions on Image Processing, 15(6), 1454-1463.
3. Zhu, R., & Wang, Y. (2012). Application of Improved Median Filter on Image Processing. J. Comput., 7(4), 838-841.