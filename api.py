from utils import mask_pii, unmask_pii
from models import predict_category

def classify_email(email):
    masked_email, entities = mask_pii(email)
    category = predict_category(masked_email)
    demasked_email = unmask_pii(masked_email, entities)

    return {
        "input_email_body": email,
        "list_of_masked_entities": str(entities),
        "masked_email": masked_email,
        "category_of_the_email": category
    }
