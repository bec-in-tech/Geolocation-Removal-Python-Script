import os
from PIL import Image

# Set the paths for the target and output folders
target_folder = r'C:\Users\leona\OneDrive\Desktop\SOS 2023 Photos\SOS_Photos'
output_folder = r'C:\Users\leona\OneDrive\Desktop\Updated SOS 2023 Photos'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to remove GPS information from a photo
def remove_gps_info(image_path):
    try:
        image = Image.open(image_path)

        # Check if the image has GPS info
        if "gpsinfo" in image.info:
            image.info["gpsinfo"] = None

        # Save the modified image to the output folder
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        image.save(output_path)
        print(f"GPS information removed from {os.path.basename(image_path)} and saved to {output_path}")

    except Exception as e:
        print(f"Error processing {os.path.basename(image_path)}: {str(e)}")

# Iterate through files in the target folder
completed = True
for filename in os.listdir(target_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        target_path = os.path.join(target_folder, filename)
        remove_gps_info(target_path)
    else:
        print(f"Skipping {filename} - Not a supported image format.")

# Check if any errors occurred during processing
if not completed:
    print("GPS information removal completed with errors.")
else:
    print("GPS information removal completed successfully.")
