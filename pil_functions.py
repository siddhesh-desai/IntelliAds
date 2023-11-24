from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(input_image_path, output_image_path, text, position=(10, 10), font_size=100, font_color=(25, 25, 25)):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)  # You can specify the path to your desired font file
    draw.text(position, text, font=font, fill=font_color)
    image.save(output_image_path)

input_path = "Template.png"
output_path = "modified_image.png"
text_to_add = "Hello Siddhesh"

add_text_to_image(input_path, output_path, text_to_add)