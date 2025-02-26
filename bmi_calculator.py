import streamlit as st

# Custom CSS for styling and animations
st.markdown(
    """
    <style>
    /* Light mode styles */
    .stApp {
        background-color: #f0f2f6 !important;
        color: #2c3e50 !important;  /* Dark blue-gray text */
        font-family: 'Arial', sans-serif;
        transition: all 0.5s ease;
    }
    /* Dark mode styles */
    .dark-mode {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
    }
    /* Text elements */
    h1, h2, h3, h4, h5, h6, p, label, div {
        color: inherit !important;  /* Inherit from parent */
    }
    /* Button styling */
    .stButton>button {
        background-color: #4CAF50 !important;
        color: white !important;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049 !important;
        transform: scale(1.05);
    }
    /* Results styling */
    .stSuccess { color: #28a745 !important; }
    .stWarning { color: #ffc107 !important; }
    .stError { color: #dc3545 !important; }
    .stInfo { color: #17a2b8 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Dark/Light Mode Toggle
dark_mode = st.checkbox("Dark Mode")

# Apply dark mode if selected
if dark_mode:
    st.markdown(
        '<style>.stApp {background-color: #1e1e1e !important; color: #ffffff !important;}</style>',
        unsafe_allow_html=True,
    )

# Title and inputs
st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) easily!")

height = st.number_input("Enter your height (in meters):", min_value=0.1, format="%.2f")
weight = st.number_input("Enter your weight (in kilograms):", min_value=1.0, format="%.2f")

# BMI calculation
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("You're underweight. ☆")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight. 😊😊")
        elif 25 <= bmi < 29.9:
            st.info("You're overweight. ❤️❤️")
        else:
            st.error("You're obese. Consult a health expert.")
    else:
        st.error("Please provide valid height and weight.")