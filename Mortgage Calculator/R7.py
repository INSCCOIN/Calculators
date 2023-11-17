import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog  # Add this import for file dialog
import csv  # Add this import for CSV handling



amortization_schedule = []    
    
# Mortgage Calculator
def calculate_mortgage():
    global principal_entry, interest_rate_entry, num_years_entry, mortgage_result_label, interest_only_var, refinance_var, amortization_table

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

        amortization_schedule.append((month, monthly_payment, principal_payment, interest_payment, remaining_balance))

    # Update the mortgage result label
    mortgage_result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")

    if refinance_var.get():
        refinance_balance_str = refinance_balance_entry.get()
        refinance_interest_rate_str = refinance_interest_rate_entry.get()
        refinance_num_years_str = refinance_num_years_entry.get()

        # Check if any of the refinance fields are empty
        if not refinance_balance_str or not refinance_interest_rate_str or not refinance_num_years_str:
            messagebox.showerror("Error", "Please fill in all refinance fields.")
            return

        refinance_balance = float(refinance_balance_str)
        refinance_interest_rate = float(refinance_interest_rate_str) / 100
        refinance_num_years = int(refinance_num_years_str)

        refinance_monthly_interest_rate = refinance_interest_rate / 12
        refinance_num_payments = refinance_num_years * 12

        refinance_monthly_payment = refinance_balance * (refinance_monthly_interest_rate * (1 + refinance_monthly_interest_rate) ** refinance_num_payments) / ((1 + refinance_monthly_interest_rate) ** refinance_num_payments - 1)

        interest_savings = (monthly_payment - refinance_monthly_payment) * num_payments

        mortgage_result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}\n"
                                          f"Interest Savings: ${interest_savings:.2f} (if refinanced)")

    # Clear the amortization table
    for row in amortization_table.get_children():
        amortization_table.delete(row)

def export_amortization_schedule(amortization_schedule):
    # Ask the user for the file name and location
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

    if file_path:
        # Create and write to the CSV file
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # Write the header row
            csv_writer.writerow(["Month", "Payment", "Principal Paid", "Interest Paid", "Remaining Balance"])
            # Write the data rows
            for entry in amortization_schedule:
                csv_writer.writerow(entry)

    # Update the amortization table
    for entry in amortization_schedule:
        amortization_table.insert("", "end", values=entry)
def generate_mortgage_chart(amortization_schedule):
    months = [entry[0] for entry in amortization_schedule]
    remaining_balances = [entry[4] for entry in amortization_schedule]

    plt.figure(figsize=(10, 6))
    plt.plot(months, remaining_balances, marker='o', linestyle='-')
    plt.title('Mortgage Balance Over Time')
    plt.xlabel('Month')
    plt.ylabel('Remaining Balance')
    plt.grid(True)

    plt.show()
    
    generate_mortgage_chart(amortization_schedule)
    

def open_mortgage_calculator():
    # Create the Mortgage Calculator window
    mortgage_window = tk.Toplevel(root)
    mortgage_window.title("Mortgage Calculator")

    # Create and place widgets for Mortgage Calculator
    global principal_entry, interest_rate_entry, num_years_entry, mortgage_result_label, interest_only_var, refinance_var, refinance_balance_entry, refinance_interest_rate_entry, refinance_num_years_entry, amortization_table

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

    # Create an amortization table with a vertical scrollbar
    amortization_table_frame = tk.Frame(mortgage_window)
    amortization_table_frame.pack(fill=tk.BOTH, expand=True)

    amortization_table = ttk.Treeview(amortization_table_frame, columns=("Month", "Payment", "Principal Paid", "Interest Paid", "Remaining Balance"), show="headings")
    amortization_table.heading("Month", text="Month")
    amortization_table.heading("Payment", text="Payment")
    amortization_table.heading("Principal Paid", text="Principal Paid")
    amortization_table.heading("Interest Paid", text="Interest Paid")
    amortization_table.heading("Remaining Balance", text="Remaining Balance")

    # Create a vertical scrollbar for the table
    scrollbar = ttk.Scrollbar(amortization_table_frame, orient=tk.VERTICAL, command=amortization_table.yview)
    amortization_table.configure(yscroll=scrollbar.set)

    amortization_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

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

export_button = tk.Button(root, text="Export Amortization Schedule", command=lambda: export_amortization_schedule(amortization_schedule))
export_button.pack()



# Create the Amortization Table
amortization_table = ttk.Treeview(root, columns=("Month", "Payment", "Principal Paid", "Interest Paid", "Remaining Balance"), show="headings")
amortization_table.heading("Month", text="Month")
amortization_table.heading("Payment", text="Payment")
amortization_table.heading("Principal Paid", text="Principal Paid")
amortization_table.heading("Interest Paid", text="Interest Paid")
amortization_table.heading("Remaining Balance", text="Remaining Balance")
amortization_table.pack()

# Start the GUI main loop
root.mainloop()
