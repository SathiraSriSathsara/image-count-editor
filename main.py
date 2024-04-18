from PIL import Image, ImageDraw, ImageFont
import os

# Paths to the input and output directories
input_folder = './input'
output_folder = './output'

# Create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load a font
try:
    font = ImageFont.truetype('arial.ttf', 100)
except IOError:
    font = ImageFont.load_default()

# Collect and sort files to maintain order
files = [f for f in os.listdir(input_folder) if f.endswith((".jpg", ".jpeg", ".png"))]
files.sort()

# Total files count to determine number width
total_files = len(files)
width = len(str(total_files))

# Rename files sequentially in the input directory
for index, filename in enumerate(files, start=1):
    old_path = os.path.join(input_folder, filename)
    new_filename = f"{str(index).zfill(width)}{os.path.splitext(filename)[1]}"  # Adding leading zeros
    new_path = os.path.join(input_folder, new_filename)
    os.rename(old_path, new_path)

# Process each renamed image in the folder
for index, filename in enumerate(sorted(os.listdir(input_folder)), start=1):
    if filename.endswith((".jpg", ".jpeg", ".png")):  # Check for supported image files
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)

        # Add text (the number and position can be adjusted)
        text = str(index).zfill(width)  # Add leading zeros
        draw.text((15, 15), text, (255, 0, 0), font=font)

        # Save the edited image
        edited_filename = f"edited_{filename}"
        output_path = os.path.join(output_folder, edited_filename)
        img.save(output_path)

        print(f"Processed {filename} -> {output_path}")

# Confirm completion
print("Processing complete. Edited images saved to:", output_folder)
