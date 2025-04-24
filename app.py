
import gradio as gr
from utils import mask_pii, unmask_pii
from models import predict_category
def classify(email):
    # Perform masking and classification
    masked_email, entities = mask_pii(email)
    category = predict_category(masked_email)
    demasked = unmask_pii(masked_email, entities)

    # Ensure the return is a tuple with 4 values
    return masked_email, str(entities), category, demasked


iface = gr.Interface(
    fn=classify,
    inputs=gr.Textbox(lines=10, label="Enter Support Email"),
    outputs=[
        gr.Textbox(label="Masked Email"),
        gr.Textbox(label="Entities"),
        gr.Textbox(label="Predicted Category"),
        gr.Textbox(label="Demasked Email")
    ],
    title="Email Classification with PII Masking"
)


if __name__ == "__main__":
    iface.launch()
