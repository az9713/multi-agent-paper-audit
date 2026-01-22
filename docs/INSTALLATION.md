# Installation Guide

This guide walks you through installing the Multi-Agent Paper Audit tool step by step. No prior experience required - we'll explain everything.

---

## Table of Contents

1. [What You're Installing](#what-youre-installing)
2. [System Requirements](#system-requirements)
3. [Step 1: Install Claude Code CLI](#step-1-install-claude-code-cli)
4. [Step 2: Install Python](#step-2-install-python)
5. [Step 3: Install Git](#step-3-install-git)
6. [Step 4: Download This Project](#step-4-download-this-project)
7. [Step 5: Verify Installation](#step-5-verify-installation)
8. [Troubleshooting Installation](#troubleshooting-installation)

---

## What You're Installing

Before we start, here's what each piece does:

| Component | What It Does | Why You Need It |
|-----------|--------------|-----------------|
| **Claude Code CLI** | AI-powered command line tool | Runs the audit agents |
| **Python** | Programming language | Runs verification scripts |
| **Git** | Version control | Downloads and updates the project |
| **This Project** | The audit pipeline | The actual tool you'll use |

---

## System Requirements

### Minimum Requirements

- **Operating System:** Windows 10+, macOS 10.15+, or Ubuntu 20.04+
- **RAM:** 4 GB (8 GB recommended)
- **Disk Space:** 500 MB free
- **Internet:** Required for fetching papers

### How to Check Your System

**Windows:**
1. Press `Windows + R`
2. Type `winver` and press Enter
3. You'll see your Windows version

**Mac:**
1. Click the Apple menu (top left)
2. Click "About This Mac"
3. You'll see your macOS version

**Linux:**
```bash
cat /etc/os-release
```

---

## Step 1: Install Claude Code CLI

Claude Code is an AI-powered command line tool. Here's how to install it:

### Windows

1. **Open PowerShell as Administrator:**
   - Press `Windows + X`
   - Click "Windows PowerShell (Admin)" or "Terminal (Admin)"

2. **Run this command:**
   ```powershell
   npm install -g @anthropic-ai/claude-code
   ```

   **Don't have npm?** Install Node.js first:
   - Go to https://nodejs.org/
   - Download the LTS version
   - Run the installer (click Next through all screens)
   - Restart PowerShell and try the npm command again

3. **Set up your API key:**
   ```powershell
   claude config set api_key YOUR_API_KEY_HERE
   ```

   **Don't have an API key?**
   - Go to https://console.anthropic.com/
   - Create an account
   - Go to API Keys section
   - Create a new key
   - Copy and paste it in the command above

### Mac

1. **Open Terminal:**
   - Press `Cmd + Space`
   - Type "Terminal" and press Enter

2. **Install Homebrew** (if you don't have it):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Install Node.js:**
   ```bash
   brew install node
   ```

4. **Install Claude Code:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

5. **Set up your API key:**
   ```bash
   claude config set api_key YOUR_API_KEY_HERE
   ```

### Linux (Ubuntu/Debian)

1. **Open Terminal** (Ctrl + Alt + T)

2. **Install Node.js:**
   ```bash
   curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

3. **Install Claude Code:**
   ```bash
   sudo npm install -g @anthropic-ai/claude-code
   ```

4. **Set up your API key:**
   ```bash
   claude config set api_key YOUR_API_KEY_HERE
   ```

### Verify Claude Code Installation

Run this command:
```bash
claude --version
```

You should see something like:
```
claude-code version 1.x.x
```

If you see an error, check the [Troubleshooting](#troubleshooting-installation) section.

---

## Step 2: Install Python

Python runs the verification scripts that check numerical claims.

### Check If Python Is Already Installed

```bash
python --version
```

or

```bash
python3 --version
```

If you see `Python 3.8` or higher, skip to [Step 3](#step-3-install-git).

### Windows

1. **Download Python:**
   - Go to https://www.python.org/downloads/
   - Click the big yellow "Download Python 3.x.x" button

2. **Run the installer:**
   - **IMPORTANT:** Check the box that says "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close"

3. **Restart your terminal** (close and reopen PowerShell)

4. **Verify:**
   ```powershell
   python --version
   ```

### Mac

Python 3 comes pre-installed on modern Macs. If you need to install it:

```bash
brew install python
```

Verify:
```bash
python3 --version
```

### Linux

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verify:
```bash
python3 --version
```

---

## Step 3: Install Git

Git downloads and updates the project.

### Check If Git Is Already Installed

```bash
git --version
```

If you see a version number, skip to [Step 4](#step-4-download-this-project).

### Windows

1. **Download Git:**
   - Go to https://git-scm.com/download/win
   - The download starts automatically

2. **Run the installer:**
   - Click Next through all screens (default options are fine)
   - Click Install
   - Click Finish

3. **Restart your terminal**

4. **Verify:**
   ```powershell
   git --version
   ```

### Mac

```bash
brew install git
```

Or Git will prompt you to install Xcode Command Line Tools when you first use it.

### Linux

```bash
sudo apt install git
```

---

## Step 4: Download This Project

Now let's get the actual paper audit tool.

### Option A: Clone with Git (Recommended)

1. **Choose where to put it:**

   **Windows:**
   ```powershell
   cd C:\Users\YourName\Documents
   ```

   **Mac/Linux:**
   ```bash
   cd ~/Documents
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/az9713/multi-agent-paper-audit.git
   ```

3. **Enter the project folder:**
   ```bash
   cd multi-agent-paper-audit
   ```

### Option B: Download ZIP (If Git Doesn't Work)

1. Go to https://github.com/az9713/multi-agent-paper-audit
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to your Documents folder
5. Open terminal and navigate to the folder:
   ```bash
   cd Documents/multi-agent-paper-audit-main
   ```

---

## Step 5: Verify Installation

Let's make sure everything works.

### Check 1: Are you in the right folder?

```bash
ls -la
```

You should see files like:
- `.claude/` (folder)
- `README.md`
- `CLAUDE.md`
- `docs/` (folder)

### Check 2: Can Claude Code find the skills?

```bash
claude
```

Then type:
```
/help
```

You should see `Audit this paper:` listed as an available skill.

### Check 3: Run a test audit

Inside Claude Code, type:
```
Audit this paper: 2512.24601
```

Wait for it to complete (3-5 minutes). If you see "Audit complete!" at the end, everything is working!

---

## Troubleshooting Installation

### Problem: "claude: command not found"

**Cause:** Claude Code isn't in your system PATH.

**Solution (Windows):**
1. Close and reopen PowerShell
2. If still not working, try:
   ```powershell
   npm install -g @anthropic-ai/claude-code
   ```

**Solution (Mac/Linux):**
1. Add npm global bin to PATH:
   ```bash
   echo 'export PATH="$PATH:$(npm bin -g)"' >> ~/.bashrc
   source ~/.bashrc
   ```

### Problem: "npm: command not found"

**Cause:** Node.js isn't installed.

**Solution:** Follow the Node.js installation steps in [Step 1](#step-1-install-claude-code-cli).

### Problem: "python: command not found"

**Cause:** Python isn't in your PATH.

**Solution (Windows):**
1. Reinstall Python
2. Make sure to check "Add Python to PATH" during installation

**Solution (Mac/Linux):**
Try `python3` instead of `python`.

### Problem: "Permission denied" errors

**Cause:** You don't have permission to install globally.

**Solution (Windows):** Run PowerShell as Administrator.

**Solution (Mac/Linux):** Use `sudo` before the command:
```bash
sudo npm install -g @anthropic-ai/claude-code
```

### Problem: "API key invalid"

**Cause:** Your Anthropic API key is wrong or expired.

**Solution:**
1. Go to https://console.anthropic.com/
2. Create a new API key
3. Run:
   ```bash
   claude config set api_key YOUR_NEW_KEY
   ```

### Problem: "git clone failed"

**Cause:** Network issues or repository URL wrong.

**Solution:**
1. Check your internet connection
2. Try the ZIP download option instead

### Problem: Audit starts but never finishes

**Cause:** Timeout or network issues.

**Solution:**
1. Check your internet connection
2. Try a smaller paper first
3. Check if arXiv is accessible: https://arxiv.org/

---

## What's Next?

Installation complete! Now:

1. **Read the [Quick Start Guide](QUICK_START.md)** - 10 example use cases
2. **Try auditing a paper in your field**
3. **Explore the [User Guide](USER_GUIDE.md)** for all features

---

## Getting Help

If you're stuck:

1. Check the [Troubleshooting Guide](TROUBLESHOOTING.md)
2. Search existing [GitHub Issues](https://github.com/az9713/multi-agent-paper-audit/issues)
3. Open a new issue with:
   - Your operating system
   - The exact error message
   - What you were trying to do
