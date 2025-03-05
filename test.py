import subprocess
from PIL import Image, ImageDraw, ImageFont
import os

class CommandHandle:
    def __init__(self, input_path, output, tv, music_file):
        self.image_file = input_path
        self.output_path = output
        self.time_value = str(tv)
        self.music_file = music_file  

        # Check if the image file exists
        if not os.path.exists(self.image_file):
            print(f"Error: Image file '{self.image_file}' not found!")
            exit(1)  # Stop script if the image is missing
        if not os.path.exists(self.music_file):
            print(f"Error: Music file '{self.music_file}' not found!")
            exit(1)

        # FFmpeg parameters command
        self.command = [
            "ffmpeg",
            "-loop", "1", # makes the video loops
            "-i", self.image_file, # source image
            "-i", self.music_file,  # Add background music
            "-c:v", "libx264", # encoding
            "-c:a", "aac",  # Audio codec
            "-b:a", "192k",  # Audio bitrate
            "-t", self.time_value,
            "-pix_fmt", "yuv420p",
            "-vf", "scale=1920:1080", # resolution of the video
            "-shortest",  # Ensures video matches audio length
            "-y", self.output_path
        ]

    def trigger_command(self):
        # Run FFmpeg and capture output
        try:
            process = subprocess.run(self.command, capture_output=True, text=True, check=True)
            print("STDOUT:", process.stdout)  # Shows normal output
            print("STDERR:", process.stderr)  # Shows errors (if any)
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg failed:\n{e.stderr}")
            exit(1)

        # Debug: Check if output file was created
        if os.path.exists(self.output_path):
            print(f"Successfully created: {self.output_path}")
        else:
            print("Error: Video not created!")


class ProcessImage:
    def __init__(self, path, output):
        self.image = Image.open(path)
        self.output = output

    def transform_image(self, transformation="grayscale"):
        if transformation == "grayscale":
            self.image = self.image.convert("L")  # Convert to grayscale
        elif transformation == "rotate":
            self.image = self.image.rotate(45)  # Rotate 45 degrees
        elif transformation == "resize":
            self.image = self.image.resize((800, 800))  # Resize to 800x800

        self.image.save(self.output)  # Save modified image

    def add_text(self, text, font_size=50):
        # Create a drawing object
        draw = ImageDraw.Draw(self.image)


        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except OSError:
            font = ImageFont.load_default()  # Use default if the font is missing


        # Calculate text size correctly
        if hasattr(draw, "textbbox"):
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        else:
            text_width, text_height = draw.textsize(text, font=font)

        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        # Define text position (centered)
        position = ((self.image.width - text_width) // 2, (self.image.height - text_height) // 2)

        # **Fix:** Adjust text color based on image mode
        text_color = 255 if self.image.mode == "L" else (255, 255, 255)  # White for RGB, 255 for grayscale

        # Add text to the image
        draw.text(position, text, fill=text_color, font=font)

        # Save and show the modified image
        self.image.save(self.output)
        self.image.show()



# Example usage (this won't run automatically)
if __name__ == "__main__":
    input_image = input("Enter image filename: ")  # e.g., "cat_9125207.jpg"
    output_image = "output.jpg"
    output_video = "output.mp4"
    background_music = input("Enter background music filename: ")  # e.g., "background.mp3"

    text_to_add = input("Enter text to overlay: ")  # e.g., "I am a cat"
    font_size = int(input("Enter font size: "))  # e.g., 100
    transformation_type = input("Choose transformation (grayscale/rotate/resize): ").strip().lower()

    # Process image
    image_processor = ProcessImage(input_image, output_image)
    image_processor.transform_image(transformation_type)  # Apply transformation
    image_processor.add_text(text_to_add, font_size)

    # Generate video with music
    command_instance = CommandHandle(output_image, output_video, 5, background_music)
    command_instance.trigger_command()