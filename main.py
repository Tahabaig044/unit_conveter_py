import streamlit as st

# Conversion dictionaries
length_units = {'Meter': 1, 'Kilometer': 0.001, 'Mile': 0.000621371, 'Yard': 1.09361, 'Foot': 3.28084}
weight_units = {'Kilogram': 1, 'Gram': 1000, 'Pound': 2.20462, 'Ounce': 35.274}
time_units = {'Second': 1, 'Minute': 1/60, 'Hour': 1/3600, 'Day': 1/86400}

def convert_units(value, from_unit, to_unit, conversion_dict):
    return value * (conversion_dict[to_unit] / conversion_dict[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        return (value * 9/5 + 32) if to_unit == 'Fahrenheit' else (value + 273.15)
    if from_unit == 'Fahrenheit':
        return ((value - 32) * 5/9) if to_unit == 'Celsius' else ((value - 32) * 5/9 + 273.15)
    if from_unit == 'Kelvin':
        return (value - 273.15) if to_unit == 'Celsius' else ((value - 273.15) * 9/5 + 32)

st.title("🌍 Advanced Unit Converter")
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature", "Time"])

if category == "Length":
    from_unit = st.selectbox("From", list(length_units.keys()))
    to_unit = st.selectbox("To", list(length_units.keys()))
    value = st.number_input("Enter Value", min_value=0.0, format="%.5f")
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, length_units)
        st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", list(weight_units.keys()))
    to_unit = st.selectbox("To", list(weight_units.keys()))
    value = st.number_input("Enter Value", min_value=0.0, format="%.5f")
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, weight_units)
        st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter Value", format="%.2f")
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Time":
    from_unit = st.selectbox("From", list(time_units.keys()))
    to_unit = st.selectbox("To", list(time_units.keys()))
    value = st.number_input("Enter Value", min_value=0.0, format="%.5f")
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, time_units)
        st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")
