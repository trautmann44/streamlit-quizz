import streamlit as st
import pandas as pd

st.title("Quiz game")
#st.write("works or not?")
#st.write(1+1)


questions = [
    {"question": "Může významně ovlivnit přímou spotřebu pitné vody v rámci hydratace sportovců teplota vnějšího prostředí?", "options": ["Yes", "No"], "correct": "Yes"},
    {"question": "Má hyperhydratace významný vliv na spotřebu ptiné vody?", "options": ["Yes", "No"], "correct": "No"},
    {"question": "Co spadá do kategorie využití vodních zdrojů - vysoká závislost, nízka spotřeba", "options": ["např. voda pro bazény, vodní plocha pro stadion",
                                                                                                                 "např. voda pro motorová závodní vozidla", 
                                                                                                                 "např. voda pro hydrataci sportovců, zavlažování venkovních travnatých sportovišť"],
                                                                                                                   "correct": "např. voda pro bazény, vodní plocha pro stadion"},
    {"question": "Kolik % vody může ušetřit využívání retenčních nádrží dle Burszta-Adamiak a Spychalski (2021)?", "options": ["25%", "75%", "90%", "70%"], "correct": "70%"},
]


# Store user responses
user_answers = {}

# Loop through the questions
for i, q in enumerate(questions):
    user_answers[i] = st.radio(q["question"], q["options"], index=None)

# Submit button
if st.button("Submit"):
    score = 0  # Initialize score
    for i, q in enumerate(questions):
        if user_answers[i] == q["correct"]:
            score += 1  # Increase score if correct

    # Show final score
    st.success(f"Your final score: {score}/{len(questions)} 🎉")
# python -m streamlit run e:/data/Statistics/Pyscripts/Streamlit_try_001.py
