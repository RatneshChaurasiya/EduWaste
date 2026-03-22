import io
from PIL import Image, ImageDraw, ImageFont
import datetime

def generate_certificate(name):
    # Create a blank image with a nice white/gray background
    width, height = 1200, 800
    img = Image.new('RGB', (width, height), color=(250, 250, 250))
    draw = ImageDraw.Draw(img)

    # Draw a decorative border
    border_color = (46, 139, 87) # SeaGreen
    draw.rectangle([20, 20, width-20, height-20], outline=border_color, width=10)
    draw.rectangle([35, 35, width-35, height-35], outline=border_color, width=4)

    # Attempt to load Arial fonts, fallback if unavailable
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 60)
        font_subtitle = ImageFont.truetype("arial.ttf", 36)
        font_name = ImageFont.truetype("arialbd.ttf", 90)
        font_message = ImageFont.truetype("arial.ttf", 32)
        font_date = ImageFont.truetype("arial.ttf", 28)
    except IOError:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_message = ImageFont.load_default()
        font_date = ImageFont.load_default()

    # Draw Title
    title = "CERTIFICATE OF COMPLETION"
    draw.text((width/2, 160), title, font=font_title, fill=border_color, anchor="mm")

    # Draw Subtitle
    subtitle = "This is proudly presented to"
    draw.text((width/2, 300), subtitle, font=font_subtitle, fill=(80, 80, 80), anchor="mm")

    # Draw Name
    name_display = name.upper() if name else "PARTICIPANT"
    draw.text((width/2, 450), name_display, font=font_name, fill=(0, 0, 0), anchor="mm")

    # Draw Message
    message = "For successfully completing the Waste Management Quiz and Survey,\ndemonstrating a commitment to environmental awareness and sustainability."
    draw.text((width/2, 600), message, font=font_message, fill=(80, 80, 80), anchor="mm", align="center")

    # Draw Date
    date_str = datetime.date.today().strftime("%B %d, %Y")
    draw.text((width/2, 700), f"Awarded on: {date_str}", font=font_date, fill=(100, 100, 100), anchor="mm")

    # Identify project/signature area
    draw.text((width/2, 740), "EduWaste — Waste Management Awareness", font=font_date, fill=(150, 150, 150), anchor="mm")

    # Add Logo
    import os
    logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "logo.png")
    if os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo.thumbnail((220, 220), Image.Resampling.LANCZOS)
            img.paste(logo, (60, 60), logo)
        except Exception:
            pass

    # Convert image to bytes
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
