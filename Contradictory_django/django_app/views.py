from django.shortcuts import render
import os
import tensorflow as tf
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, TFAutoModel
from transformers import TFXLMRobertaModel

# Define the custom object scope
custom_objects = {'TFXLMRobertaModel': TFXLMRobertaModel}

model_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'content', 'large_model.h5')

# Load the saved model with custom objects
loaded_model = tf.keras.models.load_model(model_file_path, custom_objects=custom_objects)
tokenizer = AutoTokenizer.from_pretrained('xlm-roberta-base')

def bert_encode(df, tokenizer):
    
    df['premise'] = df['premise'].astype(str)
    df['hypothesis'] = df['hypothesis'].astype(str)
    
    # Encode text using the BERT tokenizer
    batch_premises = df['premise'].tolist()
    batch_hypotheses = df['hypothesis'].tolist()

    tokens = tokenizer(
        batch_premises,
        batch_hypotheses,
        max_length=128,
        truncation=True,
        padding='max_length',
        add_special_tokens=True,
        return_attention_mask=True,
        return_tensors='tf'
    )
    inputs = {
        'input_ids': tokens['input_ids'],
        'attention_mask': tokens['attention_mask']
    }
    
    return inputs


def predict_similarity(request):
    if request.method == 'POST':
        # Get the input sentence from the request
        premises = request.POST.get('premises')
        hypotheses = request.POST.get('hypotheses')
        
        data = pd.DataFrame({'premise': [premises], 'hypothesis': [hypotheses]}, index=[0])

        inputs = bert_encode(data, tokenizer)

        # Use your trained model to predict the similarity
        similarity = loaded_model.predict(inputs)

        index = np.argmax(similarity[0])

        result = {0: "Entailment", 1: "Neutral", 2: "Contradiction"}.get(index)
 
        # Return the response as a JSON object
        response = {
            'premises': premises,
            'hypotheses': hypotheses,
            'similarity': result  
        }

        return render(request, 'result.html', context=response)

    return render(request, 'input.html')
