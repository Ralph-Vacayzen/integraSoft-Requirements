import streamlit as st
import pandas as pd

st.set_page_config(page_title='Vacayzen Tech Requirements',page_icon='images/icon.png',layout='centered',initial_sidebar_state='expanded')

st.caption('VACAYZEN')
st.header('TECHNOLOGY REQUIREMENTS')
st.info('Vacayzen requires a solution for their business model. Vacayzen is a company that offers: rental services, one-day experiences, seasonal programs, annual programs, credit programs, and partner websites. Vacayzen needs one system that coordinates their: websites, customers, orders, work orders, programs, assets, service items, logistics, marketing lists, reporting, and billing in one place.')

st.subheader('Project objectives')
left, right = st.columns(2)
left.write('- Improve website experience & conversions')
left.write('- Improve moblie booking process')
left.write('- Improve reporting')
left.write('- Improve website upkeep')
left.write('- Improve geofence restrictions')
left.write('- Improve available inventory awareness')
left.write('- Improve asset demand awareness')
left.write('- Improve business-line operations')
right.write('- Introduce inventory management via barcode')
right.write('- Introduce inventory geo-tracking')
right.write('- Introduce demand-based, dynamic pricing')
right.write('- Introduce by-day data dashboards')
right.write('- Introduce billing solution')
right.write('- Introduce multiple location support')
right.write('- Introduce customer leads solution')
right.write('- Introduce staff analytics')

st.subheader('Project scope')
st.write('Vacayzen desires to fulfill all of their existing services, but within a one-stop-shop solution catered to their use cases, and improving the operations pertaining to each of the services.')
st.caption('Websites')
st.write('The websites should be seamless from front-end to back-end. Pricing should be dynamic. The mobile booking process should be enticing and simple. Adjusting text or images on websites should happen one time, and reflect on each of the applicable websites.')
st.caption('Reporting')
st.write('Reporting should be all-encompassing and simplistic. Reports should be exportable, and common-use data should be illustrated in dashboards.')
st.caption('Customers')
st.write('Customers should be able to opt-out of marketing material (opt-in by default). There should be a way to prompt users with notices on applicable websites. Customers should be able to track the status of their orders. Customers should be able to adjust or cancel their orders without the need to speak to a representative--inventory permitting.')
st.caption('Inventory')
st.write('All inventory should be serialized and tracked, during each stage of the ordering process. Inventory should be location-based. Some locations should be able to share inventory. Movement of inventory between locations should be supported.')
st.write('...')

st.subheader('Business requirements')
br = pd.read_csv('data/summary/requirements.csv').fillna('')
st.table(br)


st.subheader('Key stakeholders')
ks = pd.read_csv('data/summary/stakeholders.csv').fillna('')
st.table(ks)


st.subheader('Project constraints')
pc = pd.read_csv('data/summary/constraints.csv').fillna('')
st.table(pc)


st.subheader('Cost-benefit analysis')
cb = pd.read_csv('data/summary/cost-benefit.csv').fillna('')
st.table(cb)