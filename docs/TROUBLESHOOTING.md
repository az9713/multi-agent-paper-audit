# Troubleshooting Guide

This guide helps you solve common problems with the Multi-Agent Paper Audit tool. Problems are organized by when they occur.

---

## Table of Contents

1. [Installation Problems](#installation-problems)
2. [Starting the Tool](#starting-the-tool)
3. [During an Audit](#during-an-audit)
4. [Output Problems](#output-problems)
5. [Verification Code Issues](#verification-code-issues)
6. [Performance Issues](#performance-issues)
7. [Getting Help](#getting-help)

---

## Installation Problems

### Problem: "claude: command not found"

**What it means:** Your system can't find the Claude Code CLI.

**Solutions:**

1. **Check if it's installed:**
   ```bash
   npm list -g @anthropic-ai/claude-code
   ```

2. **If not installed, install it:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

3. **If installed but not found, add npm to PATH:**

   **Windows:**
   ```powershell
   $env:PATH += ";$env:APPDATA\npm"
   ```

   **Mac/Linux:**
   ```bash
   export PATH="$PATH:$(npm bin -g)"
   ```

4. **Restart your terminal** and try again.

---

### Problem: "npm: command not found"

**What it means:** Node.js isn't installed.

**Solution:**

1. **Download Node.js:** https://nodejs.org/
2. **Install it** (use the LTS version)
3. **Restart your terminal**
4. **Verify:**
   ```bash
   node --version
   npm --version
   ```

---

### Problem: "Permission denied" during install

**What it means:** You don't have permission to install globally.

**Solutions:**

**Windows:**
- Run PowerShell as Administrator (right-click → Run as Administrator)

**Mac/Linux:**
- Use sudo:
  ```bash
  sudo npm install -g @anthropic-ai/claude-code
  ```

**Alternative:** Install locally without sudo:
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
npm install -g @anthropic-ai/claude-code
```

---

### Problem: "API key invalid" or "Unauthorized"

**What it means:** Your Anthropic API key is wrong, missing, or expired.

**Solutions:**

1. **Check your current key:**
   ```bash
   claude config get api_key
   ```

2. **Set a new key:**
   ```bash
   claude config set api_key YOUR_API_KEY_HERE
   ```

3. **Get a new key:**
   - Go to https://console.anthropic.com/
   - Navigate to API Keys
   - Create a new key
   - Copy and use it

---

### Problem: "python: command not found"

**What it means:** Python isn't installed or not in PATH.

**Solutions:**

1. **Try python3 instead:**
   ```bash
   python3 --version
   ```

2. **If not installed, install Python:**
   - Download from https://python.org/downloads/
   - **Important:** Check "Add Python to PATH" during installation

3. **Restart your terminal** after installation

---

## Starting the Tool

### Problem: "No skills found" or "/audit-paper not recognized"

**What it means:** Claude Code can't find the skill files.

**Solutions:**

1. **Make sure you're in the right folder:**
   ```bash
   pwd
   # Should show: /path/to/multi-agent-paper-audit
   ```

2. **Check the skill files exist:**
   ```bash
   ls .claude/skills/paper-audit/
   # Should show: SKILL.md, agent-*.md files
   ```

3. **If files are missing, re-clone the project:**
   ```bash
   cd ..
   rm -rf multi-agent-paper-audit
   git clone https://github.com/az9713/multi-agent-paper-audit.git
   cd multi-agent-paper-audit
   ```

---

### Problem: Claude Code starts but hangs

**What it means:** The tool is waiting for input or has a network issue.

**Solutions:**

1. **Check internet connection:**
   ```bash
   ping google.com
   ```

2. **Wait a moment** - initial startup can take 10-20 seconds

3. **Try restarting:**
   - Press `Ctrl + C` to exit
   - Run `claude` again

---

### Problem: "Rate limit exceeded"

**What it means:** You've made too many API requests.

**Solutions:**

1. **Wait 1-2 minutes** and try again

2. **Check your API usage:** https://console.anthropic.com/usage

3. **Upgrade your plan** if needed

---

## During an Audit

### Problem: "Paper not found" or "Failed to fetch"

**What it means:** The tool can't download the paper from arXiv.

**Solutions:**

1. **Check the arXiv ID is correct:**
   - Format: `2512.24601` (4 digits, dot, 5 digits)
   - No extra spaces or characters

2. **Try different input formats:**
   ```
   /audit-paper 2512.24601
   /audit-paper arXiv:2512.24601
   /audit-paper https://arxiv.org/abs/2512.24601
   ```

3. **Check if arXiv is accessible:**
   - Open https://arxiv.org in your browser
   - If it's down, wait and try later

4. **Check your internet connection**

---

### Problem: Audit starts but freezes mid-way

**What it means:** An agent is taking too long or encountered an error.

**Solutions:**

1. **Wait a bit longer** - complex papers take more time

2. **Check the progress output:**
   - Which phase is it stuck on?
   - Any error messages?

3. **Cancel and retry:**
   - Press `Ctrl + C`
   - Run the audit again

4. **Try a different paper** to see if the issue is paper-specific

---

### Problem: "Agent X failed"

**What it means:** One of the agents encountered an error.

**Solutions:**

1. **Check the specific error message** - it usually tells you what's wrong

2. **Common agent failures:**

   | Agent | Common Issue | Solution |
   |-------|--------------|----------|
   | Agent A | Paper format unusual | Try HTML version |
   | Agent B | No theoretical claims | Normal - some papers are purely empirical |
   | Agent C | Web search failed | Check internet connection |
   | Agent D | Code execution failed | Check Python is installed |
   | Agent E | Missing inputs | Check previous agents completed |

3. **The audit continues** even if one agent fails - check partial results

---

### Problem: "Timeout" errors

**What it means:** An operation took too long.

**Solutions:**

1. **Try a shorter paper first** to verify the system works

2. **Check your internet speed** - slow connections cause timeouts

3. **If persistent, report the issue** with the paper ID

---

## Output Problems

### Problem: Missing output files

**What it means:** Some expected files weren't created.

**Solutions:**

1. **Check the output folder exists:**
   ```bash
   ls output/
   ```

2. **Check the specific paper folder:**
   ```bash
   ls output/2512.24601/
   ```

3. **Look for error messages** in the audit output

4. **Check which agent failed** - that agent's output will be missing

---

### Problem: Empty or truncated files

**What it means:** The agent didn't complete properly.

**Solutions:**

1. **Re-run the audit:**
   ```
   /audit-paper 2512.24601
   ```

2. **Check for errors** during the previous run

3. **If persistent**, check disk space:
   ```bash
   df -h
   ```

---

### Problem: JSON parse error in deconstruction.json

**What it means:** The JSON file is malformed.

**Solutions:**

1. **Validate the JSON:**
   ```bash
   python -c "import json; json.load(open('output/2512.24601/deconstruction.json'))"
   ```

2. **If invalid, re-run the audit**

3. **Check for special characters** in the paper that might cause issues

---

### Problem: README.md not created

**What it means:** Agent E didn't complete the final phase.

**Solutions:**

1. **Check if decision_memo.md exists** - README is created after it

2. **Look for Agent E errors** in the output

3. **Re-run the audit**

---

## Verification Code Issues

### Problem: "ModuleNotFoundError" when running verification

**What it means:** Python packages are missing.

**Solutions:**

1. **Install required packages:**
   ```bash
   pip install numpy matplotlib pandas
   ```

2. **If using virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   pip install numpy matplotlib pandas
   ```

---

### Problem: Verification code runs but shows errors

**What it means:** The code encountered issues during execution.

**Solutions:**

1. **Read the error message** - it usually tells you what's wrong

2. **Check execution_log.txt** for details

3. **Common fixes:**

   | Error | Solution |
   |-------|----------|
   | `FileNotFoundError` | Check you're in the right directory |
   | `ZeroDivisionError` | Paper might have unusual data |
   | `ValueError` | Data format issue - check the claim |

4. **You can modify the code** - it's designed to be edited

---

### Problem: Plots not generated

**What it means:** matplotlib had issues.

**Solutions:**

1. **Install matplotlib:**
   ```bash
   pip install matplotlib
   ```

2. **On headless servers, use Agg backend:**
   Add this at the top of main.py:
   ```python
   import matplotlib
   matplotlib.use('Agg')
   ```

---

## Performance Issues

### Problem: Audit takes very long (>10 minutes)

**What it means:** Something is slow, but it's still working.

**Possible causes:**

1. **Long paper** - Some papers are 40+ pages
2. **Complex paper** - Many claims to process
3. **Slow internet** - Fetching and searching takes time
4. **API slowness** - External services may be slow

**Solutions:**

1. **Be patient** - long papers take longer
2. **Try at a different time** - API might be congested
3. **Check your internet speed**

---

### Problem: High memory usage

**What it means:** The tool is using a lot of RAM.

**Solutions:**

1. **Close other applications** to free memory

2. **This is normal** for large papers

3. **If system becomes unresponsive:**
   - Press `Ctrl + C` to cancel
   - Restart with a smaller paper

---

### Problem: Tool crashes without error

**What it means:** Something unexpected happened.

**Solutions:**

1. **Check system logs:**

   **Windows:**
   - Open Event Viewer
   - Look for application errors

   **Mac:**
   - Open Console app
   - Look for recent errors

   **Linux:**
   ```bash
   journalctl -xe
   ```

2. **Try with a different paper**

3. **Report the issue** with your system details

---

## Getting Help

### Before Asking for Help

1. **Read this guide** - your issue might be covered

2. **Check existing issues:**
   https://github.com/az9713/multi-agent-paper-audit/issues

3. **Gather information:**
   - Operating system and version
   - Error message (exact text)
   - What you were trying to do
   - Steps to reproduce

### How to Report a Bug

1. Go to: https://github.com/az9713/multi-agent-paper-audit/issues

2. Click "New Issue"

3. Use this template:

```markdown
## Description
[What happened]

## Expected Behavior
[What you expected to happen]

## Steps to Reproduce
1. [First step]
2. [Second step]
3. [etc.]

## Error Message
```
[Paste exact error here]
```

## Environment
- OS: [Windows 10 / macOS 13 / Ubuntu 22.04]
- Claude Code version: [output of `claude --version`]
- Python version: [output of `python --version`]

## Paper ID (if applicable)
[e.g., 2512.24601]
```

### Community Resources

- **GitHub Discussions:** Ask questions and share tips
- **GitHub Issues:** Report bugs and request features

---

## Quick Reference

### Most Common Fixes

| Problem | Quick Fix |
|---------|-----------|
| Command not found | Restart terminal |
| API key error | Re-set API key |
| Paper not found | Check arXiv ID format |
| Agent failed | Re-run the audit |
| Missing output | Check for errors |
| Code won't run | Install: `pip install numpy matplotlib pandas` |

### Emergency Reset

If nothing works, try a complete reset:

```bash
# 1. Exit Claude Code
exit

# 2. Clear any cached data
rm -rf ~/.claude/cache

# 3. Re-clone the project
cd ..
rm -rf multi-agent-paper-audit
git clone https://github.com/az9713/multi-agent-paper-audit.git
cd multi-agent-paper-audit

# 4. Start fresh
claude
```
