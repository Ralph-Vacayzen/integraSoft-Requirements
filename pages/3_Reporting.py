import streamlit as st
import pandas as pd

# from pydantic import BaseModel
# import streamlit_pydantic as sp


st.set_page_config(page_title='Reporting',page_icon='images/icon.png',layout='centered',initial_sidebar_state='expanded')

st.caption('REQUIREMENT')
st.header('Reporting')
st.info('Vacayzen requires a solution for reports on revenue and operational activity.')

st.subheader('Objectives')
st.write('- Daily Sales')
st.write('- Deferred Revenue')
st.write('- Itemized Receipts Per Transaction')

st.subheader('Scope')
st.write('Reporting should be day-by-day. Daily revenue and utilization by asset. Reports should be exportable from integraRental and not limited to a manual Microsoft Access export.')

st.subheader('Requirements')
r = pd.read_csv('data/reporting/requirements.csv').fillna('')
st.table(r)

st.divider()

st.subheader('Example Report - Stories')
st.caption('Non-functioning, visual example')

with st.expander('Specifications'):
    st.caption('Asset Category is **required**.')
    st.caption('Asset Master is optional.')
    st.caption('Range Start Date is **required**.')
    st.caption('Range End Date is **required**.')

with st.expander('Assumptions'):
    st.caption('If an Asset Master **is not** selected, it is assumed the information is requested for the entire Asset Category.')
    st.caption('If an Asset Master **is** selected, it is assumed the information is requested for the one Asset Master.')

with st.expander('Columns'):
    st.caption('Date')
    st.caption('That date\'s dynamic price (if Asset Master provided)')
    st.caption('That date\'s number of units sold.')
    st.caption('The date\'s revenue.')

left, right = st.columns(2)
category = left.selectbox('Asset Category',['Bike','Beach Gear','Baby','Golf Cart','Beach Service'])
asset = right.selectbox('Asset Master',['26" Bike Rental','24" Bike Rental','20" Bike Rental','16" Bike Rental','26" Bike with Baby Seat Rental'])
start = left.date_input('Range Start Date', value=pd.to_datetime('06/30/2024'))
end   = right.date_input('Range End Date', value=pd.to_datetime('07/07/2024'), min_value=start)

data = [
    ['June 30, 2024',10,90,900],
    ['July 01, 2024',11,100,1100],
    ['July 02, 2024',11,100,1100],
    ['July 03, 2024',12,120,1440],
    ['July 04, 2024',12,120,1440],
    ['July 05, 2024',11,100,1100],
    ['July 06, 2024',10,100,1000],
    ['July 07, 2024',10,90,900],
]

data = pd.DataFrame(data,columns=['Date','Dynamic Price ($)','Units (#)','Revenue ($)'])

st.dataframe(data, use_container_width=True)