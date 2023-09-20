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

st.subheader('Examples of Adjustments')
st.write('')

st.write('**RELEASE TO LOAD**')
with st.container():
    left, right = st.columns(2)
    left.write('When a route has been set to a status of Release to Load, there should be an option to "Load Selected Route," similar to "Download Selected Route," found on the Sync Data > Download Route screen. "Download Selected Route" should be grayed out.')
    left.write('')
    left.write('"Load Selected Route" should utilize the data that produces the load sheets, to determine what assets should be scanned on to the truck.')
    left.write('')
    left.write('There should be a means to communicate a conflict. If there is not an asset that is needed for the route, the associated order\'s dispatch activities should be removed from the route and placed back onto RAB. A loading conflict should be recorded.')
    left.write('')
    left.write('Load conflicts can be reviewed in integraRental at: Disptach > Route > {Route} > Load Conflicts. There should be a count of load conflicts on the table of routes, located in integraRental at: Dispatch > Route.')
    left.write('')
    left.write('There should be a means to complete a "Load Selected Route" event. Once a "Load Selected Route" event has been successfully completed, the route status should be change to "Release to Begin." "Download Selected Route" should no longer be grayed out.')
    right.image('data/serialized_assets/images/IMG_6038.PNG')


st.write('')
st.write('')
st.write('**ABANDONED ITEMS**')
with st.container():
    left, right = st.columns(2)
    left.write('Often a driver comes across an asset that has been abandoned. The "Load Sheet" button, found on the "Dispatch Activity" screen in VacaDo, should be replaced with "Abandoned Item."')
    left.write('')
    left.write('A driver sees an abandoned asset. They click "Abandoned Asset." They scan the asset. They indicate if they picked up the asset or not. If not, the scan also captures the latitude and longitude. The results are added to a log at the end of a sync or full sync with: asset, applicable order, picked-up-or-not, latitude, longitude.')
    left.write('')
    left.write('The abandoned log can be viewed via Dispatch > Route > {Route} > Abandoned Items. There should be a count of abandoned items on the table of routes, located in integraRental at: Dispatch > Route.')
    left.write('')
    left.write('A route reviewer would be responsible for situating the abandoned items log, and scheduling any followup actions required.')

    right.image('data/serialized_assets/images/IMG_6040.PNG')


st.write('')
st.write('')
st.write('**DELIVERY**')
with st.container():
    left, right = st.columns(2)

    right.image('data/serialized_assets/images/IMG_6043.PNG')


st.write('')
st.write('')
st.write('**PICKUP**')
with st.container():
    left, right = st.columns(2)

    right.image('data/serialized_assets/images/IMG_6049.PNG')


st.write('')
st.write('')
st.write('**SERVICE ITEM**')
with st.container():
    left, right = st.columns(2)

    right.image('data/serialized_assets/images/IMG_6041.PNG')