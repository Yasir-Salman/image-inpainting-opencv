# image-inpainting-opencv

This Python script utilizes OpenCV to perform image inpainting using the Navier-Stokes method. It restores damaged parts of an image based on a user-provided mask.


Key Features:

1. Inpaints images using OpenCV's inpaint function,
2. User-friendly command-line interface with options for image path, mask path, and inpainting radius,
3. Supports various image formats


Installation:

1. Ensure you have Python 3 installed,
2. Install OpenCV using pip: pip install opencv-python,
3. Optionally, install NumPy for better performance: pip install numpy


Usage:

1. Save the script as image_inpainting.py.
2. Place your image and mask files in the same directory as the script.
3. Open a command prompt or terminal and navigate to the directory containing the script and files.
4. Run the script with the following command, replacing <image_path>, <mask_path>, and <radius> (optional) with your actual values:

    python image_inpainting.py --image <image_path> --mask <mask_path> --radius <radius>

    Example:

    python image_inpainting.py --image ex01.png --mask mask01.png --radius 5

    This command will inpaint the image ex01.png using the mask mask01.png with a radius of 5 pixels. The inpainted image        will be saved as output_ns.jpg.


Explanation:

1. --image: Path to the image file to be inpainted.
2. --mask: Path to the mask file that highlights the damaged areas.
3. --radius (optional): Inpainting radius. Defaults to 3. Higher values can improve results but may increase processing time.

Additional Notes:
1. The script currently supports PNG image format.
2. Mask images should be in grayscale format.
3. Experiment with different radius values to find the optimal setting for your images.
4. For better performance, consider using a GPU-accelerated version of OpenCV.


Future Improvements:
1. Implement support for additional image formats (JPEG, TIFF, etc.).
2. Explore different inpainting algorithms for comparison.
3. Allow users to specify the output file name.
4. Add a graphical user interface (GUI) for easier interaction.
