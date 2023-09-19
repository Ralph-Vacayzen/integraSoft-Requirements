import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Requirement - Dynamic Pricing',page_icon='images/icon.png',layout='centered',initial_sidebar_state='expanded')

st.caption('REQUIREMENT')
st.header('DYNAMIC PRICING')
st.info('Vacayzen requires a solution for demand-based pricing.')

st.subheader('Objectives')
st.write('- [REQUIRED] Adjust asset pricing on a per-day basis, with percentage adjustment')
st.write('- [REQUIRED] Incentivize off-season sales')
st.write('- [REQUIRED] Capitalize on peak-season trends')
st.write('- [OPTIONAL] Capitalize on demand')

st.subheader('Scope')
st.write('Similar to hotels or flights, pricing should adjust based on time-of-year need and availability.')

st.subheader('Requirements')
r = pd.read_csv('data/dynamic_pricing/requirements.csv').fillna('')
st.table(r)

st.divider()

st.header('Example')

categories = ['Bike','Beach Gear','Beach Service','Baby','Bonfire','Golf Cart']

st.subheader('Asset Price Settings')
with st.expander('Assumptions'):
    st.caption('Assume at least one asset category exists.')
    st.caption('Assume at least one asset exists per category.')
    st.caption('Assume an asset has one daily rate.')
    st.caption('What follows in an example of one asset in one category.')

left, middle, right = st.columns(3)
category         = left.selectbox('Category', categories, 0)
daily_rate       = middle.number_input('Daily Rate',min_value=0, step=1, value=10)
minimum_duration = right.number_input('Minimum Duration', min_value=0, step=1, value=3)

st.divider()

st.subheader('Dynamic Price Settings')
with st.expander('Assumptions'):
    st.caption('There can be any number of dynamic ranges.')
    st.caption('Dynamic ranges cannot overlap, where they share an applicable category.')
    st.caption('Dynamic ranges can adjust by a positive or negative percentage.')
    st.caption('If there is not a dynamic range on a date, use the base asset daily rate.')


left, middle, right = st.columns(3)
dynamic_start_date  = left.date_input('Range Start Date',value=pd.to_datetime('06/29/2024'))
dynamic_end_date    = middle.date_input('Range End Date',value=pd.to_datetime('07/04/2024'))
dynamic_percentage  = right.number_input('Percent Adjustment',step=1,value=10)
dynamic_categories  = st.multiselect('Applicable Categories',categories)

dynamic_range       = pd.date_range(dynamic_start_date,dynamic_end_date)

st.divider()

st.subheader('Order Example')
left, middle, right = st.columns(3)
start_date    = left.date_input('Start Date')
end_date      = middle.date_input('End Date', min_value=start_date, value=start_date+pd.Timedelta(days=2))
quantity      = right.number_input('Quantity',step=1,min_value=0,value=1)
damage        = middle.toggle('Damage Waiver')
cancellation  = right.toggle('Flexible Cancellation')

range      = pd.date_range(start_date, end_date)

st.divider()

st.subheader('Calculation Table for Order Example')
if (len(range) < minimum_duration):
    st.error('Minimum duration of ' + str(minimum_duration) + ' days not met. Currently at ' + str(len(range)) + ' days selected.')
else:
    result = pd.DataFrame(range, columns=['Dates'])

    def IsInDynamicCategories(row):
        return category in dynamic_categories

    result['inDynamicCategories'] = result.apply(IsInDynamicCategories, axis=1)

    def IsInDynamicRange(row):
        return row.Dates in dynamic_range

    result['inDynamicRange'] = result.apply(IsInDynamicRange, axis=1)

    def CalculateCost(row):
        value = daily_rate
        if (row.inDynamicCategories & row.inDynamicRange): value = daily_rate * (1 + dynamic_percentage / 100)
        return value
    
    result['DailyCost'] = result.apply(CalculateCost, axis=1)

    st.dataframe(result, use_container_width=True)
    
    subtotal           = np.sum(result.DailyCost) * quantity
    damage_price       = 0
    cancellation_price = 0
    tax                = 0

    if damage:       damage_price = subtotal * 0.06
    if cancellation: cancellation_price = subtotal * 0.05

    tax = (subtotal + damage_price + cancellation_price) * 0.07
    
    one, two, three, four, five = st.columns(5)
    one.metric('Dynamic Subtotal', round(subtotal,2))
    two.metric('Damage Waiver', round(damage_price,2))
    three.metric('Flexible Cancellation', round(cancellation_price,2))
    four.metric('Tax', round(tax,2))
    five.metric('Total', round(subtotal + damage_price + cancellation_price + tax,2))

st.divider()

st.subheader('Psuedo Code for Calculation Table')
code = """
categories          = ['Bike','Beach Gear','Beach Service','Baby','Bonfire','Golf Cart']
dynamic_categories  = multiselect('Applicable Categories',categories)
category            = selectbox('Category', categories)
daily_rate          = number_input('Daily Rate')
dynamic_percentage  = number_input('Percent Adjustment')
range               = pd.date_range(start_date, end_date)
result              = pd.DataFrame(range, columns=['Dates'])

def IsInDynamicCategories(row):
    return category in dynamic_categories

result['inDynamicCategories'] = result.apply(IsInDynamicCategories, axis=1)

def IsInDynamicRange(row):
    return row.Dates in dynamic_range

result['inDynamicRange'] = result.apply(IsInDynamicRange, axis=1)

def CalculateCost(row):
    value = daily_rate

    if (row.inDynamicCategories & row.inDynamicRange):
        value = daily_rate * (1 + dynamic_percentage / 100)

    return value
    
result['DailyCost'] = result.apply(CalculateCost, axis=1)
"""
st.code(code)