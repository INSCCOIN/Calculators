import tkinter as tk
import matplotlib.pyplot as plt

# Mortgage Calculator
def calculate_mortgage():
    global principal_entry, interest_rate_entry, num_years_entry, mortgage_result_label, interest_only_var, refinance_var

    principal = float(principal_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100
    num_years = int(num_years_entry.get())

    monthly_interest_rate = interest_rate / 12
    num_payments = num_years * 12

    if interest_only_var.get():
        monthly_payment = principal * (monthly_interest_rate / 12)
    else:
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)

    # Create an amortization schedule
    remaining_balance = principal
    interest_paid = 0
    principal_paid = 0
    amortization_schedule = []

    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        interest_paid += interest_payment
        principal_paid += principal_payment

        amortization_schedule.append((month, remaining_balance, interest_payment, principal_payment))

    mortgage_result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")

    if refinance_var.get():
        refinance_balance = float(refinance_balance_entry.get())
        refinance_interest_rate = float(refinance_interest_rate_entry.get()) / 100
        refinance_num_years = int(refinance_num_years_entry.get())

        refinance_monthly_interest_rate = refinance_interest_rate / 12
        refinance_num_payments = refinance_num_years * 12

        refinance_monthly_payment = refinance_balance * (refinance_monthly_interest_rate * (1 + refinance_monthly_interest_rate) ** refinance_num_payments) / ((1 + refinance_monthly_interest_rate) ** refinance_num_payments - 1)

        interest_savings = (monthly_payment - refinance_monthly_payment) * num_payments

        mortgage_result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}\n"
                                          f"Interest Savings: ${interest_savings:.2f} (if refinanced)")

    # Create a graphical representation of the amortization schedule
    months = [entry[0] for entry in amortization_schedule]
    balances = [entry[1] for entry in amortization_schedule]

    plt.plot(months, balances)
    plt.xlabel('Months')
    plt.ylabel('Remaining Balance')
    plt.title('Amortization Schedule')
    plt.grid(True)

    plt.show()

def open_mortgage_calculator():
    # Create the Mortgage Calculator window
    mortgage_window = tk.Toplevel(root)
    mortgage_window.title("Mortgage Calculator")

    # Create and place widgets for Mortgage Calculator
    global principal_entry, interest_rate_entry, num_years_entry, mortgage_result_label, interest_only_var, refinance_var, refinance_balance_entry, refinance_interest_rate_entry, refinance_num_years_entry

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

    interest_only_var = tk.BooleanVar()
    interest_only_checkbox = tk.Checkbutton(mortgage_window, text="Interest Only", variable=interest_only_var)
    interest_only_checkbox.pack()

    refinance_var = tk.BooleanVar()
    refinance_checkbox = tk.Checkbutton(mortgage_window, text="Refinance", variable=refinance_var, command=toggle_refinance)
    refinance_checkbox.pack()

    refinance_frame = tk.Frame(mortgage_window)
    refinance_balance_label = tk.Label(refinance_frame, text="Refinance Balance:")
    refinance_balance_label.grid(row=0, column=0)

    refinance_balance_entry = tk.Entry(refinance_frame)
    refinance_balance_entry.grid(row=0, column=1)

    refinance_interest_rate_label = tk.Label(refinance_frame, text="Refinance Interest Rate (%):")
    refinance_interest_rate_label.grid(row=1, column=0)

    refinance_interest_rate_entry = tk.Entry(refinance_frame)
    refinance_interest_rate_entry.grid(row=1, column=1)

    refinance_num_years_label = tk.Label(refinance_frame, text="Refinance Number of Years:")
    refinance_num_years_label.grid(row=2, column=0)

    refinance_num_years_entry = tk.Entry(refinance_frame)
    refinance_num_years_entry.grid(row=2, column=1)

    refinance_frame.pack()

    calculate_mortgage_button = tk.Button(mortgage_window, text="Calculate Mortgage", command=calculate_mortgage)
    calculate_mortgage_button.pack()

    mortgage_result_label = tk.Label(mortgage_window, text="")
    mortgage_result_label.pack()

def toggle_refinance():
    if refinance_var.get():
        refinance_balance_entry.config(state=tk.NORMAL)
        refinance_interest_rate_entry.config(state=tk.NORMAL)
        refinance_num_years_entry.config(state=tk.NORMAL)
    else:
        refinance_balance_entry.config(state=tk.DISABLED)
        refinance_interest_rate_entry.config(state=tk.DISABLED)
        refinance_num_years_entry.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Mortgage Calculator")

# Create and place widgets in the window for Mortgage Calculator
principal_label = tk.Label(root, text="Loan Principal:")
principal_label.pack()

principal_entry = tk.Entry(root)
principal_entry.pack()

interest_rate_label = tk.Label(root, text="Interest Rate (%):")
interest_rate_label.pack()

interest_rate_entry = tk.Entry(root)
interest_rate_entry.pack()

num_years_label = tk.Label(root, text="Number of Years:")
num_years_label.pack()

num_years_entry = tk.Entry(root)
num_years_entry.pack()

interest_only_var = tk.BooleanVar()
interest_only_checkbox = tk.Checkbutton(root, text="Interest Only", variable=interest_only_var)
interest_only_checkbox.pack()

refinance_var = tk.BooleanVar()
refinance_checkbox = tk.Checkbutton(root, text="Refinance", variable=refinance_var, command=toggle_refinance)
refinance_checkbox.pack()

refinance_frame = tk.Frame(root)
refinance_balance_label = tk.Label(refinance_frame, text="Refinance Balance:")
refinance_balance_label.grid(row=0, column=0)

refinance_balance_entry = tk.Entry(refinance_frame)
refinance_balance_entry.grid(row=0, column=1)

refinance_interest_rate_label = tk.Label(refinance_frame, text="Refinance Interest Rate (%):")
refinance_interest_rate_label.grid(row=1, column=0)

refinance_interest_rate_entry = tk.Entry(refinance_frame)
refinance_interest_rate_entry.grid(row=1, column=1)

refinance_num_years_label = tk.Label(refinance_frame, text="Refinance Number of Years:")
refinance_num_years_label.grid(row=2, column=0)

refinance_num_years_entry = tk.Entry(refinance_frame)
refinance_num_years_entry.grid(row=2, column=1)

refinance_frame.pack()

calculate_mortgage_button = tk.Button(root, text="Calculate Mortgage", command=calculate_mortgage)
calculate_mortgage_button.pack()

mortgage_result_label = tk.Label(root, text="")
mortgage_result_label.pack()

# Start the GUI main loop
root.mainloop()
