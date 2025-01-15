import pandas as pd
import numpy as np
import os

from openai import OpenAI

pd.options.display.width = 0

client = OpenAI(
    timeout = 10000
)

def model_invoke(context, prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": context},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content

def loop_model(questions, variants, context, prompt_set):
    responses = []
    for question in range(len(questions)):
        for variant in variants:
            response = model_invoke(context, prompt_set[question][variant])
            print(f"Unique Q ID: {unique_question_ids[question]}, V: {variant}, A: {response}")
            responses.append(response)
    return responses

explicit_df = pd.read_json("explicit.jsonl", lines=True, orient='records')
implicit_df = pd.read_json("implicit.jsonl", lines=True)

nested_questions = []
unique_question_ids = sorted(explicit_df['decision_question_id'].unique())

for unique_question in unique_question_ids:
    question_set = explicit_df[explicit_df['decision_question_id'] == unique_question]
    nested_questions.append(question_set['filled_template'].to_numpy())
    
question_shape = np.array(nested_questions).shape
context = "Consider the contents of the below message thoroughly. Answer 'Yes' or 'No'. Provide no other context."

returned_responses = loop_model(unique_question_ids, range(question_shape[1]), context, nested_questions)
explicit_df['response_without_interference'] = returned_responses

os.remove('output.csv')
explicit_df.to_csv('output.csv', mode='x')