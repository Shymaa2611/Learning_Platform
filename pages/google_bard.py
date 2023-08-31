import google.generativeai as palm
from django.conf import settings

palm.configure(api_key=settings.PAML_API_KEY)
def get_response(prompt):
    response = palm.chat(messages=prompt)
    #print(response)
    return response.last