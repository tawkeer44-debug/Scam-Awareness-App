import os
import json
import uuid
import time
from datetime import datetime
from pathlib import Path

import streamlit as st


# =========================================================
# CYBER MIND PRO
# Modern AI Productivity & Creative Studio
# GitHub-ready single-file starter
# =========================================================

APP_NAME = "Cyber Mind Pro"
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

CHAT_FILE = DATA_DIR / "chats.json"


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(91, 33, 182, .16), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(6, 182, 212, .12), transparent 30%),
        #070b14;
    color: #f8fafc;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
}

section[data-testid="stSidebar"] {
    background: #090d18;
    border-right: 1px solid rgba(255,255,255,.08);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.2rem;
}

.brand {
    padding: 10px 5px 22px 5px;
}

.brand-title {
    font-size: 25px;
    font-weight: 800;
    letter-spacing: -1px;
}

.brand-title span {
    color: #8b5cf6;
}

.brand-subtitle {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 4px;
}

.hero {
    padding: 35px;
    border-radius: 25px;
    background:
        linear-gradient(135deg,
            rgba(124,58,237,.22),
            rgba(8,145,178,.12)),
        rgba(15,23,42,.8);
    border: 1px solid rgba(139,92,246,.25);
    box-shadow: 0 20px 80px rgba(0,0,0,.25);
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero p {
    color: #a5b4fc;
    font-size: 16px;
}

.card {
    background: rgba(15,23,42,.72);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;
    transition: .2s ease;
}

.card:hover {
    border-color: rgba(139,92,246,.45);
    transform: translateY(-2px);
}

.card-icon {
    font-size: 30px;
    margin-bottom: 10px;
}

.card-title {
    font-size: 17px;
    font-weight: 700;
}

.card-text {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 6px;
}

.stat {
    background: rgba(15,23,42,.65);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 18px;
    padding: 18px;
}

.stat-number {
    font-size: 27px;
    font-weight: 800;
}

.stat-label {
    color: #94a3b8;
    font-size: 12px;
}

.badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    background: rgba(139,92,246,.15);
    border: 1px solid rgba(139,92,246,.3);
    color: #c4b5fd;
    font-size: 11px;
    font-weight: 600;
}

.feature-box {
    background: linear-gradient(
        135deg,
        rgba(30,41,59,.75),
        rgba(15,23,42,.75)
    );
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 18px;
}

.small-muted {
    color: #94a3b8;
    font-size: 12px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 11px;
    margin-top: 40px;
}

</style>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------

def load_chats():
    if CHAT_FILE.exists():
        try:
            return json.loads(CHAT_FILE.read_text())
        except Exception:
            return []
    return []


def save_chats(chats):
    CHAT_FILE.write_text(json.dumps(chats, indent=2))


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chats" not in st.session_state:
    st.session_state.chats = load_chats()

if "premium" not in st.session_state:
    st.session_state.premium = False


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-title">Cyber <span>Mind</span> Pro</div>
            <div class="brand-subtitle">AI • Creative • Productivity Studio</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Workspace")

    nav_items = [
        ("🏠", "Dashboard"),
        ("💬", "AI Chat"),
        ("🎨", "Image Studio"),
        ("🎬", "Video Studio"),
        ("✍️", "Prompt Lab"),
        ("💻", "Code Assistant"),
        ("📄", "Document AI"),
        ("🗂️", "Recents"),
    ]

    for icon, name in nav_items:
        if st.button(
            f"{icon}  {name}",
            key=f"nav_{name}",
            use_container_width=True,
        ):
            st.session_state.page = name
            st.rerun()

    st.markdown("---")
    st.markdown("### Pro")

    if st.button("💎 Premium Hub", use_container_width=True):
        st.session_state.page = "Premium Hub"
        st.rerun()

    if st.button("⚙️ Settings", use_container_width=True):
        st.session_state.page = "Settings"
        st.rerun()

    st.markdown("---")

    st.markdown(
        """
        <div class="small-muted">
        Cyber Mind Pro v2.0<br>
        Modern AI workspace
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------

def page_title(title, subtitle=""):
    st.markdown(f"# {title}")
    if subtitle:
        st.markdown(
            f"<div class='small-muted'>{subtitle}</div>",
            unsafe_allow_html=True
        )


def feature_card(icon, title, description):
    st.markdown(
        f"""
        <div class="card">
            <div class="card-icon">{icon}</div>
            <div class="card-title">{title}</div>
            <div class="card-text">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# AI DEMO ENGINE
# ---------------------------------------------------------

def demo_ai_response(prompt):

    p = prompt.lower()

    if "code" in p:
        return """Here is a clean approach:

1. Define the required functionality.
2. Separate UI from business logic.
3. Add error handling.
4. Store configuration in environment variables.
5. Test the feature before deployment.

For production, connect this module to your preferred AI API."""

    if "image" in p:
        return """Image concept generated:

Create a cinematic, ultra-detailed visual with strong composition,
natural lighting, realistic textures, professional color grading,
and a clean editorial finish.

You can send this prompt to your image-generation provider."""

    if "video" in p:
        return """Video concept:

Scene 1 — Establishing shot
Scene 2 — Main subject enters
Scene 3 — Dynamic camera movement
Scene 4 — Close-up/detail shot
Scene 5 — Cinematic ending

Recommended format: 9:16 for short-form social content."""

    if "hello" in p or "hi" in p:
        return "Hey! 👋 I'm Cyber Mind Pro. What would you like to create today?"

    return f"""Cyber Mind Pro response:

I understood your request as:

“{prompt}”

This demo version is ready for API integration. Replace the
demo_ai_response() function with your preferred AI provider to
enable real AI generation."""


# ---------------------------------------------------------
# DASHBOARD
# ---------------------------------------------------------

def dashboard():

    st.markdown(
        """
        <div class="hero">
            <span class="badge">NEXT-GEN AI WORKSPACE</span>
            <h1>Welcome to Cyber Mind Pro</h1>
            <p>Create. Code. Write. Design. Analyze. All from one workspace.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
            <div class="stat">
            <div class="stat-number">24/7</div>
            <div class="stat-label">AI Workspace</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="stat">
            <div class="stat-number">10+</div>
            <div class="stat-label">Creative Tools</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="stat">
            <div class="stat-number">∞</div>
            <div class="stat-label">Ideas</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            """
            <div class="stat">
            <div class="stat-number">Pro</div>
            <div class="stat-label">AI Suite</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown("## Quick Tools")

    cols = st.columns(4)

    tools = [
        ("💬", "AI Chat", "Ask questions, brainstorm and write."),
        ("🎨", "Image Studio", "Build professional image prompts."),
        ("🎬", "Video Studio", "Create scripts and video concepts."),
        ("💻", "Code Assistant", "Generate and explain code."),
    ]

    for col, item in zip(cols, tools):
        with col:
            feature_card(*item)

    st.write("")
    st.markdown("## Everything in one workspace")

    cols = st.columns(4)

    tools2 = [
        ("✍️", "Prompt Lab", "Improve any prompt."),
        ("📄", "Document AI", "Analyze and summarize files."),
        ("🧠", "Idea Engine", "Turn ideas into projects."),
        ("🔐", "Privacy Center", "Manage local settings."),
    ]

    for col, item in zip(cols, tools2):
        with col:
            feature_card(*item)


# ---------------------------------------------------------
# AI CHAT
# ---------------------------------------------------------

def ai_chat():

    page_title(
        "AI Chat",
        "Your intelligent workspace for ideas, writing, planning and coding."
    )

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Ask Cyber Mind Pro anything...")

    if prompt:

        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        response = demo_ai_response(prompt)

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()


# ---------------------------------------------------------
# IMAGE STUDIO
# ---------------------------------------------------------

def image_studio():

    page_title(
        "Image Studio",
        "Create professional prompts for image-generation workflows."
    )

    st.markdown(
        """
        <div class="feature-box">
        <span class="badge">IMAGE CREATOR</span>
        <h3>Build your visual concept</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    subject = st.text_input(
        "Subject",
        placeholder="Example: stylish young man in an urban street"
    )

    style = st.selectbox(
        "Visual Style",
        [
            "Ultra Realistic",
            "Cinematic",
            "Editorial Fashion",
            "Anime",
            "3D Render",
            "Minimal Studio",
            "Fantasy",
        ],
    )

    ratio = st.selectbox(
        "Aspect Ratio",
        ["1:1", "4:5", "16:9", "9:16"],
    )

    lighting = st.selectbox(
        "Lighting",
        [
            "Natural",
            "Cinematic",
            "Golden Hour",
            "Studio",
            "Neon",
            "Low Key",
        ],
    )

    if st.button("✨ Generate Prompt", use_container_width=True):

        prompt = f"""
Create a {style.lower()} image featuring {subject}.

Composition:
Professional framing, strong subject separation,
high visual clarity and balanced composition.

Lighting:
{lighting} lighting with realistic shadows and highlights.

Quality:
Ultra-detailed textures, realistic materials,
professional photography quality, clean composition.

Format:
{ratio}

Avoid:
distorted anatomy, extra fingers, duplicate objects,
blurry details, unnatural facial features.
"""

        st.markdown("### Generated Prompt")
        st.code(prompt.strip(), language="text")


# ---------------------------------------------------------
# VIDEO STUDIO
# ---------------------------------------------------------

def video_studio():

    page_title(
        "Video Studio",
        "Turn a simple idea into a structured short-video concept."
    )

    topic = st.text_input(
        "Video idea",
        placeholder="Example: futuristic AI assistant launches in 2030"
    )

    duration = st.selectbox(
        "Duration",
        ["15 seconds", "30 seconds", "60 seconds", "90 seconds"]
    )

    platform = st.selectbox(
        "Platform",
        ["YouTube Shorts", "Instagram Reels", "TikTok", "YouTube"]
    )

    if st.button("🎬 Build Video Script", use_container_width=True):

        st.markdown("### 🎥 Video Blueprint")

        st.markdown(
            f"""
**Topic:** {topic}

**Platform:** {platform}

**Duration:** {duration}

**Scene 1 — Hook**
Start with a visually strong opening that immediately creates curiosity.

**Scene 2 — Setup**
Introduce the idea and establish the situation.

**Scene 3 — Main Moment**
Show the most interesting part using dynamic camera movement.

**Scene 4 — Payoff**
Reveal the key result or surprising moment.

**Scene 5 — CTA**
Finish with a short, natural call to action.

**Visual Direction**
Cinematic lighting, smooth camera movement,
high-detail environment, realistic motion and clean composition.
"""
        )


# ---------------------------------------------------------
# PROMPT LAB
# ---------------------------------------------------------

def prompt_lab():

    page_title(
        "Prompt Lab",
        "Transform simple ideas into detailed AI-ready prompts."
    )

    raw = st.text_area(
        "Your rough idea",
        placeholder="Make a cool futuristic city..."
    )

    task = st.selectbox(
        "Prompt type",
        [
            "Image",
            "Video",
            "Writing",
            "Coding",
            "Marketing",
            "Research",
        ]
    )

    if st.button("🚀 Enhance Prompt", use_container_width=True):

        enhanced = f"""
ROLE:
You are an expert {task.lower()} assistant.

OBJECTIVE:
{raw}

REQUIREMENTS:
- Clear professional output
- Strong structure
- High-quality details
- Avoid ambiguity
- Follow the requested format
- Keep the final result practical and usable

OUTPUT:
Return the final production-ready {task.lower()} prompt.
"""

        st.markdown("### Enhanced Prompt")
        st.code(enhanced.strip(), language="text")


# ---------------------------------------------------------
# CODE ASSISTANT
# ---------------------------------------------------------

def code_assistant():

    page_title(
        "Code Assistant",
        "Generate, explain and improve software ideas."
    )

    request = st.text_area(
        "Describe what you want to build",
        placeholder="Create a Python login system..."
    )

    language = st.selectbox(
        "Programming Language",
        [
            "Python",
            "JavaScript",
            "TypeScript",
            "HTML/CSS",
            "React",
            "SQL",
            "C++",
        ]
    )

    if st.button("💻 Generate Code Plan", use_container_width=True):

        st.markdown("### Development Blueprint")

        st.markdown(
            f"""
**Language:** {language}

**Project Request:**
{request}

### Recommended Architecture

1. Project structure
2. Core functionality
3. Input validation
4. Error handling
5. Configuration management
6. Security considerations
7. Testing
8. Deployment

### Production Notes

Use environment variables for secrets,
avoid hard-coding API keys,
validate user input,
and separate frontend logic from backend services.
"""
        )


# ---------------------------------------------------------
# DOCUMENT AI
# ---------------------------------------------------------

def document_ai():

    page_title(
        "Document AI",
        "Upload a document and prepare it for AI-powered analysis."
    )

    uploaded = st.file_uploader(
        "Upload a document",
        type=["txt", "md", "pdf", "docx", "csv"]
    )

    operation = st.selectbox(
        "Choose operation",
        [
            "Summarize",
            "Extract key points",
            "Create study notes",
            "Generate questions",
            "Rewrite professionally",
        ]
    )

    if uploaded:

        st.success(f"Loaded: {uploaded.name}")

        if st.button("📄 Process Document"):

            st.markdown("### Analysis Request")

            st.info(
                f"""
Operation: {operation}

File: {uploaded.name}

The document is ready to be connected to a
real document-processing / AI backend.
"""
            )


# ---------------------------------------------------------
# RECENTS
# ---------------------------------------------------------

def recents():

    page_title(
        "Recents",
        "Your latest Cyber Mind Pro activity."
    )

    if not st.session_state.chats:

        st.info("No recent projects yet.")

    else:

        for chat in reversed(st.session_state.chats[-10:]):

            st.markdown(
                f"""
                <div class="feature-box">
                    <b>{chat.get("title", "Untitled")}</b><br>
                    <span class="small-muted">
                    {chat.get("date", "")}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ---------------------------------------------------------
# PREMIUM HUB
# ---------------------------------------------------------

def premium_hub():

    page_title(
        "Premium Hub",
        "Unlock the complete Cyber Mind Pro workspace."
    )

    plans = [
        ("7 Days", "$2.99"),
        ("1 Month", "$7.99"),
        ("6 Weeks", "$10.99"),
        ("9 Weeks", "$14.99"),
        ("6 Months", "$29.99"),
        ("9 Months", "$39.99"),
        ("10 Months", "$44.99"),
        ("1 Year", "$49.99"),
        ("4 Years", "$129.99"),
        ("Lifetime", "$199.99"),
    ]

    cols = st.columns(3)

    for i, (name, price) in enumerate(plans):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-icon">💎</div>
                    <div class="card-title">{name}</div>
                    <div class="card-text">
                        Premium AI tools<br><br>
                        <b style="font-size:22px">{price}</b>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                f"Choose {name}",
                key=f"plan_{i}",
                use_container_width=True,
            ):
                st.success(
                    f"{name} selected. Connect your payment system here."
                )

    st.markdown("---")

    st.markdown(
        """
        ### Premium Features

        • Advanced AI models  
        • Higher usage limits  
        • Image generation integration  
        • Video generation integration  
        • Advanced document processing  
        • Priority processing  
        • Project history  
        • Custom AI assistants  
        • Advanced prompt tools  
        • Premium themes
        """
    )


# ---------------------------------------------------------
# SETTINGS
# ---------------------------------------------------------

def settings():

    page_title(
        "Settings",
        "Configure your Cyber Mind Pro workspace."
    )

    st.markdown("### AI Configuration")

    provider = st.selectbox(
        "AI Provider",
        [
            "Demo Mode",
            "OpenAI-compatible API",
            "Custom API",
        ]
    )

    api_key = st.text_input(
        "API Key",
        type="password",
        placeholder="Enter API key"
    )

    st.markdown("### Interface")

    theme = st.selectbox(
        "Theme",
        ["Cyber Dark", "Midnight", "Minimal Dark"]
    )

    st.toggle("Enable animations", value=True)
    st.toggle("Save chat history", value=True)

    if st.button("💾 Save Settings"):
        st.success("Settings saved for this session.")


# ---------------------------------------------------------
# ROUTER
# ---------------------------------------------------------

page = st.session_state.page

if page == "Dashboard":
    dashboard()

elif page == "AI Chat":
    ai_chat()

elif page == "Image Studio":
    image_studio()

elif page == "Video Studio":
    video_studio()

elif page == "Prompt Lab":
    prompt_lab()

elif page == "Code Assistant":
    code_assistant()

elif page == "Document AI":
    document_ai()

elif page == "Recents":
    recents()

elif page == "Premium Hub":
    premium_hub()

elif page == "Settings":
    settings()


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        © 2026 Cyber Mind Pro • AI Creative & Productivity Workspace
    </div>
    """,
    unsafe_allow_html=True,
)