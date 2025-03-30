# Burp Traffic Auto Highlight

## 📌 About
**Burp Auto Highlight** is just a small Burp Suite extension that automatically highlights HTTP requests based on custom headers. This helps security researchers differentiate traffic from multiple browsers. All traffic in the Proxy HTTP History will be different colors based on how it is configured!  Just a vibe code!

## ✨ Features
- 🚀 **Automatic Request Highlighting**: Colors requests based on custom headers.
- 🔍 **Improved Visibility**: Quickly identify requests from different browser sessions.
## Currently Working on
- 📜 **Regex-Based Matching**: Supports flexible header detection.
- 🎨 **Customizable Colors**: Modify highlight colors easily.

## 🛠 Setup & Installation
### 1️⃣ **Modify Headers in Browsers**
Use **ModHeader** (Chrome/Firefox extension) to send unique headers from different browsers.
- **Primary Browser:**
  - `X-Custom-Header: Primary`
- **Secondary Browser:**
  - `X-Custom-Header: Secondary`

### 2️⃣ **Save & Install Python Script in Burp Suite**
1. Open Burp Suite → Go to `Extender > Extensions`.
2. Click `Add` → Select `Python` as the extension type.
3. Choose the `auto_highlight.py` file.
4. Click `Next` → `Finish`.

### 3️⃣ **Clone and Run from GitHub**
```sh
# Clone the repository
git clone https://github.com/rokkamvamshi/burp-traffic-auto-highligter.git

# Navigate to the folder
cd burp-traffic-auto-highligter
```

## 🎨 Highlight Colors
- 🟠 **Primary Browser** → `orange`
- 🔵 **Secondary Browser** → `cyan`

## How it looks 
![Screenshot 2025-03-30 222159](https://github.com/user-attachments/assets/c719e0c5-1f1c-496f-b0e8-1e3b76239969)


## 📜 License
MIT License. Free to use and modify!

