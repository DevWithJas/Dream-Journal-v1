import streamlit as st
import openai

# Function to generate dream interpretation using GPT-3.5-turbo
def generate_dream_interpretation(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a dream interpreter."},
                {"role": "user", "content": prompt}
            ]
        )
        interpretation = response.choices[0].message['content']
        return interpretation
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to generate images using OpenAI's DALL-E model
def generate_dream_image(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app layout
st.set_page_config(
    page_title="Dream Interpreter and Image Generator",
    page_icon=":stars:",
    layout="wide"
)

st.title("Dream Interpreter and Image Generator")

# Adding animations in a single row
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown("![Dream Animation 1](https://media.giphy.com/media/srV1G3EnqSLtL11Nsx/giphy.gif)")
with col2:
    st.markdown("![Dream Animation 2](https://media.giphy.com/media/kHTE4l8X9LZ29iINbk/giphy.gif)")
with col3:
    st.markdown("![Dream Animation 3](https://media.giphy.com/media/uM0QzrHWSDr4KwbC3v/giphy.gif)")

# API key input
api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    dream_entry = st.text_area("Enter your dream", height=200)

    if st.button("Interpret Dream and Generate Image"):
        if dream_entry:
            with st.spinner('Interpreting your dream...'):
                interpretation = generate_dream_interpretation(dream_entry, api_key)

            st.markdown(f"## Dream Interpretation :thought_balloon:")
            st.write(interpretation)

            with st.spinner('Generating your dream image...'):
                dream_image_url = generate_dream_image(dream_entry, api_key)

            st.markdown(f"## Generated Dream Image :framed_picture:")
            st.image(dream_image_url, use_column_width=True)

            st.markdown("## Download Interpretation")
            st.download_button(
                label="Download Interpretation",
                data=interpretation,
                file_name="dream_interpretation.txt",
                key="download_interpretation"
            )
        else:
            st.warning("Please enter your dream before generating interpretation and image.")
else:
    st.warning("Please enter your OpenAI API key to use the app.")
