import streamlit as st
import pandas as pd

st.set_page_config(page_title='Vacayzen Requirements',page_icon='images/icon.png',layout='centered',initial_sidebar_state='expanded')

st.caption('VACAYZEN')
st.header('integraSoft Requirements')
st.info('Communication of Vacayzen\'s integraRental & VacaDo requirements.')

st.subheader('Project objectives')
left, right = st.columns(2)
left.write('- Improve reporting')
left.write('- Improve available inventory awareness')
left.write('- Improve asset demand awareness')
right.write('- Introduce inventory management via scan')
right.write('- Introduce inventory geo-tracking')
right.write('- Introduce date-based, dynamic pricing')
right.write('- Introduce by-day pricing & reporting')


st.subheader('Project scope')
st.caption('Dynamic Pricing')
st.write('Pricing should be adjustable by date range. During a period of slowness, there should be an adjustable percentage of automatic discount. During a period of demand, there should be an adjustable percentage of automatic increase. During a period of normality, pricing should be unadjusted. Pricing and reporting should reflect the adjustments. Periods should be user defineable and adjustable.')
st.caption('Reporting')
st.write('Reporting should be all-encompassing and simplistic. Reports should be exportable, and common-use data should be illustrated in dashboards.')
st.caption('Serialized Inventory')
st.write('All inventory should be serialized and tracked, during each stage of the ordering process. Inventory should be location-based. Some locations should be able to share inventory. Movement of inventory between locations should be supported.')

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