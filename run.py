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


def update_survey_sheet():
    print("\n updating sheet")
    
        
def validate_data(values):
    """
    Convert survey onput to integerss
    and validate wether input was correctly
    formatted
    """

    required_values = 5
    try:
        for value in values:
            
            if int(value) >= 1 and int(value) <= 10:
                continue
            else:
                raise ValueError(
                    "Wrong input"
                    "All numbers must be between 1 and 10")
    except ValueError as e:
            print(f"\n {e} is not a number")
    

    
def android_capture():
    """
    Captures android device survey data
    """
    print("Please enter survey data as follows: 10,10,10,10,10\n"
                "(Overall) (Design) (Ease of use) (Camera) (Battery) (Same device brands) (Would switch)\n"
                "\n(Same device brands) and (Would switch) 'booleans' are represented as 1 or 0 depending if yes or no")
    survey_str = input("Please input survey data values, "
                    "then press enter: \n")
    survey_data = survey_str.split(",")
    if len(survey_data) != 6:
            raise ValueError(
                f" 5 values required, you provided {len(values)}"
            )
    validate_data(survey_data)   

#def select_comparison():
def ask_pass():
    from secret import pwd as pwd
    password = input("Input Password: \n")
    if password == pwd:
        return True
    else:
        print("Invalid")
        ask_pass()
          

       
def select_function():
    """
    Let user select an action
    """
    print("\n Please choose an action:\n"
            "\n 1. Input Android survey data\n"
            " 2. Input iPhone survey data\n"
            " 3. Compare survey data\n")
    action = input("Please input desired action, "
                    "then press enter: \n")    
    if action == "1":
        android_capture()
    elif action == "2":
        iphone_capture()
    elif action == "3":
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