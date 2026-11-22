import os
import json
from pathlib import Path
from datetime import datetime

import streamlit as st

# Optional OpenAI-compatible client
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


# =========================================================
# NOVAMIND AI
# Universal AI Assistant & Creative Workspace
# =========================================================

APP_NAME = "NovaMind AI"
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

CHAT_FILE = DATA_DIR / "chat_history.json"


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NovaMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CUSTOM UI
# =========================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {
    font-family: Inter, sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(124,58,237,.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(6,182,212,.12),
            transparent 30%
        ),
        #060914;
    color: #f8fafc;
}

.block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
}

section[data-testid="stSidebar"] {
    background: #080c16;
    border-right: 1px solid rgba(255,255,255,.08);
}

.nova-brand {
    padding: 10px 4px 25px;
}

.nova-logo {
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -1px;
}

.nova-logo span {
    color: #8b5cf6;
}

.nova-tag {
    color: #94a3b8;
    font-size: 11px;
    margin-top: 4px;
}

.hero {
    padding: 38px;
    border-radius: 26px;
    background:
        linear-gradient(
            135deg,
            rgba(124,58,237,.24),
            rgba(8,145,178,.10)
        ),
        rgba(15,23,42,.7);
    border: 1px solid rgba(139,92,246,.25);
    box-shadow: 0 25px 90px rgba(0,0,0,.25);
}

.hero h1 {
    font-size: 44px;
    font-weight: 800;
    margin: 10px 0;
}

.hero p {
    color: #a5b4fc;
    font-size: 16px;
}

.badge {
    display: inline-block;
    padding: 6px 11px;
    border-radius: 999px;
    background: rgba(139,92,246,.14);
    border: 1px solid rgba(139,92,246,.30);
    color: #c4b5fd;
    font-size: 10px;
    font-weight: 700;
}

.card {
    background: rgba(15,23,42,.72);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;
}

.card-icon {
    font-size: 29px;
}

.card-title {
    margin-top: 9px;
    font-weight: 700;
    font-size: 16px;
}

.card-text {
    margin-top: 6px;
    color: #94a3b8;
    font-size: 12px;
    line-height: 1.5;
}

.stat {
    padding: 18px;
    border-radius: 18px;
    background: rgba(15,23,42,.65);
    border: 1px solid rgba(255,255,255,.07);
}

.stat-number {
    font-size: 27px;
    font-weight: 800;
}

.stat-label {
    color: #94a3b8;
    font-size: 11px;
}

.chat-welcome {
    padding: 30px;
    text-align: center;
    border-radius: 22px;
    background: rgba(15,23,42,.55);
    border: 1px solid rgba(255,255,255,.07);
    margin-bottom: 20px;
}

.small {
    color: #94a3b8;
    font-size: 12px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 10px;
    margin-top: 45px;
}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True


# =========================================================
# NAVIGATION
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="nova-brand">
            <div class="nova-logo">
                Nova<span>Mind</span> AI
            </div>
            <div class="nova-tag">
                Your Intelligent Everything Assistant
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Workspace")

    navigation = [
        ("🏠", "Home"),
        ("💬", "AI Chat"),
        ("🎨", "Image Studio"),
        ("🎬", "Video Studio"),
        ("✍️", "Prompt Lab"),
        ("💻", "Code Assistant"),
        ("📄", "Document AI"),
        ("🗂️", "History"),
    ]

    for icon, name in navigation:
        if st.button(
            f"{icon}  {name}",
            key=f"nav_{name}",
            use_container_width=True,
        ):
            st.session_state.page = name
            st.rerun()

    st.markdown("---")

    if st.button(
        "💎 Premium Hub",
        use_container_width=True
    ):
        st.session_state.page = "Premium Hub"
        st.rerun()

    if st.button(
        "⚙️ Settings",
        use_container_width=True
    ):
        st.session_state.page = "Settings"
        st.rerun()

    st.markdown("---")

    st.markdown(
        """
        <div class="small">
        NovaMind AI v3.0<br>
        Universal AI Workspace
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# AI CLIENT
# =========================================================

def get_ai_client():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or OpenAI is None:
        return None

    return OpenAI(api_key=api_key)


# =========================================================
# REAL AI RESPONSE
# =========================================================

def ask_ai(user_message):

    client = get_ai_client()

    if client is None:

        return """
**NovaMind AI is currently running in Demo Mode.**

To activate the full AI assistant, add your API key as:

`OPENAI_API_KEY`

Then restart the application.

Once connected, NovaMind AI can handle normal conversation,
questions, coding, writing, brainstorming, explanations,
summaries and many other tasks.
"""

    try:

        response = client.chat.completions.create(
            model=os.getenv(
                "NOVAMIND_MODEL",
                "gpt-4o-mini"
            ),
            messages=[
                {
                    "role": "system",
                    "content": """
You are NovaMind AI, a friendly, intelligent,
general-purpose AI assistant.

Your job is to help the user with almost any
legitimate question or task.

You can:
- answer general questions
- explain difficult topics
- help with school and learning
- write and rewrite text
- help with programming
- debug code
- brainstorm ideas
- create plans
- create image prompts
- create video scripts
- summarize information
- analyze documents
- have natural casual conversations

Be helpful, accurate, clear and natural.

If the user says Hi, Hello, Hey, How are you,
or similar casual greetings, respond naturally
instead of giving a technical answer.

If the user asks a question you don't know,
say that clearly instead of inventing facts.

Do not claim to have browsed the internet unless
a real browsing tool is connected.
"""
                },
                *st.session_state.messages,
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as error:

        return f"""
⚠️ **NovaMind AI connection error**

The AI service could not complete this request.

Please check:
- API key
- Internet connection
- Model name
- API account status

Technical message:

`{str(error)}`
"""


# =========================================================
# HOME
# =========================================================

def home():

    st.markdown(
        """
        <div class="hero">
            <span class="badge">NEXT-GENERATION AI ASSISTANT</span>

            <h1>Meet NovaMind AI</h1>

            <p>
            Your intelligent everything assistant for questions,
            conversations, coding, creativity, documents and ideas.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    stats = [
        ("∞", "Questions"),
        ("24/7", "AI Assistant"),
        ("10+", "Creative Tools"),
        ("1", "Unified Workspace"),
    ]

    for col, (number, label) in zip(
        [c1, c2, c3, c4],
        stats
    ):

        with col:
            st.markdown(
                f"""
                <div class="stat">
                    <div class="stat-number">{number}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    st.markdown("## What can NovaMind AI do?")

    features = [
        ("💬", "AI Chat",
         "Ask questions, have conversations and get explanations."),
        ("🎨", "Image Studio",
         "Create advanced prompts for image generation."),
        ("🎬", "Video Studio",
         "Build scripts, scenes and short-video concepts."),
        ("💻", "Code Assistant",
         "Write, explain, debug and improve code."),
        ("✍️", "Prompt Lab",
         "Turn simple ideas into powerful AI prompts."),
        ("📄", "Document AI",
         "Summarize and analyze your documents."),
        ("🧠", "Idea Engine",
         "Brainstorm projects, content and business ideas."),
        ("🔐", "Privacy",
         "Keep API credentials out of your source code."),
    ]

    cols = st.columns(4)

    for index, feature in enumerate(features):

        with cols[index % 4]:
            feature_card(*feature)


# =========================================================
# FEATURE CARD
# =========================================================

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


# =========================================================
# AI CHAT
# =========================================================

def ai_chat():

    st.markdown("# 💬 NovaMind AI")

    st.markdown(
        """
        <div class="chat-welcome">
            <span class="badge">GENERAL PURPOSE AI</span>
            <h2>How can I help you today?</h2>
            <div class="small">
            Ask me anything — questions, coding, writing,
            learning, ideas or just have a conversation.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Display previous messages
    for message in st.session_state.messages:

        role = message["role"]

        if role == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])

        else:
            with st.chat_message("assistant"):
                st.markdown(message["content"])

    prompt = st.chat_input(
        "Message NovaMind AI..."
    )

    if prompt:

        # Show user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate answer
        with st.chat_message("assistant"):

            with st.spinner("NovaMind is thinking..."):

                answer = ask_ai(prompt)

            st.markdown(answer)

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        save_conversation()

        st.rerun()


# =========================================================
# SAVE CONVERSATION
# =========================================================

def save_conversation():

    history = []

    if CHAT_FILE.exists():

        try:
            history = json.loads(
                CHAT_FILE.read_text()
            )
        except Exception:
            history = []

    history.append(
        {
            "id": len(history) + 1,
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "messages": st.session_state.messages
        }
    )

    # Keep recent conversations
    history = history[-50:]

    CHAT_FILE.write_text(
        json.dumps(
            history,
            indent=2,
            ensure_ascii=False
        )
    )


# =========================================================
# IMAGE STUDIO
# =========================================================

def image_studio():

    st.markdown("# 🎨 Image Studio")

    subject = st.text_area(
        "Describe your image",
        placeholder=(
            "Example: cinematic portrait of a stylish "
            "young man standing in a futuristic city"
        ),
    )

    style = st.selectbox(
        "Style",
        [
            "Ultra Realistic",
            "Cinematic",
            "Editorial Fashion",
            "Anime",
            "3D",
            "Fantasy",
            "Minimal",
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
            "Dramatic",
        ],
    )

    if st.button(
        "✨ Generate Professional Prompt",
        use_container_width=True
    ):

        prompt = f"""
Create a {style.lower()} image featuring:

{subject}

Visual Direction:
Professional composition, realistic details,
high-quality textures, natural proportions,
strong subject separation and cinematic depth.

Lighting:
{lighting} lighting with realistic highlights,
shadows and reflections.

Camera:
Professional photography, sharp focus,
natural perspective and detailed environment.

Aspect Ratio:
{ratio}

Negative Requirements:
blurry image, distorted anatomy, duplicate objects,
extra fingers, unnatural proportions, low detail.
"""

        st.markdown("### Generated Prompt")

        st.code(
            prompt.strip(),
            language="text"
        )


# =========================================================
# VIDEO STUDIO
# =========================================================

def video_studio():

    st.markdown("# 🎬 Video Studio")

    idea = st.text_area(
        "Video idea",
        placeholder="Example: futuristic AI assistant wakes up in 2035"
    )

    duration = st.selectbox(
        "Duration",
        [
            "15 seconds",
            "30 seconds",
            "60 seconds",
            "90 seconds",
        ]
    )

    platform = st.selectbox(
        "Platform",
        [
            "YouTube Shorts",
            "Instagram Reels",
            "TikTok",
            "YouTube",
        ]
    )

    if st.button(
        "🎬 Create Video Blueprint",
        use_container_width=True
    ):

        st.markdown(
            f"""
### Video Blueprint

**Idea:** {idea}

**Platform:** {platform}

**Duration:** {duration}

#### Scene 1 — Hook
Create an immediate visual hook.

#### Scene 2 — Introduction
Establish the story and main subject.

#### Scene 3 — Main Action
Use dynamic camera movement and strong visuals.

#### Scene 4 — Payoff
Deliver the main reveal or interesting moment.

#### Scene 5 — Ending
Finish naturally with a memorable final shot.

### Visual Style

Cinematic lighting, realistic motion,
high-detail environment, smooth transitions
and professional composition.
"""
        )


# =========================================================
# PROMPT LAB
# =========================================================

def prompt_lab():

    st.markdown("# ✍️ Prompt Lab")

    raw_prompt = st.text_area(
        "Enter your simple idea",
        placeholder="Make a futuristic city..."
    )

    prompt_type = st.selectbox(
        "Prompt Type",
        [
            "Image",
            "Video",
            "Writing",
            "Coding",
            "Marketing",
            "Research",
        ]
    )

    if st.button(
        "🚀 Upgrade Prompt",
        use_container_width=True
    ):

        enhanced = f"""
ROLE:
Act as an expert {prompt_type.lower()} specialist.

OBJECTIVE:
{raw_prompt}

REQUIREMENTS:
- Make the request specific
- Add useful context
- Improve clarity
- Define the desired output
- Remove ambiguity
- Keep the result practical

FINAL OUTPUT:
Return a polished, production-ready prompt.
"""

        st.markdown("### Enhanced Prompt")

        st.code(
            enhanced.strip(),
            language="text"
        )


# =========================================================
# CODE ASSISTANT
# =========================================================

def code_assistant():

    st.markdown("# 💻 Code Assistant")

    request = st.text_area(
        "What do you want to build?",
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

    if st.button(
        "💻 Generate Development Plan",
        use_container_width=True
    ):

        st.markdown(
            f"""
### Development Plan

**Language:** {language}

**Project:**
{request}

### Architecture

1. Project structure
2. Core functionality
3. Input validation
4. Error handling
5. Security
6. Configuration
7. Testing
8. Deployment

### Security

Never hard-code API keys or passwords.
Use environment variables and validate user input.
"""
        )


# =========================================================
# DOCUMENT AI
# =========================================================

def document_ai():

    st.markdown("# 📄 Document AI")

    uploaded = st.file_uploader(
        "Upload a document",
        type=[
            "txt",
            "md",
            "pdf",
            "docx",
            "csv"
        ]
    )

    operation = st.selectbox(
        "Operation",
        [
            "Summarize",
            "Extract Key Points",
            "Create Study Notes",
            "Generate Questions",
            "Rewrite Professionally",
        ]
    )

    if uploaded:

        st.success(
            f"Document loaded: {uploaded.name}"
        )

        if st.button(
            "📄 Analyze Document",
            use_container_width=True
        ):

            st.info(
                f"""
Document: {uploaded.name}

Requested operation:
{operation}

The document-processing layer is ready
for full AI integration.
"""
            )


# =========================================================
# HISTORY
# =========================================================

def history_page():

    st.markdown("# 🗂️ Chat History")

    if not CHAT_FILE.exists():

        st.info("No saved conversations yet.")
        return

    try:
        history = json.loads(
            CHAT_FILE.read_text()
        )
    except Exception:
        history = []

    if not history:

        st.info("No saved conversations yet.")
        return

    for conversation in reversed(history):

        date = conversation.get(
            "date",
            "Unknown date"
        )

        messages = conversation.get(
            "messages",
            []
        )

        with st.expander(
            f"Conversation — {date}"
        ):

            for message in messages:

                role = message.get(
                    "role",
                    ""
                )

                content = message.get(
                    "content",
                    ""
                )

                if role == "user":

                    st.markdown(
                        f"**You:** {content}"
                    )

                else:

                    st.markdown(
                        f"**NovaMind AI:** {content}"
                    )


# =========================================================
# PREMIUM HUB
# =========================================================

def premium_hub():

    st.markdown("# 💎 Premium Hub")

    st.markdown(
        """
        <div class="hero">
            <span class="badge">NOVAMIND PRO</span>
            <h1>Unlock More AI Power</h1>
            <p>
            Advanced tools, higher limits and premium workspace features.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
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

    for index, (name, price) in enumerate(plans):

        with cols[index % 3]:

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-icon">💎</div>
                    <div class="card-title">
                        {name}
                    </div>
                    <div class="card-text">
                        Advanced AI tools<br>
                        Higher usage limits<br>
                        Premium workspace<br><br>

                        <strong style="font-size:22px">
                        {price}
                        </strong>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                f"Choose {name}",
                key=f"premium_{index}",
                use_container_width=True
            ):

                st.success(
                    f"{name} selected."
                )


# =========================================================
# SETTINGS
# =========================================================

def settings():

    st.markdown("# ⚙️ Settings")

    st.markdown("### AI Configuration")

    st.info(
        "For GitHub, keep API keys in environment variables "
        "or Streamlit secrets. Do not commit them to GitHub."
    )

    model = st.text_input(
        "AI Model",
        value=os.getenv(
            "NOVAMIND_MODEL",
            "gpt-4o-mini"
        )
    )

    st.markdown("### Interface")

    st.selectbox(
        "Theme",
        [
            "Cyber Dark",
            "Midnight",
            "Minimal Dark",
        ]
    )

    st.toggle(
        "Save chat history",
        value=True
    )

    st.toggle(
        "Enable animations",
        value=True
    )

    if st.button(
        "💾 Save Settings"
    ):

        st.success(
            "Settings saved for this session."
        )


# =========================================================
# ROUTER
# =========================================================

page = st.session_state.page

if page == "Home":
    home()

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

elif page == "History":
    history_page()

elif page == "Premium Hub":
    premium_hub()

elif page == "Settings":
    settings()


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        © 2026 NovaMind AI — Your Intelligent Everything Assistant
    </div>
    """,
    unsafe_allow_html=True,
)