import streamlit as st
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    RoundedModuleDrawer, CircleModuleDrawer,
    GappedSquareModuleDrawer, SquareModuleDrawer
)
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image
import io
import re

# Helper function to convert hex color to RGB tuple
def hex_to_rgb(hex_color):
    """Convert hex color string to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Page configuration
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better UX
st.markdown("""
<style>
    .big-input textarea {
        font-size: 18px !important;
    }
    .template-button {
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        cursor: pointer;
    }
    .stDownloadButton button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 12px;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'qr_data' not in st.session_state:
    st.session_state.qr_data = "https://streamlit.io"
if 'template_type' not in st.session_state:
    st.session_state.template_type = "url"
if 'show_advanced' not in st.session_state:
    st.session_state.show_advanced = False

# Header
st.title("📱 QR Code Generator")
st.markdown("**Create a QR code in seconds** - Enter your content below or choose a template")

# ============ TEMPLATES (QUICK START) ============
st.markdown("### 🚀 Quick Start Templates")

templates = [
    ("URL", "🌐", "url", "https://example.com"),
    ("WiFi", "📶", "wifi", ""),
    ("Email", "📧", "email", "mailto:name@example.com"),
    ("Phone", "📞", "phone", "tel:+1234567890"),
    ("Text", "💬", "text", "Hello World!")
]

# Create responsive grid layout (3 columns on first row, 2 on second)
col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for idx, (name, icon, template_id, placeholder) in enumerate(templates[:3]):
    with cols[idx]:
        if st.button(f"{icon}\n{name}", use_container_width=True, key=f"btn_{template_id}"):
            st.session_state.template_type = template_id
            if template_id == "wifi":
                st.session_state.qr_data = ""
            else:
                st.session_state.qr_data = placeholder
            st.rerun()

col4, col5, col6 = st.columns(3)
cols2 = [col4, col5, col6]

for idx, (name, icon, template_id, placeholder) in enumerate(templates[3:]):
    with cols2[idx]:
        if st.button(f"{icon}\n{name}", use_container_width=True, key=f"btn_{template_id}"):
            st.session_state.template_type = template_id
            if template_id == "wifi":
                st.session_state.qr_data = ""
            else:
                st.session_state.qr_data = placeholder
            st.rerun()

# ============ SMART INPUT AREA ============
st.markdown("---")

# Template-specific input
if st.session_state.template_type == "wifi":
    st.markdown("### 📶 WiFi Configuration")
    col1, col2 = st.columns(2)
    with col1:
        wifi_ssid = st.text_input("Network Name (SSID)", placeholder="MyWiFi")
        wifi_password = st.text_input("Password", type="password", placeholder="password123")
    with col2:
        wifi_security = st.selectbox("Security Type", ["WPA", "WEP", "nopass"], index=0)
        wifi_hidden = st.checkbox("Hidden Network", value=False)

    # Generate WiFi QR format
    if wifi_ssid:
        hidden_str = "true" if wifi_hidden else "false"
        if wifi_security == "nopass":
            qr_data = f"WIFI:T:{wifi_security};S:{wifi_ssid};H:{hidden_str};;"
        else:
            qr_data = f"WIFI:T:{wifi_security};S:{wifi_ssid};P:{wifi_password};H:{hidden_str};;"
    else:
        qr_data = ""
else:
    # Standard input for all other types
    input_labels = {
        "url": "🌐 Enter your URL or website",
        "email": "📧 Enter email address or mailto link",
        "phone": "📞 Enter phone number",
        "text": "💬 Enter any text"
    }

    label = input_labels.get(st.session_state.template_type, "Enter your content")

    qr_data = st.text_area(
        label,
        value=st.session_state.qr_data,
        height=100,
        placeholder="Type or paste your content here...",
        key=f"input_{st.session_state.template_type}"
    )
    st.session_state.qr_data = qr_data

# Input validation and helpful feedback
validation_message = ""
validation_type = "info"

if qr_data:
    # URL validation
    if st.session_state.template_type == "url":
        url_pattern = re.compile(r'^https?://')
        if not url_pattern.match(qr_data):
            validation_message = "💡 Tip: URLs should start with http:// or https://"
            validation_type = "warning"

    # Character count
    char_count = len(qr_data)
    if char_count > 2000:
        validation_message = f"⚠️ Warning: {char_count} characters may result in a complex QR code"
        validation_type = "warning"
    elif char_count > 500:
        validation_message = f"ℹ️ {char_count} characters - consider using a URL shortener for easier scanning"
        validation_type = "info"

if validation_message:
    if validation_type == "warning":
        st.warning(validation_message)
    else:
        st.info(validation_message)

# ============ CUSTOMIZATION (COLLAPSED BY DEFAULT) ============
with st.expander("🎨 Customize Appearance (Optional)", expanded=False):

    tab1, tab2, tab3 = st.tabs(["Colors & Style", "Size", "Logo"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            fill_color = st.color_picker("QR Code Color", "#000000")
            module_style = st.selectbox(
                "Shape Style",
                options=["Square", "Rounded", "Circle", "Gapped Square"],
                help="Shape of the QR code modules"
            )
        with col2:
            back_color = st.color_picker("Background Color", "#FFFFFF")
            error_correction = st.select_slider(
                "Error Correction",
                options=["Low", "Medium", "High", "Very High"],
                value="Medium",
                help="Higher levels make QR code more readable if damaged"
            )

    with tab2:
        box_size = st.slider(
            "Resolution (pixels per module)",
            min_value=5,
            max_value=30,
            value=10,
            help="Higher = larger file size but better quality"
        )
        border_size = st.slider(
            "Border Thickness",
            min_value=1,
            max_value=10,
            value=4
        )

    with tab3:
        st.markdown("Add a logo or image to the center of your QR code")
        logo_file = st.file_uploader(
            "Upload logo",
            type=["png", "jpg", "jpeg"],
            help="Best results with square, transparent PNG images"
        )

        if logo_file:
            logo_size_percent = st.slider(
                "Logo size (%)",
                min_value=10,
                max_value=40,
                value=20,
                help="Logo shouldn't exceed 30% for reliable scanning"
            )
        else:
            logo_size_percent = 20
            st.info("💡 Tip: Use high error correction with logos to maintain scannability")

# ============ QR CODE GENERATION ============

# Maps
error_correction_map = {
    "Low": qrcode.constants.ERROR_CORRECT_L,
    "Medium": qrcode.constants.ERROR_CORRECT_M,
    "High": qrcode.constants.ERROR_CORRECT_Q,
    "Very High": qrcode.constants.ERROR_CORRECT_H
}

module_drawer_map = {
    "Square": SquareModuleDrawer(),
    "Rounded": RoundedModuleDrawer(),
    "Circle": CircleModuleDrawer(),
    "Gapped Square": GappedSquareModuleDrawer()
}

def generate_qr_code(data, fill, back, style, error_lvl, box, border, logo, logo_size):
    """Generate QR code with given parameters"""
    try:
        # Convert hex colors to RGB tuples
        fill_rgb = hex_to_rgb(fill)
        back_rgb = hex_to_rgb(back)

        qr = qrcode.QRCode(
            version=1,
            error_correction=error_correction_map[error_lvl],
            box_size=box,
            border=border,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=module_drawer_map[style],
            color_mask=SolidFillColorMask(
                back_color=back_rgb,
                front_color=fill_rgb
            )
        )

        # Convert to standard PIL Image for Streamlit compatibility
        img = img.convert('RGB')

        # Add logo if provided
        if logo is not None:
            logo_img = Image.open(logo)

            # Calculate logo size
            qr_width, qr_height = img.size
            logo_max_size = min(qr_width, qr_height) * logo_size // 100

            # Resize logo maintaining aspect ratio
            logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)

            # Create a white background for logo if it doesn't have transparency
            if logo_img.mode != 'RGBA':
                logo_bg = Image.new('RGB', logo_img.size, 'white')
                logo_bg.paste(logo_img, (0, 0))
                logo_img = logo_bg

            # Calculate position to center logo
            logo_pos = (
                (qr_width - logo_img.width) // 2,
                (qr_height - logo_img.height) // 2
            )

            # Paste logo
            img.paste(logo_img, logo_pos, logo_img if logo_img.mode == 'RGBA' else None)

        return img, qr
    except Exception as e:
        st.error(f"Error generating QR code: {str(e)}")
        return None, None

# ============ DISPLAY QR CODE ============
st.markdown("---")

if qr_data:
    img, qr = generate_qr_code(
        qr_data, fill_color, back_color, module_style,
        error_correction, box_size, border_size, logo_file, logo_size_percent
    )

    if img:
        # Display QR code
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.image(img, use_container_width=True)

        # Download button (prominent)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="⬇️ Download QR Code",
            data=byte_im,
            file_name="qr_code.png",
            mime="image/png",
            use_container_width=True
        )

        # QR Code info
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Size", f"{img.size[0]}×{img.size[1]}px")
        with col2:
            st.metric("Version", qr.version)
        with col3:
            st.metric("Characters", len(qr_data))

else:
    # Show helpful message when empty
    st.info("👆 Enter content above or select a template to generate your QR code")

    # Show example QR code
    example_img, _ = generate_qr_code(
        "https://streamlit.io",
        "#000000", "#FFFFFF", "Square", "Medium", 10, 4, None, 20
    )
    if example_img:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(example_img, caption="Example QR Code", use_container_width=True)

# ============ HELPFUL TIPS ============
with st.expander("ℹ️ Tips & Examples"):
    st.markdown("""
    ### 📝 Format Examples:

    **Website/URL:**
    - `https://www.example.com`
    - `https://mysite.com/page?id=123`

    **Email:**
    - `mailto:name@example.com`
    - `mailto:name@example.com?subject=Hello&body=Message`

    **Phone:**
    - `tel:+1234567890`

    **SMS:**
    - `sms:+1234567890`
    - `sms:+1234567890?body=Hello there`

    **WiFi** (use WiFi template):
    - Automatically formatted when you fill the form

    **Plain Text:**
    - Any text you want to encode

    ### 💡 Best Practices:
    - Keep content short for easier scanning
    - Use URL shorteners for long links
    - Test QR codes before printing
    - Use high error correction if adding logos
    - Ensure good contrast (dark on light background)
    - Maintain minimum size (2×2 cm for print)
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888; font-size: 14px;'>"
    "Made with ❤️ using Streamlit | Scan safely!"
    "</div>",
    unsafe_allow_html=True
)
