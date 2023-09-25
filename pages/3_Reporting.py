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

st.subheader('Example - Stories')
st.caption('Non-functioning, visual example')
left, right = st.columns(2)
start = left.date_input('Start of Range')
end   = right.date_input('End of Range', value=start+pd.Timedelta(days=1))

data = [
    ['Bikes',17500,18230],
    ['Beach',12100,13000],
    ['Baby',5000,4750],
    ['Bonfire',6000,7200],
    ['LSV',15000,20000]
]

data = pd.DataFrame(data,columns=['Quickbooks Relationship','Day 1 of Range','Day 2 of Range'])

st.dataframe(data, use_container_width=True)


st.subheader('Example - Deferred Revenue')
st.caption('Non-functioning, visual example')

data = [
    ['26" Bike','Bikes',1000,560],
    ['24" Bike','Bikes',820,700],
    ['Classic Beach Service','Beach',2000,850],
    ['Full-size Crib','Baby',300,530],
    ['Car Seat','Baby',120,200],
    ['Deluxe Bonfire','Bonfire',2950,2220],
    ['4-Seat Golf Cart','LSV',4270,2725],
    ['6-Seat Golf Cart','LSV',3390,5230],
]

data = pd.DataFrame(data,columns=['Asset','Quickbooks Relationship','Revenue Recognized Date 1','Revenue Recognized Date 2'])

st.dataframe(data, use_container_width=True)


st.subheader('Example - Transaction Receipt')
st.caption('Non-functioning, visual example')

st.metric('Transaction','$205.98')

data = [
    ['26" Bike','Bikes',175],
    ['Damage Waiver','Fee',8.75],
    ['Flexible Cancellation','Fee',8.75],
    ['Sales Tax','Tax',13.48],
]

data = pd.DataFrame(data,columns=['Description','Quickbooks Relationship','Amount'])

st.dataframe(data, use_container_width=True)