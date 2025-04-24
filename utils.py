import re

def mask_pii(text):
    entities = []
    
    patterns = {
        "full_name": r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b",
        "email": r"[\w\.-]+@[\w\.-]+",
        "phone_number": r"\b\d{10}\b",
        "dob": r"\b\d{2}-\d{2}-\d{4}\b",
        "aadhar_num": r"\b\d{4}-\d{4}-\d{4}\b",
        "credit_debit_no": r"\b\d{16}\b",
        "cvv_no": r"\b\d{3}\b",
        "expiry_no": r"\b\d{2}/\d{2}\b"
    }

    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            entity = {
                "position": [match.start(), match.end()],
                "classification": label,
                "entity": match.group()
            }
            entities.append(entity)
            text = text.replace(match.group(), f"[{label}]")
    
    return text, entities

def unmask_pii(text, entities):
    for entity in entities:
        text = text.replace(f"[{entity['classification']}]", entity["entity"])
    return text