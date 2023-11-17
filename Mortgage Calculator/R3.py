import tkinter as tk

# Tax Calculator
def calculate_tax():
    income = float(income_entry.get())
    federal_tax_rate = float(federal_tax_rate_entry.get())
    state_tax_rate = float(state_tax_rate_entry.get())

    federal_tax = income * (federal_tax_rate / 100)
    state_tax = income * (state_tax_rate / 100)
    total_tax = federal_tax + state_tax

    result_label.config(text=f"Federal Tax: ${federal_tax:.2f}\n"
                             f"State Tax: ${state_tax:.2f}\n"
                             f"Total Tax: ${total_tax:.2f}")

# Mortgage Calculator
def calculate_mortgage():
    global principal_entry, interest_rate_entry, num_years_entry, mortgage_result_label

    principal = float(principal_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100
    num_years = int(num_years_entry.get())

    monthly_interest_rate = interest_rate / 12
    num_payments = num_years * 12

    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)

    mortgage_result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")

def open_mortgage_calculator():
    # Create the Mortgage Calculator window
    mortgage_window = tk.Toplevel(root)
    mortgage_window.title("Mortgage Calculator")

    # Create and place widgets for Mortgage Calculator
    global principal_entry, interest_rate_entry, num_years_entry, mortgage_result_label

    principal_label = tk.Label(mortgage_window, text="Loan Principal:")
    principal_label.pack()

    principal_entry = tk.Entry(mortgage_window)
    principal_entry.pack()

    interest_rate_label = tk.Label(mortgage_window, text="Interest Rate (%):")
    interest_rate_label.pack()

    interest_rate_entry = tk.Entry(mortgage_window)
    interest_rate_entry.pack()

    num_years_label = tk.Label(mortgage_window, text="Number of Years:")
    num_years_label.pack()

    num_years_entry = tk.Entry(mortgage_window)
    num_years_entry.pack()

    calculate_mortgage_button = tk.Button(mortgage_window, text="Calculate Mortgage", command=calculate_mortgage)
    calculate_mortgage_button.pack()

    mortgage_result_label = tk.Label(mortgage_window, text="")
    mortgage_result_label.pack()

# Create the main window
root = tk.Tk()
root.title("Tax Calculator")

# Create and place widgets in the window for Tax Calculator
income_label = tk.Label(root, text="Income:")
income_label.pack()

income_entry = tk.Entry(root)
income_entry.pack()

federal_tax_rate_label = tk.Label(root, text="Federal Tax Rate (%):")
federal_tax_rate_label.pack()

federal_tax_rate_entry = tk.Entry(root)
federal_tax_rate_entry.pack()

state_tax_rate_label = tk.Label(root, text="State Tax Rate (%):")
state_tax_rate_label.pack()

state_tax_rate_entry = tk.Entry(root)
state_tax_rate_entry.pack()

calculate_button = tk.Button(root, text="Calculate Tax", command=calculate_tax)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Add a button to open the Mortgage Calculator window
mortgage_button = tk.Button(root, text="Open Mortgage Calculator", command=open_mortgage_calculator)
mortgage_button.pack()

# Start the GUI main loop
root.mainloop()
