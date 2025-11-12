# 📱 QR Code Generator

A simple, user-friendly QR code generator built with Streamlit. Create custom QR codes with various styles, colors, and even add logos - all in your browser!

## ✨ Features

- **🚀 Quick Start Templates** - One-click templates for URL, WiFi, Email, Phone, and Text
- **🎨 Customization Options** - Colors, shapes, sizes, and error correction levels
- **🖼️ Logo Integration** - Add your logo or image to the center of QR codes
- **📱 Mobile-Friendly** - Works perfectly on phones and tablets
- **⬇️ Instant Download** - Download QR codes as PNG images
- **✅ Input Validation** - Smart hints and warnings for better results
- **💡 Helpful Tips** - Built-in examples and best practices

## 🚀 Quick Start

### Run Locally

1. Clone this repository:
```bash
git clone <your-repo-url>
cd streamlit-QRCode
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run qr_generator.py
```

4. Open your browser to `http://localhost:8501`

### Deploy to Streamlit Cloud (Free Hosting)

1. **Fork/Upload to GitHub**
   - Create a new repository on GitHub
   - Push this code to your repository

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository, branch, and `qr_generator.py`
   - Click "Deploy"

3. **That's it!** Your app will be live in a few minutes at a free Streamlit URL

## 📖 How to Use

### Basic Usage

1. **Choose a template** (optional) - Click one of the quick start buttons
2. **Enter your content** - Type or paste your text/URL
3. **Download** - Click the download button to save your QR code

### WiFi QR Codes

1. Click the "WiFi" template button
2. Enter your network name (SSID)
3. Enter your password
4. Select security type
5. Download and share!

### Customization

Click "🎨 Customize Appearance (Optional)" to access:

- **Colors & Style** - Change QR code and background colors, select module shapes
- **Size** - Adjust resolution and border thickness
- **Logo** - Upload a logo to place in the center

## 📋 Requirements

- Python 3.7+
- streamlit >= 1.28.0
- qrcode[pil] >= 7.4.2
- Pillow >= 10.0.0

## 🎯 Use Cases

- **Marketing** - Create QR codes for websites, social media, promotions
- **Events** - WiFi access, event registration, contact info
- **Business Cards** - vCard, contact details, LinkedIn profiles
- **Menus** - Restaurant menus, price lists
- **Education** - Learning resources, assignments, feedback forms
- **Personal** - Share WiFi, contact info, messages

## 💡 Tips for Best Results

- Keep content short for easier scanning
- Use URL shorteners for long links
- Test QR codes before printing
- Use high error correction when adding logos
- Ensure good contrast (dark on light background)
- Maintain minimum print size of 2×2 cm

## 🛠️ Technical Details

### QR Code Features

- **Error Correction Levels**: Low (7%), Medium (15%), High (25%), Very High (30%)
- **Module Shapes**: Square, Rounded, Circle, Gapped Square
- **Output Format**: PNG
- **Resolution**: Adjustable (5-30 pixels per module)

### Supported QR Code Types

- URLs and websites
- WiFi credentials
- Email addresses
- Phone numbers
- SMS messages
- Plain text
- Any custom formatted string

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- QR code generation by [python-qrcode](https://github.com/lincolnloop/python-qrcode)
- Image processing by [Pillow](https://python-pillow.org/)

## 📞 Support

If you encounter any issues or have questions:

1. Check the "ℹ️ Tips & Examples" section in the app
2. Review this README
3. Open an issue on GitHub

---

**Made with ❤️ using Streamlit**
