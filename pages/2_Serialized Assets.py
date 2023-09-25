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

st.subheader('Examples of Adjustments - Stories')
st.write('')

st.write('**RELEASE TO LOAD**')
with st.container():
    left, right = st.columns(2)
    left.write('When a route has been set to a status of Release to Load, there should be an option to "Load Selected Route," similar to "Download Selected Route," found on the Sync Data > Download Route screen. "Download Selected Route" should be grayed out and not tappable, or not present.')
    left.write('')
    left.write('"Load Selected Route" should utilize the data that produces the load sheets, to determine what assets should be scanned on to the truck.')
    left.write('')
    left.write('There should be a means to communicate a conflict. If there is not an asset that is needed for the route, the associated order\'s dispatch activities should be removed from the route and placed back onto the Route Assignment Board. A loading conflict should be recorded.')
    left.write('')
    left.write('Load conflicts can be reviewed in integraRental at: Disptach > Route > {Route} > Load Conflicts. There should be a count of load conflicts on the table of routes, located in integraRental at: Dispatch > Route.')
    left.write('')
    left.write('There should be a means to complete a "Load Selected Route" event. Once a "Load Selected Route" event has been successfully completed, the route status should be change to "Load Complete."')
    left.write('')
    left.write('"Download Selected Route" should be grayed out and not tappable, or not present, for route statuses: "Release to Load" and "Load Complete".')
    left.write('')
    left.write('"Download Selected Route" should be tappable, when the route status is set to "Release to Begin."')
    right.image('data/serialized_assets/images/IMG_6038.PNG')

st.divider()

st.write('**ABANDONED ITEMS**')
with st.container():
    left, right = st.columns(2)
    left.write('Often a driver comes across an asset that has been abandoned. The "Load Sheet" button, found on the "Dispatch Activity" screen in VacaDo, should be replaced with "Abandoned Item."')
    left.write('')
    left.write('A driver sees an abandoned asset. They click "Abandoned Asset." They scan the asset. They indicate if they picked up the asset or not. If not, the scan also captures the latitude and longitude. The results are added to a log at the end of a sync or full sync with: asset, applicable order, picked-up-or-not, latitude, longitude.')
    left.write('')
    left.write('The abandoned log can be viewed via Dispatch > Route > {Route} > Abandoned Items. There should be a count of abandoned items on the table of routes, for the applicable route, located in integraRental at: Dispatch > Route.')
    left.write('')
    left.write('A route reviewer would be responsible for situating the abandoned items log, and scheduling any followup actions required.')

    right.image('data/serialized_assets/images/IMG_6040.PNG')

st.divider()

st.write('**DELIVERY**')
with st.container():
    left, right = st.columns(2)
    left.write('Before a DELIVERY dispatch can be completed, the assets being delivered need to be scanned.')
    left.write('')
    left.write('"Complete Dispatch", located in a dispatch activity\'s Dispatch Details, will happen after asset scanning.')
    left.write('')
    left.write('On the "Dispatch Details" screen for a DELIVERY stop in VacaDo, the "Complete Dispatch" button will be replaced with "Scan Assets."')
    left.write('')
    left.write('The resulting, new screen will prompt for scans of the assets that are to be delivered.')
    left.write('')
    left.write('Any scan conflicts, where an asset is needed for a delivery but is not present for scan, would be sent back to the Route Assignment Board in integraRental. If the missing item is part of a bundle, the bundle will be partitioned on the associated rental agreement. Any scan conflict will be placed back on the Route Assignment Board.')
    left.write('')
    left.write('*For example, if a DELIVERY was for (4) 26" Bike Rentals, and three of the four were scanned, the rental agreement would have a rental agreement line for (3) 26" Bike Rentals that are delivered and (1) 26" Bike Rental that still needs to be delivered and is sitting on the Route Assignment Board to be scheduled on a route.*')
    left.write('')
    left.write('After scanning, there should be a "Complete Dispatch" button, like there is today, and the flow should continue as it does today.')

    right.image('data/serialized_assets/images/IMG_6043.PNG')


st.divider()

st.write('**PICKUP**')
with st.container():
    left, right = st.columns(2)
    left.write('Before a PICKUP dispatch can be completed, the assets being delivered need to be scanned.')
    left.write('')
    left.write('"Complete Dispatch", located in a dispatch activity\'s Dispatch Details, will happen after asset scanning.')
    left.write('')
    left.write('On the "Dispatch Details" screen for a PICKUP stop in VacaDo, the "Complete Dispatch" button will be replaced with "Scan Assets."')
    left.write('')
    left.write('The resulting, new screen will prompt for scans of the assets that are to be picked up.')
    left.write('')
    left.write('Any scan conflicts, where an asset is supposed to be picked up but is not present for scan, would be sent back to the Route Assignment Board in integraRental. If the missing item is part of a bundle, the bundle will be partitioned on the associated rental agreement. Any scan conflict will be placed back on the Route Assignment Board.')
    left.write('')
    left.write('In the event that a scan takes places for an asset that should not be present, there should be a pickup conflict recorded. The results are added to a log at the end of a sync or full sync with: asset, applicable order, latitude, longitude. The misplaced asset log can be viewed via Dispatch > Route > {Route} > Misplaced Items. There should be a count of misplaced items on the table of routes, for the applicable route, located in integraRental at: Dispatch > Route.')
    left.write('')
    left.write('*For example, if a PICKUP was for (4) 26" Bike Rentals, and three of the four were scanned, the rental agreement would have a rental agreement line for (3) 26" Bike Rentals that are picked up and (1) 26" Bike Rental that still needs to be picked up and is sitting on the Route Assignment Board to be scheduled on route.*')
    left.write('')
    left.write('After scanning, there should be a "Complete Dispatch" button, like there is today, and the flow should continue as it does today.')

    right.image('data/serialized_assets/images/IMG_6049.PNG')

st.divider()

st.write('**SERVICE ITEM**')
with st.container():
    left, right = st.columns(2)
    left.write('When a service item dispatch activity occurs, today we do not prompt the driver for what physical resources were used nor how long they took on the activity.')
    left.write('')
    left.write('"Complete Dispatch", located in a dispatch activity\'s Dispatch Details, will happen after that information is prompted for.')
    left.write('')
    left.write('On the "Dispatch Details" screen for a service item stop in VacaDo, the "Complete Dispatch" button will be replaced with "Service Details."')
    left.write('')
    left.write('The resulting, new screen will prompt for parts used and how many and how long the activity took, and the parts and work should be tied to the individual asset. It will also prompt for a potential swapping or replacement of assets. If a swap did take place, scan-in the old asset and scan-out the new asset. If a replacement did take place, scan-out the new asset, and prompt for indication of the asset that is not present.')
    left.write('')
    left.write('In the event that a scan takes places for an asset that should not be present, there should be a pickup conflict recorded. The results are added to a log at the end of a sync or full sync with: asset, applicable order, latitude, longitude. The misplaced asset log can be viewed via Dispatch > Route > {Route} > Misplaced Items. There should be a count of misplaced items on the table of routes, for the applicable route, located in integraRental at: Dispatch > Route.')
    left.write('')
    left.write('After service details have been provided, there should be a "Complete Dispatch" button, like there is today, and the flow should continue as it does today.')
    left.write('')
    left.write('Any service details should be created into a service ticket in integraRental, at the time of sync of full sync. The service ticket should be connect to an asset, reference the applicable rental agreement, and be connected to the applicable customer.')
    left.write('')
    left.write('Service tickets should be due for payment or not (on a record keeping basis). For example, we bill some partners for parts and some others we do not, but we would still like to know how many of each part and when and how long.')

    right.image('data/serialized_assets/images/IMG_6041.PNG')