from PIL import Image

def image_to_ascii(image_path, output_width=100):
    ascii_chars = "@%#*+=-:. "
    
    def pixel_to_ascii(pixel):
        # Convert pixel to ASCII using intensity
        intensity = sum(pixel[:3]) / 3  # Average of R, G, B
        return ascii_chars[int(intensity / 256 * len(ascii_chars))]
    
    # Load the image and convert to grayscale
    img = Image.open(image_path)
    width, height = img.size
    aspect_ratio = height / width
    new_width = output_width
    new_height = int(aspect_ratio * new_width * 0.55)
    img = img.resize((new_width, new_height))
    img = img.convert("RGB")  # To make sure image is in RGB format
    
    # Generate ASCII art
    ascii_art = []
    for y in range(new_height):
        line = ""
        for x in range(new_width):
            pixel = img.getpixel((x, y))
            line += pixel_to_ascii(pixel)
        ascii_art.append(line)
    
    return "\n".join(ascii_art)

# Path to your image
image_path = "C:\\Users\\user\\Downloads\\chill guy.jpeg"  # Replace with chill guy image
ascii_art = image_to_ascii(image_path)

# Save or print the ASCII art
with open("ascii_art.txt", "w") as f:
    f.write(ascii_art)
print(ascii_art)
