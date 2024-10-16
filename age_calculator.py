import streamlit as st
from datetime import datetime

# Set the page configuration
st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .title {
        color: #4B0082;
        font-size: 50px;
        text-align: center;
    }
    .subtitle {
        color: #6A5ACD;
        font-size: 25px;
        text-align: center;
    }
    .result {
        color: #2E8B57;
        font-size: 30px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<p class="title">🎉 Age Calculator 🎉</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Find out your age in years, hours, and minutes!</p>', unsafe_allow_html=True)

# Date of Birth Input
dob = st.date_input(
    "Select your Date of Birth:",
    datetime(2000, 1, 1),
    min_value=datetime(1900, 1, 1),
    max_value=datetime.now()
)

# Button to calculate age
if st.button("Calculate Age"):
    # Current datetime
    now = datetime.now()
    
    # User's datetime of birth at midnight
    dob_datetime = datetime.combine(dob, datetime.min.time())
    
    # Calculate time difference
    delta = now - dob_datetime
    
    # Calculate age in years
    try:
        birthday_this_year = dob_datetime.replace(year=now.year)
    except ValueError:
        # Handle February 29th for non-leap years
        birthday_this_year = dob_datetime.replace(year=now.year, month=dob.month+1, day=1)
    
    if birthday_this_year > now:
        age_years = now.year - dob_datetime.year - 1
    else:
        age_years = now.year - dob_datetime.year
    
    # Total minutes and hours
    total_minutes = int(delta.total_seconds() // 60)
    total_hours = int(delta.total_seconds() // 3600)
    
    # Display the results
    st.markdown(f'<p class="result">You are {age_years} years old.</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="result">That is approximately {total_hours:,} hours.</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="result">Or around {total_minutes:,} minutes.</p>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:gray;">
    Made with ❤️ using Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
