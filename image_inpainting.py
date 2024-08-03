import cv2
import numpy as np

def inpaint_image(image_path, mask_path, radius=3):
  """Performs image inpainting using the Navier-Stokes method.

  Args:
    image_path: Path to the input image.
    mask_path: Path to the input mask.
    radius: Inpainting radius.

  Returns:
    The inpainted image.
  """

  image = cv2.imread(image_path)
  mask = cv2.imread(mask_path)

  # Convert mask to grayscale
  mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

  # Ensure image and mask have the same data type
  mask = mask.astype(image.dtype)

  # Use Navier-Stokes method for inpainting
  output = cv2.inpaint(image, mask, radius, flags=cv2.INPAINT_NS)

  return output

# Example usage
image_path = "...ex01.png" #enter image path
mask_path = "...mask01.png" #enter mask path
output_image = inpaint_image(image_path, mask_path, radius=25)
cv2.imwrite("output_ns.jpg", output_image)