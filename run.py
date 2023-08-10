import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('privatekey.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_project')

sales = SHEET.worksheet('project3')

def tax_calculate(x):
    print("Calculating....")
    if x <= 12570:
        tax_pay = 0
        return tax_pay

    elif x >= 12571 and x <= 50270:
        tax_pay = 0.2 * (x - 12570)
        return tax_pay

    elif x >= 50271 and x <= 125140:
        tax_pay = 7539.8 + 0.4 * (x - 50271)
        return tax_pay

    elif x > 125140:
        tax_pay = 29947.6 + 0.45 * (x - 125140)
        return tax_pay

def main():
    user_name = input("Enter your Name: ")
    user_earn = input("How much you earn a year: £")
    user_earn = int(user_earn)
    print(tax_calculate(user_earn))
    

main()