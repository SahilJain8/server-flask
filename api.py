import requests
from test import send_data
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization":  "Bearer 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"}


m=send_data()
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def get_data(source):
	
    output = query({
        "inputs": {
            "source_sentence":source,
            "sentences": m
        },
    })

   
    if max(output)*100>70:
        return True
    else:
        return False
