import numpy as np
import pickle
import streamlit as st
with open('C:\\Users\\91636\\OneDrive\\Desktop\\cancerfolder\\lr.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
def cancer_prediction(input_data):
    prediction = loaded_model.predict(input_data)
    return prediction
def main():
    st.set_page_config(page_title='LUNG CANCER PREDICTION WEB APP', page_icon=":microscope:")
    st.title('Lung Cancer Prediction Web App')
    st.markdown(
        """<div style='background-color: #f0f0f0; padding: 10px; border-radius: 10px;'>
           <h3 style='color: #008080; text-align: center;'>Enter Patient Information</h3>
           </div>
        """, unsafe_allow_html=True)
    gender = st.text_input('Gender')
    airpollution = st.text_input('Air Pollution')
    alcohol = st.text_input('Alcohol usage')
    dustallergy = st.text_input('Dust Allergy')
    occupational_hazards = st.text_input('Occupational Hazards')
    geneticrisk = st.text_input('Genetic Risk')
    chronic_disease = st.text_input('Chronic Lung Disease')
    balanced_diet = st.text_input('Balanced Diet')
    obesity = st.text_input('Obesity')
    smoking = st.text_input('Smoking')
    passive_smoker = st.text_input('Passive Smoker')
    chest_pain = st.text_input('Chest Pain')
    coughing_blood = st.text_input('Coughing of Blood')
    weight_loss = st.text_input('Weight Loss')
    wheezing = st.text_input('Wheezing')
    swallowing_difficulty = st.text_input('Swallowing Difficulty')
    dry_cough = st.text_input('Dry Cough')
    diagnosis = ''
    if st.button('Cancer Test Result', key='prediction_button', help="Click to see the result"):
        input_data = np.array([[gender, airpollution, alcohol, dustallergy, occupational_hazards, geneticrisk, chronic_disease,
                                balanced_diet, obesity, smoking, passive_smoker, chest_pain, coughing_blood,
                                weight_loss, wheezing, swallowing_difficulty, dry_cough]])  
        prediction = cancer_prediction(input_data)
        if prediction[0] == 1:
            diagnosis = 'The person has cancer'
        else:
            diagnosis = 'The person does not have cancer'
    st.markdown(f"<h3 style='color: {'green' if 'does not' in diagnosis else 'red'};'>{diagnosis}</h3>", unsafe_allow_html=True)
if __name__ == '__main__':
    main()
