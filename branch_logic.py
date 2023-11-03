# Define the questionnaire structure using a dictionary
questionnaire = {
    "Q1": {
        "question": "Which fuel heats your home?",
        "options": {
            "Mains Gas": "Q2",
            "LPG": "Q2",
        },
        "tally":0,
    },
    "Q2": {
        "question": "What type of existing boiler do you have?",
        "options": {
            "Combi Boiler":{
                "tally":0.5,
                "next question":"Q5",
            },

            "Regular Boiler":{
                "tally":1,
                "next question": "Q3",
            },

            "System Boiler":{
                "tally":1,
                "next question": "Q3",
            },

            "Back Boiler":{
                "tally":1,
                "next question": "Q3",
        },

    },
    "Q3": {
        "question": "How fast does water flow from your cold tap?",
        "options": {
            "Slow":{
                "tally":0
                "next question":"Q22",
            },
            # --------------------------left off here------------------#
            "Medium": "Q5",
            "Fast": "Q10",
        },
    },
    "Q4": {
        "question": "Do you want to convert to a combi boiler?",
        "options": {
            "Yes": "Q5",
            "No": "Q5",
        },
    },
    "Q5": {
        "question": "Is your boiler currently working?",
        "options": {
            "Yes": "Q6",
            "No": "Q6",
        },
    },
    "Q6": {
        "question": "How old is your existing boiler?",
        "options": {
            "Less than 10 years": "Q7",
            "11-20 Years": "Q7",
            "21-25 Years":"Q7",
            "26+ Years": "Q7",
        },
    },
    "Q7": {
        "question": "Do you want to move the boiler location?",
        "options": {
            "Yes": "Q8",
            "No": "Q10",
        },
    },
    "Q8": {
        "question": "Where is your existing boiler located?",
        "options": {
            "Kitchen": "Q9",
            "Utility Room": "Q9",
            "Garage": "Q9",
            "Cupboard": "Q9",
            "Other": "Q9",
        },
    },
    "Q9":{
        "question": "Where do you want the new boiler to be located?",
        "options": {
            "Same Room (+£695)": "Q10",
            "Same Level (£895)": "Q10",
            "Another Level": "Q10",
            "Attic/Loft": "Q10",
        },
    },
    "Q10":{
        "question": "What type of house do you live in?",
        "options": {
            "Detached": "Q25",
            "Semi Detached": "Q ",
            "Terraced": "Q26",
            "Flat": "Q11",
            "Bungalow": "Q28",
        },
    },
    "Q11":{
        "question": "Which floor do you live on?",
        "options": {
            "Ground Floor": "Q13",
            "First Floor": "Q13",
            "Second Floor or Higher": "Q22",
        },
    },
    "Q12":{
        "question": "How many radiators are there?",
        "options": {
            "0-9": "Q13",
            "10-15": "Q13",
            "15+": "Q13",
            "Not Sure": "Q13",
        },
    },
    "Q13":{
        "question": "How many bedrooms are there in your home?",
        "options": {
            "1": "Q14",
            "2": "Q14",
            "3": "Q14",
            "4": "Q14",
            "5 or more": "Q14"
        },
    },
    "Q14":{
        "question": "How many bathtubs are there in your home?",
        "options": {
            "1": "Q15",
            "2": "Q15",
            "3 or more": "Q15",
        },
    },
    "Q15":{
        "question": "How many shower cubicles?",
        "options": {
            "1": "Q16",
            "2": "Q16",
            "3 or more": "Q16",
        },
    },
    "Q16":{
        "question": "Where does your boiler flue exit?",
        "options": {
            "External Wall": "Q19",
            "Roof": "Q17",
        },
    },
    "Q17":{
        "question": "Will the new boiler flue exit from a flat or pitched roof?",
        "options": {
            "Flat": "Q21",
            "Pitched": "Q18",
        },
    },
    "Q18":{
        "question": "What is the position of the flue on the roof",
        "options": {
            "Top Third": "Q21",
            "Middle Third": "Q21",
            "Bottom Third": "Q21",
        },
    },
    "Q19":{
        "question": "How long is the boiler flue",
        "options": {
            "less than 1 Metre": "Q20",
            "More than 1 Metre": "Q20",
            "Unsure": "Q20",
        },
    },
    "Q20":{
        "question": "How close is the boiler flue to a door or window?",
        "options": {
            "Less than 30cm": "Q21",
            "More than 30cm": "Q21",
            "Unsure": "Q21",
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
            "Small",
            "Medium",
            "Large",
        },
    }
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