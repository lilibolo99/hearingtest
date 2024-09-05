import streamlit as st

# Initialize session state for language selection
def initialize_language_state():
    if 'language' not in st.session_state:
        st.session_state.language = 'English'  # Default language

initialize_language_state()

# Custom CSS to style the language selector buttons
st.markdown("""
    <style>
    /* Style the language select buttons */
    .language-button {
        width: 100%;
        font-size: 16px !important;
        padding: 10px !important;
        border-radius: 5px;
        color: white;
    }
    .language-button-english {
        background-color: #007bff; /* Blue for English */
    }
    .language-button-german {
        background-color: #28a745; /* Green for German */
    }
    .language-button-selected {
        background-color: #004085 !important; /* Darker blue for selected English */
    }
    .language-button-selected-german {
        background-color: #155724 !important; /* Darker green for selected German */
    }
    </style>
""", unsafe_allow_html=True)

# Language Selector buttons at the top
lang_col1, lang_col2, lang_col3 = st.columns([4, 1, 1])  # Adjust the ratio as needed to center the buttons
with lang_col2:
    english_selected = st.session_state.language == 'English'
    if st.button('English', key='english', help='Switch to English', 
                 on_click=lambda: st.session_state.update(language='English'), 
                 use_container_width=True):
        st.session_state.language = 'English'

with lang_col3:
    german_selected = st.session_state.language == 'German'
    if st.button('Deutsch', key='german', help='Switch to German', 
                 on_click=lambda: st.session_state.update(language='German'), 
                 use_container_width=True):
        st.session_state.language = 'German'

# Conditional logic to load and execute the respective code
if st.session_state.language == 'English':
    # Include your English version code here
    def english_app():
        # Custom CSS to style the application
        st.markdown("""
        <style>
        /* Force buttons to fill the column width and center align text inside them */
        div.stButton > button {
            width: 100%;
            border-radius: 5px; /* Rounded corners */
            background-color: #4CAF50; /* Default Green background */
            color: white; /* White text */
        }
        /* Adjust button hover style */
        div.stButton > button:hover {
            background-color: #45a049; /* Darker green */
        }
        /* Style for Weber test buttons */
        .element-container:has(#weber-lateralizes-to-the-right) + div button,
        .element-container:has(#weber-center) + div button,
        .element-container:has(#weber-lateralizes-to-the-left) + div button {
            background-color: #1662a7; /* Blue background */
        }
        /* Style for Rinne Positive buttons */
        .element-container:has(#right-positive) + div button,
        .element-container:has(#left-positive) + div button {
            background-color: #2b790a; /* Green background */
        }
        /* Style for Rinne Negative buttons */
        .element-container:has(#right-negative) + div button,
        .element-container:has(#left-negative) + div button {
            background-color: #c00404; /* Red background */
        }
        /* Style for Reset button */
        .element-container:has(#reset-button) + div button {
            background-color: #7c8994; /* Grey background */
        }
        /* Selected state styles */
        .selected-weber {
            background-color: #218184 !important; /* darker blue */
        }
        .selected-rinne-positive {
            background-color: #32b28d !important; /* 20% darker green */
        }
        .selected-rinne-negative {
            background-color: #d65b5b !important; /* 20% darker red */
        }
        /* Add larger dots to the left and right of the button text */
        .selected-dot::before {
            content: '●';
            color: white;
            font-weight: bold;
            margin-right: 5px;
            font-size: 20px; /* Double the size */
        }
        .selected-dot::after {
            content: '●';
            color: white;
            font-weight: bold;
            margin-left: 5px;
            font-size: 20px; /* Double the size */
        }
        </style>
        """, unsafe_allow_html=True)

        # JavaScript to toggle selected state class
        st.markdown("""
        <script>
        function clearSelectedClass() {
            var weberButtons = document.querySelectorAll('.selected-weber');
            weberButtons.forEach(function(button) {
                button.classList.remove('selected-weber');
                button.classList.remove('selected-dot');
            });

            var rinnePositiveButtons = document.querySelectorAll('.selected-rinne-positive');
            rinnePositiveButtons.forEach(function(button) {
                button.classList.remove('selected-rinne-positive');
                button.classList.remove('selected-dot');
            });

            var rinneNegativeButtons = document.querySelectorAll('.selected-rinne-negative');
            rinneNegativeButtons.forEach(function(button) {
                button.classList.remove('selected-rinne-negative');
                button.classList.remove('selected-dot');
            });
        }

        function addSelectedClass(label, className) {
            var buttons = document.querySelectorAll('div.stButton > button');
            buttons.forEach(function(button) {
                if (button.innerText.includes(label)) {
                    button.classList.add(className);
                    button.classList.add('selected-dot');
                }
            });
        }

        document.addEventListener("DOMContentLoaded", function() {
            // Weber buttons
            var weberButtons = ['Lateralizes to the right', 'Center', 'Lateralizes to the left'];
            weberButtons.forEach(function(label) {
                var button = document.querySelector(`div.stButton > button[aria-label="${label}"]`);
                if (button) {
                    button.addEventListener('click', function() {
                        clearSelectedClass();
                        addSelectedClass(label, 'selected-weber');
                    });
                }
            });

            // Rinne Positive buttons
            var rinnePositiveButtons = ['Right Positive', 'Left Positive'];
            rinnePositiveButtons.forEach(function(label) {
                var button = document.querySelector(`div.stButton > button[aria-label="${label}"]`);
                if (button) {
                    button.addEventListener('click', function() {
                        clearSelectedClass();
                        addSelectedClass(label, 'selected-rinne-positive');
                    });
                }
            });

            // Rinne Negative buttons
            var rinneNegativeButtons = ['Right Negative', 'Left Negative'];
            rinneNegativeButtons.forEach(function(label) {
                var button = document.querySelector(`div.stButton > button[aria-label="${label}"]`);
                if (button) {
                    button.addEventListener('click', function() {
                        clearSelectedClass();
                        addSelectedClass(label, 'selected-rinne-negative');
                    });
                }
            });
        });
        </script>
        """, unsafe_allow_html=True)

        # Initialize session states
        def initialize_state():
            if 'rinne_right' not in st.session_state:
                st.session_state.rinne_right = ''
            if 'rinne_left' not in st.session_state:
                st.session_state.rinne_left = ''
            if 'weber' not in st.session_state:
                st.session_state.weber = ''
            if 'result' not in st.session_state:
                st.session_state.result = 'Please complete all selections.'
            if 'last_weber_clicked' not in st.session_state:
                st.session_state.last_weber_clicked = None
            if 'last_rinne_right_clicked' not in st.session_state:
                st.session_state.last_rinne_right_clicked = None
            if 'last_rinne_left_clicked' not in st.session_state:
                st.session_state.last_rinne_left_clicked = None

        initialize_state()

        def set_rinne(side, value):
            st.session_state[side] = value
            if side == 'rinne_right':
                st.session_state.last_rinne_right_clicked = value
            elif side == 'rinne_left':
                st.session_state.last_rinne_left_clicked = value
            evaluate_result()

        def set_weber(value):
            st.session_state.weber = value
            st.session_state.last_weber_clicked = value
            evaluate_result()

        def evaluate_result():
            st.session_state.result = ''
            weber = st.session_state.weber
            rinne_left = st.session_state.rinne_left
            rinne_right = st.session_state.rinne_right
            
            # Adding checks for physiologically impossible combinations
            if weber == "Center" and rinne_left == "Negative" and rinne_right == "Positive":
                st.session_state.result = "Please retest, results are physiologically impossible."
            elif weber == "Center" and rinne_right == "Negative" and rinne_left == "Positive":
                st.session_state.result = "Please retest, results are physiologically impossible."
            else:
                if weber and rinne_left and rinne_right:
                    conditions = [
                        (weber == "Center" and rinne_left == "Positive" and rinne_right == "Positive", "Normal hearing or symmetric sensorineural hearing loss"),
                        (weber == "Lateralizes to the right" and rinne_left == "Positive" and rinne_right == "Negative", "Conductive hearing loss on the right side"),
                        (weber == "Lateralizes to the left" and rinne_left == "Negative" and rinne_right == "Positive", "Conductive hearing loss on the left side"),
                        (weber == "Lateralizes to the left" and rinne_left == "Positive" and rinne_right == "Positive", "Sensorineural hearing loss on the right side"),
                        (weber == "Lateralizes to the right" and rinne_left == "Positive" and rinne_right == "Positive", "Sensorineural hearing loss on the left side"),
                        (weber == "Center" and rinne_left == "Negative" and rinne_right == "Negative", "Symmetric conductive hearing loss"),
                        (weber == "Lateralizes to the right" and rinne_left == "Negative" and rinne_right == "Positive", "Deafness on the left side or combined hearing loss on the left side"),
                        (weber == "Lateralizes to the left" and rinne_left == "Positive" and rinne_right == "Negative", "Deafness on the right side or combined hearing loss on the right side"),
                        (weber == "Lateralizes to the left" and rinne_left == "Negative" and rinne_right == "Negative", "Conductive hearing loss in both ears, more pronounced on the right side or combined hearing loss on both sides with varying degrees -> further examination is needed for conclusive results"),
                        (weber == "Lateralizes to the right" and rinne_left == "Negative" and rinne_right == "Negative", "Conductive hearing loss in both ears, more pronounced on the left side or combined hearing loss on both sides with varying degrees -> further examination is needed for conclusive results")
                    ]
                    for condition, result in conditions:
                        if condition:
                            st.session_state.result = result
                            break
                else:
                    st.session_state.result = "Please complete all selections."

        def reset():
            st.session_state.rinne_left = ''
            st.session_state.rinne_right = ''
            st.session_state.weber = ''
            st.session_state.result = 'Please complete all selections.'
            st.session_state.last_weber_clicked = None
            st.session_state.last_rinne_right_clicked = None
            st.session_state.last_rinne_left_clicked = None

        # UI Layout with headers and buttons centered
        st.markdown("<h1 style='text-align: center;'>Hearing Test Diagnosis</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Weber Test:</h2>", unsafe_allow_html=True)
        cols = st.columns(3)
        button_styles = {"Lateralizes to the right": cols[0], "Center": cols[1], "Lateralizes to the left": cols[2]}
        for label, col in button_styles.items():
            clicked = st.session_state.last_weber_clicked == label
            with col:
                st.markdown(f'<span id="weber-{label.lower().replace(" ", "-")}"></span>', unsafe_allow_html=True)
                st.button(f"● {label} ●" if clicked else label, on_click=set_weber, args=(label,), key=label)

        st.markdown("<h2 style='text-align: center;'>Rinne Test:</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            for label in ["Positive", "Negative"]:
                clicked = st.session_state.last_rinne_right_clicked == label
                st.markdown(f'<span id="right-{label.lower()}"></span>', unsafe_allow_html=True)
                st.button(f"● Right {label} ●" if clicked else f"Right {label}", on_click=lambda label=label: set_rinne('rinne_right', label), key=f"Right {label}")
        with col2:
            for label in ["Positive", "Negative"]:
                clicked = st.session_state.last_rinne_left_clicked == label
                st.markdown(f'<span id="left-{label.lower()}"></span>', unsafe_allow_html=True)
                st.button(f"● Left {label} ●" if clicked else f"Left {label}", on_click=lambda label=label: set_rinne('rinne_left', label), key=f"Left {label}")

        st.markdown("<h2 style='text-align: center;'>Examination Result:</h2>", unsafe_allow_html=True)
        if st.session_state.result:
            st.markdown(f"<div style='text-align: center;'>{st.session_state.result}</div>", unsafe_allow_html=True)

        st.markdown('<span id="reset-button"></span>', unsafe_allow_html=True)
        st.button("Reset", on_click=reset)

    english_app()  # Run the English version of the app
    
    # Add the PayPal donation button for the English version
    st.markdown("""
    <form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="hosted_button_id" value="D9YET727WSQLW" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_CH/i/scr/pixel.gif" width="1" height="1" />
</form>


    """, unsafe_allow_html=True)

elif st.session_state.language == 'German':
    # Include your German version code here
    def german_app():
        # Add German version code here as per the previous example

        # Benutzerdefiniertes CSS, um die Anwendung zu stylen
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100..900&display=swap');

        body {
            font-family: 'Roboto Slab', serif;
        }

        /* Zwingen Sie die Schaltflächen, die Spaltenbreite auszufüllen und den Text innerhalb dieser zu zentrieren */
        div.stButton > button {
            width: 100%;
            border-radius: 5px; /* Abgerundete Ecken */
            background-color: #4CAF50; /* Standardmäßiger grüner Hintergrund */
            color: white; /* Weißer Text */
            font-family: 'Roboto Slab', serif; /* Anwendung des neuen Fonts auf die Schaltflächen */
        }

        /* Anpassen des Hover-Stils der Schaltfläche */
        div.stButton > button:hover {
            background-color: #45a049; /* Dunkleres Grün */
        }

        /* Stil für Weber-Test-Schaltflächen */
        .element-container:has(#weber-lateralisiert-nach-rechts) + div button,
        .element-container:has(#weber-mitte) + div button,
        .element-container:has(#weber-lateralisiert-nach-links) + div button {
            background-color: #1662a7; /* Blauer Hintergrund */
        }

        /* Stil für Rinne Positive Schaltflächen */
        .element-container:has(#rechts-positiv) + div button,
        .element-container:has(#links-positiv) + div button {
            background-color: #2b790a; /* Grüner Hintergrund */
        }

        /* Stil für Rinne Negative Schaltflächen */
        .element-container:has(#rechts-negativ) + div button,
        .element-container:has(#links-negativ) + div button {
            background-color: #c00404; /* Roter Hintergrund */
        }

        /* Stil für Zurücksetzen-Schaltfläche */
        .element-container:has(#reset-button) + div button {
            background-color: #7c8994; /* Grauer Hintergrund */
        }

        /* Ausgewählter Zustand Stile */
        .selected-weber {
            background-color: #218184 !important; /* dunkleres Blau */
        }

        .selected-rinne-positive {
            background-color: #32b28d !important; /* 20% dunkleres Grün */
        }

        .selected-rinne-negative {
            background-color: #d65b5b !important; /* 20% dunkleres Rot */
        }

        /* Fügen Sie größere Punkte links und rechts vom Schaltflächentext hinzu */
        .selected-dot::before {
            content: '●';
            color: white;
            font-weight: bold;
            margin-right: 5px;
            font-size: 20px; /* Doppelte Größe */
        }

        .selected-dot::after {
            content: '●';
            color: white;
            font-weight: bold;
            margin-left: 5px;
            font-size: 20px; /* Doppelte Größe */
        }
        </style>
        """, unsafe_allow_html=True)

        # JavaScript, um die ausgewählte Klassenbezeichnung umzuschalten
        st.markdown("""
        <script>
        function clearSelectedClass() {
            var weberButtons = document.querySelectorAll('.selected-weber');
            weberButtons.forEach(function(button) {
                button.classList.remove('selected-weber');
                button.classList.remove('selected-dot');
            });

            var rinnePositiveButtons = document.querySelectorAll('.selected-rinne-positive');
            rinnePositiveButtons.forEach(function(button) {
                button.classList.remove('selected-rinne-positive');
                button.classList.remove('selected-dot');
            });

            var rinneNegativeButtons = document.querySelectorAll('.selected-rinne-negative');
            rinneNegativeButtons.forEach(function(button) {
                button.classList.remove('selected-rinne-negative');
                button.classList.remove('selected-dot');
            });
        }

        function addSelectedClass(label, className) {
            var buttons = document.querySelectorAll('div.stButton > button');
            buttons.forEach(function(button) {
                if (button.innerText.includes(label)) {
                    button.classList.add(className);
                    button.classList.add('selected-dot');
                }
            });
        }

        document.addEventListener("DOMContentLoaded", function() {
            // Weber-Schaltflächen
            var weberButtons = ['Lateralisiert nach rechts', 'Mitte', 'Lateralisiert nach links'];
            weberButtons.forEach(function(label) {
                var button = document.querySelector(`div.stButton > button[aria-label="${label}"]`);
                if (button) {
                    button.addEventListener('click', function() {
                        clearSelectedClass();
                        addSelectedClass(label, 'selected-weber');
                    });
                }
            });

            // Rinne Positive Schaltflächen
            var rinnePositiveButtons = ['Rechts Positiv', 'Links Positiv'];
            rinnePositiveButtons.forEach(function(label) {
                var button = document.querySelector(`div.stButton > button[aria-label="${label}"]`);
                if (button) {
                    button.addEventListener('click', function() {
                        clearSelectedClass();
                        addSelectedClass(label, 'selected-rinne-positive');
                    });
                }
            });

            // Rinne Negative Schaltflächen
            var rinneNegativeButtons = ['Rechts Negativ', 'Links Negativ'];
            rinneNegativeButtons.forEach(function(label) {
                var button = document.querySelector(`div.stButton > button[aria-label="${label}"]`);
                if (button) {
                    button.addEventListener('click', function() {
                        clearSelectedClass();
                        addSelectedClass(label, 'selected-rinne-negative');
                    });
                }
            });
        });
        </script>
        """, unsafe_allow_html=True)

        # Initialisieren von Sitzungszuständen
        def initialize_state():
            if 'rinne_rechts' not in st.session_state:
                st.session_state.rinne_rechts = ''
            if 'rinne_links' not in st.session_state:
                st.session_state.rinne_links = ''
            if 'weber' not in st.session_state:
                st.session_state.weber = ''
            if 'result' not in st.session_state:
                st.session_state.result = 'Bitte vervollständigen Sie alle Auswahlmöglichkeiten.'
            if 'letzter_weber_geklickt' not in st.session_state:
                st.session_state.letzter_weber_geklickt = None
            if 'letzter_rinne_rechts_geklickt' not in st.session_state:
                st.session_state.letzter_rinne_rechts_geklickt = None
            if 'letzter_rinne_links_geklickt' not in st.session_state:
                st.session_state.letzter_rinne_links_geklickt = None

        initialize_state()

        def set_rinne(seite, wert):
            st.session_state[seite] = wert
            if seite == 'rinne_rechts':
                st.session_state.letzter_rinne_rechts_geklickt = wert
            elif seite == 'rinne_links':
                st.session_state.letzter_rinne_links_geklickt = wert
            auswertung_ergebnis()

        def set_weber(wert):
            st.session_state.weber = wert
            st.session_state.letzter_weber_geklickt = wert
            auswertung_ergebnis()

        def auswertung_ergebnis():
            st.session_state.result = ''
            weber = st.session_state.weber
            rinne_links = st.session_state.rinne_links
            rinne_rechts = st.session_state.rinne_rechts
            
            # Überprüfung auf physiologisch unmögliche Kombinationen
            if weber == "Mitte" and rinne_links == "Negativ" and rinne_rechts == "Positiv":
                st.session_state.result = "Bitte erneut testen, Ergebnisse sind physiologisch unmöglich."
            elif weber == "Mitte" and rinne_rechts == "Negativ" and rinne_links == "Positiv":
                st.session_state.result = "Bitte erneut testen, Ergebnisse sind physiologisch unmöglich."
            else:
                if weber and rinne_links and rinne_rechts:
                    conditions = [
                        (weber == "Mitte" and rinne_links == "Positiv" and rinne_rechts == "Positiv", "Normales Gehör oder beidseits symmetrische Schallempfindungsstörung"),
                        (weber == "Lateralisiert nach rechts" and rinne_links == "Positiv" and rinne_rechts == "Negativ", "Schallleitungsstörung rechts"),
                        (weber == "Lateralisiert nach links" and rinne_links == "Negativ" and rinne_rechts == "Positiv", "Schallleitungsstörung links"),
                        (weber == "Lateralisiert nach links" and rinne_links == "Positiv" and rinne_rechts == "Positiv", "Schallempfindungsstörung rechts "),
                        (weber == "Lateralisiert nach rechts" and rinne_links == "Positiv" and rinne_rechts == "Positiv", "Schallempfindungsstörung links"),
                        (weber == "Mitte" and rinne_links == "Negativ" and rinne_rechts == "Negativ", "Beidseits symmetrische Schallleitungsstörung"),
                        (weber == "Lateralisiert nach rechts" and rinne_links == "Negativ" and rinne_rechts == "Positiv", "Taubheit links oder kombinierte Schwerhörigkeit links"),
                        (weber == "Lateralisiert nach links" and rinne_links == "Positiv" and rinne_rechts == "Negativ", "Taubheit rechts oder kombinierte Schwerhörigkeit rechts"),
                        (weber == "Lateralisiert nach links" and rinne_links == "Negativ" and rinne_rechts == "Negativ", "Schallleitungsstörung beidseits, ausgeprägter auf der rechten Seite oder kombinierter Hörverlust auf beiden Seiten mit unterschiedlichen Ausprägungen -> weitere Untersuchungen notwendig für eindeutige Ergebnisse"),
                        (weber == "Lateralisiert nach rechts" and rinne_links == "Negativ" and rinne_rechts == "Negativ", "Schallleitungsstörung beidseits, ausgeprägter auf der linken Seite oder kombinierter Hörverlust auf beiden Seiten mit unterschiedlichen Ausprägungen -> weitere Untersuchungen notwendig für eindeutige Ergebnisse")
                    ]
                    for condition, result in conditions:
                        if condition:
                            st.session_state.result = result
                            break
                else:
                    st.session_state.result = "Bitte vervollständigen Sie alle Auswahlmöglichkeiten."

        def reset():
            st.session_state.rinne_links = ''
            st.session_state.rinne_rechts = ''
            st.session_state.weber = ''
            st.session_state.result = 'Bitte vervollständigen Sie alle Auswahlmöglichkeiten.'
            st.session_state.letzter_weber_geklickt = None
            st.session_state.letzter_rinne_rechts_geklickt = None
            st.session_state.letzter_rinne_links_geklickt = None

        # UI-Layout mit Überschriften und zentrierten Schaltflächen
        st.markdown("<h1 style='text-align: center;'>Hörprüfung</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Weber Test:</h2>", unsafe_allow_html=True)
        cols = st.columns(3)
        button_styles = {"Lateralisiert nach rechts": cols[0], "Mitte": cols[1], "Lateralisiert nach links": cols[2]}
        for label, col in button_styles.items():
            clicked = st.session_state.letzter_weber_geklickt == label
            with col:
                st.markdown(f'<span id="weber-{label.lower().replace(" ", "-")}"></span>', unsafe_allow_html=True)
                st.button(f"● {label} ●" if clicked else label, on_click=set_weber, args=(label,), key=label)

        st.markdown("<h2 style='text-align: center;'>Rinne Test:</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            for label in ["Positiv", "Negativ"]:
                clicked = st.session_state.letzter_rinne_rechts_geklickt == label
                st.markdown(f'<span id="rechts-{label.lower()}"></span>', unsafe_allow_html=True)
                st.button(f"● Rechts {label} ●" if clicked else f"Rechts {label}", on_click=lambda label=label: set_rinne('rinne_rechts', label), key=f"Rechts {label}")
        with col2:
            for label in ["Positiv", "Negativ"]:
                clicked = st.session_state.letzter_rinne_links_geklickt == label
                st.markdown(f'<span id="links-{label.lower()}"></span>', unsafe_allow_html=True)
                st.button(f"● Links {label} ●" if clicked else f"Links {label}", on_click=lambda label=label: set_rinne('rinne_links', label), key=f"Links {label}")

        st.markdown("<h2 style='text-align: center;'>Untersuchungsergebnis:</h2>", unsafe_allow_html=True)
        if st.session_state.result:
            st.markdown(f"<div style='text-align: center;'>{st.session_state.result}</div>", unsafe_allow_html=True)

        st.markdown('<span id="reset-button"></span>', unsafe_allow_html=True)
        st.button("Zurücksetzen", on_click=reset)

    german_app()  # Run the German version of the app

    # Add the PayPal donation button for the German version
    st.markdown("""
  <form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="hosted_button_id" value="D9YET727WSQLW" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_CH/i/scr/pixel.gif" width="1" height="1" />
</form>
    """, unsafe_allow_html=True)
