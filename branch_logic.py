# Define the questionnaire structure using a dictionary
questionnaire = {
    "Q1": {
        "question": "Which fuel heats your home?",
        "options": {
            "Mains Gas": "Q2",
            "LPG": "Q2",
        },
    },
    "Q2": {
        "question": "What type of existing boiler do you have?",
        "options": {
            "Combi Boiler": "Q5",
            "Regular Boiler": "Q3",
            "System Boiler": "Q3 ",
            "Back Boiler": "Q3",
        },
    },
    "Q3": {
        "question": "How fast does water flow from your cold tap?",
        "options": {
            "Slow": "Q6",
            "Medium": "Q7",
            "Fast": "Q",
        },
    },
    "Q4": {
        "question": "Do you want to convert to a combi boiler?",
        "options": {
            "Yes": "Q8",
            "No": "Q9",
        },
    },
    "Q5": {
        "question": "Is your boiler currently working?",
        "options": {
            "Yes": "Q10",
            "No": "Q11",
        },
    },
    "Q6": {
        "question": "How old is your existing boiler?",
        "options": {
            "Less than 10 years": "Q12",
            "11-20 Years": "Q13",
            "21-25 Years":"Q ",
            "26+ Years": "Q ",
        },
    },
    "Q7": {
        "question": "Do you want to move the boiler location?",
        "options": {
            "Yes": "Q14",
            "No": "Q15",
        },
    },
    "Q8": {
        "question": "Where is your existing boiler located?",
        "options": {
            "Kitchen": "Q16",
            "Utility Room": "Q17",
            "Garage": "Q18",
            "Cupboard": "Q19",
            "Other": "Q20",
        },
    },
    "Q9":{
        "question": "Where do you want the new boiler to be located?",
        "options": {
            "Same Room (+£695)": "Q21",
            "Same Level (£895)": "Q22",
            "Another Level": "Q23",
            "Attic/Loft": "Q24",
        },
    },
    "Q10":{
        "question": "What type of house do you live in?",
        "options": {
            "Detached": "Q25",
            "Semi Detached": "Q ",
            "Terraced": "Q26",
            "Flat": "Q27",
            "Bungalow": "Q28",
        },
    },
    "Q11":{
        "question": "Which floor do you live on?",
        "options": {
            "Ground Floor": "Q29",
            "First Floor": "Q30",
            "Second Floor or Higher": "Q31",
        },
    },
    "Q12":{
        "question": "How many radiators are there?",
        "options": {
            "0-9": "Q32",
            "10-15": "Q33",
            "15+": "Q34",
            "Not Sure": "",
        },
    },
    "Q13":{
        "question": "How many bedrooms are there in your home?",
        "options": {
            "1": "Q35",
            "2": "Q36",
            "3": "Q37",
            "4": "Q38",
            "5 or more": "Q "
        },
    },
    "Q14":{
        "question": "How many bathtubs are there in your home?",
        "options": {
            "1": "Q39",
            "2": "Q40",
            "3 or more": "Q41",
        },
    },
    "Q15":{
        "question": "How many shower cubicles?",
        "options": {
            "1": "Q42",
            "2": "Q43",
            "3 or more": "Q44",
        },
    },
    "Q16":{
        "question": "Where does your boiler flue exit?",
        "options": {
            "External Wall": "Q45",
            "Roof": "Q46",
        },
    },
    "Q17":{
        "question": "Will the new boiler flue exit from a flat or pitched roof?",
        "options": {
            "Flat": "Q47",
            "Pitched": "Q48",
        },
    },
    "Q18":{
        "question": "What is the position of the flue on the roof",
        "options": {
            "Top Third": "Q49",
            "Middle Third": "Q50",
            "Bottom Third": "Q51",
        },
    },
    "Q19":{
        "question": "How long is the boiler flue",
        "options": {
            "less than 1 Metre": "Q52",
            "More than 1 Metre": "Q53",
            "Unsure": "Q ",
        },
    },
    "Q20":{
        "question": "How close is the boiler flue to a door or window?",
        "options": {
            "Less than 30cm": "Q54",
            "More than 30cm": "Q55",
            "Unsure": "Q ",
        },
    },
    "Q21":{
        "question": "What is your postcode?",
        "options": {},
    },
    "Q22":{
        "question": "Sorry, we need more details, Please call so we ma assist with your quote.",
    },
    "Q23":{
        "question": "Results: Boiler Sizes",
        "options": {
            "Small": "Q56",
            "Medium": "Q57",
            "Large": "Q58",
        },
    }







    # Add more questions and branches as needed
}

# Initialize the user's responses as an empty dictionary
user_responses = {}

current_question = "Q1"
while current_question in questionnaire:
    question_data = questionnaire[current_question]
    print(question_data["question"])
    for option, next_question in question_data["options"].items():
        print(f"{option}: {next_question}")

    user_input = input("Your choice: ").strip()

    if user_input == "Other":
        custom_response = input("Please specify: ").strip()
        user_responses[current_question] = custom_response
        break

    user_responses[current_question] = user_input

    current_question = question_data["options"].get(user_input, None)

print("User responses:")
for question, response in user_responses.items():
    print(f"{question}: {response}")