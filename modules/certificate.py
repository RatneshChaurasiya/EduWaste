import io
import os
import urllib.request
import uuid
from PIL import Image, ImageDraw, ImageFont
import datetime

def get_font(font_name, size):
    font_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "fonts")
    font_path = os.path.join(font_dir, f"{font_name}.ttf")
    
    # Attempt to load bundled static font
    if os.path.exists(font_path):
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
            
    # Fallback to system fonts if custom fails to load/download
    # This prevents the font from becoming unreadably small
    system_fallbacks = [
        "arialbd.ttf", "arial.ttf", "times.ttf", "georgia.ttf", 
        "trebuc.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans.ttf", 
        "FreeSans.ttf", "LiberationSans-Regular.ttf"
    ]
    for fb in system_fallbacks:
        try:
            return ImageFont.truetype(fb, size)
        except Exception:
            continue
            
    # Ultimate fallback to default pixel font
    return ImageFont.load_default()

def generate_certificate(name):
    width, height = 1200, 800
    
    # ── Background ───────────────────────────────────────────
    # Elegant off-white background with a slight warm tint
    img = Image.new('RGB', (width, height), color=(253, 251, 247))
    draw = ImageDraw.Draw(img)

    # ── Borders ──────────────────────────────────────────────
    border_outer = (34, 94, 60) # Deep Emerald Green
    border_inner = (197, 160, 89) # Premium Gold
    
    # Outer dark green border
    draw.rectangle([20, 20, width-20, height-20], outline=border_outer, width=12)
    # Inner gold border
    draw.rectangle([40, 40, width-40, height-40], outline=border_inner, width=4)

    # Decorative inner corner accents
    c_len = 40
    # Top-Left
    draw.line((40, 40+c_len, 40+c_len, 40), fill=border_inner, width=4)
    # Top-Right
    draw.line((width-40-c_len, 40, width-40, 40+c_len), fill=border_inner, width=4)
    # Bottom-Left
    draw.line((40, height-40-c_len, 40+c_len, height-40), fill=border_inner, width=4)
    # Bottom-Right
    draw.line((width-40, height-40-c_len, width-40-c_len, height-40), fill=border_inner, width=4)

    # ── Load Fonts ───────────────────────────────────────────
    font_title = get_font("title", 48)
    font_subtitle = get_font("text", 26)
    font_name = get_font("name", 80) 
    font_message = get_font("text", 22)
    font_date = get_font("text", 18)
    font_small = get_font("text", 16)

    # ── Paste Logo (Top Center) ──────────────────────────────
    logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "logo.png")
    logo_offset_y = 0
    
    if os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo.thumbnail((160, 160), Image.Resampling.LANCZOS)
            logo_w, logo_h = logo.size
            img.paste(logo, (int(width/2 - logo_w/2), 55), logo)
            logo_offset_y = 130 # Shift text elements below down
        except Exception:
            pass

    # ── Render Text ──────────────────────────────────────────
    # 1. Certificate Title
    draw.text((width/2, 160 + logo_offset_y), "CERTIFICATE OF COMPLETION", 
              font=font_title, fill=border_outer, anchor="mm")
    
    # 2. Subtitle
    draw.text((width/2, 250 + logo_offset_y), "This certificate is proudly awarded to", 
              font=font_subtitle, fill=(100, 100, 100), anchor="mm")
    
    # 3. User Name
    name_display = name.title() if name else "Participant Name"
    draw.text((width/2, 350 + logo_offset_y), name_display, 
              font=font_name, fill=border_inner, anchor="mm")
    
    # Name underline
    try:
        name_bbox = draw.textbbox((width/2, 350 + logo_offset_y), name_display, font=font_name, anchor="mm")
        line_y = name_bbox[3] + 15
        draw.line((width/2 - 250, line_y, width/2 + 250, line_y), fill=(210, 210, 210), width=2)
    except AttributeError:
        # Fallback for older PIL versions without textbbox
        line_y = 400 + logo_offset_y
        draw.line((width/2 - 250, line_y, width/2 + 250, line_y), fill=(210, 210, 210), width=2)
    
    # 4. Completion Message
    message = (
        "For successfully passing the Waste Management Quiz and Survey.\n"
        "Thank you for demonstrating a strong commitment to\n"
        "environmental awareness and sustainability."
    )
    draw.text((width/2, 470 + logo_offset_y), message, 
              font=font_message, fill=(80, 80, 80), anchor="mm", align="center")
    
    # 5. Date and Signature Fields (Bottom)
    date_str = datetime.date.today().strftime("%B %d, %Y")
    bottom_y = height - 120
    
    # Date Line
    draw.line((250, bottom_y, 450, bottom_y), fill=(100, 100, 100), width=1)
    draw.text((350, bottom_y + 25), "Date", font=font_date, fill=(100, 100, 100), anchor="mm")
    draw.text((350, bottom_y - 20), date_str, font=font_date, fill=(0, 0, 0), anchor="mm")
    
    # Signature Line (Line Removed)
    draw.text((width - 350, bottom_y + 25), "EduWaste Team", font=font_date, fill=(100, 100, 100), anchor="mm")
    
    # Very bottom branding
    draw.text((width/2, height - 75), "Together towards a cleaner and greener future.", 
              font=font_small, fill=(100, 100, 100), anchor="mm")
              
    # Unique Certificate ID (Bottom Left)
    cert_id = f"Certificate ID: {uuid.uuid4().hex[:10].upper()}"
    draw.text((70, height - 75), cert_id, font=font_small, fill=(100, 100, 100), anchor="lm")

    # ── Export ───────────────────────────────────────────────
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
