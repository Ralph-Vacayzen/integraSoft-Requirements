import streamlit as st
import pandas as pd

# from pydantic import BaseModel
# import streamlit_pydantic as sp


st.set_page_config(page_title='Requirement - Template',page_icon='images/icon.png',layout='centered',initial_sidebar_state='expanded')

st.caption('REQUIREMENT')
st.header('THIS IS A TEMPLATE')
st.info('Vacayzen requires a solution for ...')

st.subheader('Objectives')
st.write('- objective one')
st.write('- objective two')

st.subheader('Scope')
st.write('Vacayzen should be able to...')

st.subheader('Requirements')
r = pd.read_csv('data/dynamic_pricing/requirements.csv').fillna('')
st.table(r)

st.divider()

st.subheader('Example')
