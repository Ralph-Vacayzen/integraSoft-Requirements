import streamlit as st
import pandas as pd

# from pydantic import BaseModel
# import streamlit_pydantic as sp


st.set_page_config(page_title='Requirement - Locations',page_icon='images/icon.png',layout='centered',initial_sidebar_state='expanded')

st.caption('REQUIREMENT')
st.header('LOCATIONS')
st.info('Vacayzen requires a solution for multiple locations.')

st.subheader('Objectives')
st.write('- Separation of inventory')
st.write('- Sharing of inventory')
st.write('- Location-based pricing')
st.write('- Location-based service handling')

st.subheader('Scope')
st.write('Vacayzen should be able to have location-based: inventory, pricing, and service handling.')

st.subheader('Requirements')
r = pd.read_csv('data/locations/requirements.csv').fillna('')
st.table(r)

st.divider()

st.subheader('Example')
