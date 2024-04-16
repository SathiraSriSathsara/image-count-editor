from PIL import Image, ImageDraw, ImageFont
import os

# Paths to the input and output directories
input_folder = './input'
output_folder = './output'

# Create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load a font (the size can be adjusted to your needs)
try:
    font = ImageFont.truetype('arial.ttf', 75)
except IOError:
    font = ImageFont.load_default()

# Process each image in the folder
for index, filename in enumerate(sorted(os.listdir(input_folder)), 1):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):  # Check for supported image files
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)

        # Add text (the number and position can be adjusted)
        text = str(index)
        draw.text((15, 15), text, (255, 0, 0), font=font)

        # Save the edited image
        edited_filename = f"edited_{filename}"
        output_path = os.path.join(output_folder, edited_filename)
        img.save(output_path)

        print(f"Processed {filename} -> {output_path}")

# Confirm completion
print("Processing complete. Edited images saved to:", output_folder)
