import streamlit as st
from transformers import pipeline

# Use the T5 model for summarization
summarizer = pipeline("summarization", model="t5-small", framework="pt")

# Streamlit app
st.title('Article Summarizer')


st.write('Paste the article text below and click on the "Summarize" button.')

# Text area for user input
article_text = st.text_area('Article Text', height=300)

# Button to trigger summarization
if st.button('Summarize'):
    if article_text:
        with st.spinner('Summarizing...'):
            # Summarize the text
            summary = summarizer(article_text[:1024], max_length=150, min_length=50, do_sample=False)
            # Display the summary
            st.subheader('Summary')
            st.write(summary[0]['summary_text'])
    else:
        st.error('Please paste the article text above.')
