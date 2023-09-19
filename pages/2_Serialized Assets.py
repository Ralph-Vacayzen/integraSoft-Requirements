import streamlit as st
import pandas as pd

# from pydantic import BaseModel
# import streamlit_pydantic as sp


st.set_page_config(page_title='Serialized Assets',page_icon='images/icon.png',layout='centered',initial_sidebar_state='expanded')

st.caption('REQUIREMENT')
st.header('Serialized Assets')
st.info('Vacayzen requires a solution for serialized inventory with tracking capabilities.')

st.subheader('Objectives')
left, right = st.columns(2)
left.write('- Serialize all assets via barcode')
left.write('- Track movement of assets via last scan')
left.write('- Track movement of assets live via gps')
left.write('- Track maintenance on assets')
left.write('- Report on asset history')
right.write('- Associate actual assets to orders')
right.write('- Charge for lost items')
right.write('- Attribute quality of asset')
right.write('- Determine lifespan of asset')
right.write('- Introduce storage areas')


st.subheader('Scope')
st.write('Vacayzen should be able to track inventory movement and lifespan to facilitate decision making and reimbursement for lost items.')

st.subheader('Requirements')
r = pd.read_csv('data/serialized_assets/requirements.csv', index_col='Requirement').fillna('')
st.table(r)
st.download_button('Download Requirements',pd.read_csv('data/serialized_assets/requirements.csv',index_col=False).to_csv(index=False),'requirements.csv',use_container_width=True)

st.divider()

st.subheader('Example')
