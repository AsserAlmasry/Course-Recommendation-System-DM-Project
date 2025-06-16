
import os
import pickle
import streamlit as st
import pandas as pd

# Load pre-trained data
courses_list = pd.DataFrame(pickle.load(open('course_list.pkl', 'rb')))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend courses
def recommend(course):
    try:
        index = courses_list[courses_list['course_name'] == course].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_course_names = [courses_list.iloc[i[0]].course_name for i in distances[1:7]]
        return recommended_course_names
    except IndexError:
        return ["Course not found in the dataset. Please try another."]

# <==== Streamlit UI ====>
st.set_page_config(page_title="Course Recommendation System", layout="wide", page_icon="🎓")

# Page title and subtitle
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #2c3e50;">Coursera Course Recommendation System</h1>
        <h4 style="color: #7f8c8d;">Find courses similar to your favorite from a dataset of over 3,000 Coursera courses.</h4>
    </div>
    """, 
    unsafe_allow_html=True
)

# Dropdown for selecting a course
st.markdown("<h3 style='color: #3498db;'>Select a Course You Like:</h3>", unsafe_allow_html=True)
course_list = courses_list['course_name'].values
selected_course = st.selectbox("", course_list)

# Recommendation button and results display
if st.button('Show Recommended Courses'):
    st.markdown("<h3 style='color: #e74c3c;'>Recommended Courses for You:</h3>", unsafe_allow_html=True)
    recommended_courses = recommend(selected_course)
    
    if len(recommended_courses) > 0 and "Course not found" not in recommended_courses[0]:
        for idx, course in enumerate(recommended_courses):
            st.markdown(f"**{idx + 1}. {course}**")
    else:
        st.markdown(f"<p style='color: red;'>{recommended_courses[0]}</p>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <p style="color: #bdc3c7;">Copyright &copy; Coursera and respective course owners.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

