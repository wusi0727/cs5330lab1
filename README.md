# CS5330-Lab1
## Sky Pixel Identification in Images using Traditional Computer Vision Techniques
### by Si Wu

#### Introduction 
This repo contains all my work of sky pixel identification 
project. I was exploring two methods to solve this problem and 
compared their effectiveness. 

#### How to Use
1. [sky_images](skyImages) stored all my 20 tested pictures with various sky appearances.
2. Run the [color_thresholding](color_thresholding.python.py), replace the "image_path" in the main to test the function.
3. Run the [gradient_methods](gradient_methods.py), replace the "image_path" in main to test its result.
4. I also write a program to generate a set of comparison to show the original image, the result from my first and the result from my second methods. They are all located in the [output_images folder](output_images).
5. You can also check your own tested images by running my [gradio_demo](gradio_demo.python) program, which employed my second method.
After you run this program, you will have a link to upload your image and submit it. On the left side, the output will appear.
6. Here is the link for my final report and documentation [final_report](final_report.md) 