import streamlit as st
import pandas as pd
import random

st.title("Kvíz")
#st.write("works or not?")
#st.write(1+1)


questions = [
    
    # Water questions
    {"question": "Může významně ovlivnit přímou spotřebu pitné vody v rámci hydratace sportovců teplota vnějšího prostředí?",
     "options": ["Ano", "Ne"], "correct": "Ano"},

    {"question": "Má hyperhydratace významný vliv na spotřebu ptiné vody?", 
     "options": ["Ano", "Ne"], "correct": "Ne"},

    {"question": "Co spadá do kategorie využití vodních zdrojů - vysoká závislost, nízka spotřeba", 
     "options": ["Např. voda pro bazény, vodní plocha pro stadion",
                 "Např. voda pro motorová závodní vozidla", 
                 "Např. voda pro hydrataci sportovců, zavlažování venkovních travnatých sportovišť"],
                 "correct": "Např. voda pro bazény, vodní plocha pro stadion"},

    {"question": "Kolik '%' vody může ušetřit využívání retenčních nádrží dle Burszta-Adamiak a Spychalski (2021)?", 
     "options": ["25%", "75%", "90%", "70%"], "correct": "70%"},

    {"question": "Jsou umělé hrací plochy rizikovější z hlediska zranění?", 
     "options":["Ano", "Ne"], "correct":"Ne"},

    {"question": "Může dle Kanaan a kol. (2020) povrch umělých hracích ploch v letních měsících přesáhnout i teplotu:", 
     "options":["90°C", "80°C", "60°C", "70°C"], "correct":"80°C"},

    {"question": "Jaké opatření byste navrhli ke snížení spotřeby vody ve sportovních zařízeních?", 
     "options":["Retenční nádrže", "Odtoková zařízení", "Vsakovací zařízení"], "correct":"Retenční nádrže"},

    {"question": "Jaká je nevýhoda retenčních (vodních) nádrží?",
     "options": ["Jsou nákladné na výrobu", "Jsou nákladné na údržbu", "Jsou finančně nákladné"], "correct": "Jsou finančně nákladné"},

    {"question": "Jaký je přibližný počet hodin možné pohybové aktivity na travnatých plochách oproti plochám umělým?",
     "options": ["400 : 800", "300 : 600", "900 : 600", "200:500"], "correct": "300 : 600"},

    {"question": "Je -omezení některých způsobů využití vody- strukturální opatření?",
     "options": ["Ano", "Ne"], "correct": "Ne"},
    
    # Food questions
    {"question": "Co zahrnuje kritérium Life cycle assessment (LCA)?",
     "options":["Náklady spojené s výrobou a distribucí produktu", 
                "Náklady spojené s výrobou, distribucí, užíváním a likvidací produktu", 
                "Náklady spojené s transportem a spotřebou produktu"], 
                "correct":"Náklady spojené s výrobou, distribucí, užíváním a likvidací produktu"},

    {"question": "Z hlediska jakých hodnot hledíme na produkci a konzumaci stravy dle Thomé et al. (2020)?",
     "options":["Sociální, strukturální, emocionální, podmínečná a vědomostní", 
                "Funkcionální, sociální, emocionální, podmínečná a vědomostní", 
                "Funkcionální, tradicionální, emocionální, podmínečná a vědomostní"], 
                "correct":"Funkcionální, sociální, emocionální, podmínečná a vědomostní"},

    {"question": "Jaká je hlavní pozitivum lokálních potravin oproti potravinám dováženým dle Edwards-Jones (2010)?",
     "options":["Nižší finanční náklady", 
                "Nižší dopad na životní prostředí", 
                "Nižší produkce tzv. skleníkových plynů",
                "Snížení rizika zněčištění vodních zdrojů"], 
                "correct":"Nižší produkce tzv. skleníkových plynů"},

    {"question": "Co znamená -socialní hodnota- potravin?",
     "options":["Konzumace stravy dle návaznosti na sociální pravidla dané společnosti", 
                "Konzumace stravy dle návaznosti na danou situaci", 
                "Konzumace stravy dle návaznosti na danou sociální skupinu"], 
                "correct":"Konzumace stravy dle návaznosti na danou sociální skupinu"},

    {"question": "Celulóza je vhodným obalovým materiálem kvůli:",
     "options":["Non-toxicitě a recyklovatelnosti", 
                "Non-toxicitě a možnosti rychlého rozkladu, a nenákladné produkci", 
                "Non-toxicitě, recyklovatelnosti a nenákladné produkci"], 
                "correct":"Non-toxicitě a recyklovatelnosti"},
    
    {"question": "Jedním z nejvýznamnějších faktorů v plýtvání potravinami je dle Visscherse et al. (2016):",
     "options":["Vzdělanost spotřebitelů v oblasti zacházení s potravinami", 
                "Snížení konzumace stravy", 
                "Zvýšení konzumace stravy zejména lokálních potravin"], 
                "correct":"Vzdělanost spotřebitelů v oblasti zacházení s potravinami"},

    {"question": "Jedním z nejvýznamnějších faktorů v plýtvání potravinami je dle Visscherse et al. (2016):",
     "options":["Vzdělanost spotřebitelů v oblasti zacházení s potravinami", 
                "Snížení konzumace stravy", 
                "Zvýšení konzumace stravy zejména lokálních potravin"], 
                "correct":"Vzdělanost spotřebitelů v oblasti zacházení s potravinami"},
    
    {"question": "Která země má na svědomí nejvyšší podíl v plýtvání jídlem?",
     "options":["Austrálie", 
                "USA", 
                "Čína",
                "Indie"],
                "correct":"Čína"},
    
    {"question": "Dle Packiyadhas a kol. (2025) může v příštích deseti letech vzrůst produkce potravinového odpadu až o:",
     "options":["50%", 
                "28%", 
                "42%",
                "33%"], 
                "correct":"33%"},

    # Light and sound questions
    {"question": "Kolik '%' světelného toku Podle Sielachowska a Zajkowski (2020) může (neefektivně) směřovat do horního poloprostoru:", 
     "options":["60%", "80%", "40%", "50%"], "correct":"50%"}, 

    {"question": "V jakých sportovních oblastech je světelné a hlukové znečištění řešeno?", 
     "options":["Nejčastěji v kontextu velkých sportovních akcí (např. Olympijské hry)", 
                "Nejčastěji v oblastech sezónních sportů", 
                "Nejčastěji v kontextu specifických sportovních zařízení rekreačních sportovišť"], 
                "correct":"Nejčastěji v kontextu velkých sportovních akcí (např. Olympijské hry)"},
    
    # Materials questions
    {"question": "Kolik '%' je recyklováno z celkového množství oblečení v USA a Evropě v posledních letech? (Napiš pouze číslo)", 
     "open": True, "correct": "20"}, 

    {"question": "Kolik tun textilního odpadu je ročně na světě vyprodukováno?",
     "options":["100 milionů", "200 milionů", "100 tisíc", "200 tisíc"], "correct":"100 milionů"},

    {"question": "Zahrnuje kritérium Life cycle assessment (LCA) transport/distribuci produktu?",
     "options":["Ne", "Ano"], 
                "correct":"Ano"},

    {"question": "Mezi přírodní materiály patří:",
     "options":["Bambus, bavlna, vlna a recyklovaný polyester", 
                "Bambus, bavlna, vlna a hedvábí", 
                "Recyklovaný polyester, bavlna, hedvábí a nylon"], 
                "correct":"Bambus, bavlna, vlna a hedvábí"},

    {"question": "Jak moc významnou roli hrají sportovní značky (Adidas/Nike aj.) v šíření ekolgického marketingu?",
     "options":["Nepříliš významnou", "Žádnou", "Klíčovou"], 
                "correct":"Klíčovou"} 

]

NUM_QUESTIONS = 10

if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = random.sample(questions, NUM_QUESTIONS)

# Store user answers
user_answers = {}

for i, q in enumerate(st.session_state.selected_questions):
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
    total_questions = len(st.session_state.selected_questions)

    for q in st.session_state.selected_questions:
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
        






