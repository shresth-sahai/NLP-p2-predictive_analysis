# Import necessary libraries
import gradio as gr
import pandas as pd
import joblib




# Load your model
model = joblib.load('model.pkl')

# Define the prediction function
def predict(Type, Air_temp, Process_temp, Rotational_speed, Torque, Tool_wear, nf):
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

    # Convert categorical data to dummy/indicator variables
    input_data = pd.get_dummies(input_data, columns=['Type'], drop_first=True)

    # Ensure all expected columns are present
    missing_cols = set(model.feature_names_in_) - set(input_data.columns)
    for col in missing_cols:
        input_data[col] = 0

    # Make predictions
    prediction = model.predict(input_data)

    return prediction[0]

# Define the Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(['Type1', 'Type2', 'Type3'], label='Type'),
        gr.Number(label='Air temperature [K]'),
        gr.Number(label='Process temperature [K]'),
        gr.Number(label='Rotational speed [rpm]'),
        gr.Number(label='Torque [Nm]'),
        gr.Number(label='Tool wear [min]'),
        gr.Number(label='nf')
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Model Deployment with Gradio",
    description="Enter the parameters to get a prediction"
)

# Launch the Gradio interface
interface.launch()
