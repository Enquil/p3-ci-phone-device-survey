import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("phonedevice_survey_sheet")


def update_survey_sheet(values):
    print(values)
    print("Select Phone Operating System:\n"
          "1. Android\n"
          "2. iOS")
    
    os = input("Please input corresponding number: \n")
    
    try:
        if os == "1":
            print("Android")
        elif os == "2":
            print("iOS")
    except ValueError as e:
            print(f"\n {e} is not a valid option")
    update_survey_sheet(values)
            
    
        
def validate_data(values):
    """
    Convert survey onput to integerss
    and validate wether input was correctly
    formatted
    """
    
    try:
        for value in values:
            
            if int(value) >= 1 and int(value) <= 10:
                continue
            else:
                raise ValueError(
                    "Wrong input\n"
                    "All numbers must be between 1 and 10")
    except ValueError as e:
            print(f"\n {e} is not a number")    
            survey_capture()
    update_survey_sheet(values)


def survey_capture():
    """
    Captures android device survey data
    """
    print("Please enter survey data as follows: 10,10,10,10,10\n"
                "(Overall) (Design) (Ease of use) (Camera) (Battery)\n"
                "\n Input values must be number between 1 and 10")
    survey_str = input("Please input survey data, "
                    "then press enter: \n")
    survey_data = survey_str.split(",")
        
    if len(survey_data) != 5:
        print(
            f" 5 values required, you provided {len(survey_data)}"
        )
        survey_capture()
    else:          
        validate_data(survey_data)   

#def select_comparison():         

       
def select_function():
    """
    Let user select an action
    """
    print("\n Please choose an action:\n"
            "\n 1. Input Phone survey data\n"
            " 2. Compare survey data\n")
    action = input("Please input desired action, "
                    "then press enter: \n")    
    if action == "1":
        survey_capture()
    elif action == "2":
        select_comparison()
    else:
        print("\nInvalid action, try again!")
    main()
        
def main():
    """
    Runs all program functions
    """
    select_function()
    
main()