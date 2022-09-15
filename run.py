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


def ask_os():
    """
    ask for operating system of customers phone
    """
    print("\n Please choose customer os:\n"
            "\n 1. Android\n"
            " 2. iOS")
    action = input("Please input desired action, "
                    "then press enter: \n")    
    if action == "1":
        android_capture()
    elif action == "2":
        print("goodbye")

    
def android_capture():
    """
    Captures android device survey data
    """
    print("Please enter survey data as follows\n"
                "(Overall) (Design)(Ease of use) (Camera) (Battery) (Same device brands) (Would switch)\n"
                "\n(Same device brands) and (Would switch) 'booleans' are represented as 1 or 0 depending if yes or no")
    survey_str= input("Please input survey data values, "
                    "then press enter: \n")
    survey_data = survey_str.split(",")
    print
        
def select_function():
    """
    Let user select an action
    """
    print("\n Please choose an action:\n"
            "\n 1. Input customer survey data\n"
            " 2. Compare data\n")
    action = input("Please input desired action, "
                    "then press enter: \n")    
    if action == "1":
        ask_os()
    elif action == "2":
        select_comparion()
    else:
        print("Invalid input, try again")
    main()
        
def main():
    """
    Runs all program functions
    """
    select_function()
    
main()