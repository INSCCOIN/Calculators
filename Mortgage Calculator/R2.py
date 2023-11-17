import tkinter as tk

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

# Create the main window
root = tk.Tk()
root.title("Tax Calculator")

# Create and place widgets in the window
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

calculate_button = tk.Button(root, text="Calculate", command=calculate_tax)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
