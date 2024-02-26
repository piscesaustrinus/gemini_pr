import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate blog content using Gen AI
def generate_blog_content(input_text, no_words, blog_style):
    template = """  
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """
    prompt = template.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
    model_name = "gemini-pro"  # Adjust model name if necessary
    model = genai.GenerativeModel(model_name)
    initial_content = "In this blog, we will discuss..."
    content = model.generate_content(contents=[initial_content, prompt])
    return content.text

# Initialize Streamlit app
st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

## creating two more columns for additional two fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')

with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

## Final response
if submit:
    st.write(generate_blog_content(input_text, no_words, blog_style))
