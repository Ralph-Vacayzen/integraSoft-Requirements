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
left.write('- Track movement of larger assets live via gps')
left.write('- Track maintenance on assets')
right.write('- Report on asset history')
right.write('- Associate actual assets to orders')
right.write('- Charge for lost items')
right.write('- Determine lifespan of asset')


st.subheader('Scope')
st.write('All inventory should be serialized and tracked, during each stage of the order process. The current location of each asset should be known, in addition to all past locations. The lifespan of each asset should also be maintained. If assets are lost, there should be means to relocate or charge the appicable customer for lost goods.')

st.subheader('Requirements')
r = pd.read_csv('data/serialized_assets/requirements.csv', index_col='Requirement').fillna('')
st.table(r)
st.download_button('Download Requirements',pd.read_csv('data/serialized_assets/requirements.csv',index_col=False).to_csv(index=False),'requirements.csv',use_container_width=True)

st.divider()

st.subheader('Example Workflow')

left, right = st.columns(2)
st.write()
left.image('data/serialized_assets/images/IMG_6036.PNG')