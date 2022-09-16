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
SHEET = GSPREAD_CLIENT.open("phone_device_survey_sheet")


def update_survey_sheet(values):
    """
    Choose operating system for current survey sheet.
    Print error message if wrong input and request new input.
    Loop back to survey_capture after successful input.
    """
    print("Select Phone Operating System:\n"
          "1. Android\n"
          "2. iOS")

    operating_system = input("Please input corresponding number: \n")

    if operating_system == "1":
        print("Updating Android survey sheet...")
        sheet = SHEET.worksheet("android")
        sheet.append_row(values)
        print("Data sent!")
        survey_capture()
    elif operating_system == "2":
        print("\nUpdating Iphone survey sheet...")
        sheet = SHEET.worksheet("iphone")
        sheet.append_row(values)
        print("Data sent!")
        survey_capture()
    else:
        print(
            "\033[1;31;40m      Not a valid input"
            "\n     Correct input is either 1 or 2 \033[0;37;40m"
        )
    update_survey_sheet(values)



def validate_data(values):
    """
    Convert survey onput to integers
    Validate wether input format was correct
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
            print(f"\n\033[1;31;40m {e} is not a number\033[0;37;40m")    
            survey_capture()

    values = [int(value) for value in values]
    update_survey_sheet(values)


def survey_capture():
    """
    Captures android device survey data
    """
    print("\nPlease enter survey data as follows: 10,10,10,10,10\n"
                "   (Battery) (Camera) (Design) (Ease of Use) (Overall)\n"
            "\nInput values must be number between 1 and 10")
    survey_str = input("Please input survey data, "
                    "then press enter: \n")
    survey_data = survey_str.split(",")

    if len(survey_data) != 5:
        print(
            f"\033[1;31;40m     5 values required, you provided {len(survey_data)}\033[0;37;40m"
        )
        survey_capture()
    else:
        validate_data(survey_data)


def select_comparison():
    """
    Compare data between Android and Iphone
    Get all data from specified column and
    calculate average score.
    """
    comparison_data = input("Select a category to compare: \n")
    
    if comparison_data == 1:
        x = [item for item in worksheet.col_values(1) if item]
        print(x)
    elif comparison_data == 2:
    elif comparison_data == 3: 
    elif comparison_data == 4: 
    elif comparison_data == 5: 
    else:     


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