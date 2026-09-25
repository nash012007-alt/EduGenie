import time
import pyautogui

# 5 செகண்ட் டைம் தரும் - உடனே SkillWallet பாக்ஸில் Click செய்ய வேண்டும்
time.sleep(5)

workflow_text = """EduGenie Project Workflow Architecture:
1.  user Interface (Frontend):
   - User inputs a learning query into the web interface.

2. API Request Routing:
   - Frontend captures input and sends a POST request to FastAPI backend at '/generate'.

3. FastAPI Backend:
   - Processes input and calls Google Gemini API using configured API Key.

4. Gemini AI Model:
   - Google Gemini Flash model processes prompt and generates explanation.
# Conclusion report updated
5. Response Delivery:
   - FastAPI receives response and returns it back to frontend UI."""

pyautogui.write(workflow_text, interval=0.01)