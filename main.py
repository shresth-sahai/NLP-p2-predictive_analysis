# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib

# Load your model
model = joblib.load('model.pkl')

# Define the Streamlit app

def main():
    st.title("Predictive Maintainence")

    # Define the input fields
    
    Type = st.selectbox('Type', [0, 1, 2])
    Air_temp = st.number_input('Air temperature [K]', min_value=0.0, step=0.1)
    Process_temp = st.number_input('Process temperature [K]', min_value=0.0, step=0.1)
    Rotational_speed = st.number_input('Rotational speed [rpm]', min_value=0.0, step=0.1)
    Torque = st.number_input('Torque [Nm]', min_value=0.0, step=0.1)
    Tool_wear = st.number_input('Tool wear [min]', min_value=0.0, step=0.1)
    nf = st.number_input('nf', min_value=0.0, step=0.1)

    # Create a button to make predictions
    if st.button('Predict'):
        
        # Create a DataFrame for the input
        input_data = pd.DataFrame({
            'Type': [Type],
            'Air temperature [K]': [Air_temp],
            'Process temperature [K]': [Process_temp],
            'Rotational speed [rpm]': [Rotational_speed],
            'Torque [Nm]': [Torque],
            'Tool wear [min]': [Tool_wear],
            'nf': [nf]
        })

        # Convert categorical data to dummy/indicator variables if needed
        # input_data = pd.get_dummies(input_data)

        # Make predictions
        prediction = model.predict(input_data)

        # Display the prediction

        if prediction[0]==0:
            
            st.write('The component is safe for now')

        elif prediction[0]==1:

            st.write('The component is at RISK')

            

# Run the app
if __name__ == '__main__':
    main()
