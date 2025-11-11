import streamlit as st
import pandas as pd

st.title("Quiz game")
#st.write("works or not?")
#st.write(1+1)


questions = [
    {"question": "Může významně ovlivnit přímou spotřebu pitné vody v rámci hydratace sportovců teplota vnějšího prostředí?",
     "options": ["Yes", "No"], "correct": "Yes"},
    {"question": "Má hyperhydratace významný vliv na spotřebu ptiné vody?", 
     "options": ["Yes", "No"], "correct": "No"},
    {"question": "Co spadá do kategorie využití vodních zdrojů - vysoká závislost, nízka spotřeba", 
     "options": ["např. voda pro bazény, vodní plocha pro stadion",
                 "např. voda pro motorová závodní vozidla", 
                 "např. voda pro hydrataci sportovců, zavlažování venkovních travnatých sportovišť"],
                 "correct": "např. voda pro bazény, vodní plocha pro stadion"},
    {"question": "Kolik % vody může ušetřit využívání retenčních nádrží dle Burszta-Adamiak a Spychalski (2021)?", 
     "options": ["25%", "75%", "90%", "70%"], "correct": "70%"},
    {"question": "Jsou umělé hrací plochy rizikovější z hlediska zranění?", 
     "options":["Ano", "Ne"], "correct":"Ne"},
    {"question": "Dle Kanaan et al. (2020) může povrch umělých hracích ploch v letních měsících přesáhnout i teplotu:", 
     "options":["90°C", "80°C", "60°C", "70°C"], "correct":"80°C"},

    {"question": "Jaké opatření byste navrhli ke snížení spotřeby vody ve sportovních zařízeních?", 
     "options":["retenční nádrže", "odtoková zařízení", "vsakovací zařízení"], "correct":"retenční nádrže"},
    
    {"question": "Kolik % je recyklováno z celkového množství oblečení v USA a Evropě v posledních letech? (Napiš pouze číslo)", 
     "open": True, "correct": "20"}, 
    
    {"question": "Kolik '%' světelného toku Podle Sielachowska a Zajkowski (2020) může (neefektivně) směřovat do horního poloprostoru:", 
     "options":["60%", "80%", "40%", "50%"], "correct":"50%"}, 

    {"question": "Kolik tun textilního odpadu je ročně na světě vyprodukováno?",
     "options":["100 milionů", "200 milionů", "100 tisíc", "200 tisíc"], "correct":"100 milionů"},

    {"question": "Co zahrnuje kritérium Life cycle assessment (LCA)?",
     "options":["Náklady spojené s výrobou a distribucí produktu", 
                "Náklady spojené s výrobou, distribucí, užíváním a likvidací produktu", 
                "Náklady spojené s transportem a spotřebou produktu"], 
                "correct":"Náklady spojené s výrobou, distribucí, užíváním a likvidací produktu"},

     {"question": "Mezi přírodní materiály patří:",
     "options":["Bambus, bavlna, vlna a recyklovaný polyester", 
                "Bambus, bavlna, vlna a hedvábí", 
                "Recyklovaný polyester, bavlna, hedvábí a nylon"], 
                "correct":"Bambus, bavlna, vlna a hedvábí"}
]


# Store user answers
# Store user answers
user_answers = {}

for i, q in enumerate(questions):
    st.subheader(f"Otázka {i+1}: {q['question']}")
    
    # Handle multiple-choice questions
    if "options" in q:
        user_answers[q["question"]] = st.radio("Vyberte odpověď:", q["options"], key=f"q{i}")
    
    # Handle open-ended questions (convert to lowercase)
    elif "open" in q:
        user_input = st.text_area("Vaše odpověď:", key=f"q{i}")
        user_answers[q["question"]] = user_input.strip().lower()  # Convert to lowercase and remove extra spaces

if st.button("Odeslat odpovědi"):
    correct_count = 0  # Initialize score counter
    total_questions = len(questions)

    for q in questions:
        user_answer = user_answers.get(q["question"], "").strip()
        
        # Check multiple-choice correctness
        if "options" in q and user_answer == q["correct"]:
            correct_count += 1
        
        # Check open-ended correctness (case insensitive)
        elif "open" in q and user_answer.lower() == q["correct"].lower():
            correct_count += 1

    # Display the final score
    st.success(f"✅ Váš konečný výsledek: **{correct_count} / {total_questions}** správně!")

    # Optional: Give feedback based on score
    if correct_count == total_questions:
        st.balloons()
        st.write("🎉 Perfektní! Odpověděli jste správně na všechny otázky.")
    elif correct_count > total_questions / 2:
        st.write("👍 Dobrá práce! Máte většinu odpovědí správně.")
    else:
        st.write("🔍 Zkusil bych to znovu...")
# python -m streamlit run e:/data/Statistics/Python_scripts/Streamlit_try_001.py







