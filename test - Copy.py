import subprocess
from PIL import Image, ImageDraw, ImageFont
import os


class CommandHandle:
    def __init__(self, input , output, tv):
        self.image_file =input
        self.output_path = output
        self.time_value = tv
        
    # Debug: Check if the image file exists
    image_file =""
    if not os.path.exists(image_file):
        print(f"Error: Image file '{image_file}' not found!")
        exit(1)  # Stop the script if the image is missing

    # FFmpeg parameters
    loops = "-loop"  # Fix variable naming
    image_path = "-i"
    encoding = "-c:v"
    codec = "libx264"
    duration = "-t"
    time_value = "5"
    compatibility = "-pix_fmt"
    pix_fmt_value = "yuv420p"
    rescales = "-vf"
    scale_value = "scale=1920:1080"
    quality = "-crf"
    quality_value = "0"
    output_path = "output.mp4"

    # Build FFmpeg command as a list (safer)
    command = [
        "ffmpeg",
        loops, "1",
        image_path, image_file,
        encoding, codec,
        duration, time_value,
        compatibility, pix_fmt_value,
        rescales, scale_value,
        quality, quality_value,
        "-y", output_path
    ]
    
    def trigger_command(self):
        # Run FFmpeg and capture output
        try:
            process = subprocess.run(self.command, capture_output=True, text=True, check=True)
            print("STDOUT:", process.stdout)  # Shows normal output
            print("STDERR:", process.stderr)  # Shows errors (if any)
        except subprocess.CalledProcessError as e:
            print(f"X FFmpeg failed :\n{e.stderr}")
            exit(1)

        # Debug: Check if output file was created
        if os.path.exists(self.output_path):
            print(f"successfully: {self.output_path}")
        else:
            print("X Error: Video not created!")
  
class ProcessImage:
    def __init__(self, path,output):
        self.image = Image.open(path)
        self.output = output

    output ="output.jpg"
    def add_text(self, text, font_size=50):
        # Create a drawing object
        draw = ImageDraw.Draw(self.image)

        # Choose a font and set size
        try:
            font = ImageFont.truetype("arial.ttf", font_size)  # Change font & size
        except:
            font = ImageFont.load_default()  # Fallback to default font

        # Define text position (centered)
        position = (self.image.width // 4, self.image.height // 4)

        # Set text color
        text_color = (255, 255, 255)  # White

        # Add text to the image
        draw.text(position, text, fill=text_color, font=font)

        # Save and show the modified image
        self.image.save("output.jpg")
        self.image.show()
        
        
# Example usage (this won't run automatically)
if __name__ == "__main__":
    outputImage ="output.jpg"
    image_processor = ProcessImage("cat_9125207.jpg","output.jpg")
    image_processor.add_text("I am a cat", font_size=400)  # Bigger text!
    command_instance = CommandHandle(outputImage,"cat", 5)
    command_instance.trigger_command()  # This will only run when explicitly called