import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Page settings
st.set_page_config(
    page_title="AI Learning Buddy HimaBindu",
    page_icon="🎓"
)

# App title
st.title("🎓 AI Learning Buddy HimaBindu")

st.write("Learn any topic easily with AI assistance!")

# User input
topic = st.text_input("Enter a Topic")

# Activity selection
option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# Generate button
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        # Create prompts
        if option == "Explain Concept":
            prompt = f"""
            Explain {topic} in simple language for a beginner.
            Use easy words and a simple example.
            """

        elif option == "Real-Life Example":
            prompt = f"""
            Give one clear real-life example of {topic}.
            Explain how it works in simple terms.
            """

        elif option == "Generate Quiz":
            prompt = f"""
            Create 5 multiple-choice questions (MCQs) on {topic}.
            Give 4 options for each question and mention the correct answer.
            """

        else:
            prompt = topic


        # Generate AI response
        try:
            response = model.generate_content(prompt)

            st.subheader("🤖 AI Response")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error occurred: {e}")
