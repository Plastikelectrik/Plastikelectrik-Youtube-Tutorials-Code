import random

def get_response(query, prob_threshold=0.5):
    if random.random() < prob_threshold:
        return "I'm happy to help!" 
    else:
        return "Sorry, I'm not sure."
