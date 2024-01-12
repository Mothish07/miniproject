from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (update this with your path)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def image_to_text(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    return text

# Replace 'path/to/your/image.png' with the actual path to your image file
image_path = '/home/mothish/Downloads/AdhaarCard.png'
result_text = image_to_text(image_path)

print("Text extracted from the image:")
print(result_text)
