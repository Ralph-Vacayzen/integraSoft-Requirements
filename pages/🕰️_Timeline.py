import streamlit as st
import streamlit_timeline as timeline

# use full page width
st.set_page_config(page_title="Technology Timeline", layout="wide")

# load data
with open('data/timeline.json', "r") as f:
    data = f.read()

# render timeline
timeline.timeline(data, height=800)