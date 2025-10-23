import secrets
import string
import random
import xlsxwriter
from datetime import datetime
from statistics import mean


# ------------------- Random Data Generators -------------------

def generate_random_name():
    first_names = [
        "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun",
        "Sai", "Krishna", "Ananya", "Diya", "Ishita",
        "Meera", "Aditi", "Riya", "Nisha", "Sneha",
        "Karthik", "Pooja", "Lakshmi", "Rajesh", "Deepak"
    ]
    last_names = [
        "Sharma", "Patel", "Reddy", "Gupta", "Kumar",
        "Singh", "Naidu", "Das", "Nair", "Verma",
        "Iyer", "Rao", "Chowdhury", "Bose", "Mehta"
    ]
    return f"{random.choice(first_names)} {random.choice(last_names)}"


def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


def generate_excel_password(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


# ------------------- Financial Data Simulation -------------------

countries = [
    ("United States", "USD", 1.0, 3.2),
    ("India", "INR", 83.0, 5.5),
    ("United Kingdom", "GBP", 0.78, 4.0),
    ("Japan", "JPY", 150.0, 2.8),
    ("Germany", "EUR", 0.93, 3.5),
    ("Canada", "CAD", 1.36, 3.0),
    ("Australia", "AUD", 1.52, 3.4),
    ("UAE", "AED", 3.67, 2.9),
    ("Singapore", "SGD", 1.35, 3.1),
    ("Switzerland", "CHF", 0.89, 1.9)
]


def generate_financial_data():
    country, currency, rate_to_usd, inflation = random.choice(countries)

    salary_usd = random.randint(30000, 150000)
    salary_local = salary_usd * rate_to_usd

    expenditure = salary_local * random.uniform(0.5, 0.9)
    bank_credit = salary_local * random.uniform(0.0, 0.35)
    trading = salary_local * random.uniform(-0.3, 0.2)
    tax = salary_local * random.uniform(0.05, 0.35)

    net_savings = salary_local - (expenditure + tax) + bank_credit + trading
    inflation_factor = (100 - inflation) / 100
    adjusted_savings = net_savings * inflation_factor

    # --- Ethical Rules ---
    ethical_status = "Legally Ethical"
    red_flags = []

    if tax < (0.1 * salary_local):
        ethical_status = "Suspicious"
        red_flags.append("Low tax payment")

    if trading < (-0.25 * salary_local):
        ethical_status = "Suspicious"
        red_flags.append("Excessive trading loss")

    if bank_credit > (0.3 * salary_local):
        ethical_status = "Suspicious"
        red_flags.append("High unexplained bank credits")

    return {
        "Country": country,
        "Currency": currency,
        "Salary": round(salary_local, 2),
        "Expenditure": round(expenditure, 2),
        "Bank Credits": round(bank_credit, 2),
        "Trading": round(trading, 2),
        "Tax": round(tax, 2),
        "Net Savings": round(net_savings, 2),
        "Inflation %": round(inflation, 2),
        "Adj. Savings": round(adjusted_savings, 2),
        "Ethical Status": ethical_status,
        "Red Flags": ", ".join(red_flags) if red_flags else "-"
    }


# ------------------- Excel Generation -------------------

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
excel_file = f"Ethical_Financial_Data_{timestamp}.xlsx"
excel_password = generate_excel_password()

workbook = xlsxwriter.Workbook(excel_file, {'password': excel_password})
worksheet = workbook.add_worksheet("EthicalData")

# Header
headers = [
    "S.No", "Person Name", "Password", "Country", "Currency", "Salary",
    "Expenditure", "Bank Credits", "Trading", "Tax",
    "Net Savings", "Inflation %", "Adj. Savings", "Ethical Status", "Red Flags"
]
header_format = workbook.add_format({'bold': True, 'bg_color': '#DCE6F1', 'border': 1, 'align': 'center'})
for col, header in enumerate(headers):
    worksheet.write(0, col, header, header_format)

# Data
num_people = 1000
records_by_country = {}

for i in range(num_people):
    name = generate_random_name()
    password = generate_secure_password(random.randint(12, 20))
    data = generate_financial_data()

    row = [
        i + 1, name, password, data["Country"], data["Currency"],
        data["Salary"], data["Expenditure"], data["Bank Credits"],
        data["Trading"], data["Tax"], data["Net Savings"],
        data["Inflation %"], data["Adj. Savings"],
        data["Ethical Status"], data["Red Flags"]
    ]

    for col, value in enumerate(row):
        worksheet.write(i + 1, col, value)

    c = data["Country"]
    if c not in records_by_country:
        records_by_country[c] = {"Salary": [], "AdjSavings": [], "Inflation": []}
    records_by_country[c]["Salary"].append(data["Salary"])
    records_by_country[c]["AdjSavings"].append(data["Adj. Savings"])
    records_by_country[c]["Inflation"].append(data["Inflation %"])

worksheet.set_column(0, 0, 6)
worksheet.set_column(1, 2, 25)
worksheet.set_column(3, 13, 18)
worksheet.set_column(14, 14, 30)

# ------------------- Summary and Charts -------------------

chart_sheet = workbook.add_worksheet("Charts")
chart_sheet.write(0, 0, "Country")
chart_sheet.write(0, 1, "Avg Salary")
chart_sheet.write(0, 2, "Avg Adjusted Savings")
chart_sheet.write(0, 3, "Avg Inflation %")

countries_sorted = sorted(records_by_country.keys())
for idx, c in enumerate(countries_sorted, start=1):
    avg_salary = mean(records_by_country[c]["Salary"])
    avg_savings = mean(records_by_country[c]["AdjSavings"])
    avg_inflation = mean(records_by_country[c]["Inflation"])
    chart_sheet.write(idx, 0, c)
    chart_sheet.write(idx, 1, avg_salary)
    chart_sheet.write(idx, 2, avg_savings)
    chart_sheet.write(idx, 3, avg_inflation)

# Chart 1: Salary per Country
chart1 = workbook.add_chart({'type': 'column'})
chart1.add_series({
    'name': 'Avg Salary',
    'categories': ['Charts', 1, 0, len(countries_sorted), 0],
    'values': ['Charts', 1, 1, len(countries_sorted), 1],
    'fill': {'color': '#4F81BD'}
})
chart1.set_title({'name': 'Average Salary by Country'})
chart1.set_x_axis({'name': 'Country'})
chart1.set_y_axis({'name': 'Salary'})
chart_sheet.insert_chart('F2', chart1)

# Chart 2: Adjusted Savings
chart2 = workbook.add_chart({'type': 'column'})
chart2.add_series({
    'name': 'Adjusted Savings',
    'categories': ['Charts', 1, 0, len(countries_sorted), 0],
    'values': ['Charts', 1, 2, len(countries_sorted), 2],
    'fill': {'color': '#9BBB59'}
})
chart2.set_title({'name': 'Average Adjusted Savings by Country'})
chart_sheet.insert_chart('F22', chart2)

# Chart 3: Inflation Rates
chart3 = workbook.add_chart({'type': 'line'})
chart3.add_series({
    'name': 'Inflation Rate',
    'categories': ['Charts', 1, 0, len(countries_sorted), 0],
    'values': ['Charts', 1, 3, len(countries_sorted), 3],
    'line': {'color': '#C0504D'}
})
chart3.set_title({'name': 'Inflation Rate Comparison'})
chart_sheet.insert_chart('F42', chart3)

workbook.close()

print(f"✅ Excel file '{excel_file}' created successfully with ethical financial records.")
print(f"🔒 Excel file password (keep this safe): {excel_password}")
