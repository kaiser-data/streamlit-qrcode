# 🚀 Deploying to Hugging Face Spaces

Complete guide for deploying this QR Code Generator to Hugging Face Spaces.

---

## 📋 **Required Files and Naming**

Hugging Face Spaces has **specific file naming requirements**:

| Local File Name | Upload As | Required? | Purpose |
|----------------|-----------|-----------|---------|
| `qr_generator.py` | `qr_generator.py` | ✅ **YES** | Main application file |
| `requirements.txt` | `requirements.txt` | ✅ **YES** | Python dependencies |
| `Dockerfile` | `Dockerfile` | ✅ **YES** | Docker configuration |
| `README_HF.md` | **`README.md`** | ✅ **YES** | Space description with YAML metadata |
| `.streamlit/config.toml` | `.streamlit/config.toml` | ⚠️ Optional | Streamlit configuration |
| `screenshot.png` | `screenshot.png` | ⚠️ Optional | For README display |

### ⚠️ **CRITICAL NAMING REQUIREMENTS:**

1. **README must be named `README.md`** on Hugging Face (even though it's `README_HF.md` locally)
2. **Main app file** must match the `app_file:` in README.md YAML (we use `qr_generator.py`)
3. **Dockerfile** must be named exactly `Dockerfile` (no extension)

---

## 🔧 **Step-by-Step Deployment Process**

### **Step 1: Create Hugging Face Account**

1. Go to https://huggingface.co/join
2. Sign up (email or GitHub)
3. Verify your email address

---

### **Step 2: Create a New Space**

1. Click **"Spaces"** in the top menu
2. Click **"Create new Space"**
3. **Fill in the form:**

```
Space name: qr-code-generator
License: MIT
Select the SDK: Docker (Streamlit)  ← Must select Docker!
Space hardware: CPU basic - Free
Visibility: Public
```

4. **Click "Create Space"**

---

### **Step 3: Prepare README.md with Metadata**

Hugging Face Spaces **REQUIRES** a README.md with YAML frontmatter at the top.

**The YAML section (between `---` lines) is mandatory:**

```yaml
---
title: QR Code Generator          # Display name in Hugging Face
emoji: 📱                          # Icon shown in Space card
colorFrom: green                   # Gradient start color
colorTo: blue                      # Gradient end color
sdk: docker                        # MUST match your SDK choice
app_file: qr_generator.py          # Main Python file (MUST match actual filename!)
pinned: false                      # Pin to your profile
license: mit                       # Project license
---
```

**Full README.md content for Hugging Face:**

```markdown
---
title: QR Code Generator
emoji: 📱
colorFrom: green
colorTo: blue
sdk: docker
app_file: qr_generator.py
pinned: false
license: mit
---

# 📱 QR Code Generator

**Free & Open Source** • **No Ads** • **Privacy-Friendly**

Create custom QR codes with various styles, colors, and logos - all in your browser, completely free!

## ✨ Features

- 🚀 **Quick Start Templates** - URL, WiFi, Email, Phone, Text
- 🎨 **Full Customization** - Colors, shapes, sizes, error correction
- 🖼️ **Logo Integration** - Add your logo to QR codes
- 🛡️ **Privacy First** - No tracking, no data collection
- ⬇️ **Instant Download** - PNG format, ready to use

## 🚀 How to Use

1. Choose a template or enter your content
2. (Optional) Customize appearance
3. Download your QR code!

## 📦 Source Code

Full documentation and source code:
👉 [GitHub Repository](https://github.com/YOUR_USERNAME/streamlit-qrcode)
```

---

### **Step 4: Upload Files**

**On the Files tab of your Space:**

1. **Replace/Edit the template README.md:**
   - Click on `README.md` → Edit
   - Delete all template content
   - Paste the README content from Step 3
   - Commit changes

2. **Upload application files:**
   - Click **"Add file"** → **"Upload files"**
   - Select these files from your local project:
     - `qr_generator.py`
     - `requirements.txt`
     - `Dockerfile`
   - Commit message: `Add QR code generator app`
   - Click **"Commit changes to main"**

3. **Optional: Upload additional files:**
   - `screenshot.png` (for README)
   - `.streamlit/config.toml` (create `.streamlit` folder first)

---

### **Step 5: Wait for Build**

- Hugging Face automatically builds your Docker container
- **Build time:** 2-5 minutes (first build is slower)
- Watch the status indicator: **"Building"** → **"Running"**
- View build logs if needed (click on the status)

---

### **Step 6: Test Your App**

Once status shows **"Running"**:

1. Click the **"App"** tab
2. Your QR code generator is now **LIVE!** 🎉
3. Test all features:
   - Try different templates
   - Test customization options
   - Verify download functionality

**Your public URL:**
```
https://huggingface.co/spaces/YOUR_USERNAME/qr-code-generator
```

---

## 📁 **File Structure on Hugging Face**

After deployment, your Space should look like this:

```
qr-code-generator/
├── README.md              ← With YAML frontmatter (required!)
├── Dockerfile             ← Docker configuration (required!)
├── qr_generator.py        ← Main app (required!)
├── requirements.txt       ← Dependencies (required!)
├── screenshot.png         ← Optional
└── .streamlit/
    └── config.toml        ← Optional
```

---

## 🔍 **Dockerfile Requirements for Hugging Face**

Hugging Face Spaces expects your app to run on **port 7860**.

**Our Dockerfile (`Dockerfile`):**

```dockerfile
# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY qr_generator.py .

# Expose Streamlit port (Hugging Face requires 7860)
EXPOSE 7860

# Set environment variables
ENV STREAMLIT_SERVER_PORT=7860
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run the app
CMD ["streamlit", "run", "qr_generator.py", "--server.port=7860", "--server.address=0.0.0.0"]
```

**Key requirements:**
- ✅ Port **7860** (Hugging Face standard)
- ✅ Address **0.0.0.0** (accept external connections)
- ✅ Copy your main `.py` file
- ✅ Install all requirements

---

## 🔄 **Updating Your Deployed App**

To update your app after deployment:

### **Method 1: Direct Upload (Easiest)**

1. Go to your Space → **Files** tab
2. Click on the file you want to update
3. Click **"Edit"** (for text files) or upload new version
4. Commit changes
5. App automatically rebuilds (1-2 minutes)

### **Method 2: Git Push (Advanced)**

```bash
# Clone your Space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/qr-code-generator
cd qr-code-generator

# Make changes to files
# ...

# Commit and push
git add .
git commit -m "Update app"
git push
```

App automatically rebuilds after push.

---

## ⚙️ **Common Issues & Solutions**

### **Issue 1: "Build failed" Error**

**Causes:**
- Wrong `app_file:` name in README.md YAML
- Missing required files
- Incorrect Dockerfile syntax
- Dependency conflicts in requirements.txt

**Solution:**
- Check that `app_file:` matches your actual Python filename
- Verify all required files are uploaded
- Check build logs for specific error messages

---

### **Issue 2: App Won't Start**

**Causes:**
- Wrong port (must be 7860)
- Streamlit can't find the main file
- Python syntax errors in code

**Solution:**
- Verify Dockerfile uses port 7860
- Check `app_file:` in README.md matches actual filename
- Test your code locally first: `streamlit run qr_generator.py`

---

### **Issue 3: README.md Metadata Not Working**

**Causes:**
- Missing `---` delimiters around YAML
- Incorrect YAML syntax (indentation, colons)
- Required fields missing

**Solution:**
- Ensure YAML is at the **very top** of README.md
- Check all required fields are present:
  - `title:`
  - `emoji:`
  - `sdk:`
  - `app_file:`

**Example correct format:**
```yaml
---
title: My App
emoji: 🚀
sdk: docker
app_file: main.py
---

# Rest of README...
```

---

### **Issue 4: Template Files Still Showing**

**Causes:**
- Didn't delete template `src/` folder
- Didn't upload your actual files

**Solution:**
- Delete template files/folders
- Upload your actual application files
- Make sure filenames match what's in README.md and Dockerfile

---

## 🆚 **Hugging Face vs Streamlit Cloud**

| Feature | Hugging Face Spaces | Streamlit Cloud |
|---------|-------------------|----------------|
| **Permissions** | ✅ Minimal (Space-only access) | ⚠️ Full repo access required |
| **Setup** | Manual file upload | GitHub OAuth integration |
| **Build Time** | 2-5 minutes | 2-3 minutes |
| **Free Tier** | ✅ Yes (CPU basic) | ✅ Yes |
| **Auto-Deploy** | ✅ Yes (on git push) | ✅ Yes (on git push) |
| **Custom Domain** | 💰 Paid | 💰 Paid |
| **Docker Support** | ✅ Native | ⚠️ Limited |
| **Privacy** | ✅ Better (minimal access) | ⚠️ More access required |

---

## 📝 **Checklist for Deployment**

Use this checklist when deploying:

- [ ] Created Hugging Face account
- [ ] Created new Space with **Docker SDK**
- [ ] Updated README.md with proper YAML frontmatter
- [ ] Verified `app_file:` matches actual Python filename
- [ ] Uploaded `qr_generator.py`
- [ ] Uploaded `requirements.txt`
- [ ] Uploaded `Dockerfile` (with port 7860)
- [ ] Removed any template files
- [ ] Waited for build to complete (2-5 min)
- [ ] Tested app functionality
- [ ] Shared public URL! 🎉

---

## 🎯 **Best Practices**

1. **Test Locally First:**
   ```bash
   streamlit run qr_generator.py
   ```
   Make sure it works before deploying!

2. **Keep README.md YAML Simple:**
   - Only include required fields
   - Double-check `app_file:` matches your filename
   - Use consistent emoji and colors

3. **Optimize Docker Build:**
   - Put `COPY requirements.txt` before `COPY *.py`
   - This caches dependency installation
   - Faster rebuilds when only code changes

4. **Monitor Build Logs:**
   - Click on build status to see logs
   - Helps debug issues quickly
   - Shows what's being installed

5. **Keep Dependencies Minimal:**
   - Only include packages you actually use
   - Faster builds and smaller containers

---

## 🔗 **Useful Links**

- **Hugging Face Spaces Docs:** https://huggingface.co/docs/hub/spaces
- **Spaces Config Reference:** https://huggingface.co/docs/hub/spaces-config-reference
- **Docker SDK Guide:** https://huggingface.co/docs/hub/spaces-sdks-docker
- **This Project on GitHub:** https://github.com/kaiser-data/streamlit-qrcode

---

## 📞 **Need Help?**

- **Hugging Face Community:** https://discuss.huggingface.co/
- **This Project Issues:** https://github.com/kaiser-data/streamlit-qrcode/issues

---

**Congratulations! Your app is deployed on Hugging Face Spaces!** 🎉
