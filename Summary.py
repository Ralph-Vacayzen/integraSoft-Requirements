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


st.subheader('Project scope - Epic Level')
st.caption('Dynamic Pricing')
st.write('Pricing should be adjustable by date range. During a period of slowness, there should be an adjustable percentage of automatic discount. During a period of demand, there should be an adjustable percentage of automatic increase. During a period of normality, pricing should be unadjusted. Pricing and reporting should reflect the adjustments. Periods should be user defineable and adjustable.')
st.caption('Reporting')
st.write('Reporting should be day-by-day. Daily revenue and utilization by asset. Reports should be exportable from integraRental and not limited to a manual Microsoft Access export.')
st.caption('Serialized Inventory')
st.write('All inventory should be serialized and tracked, during each stage of the order process. The current location of each asset should be known, in addition to all past locations. The lifespan of each asset should also be maintained. If assets are lost, there should be means to relocate or charge the appicable customer for lost goods.')

st.subheader('Business requirements - Epic Level')
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