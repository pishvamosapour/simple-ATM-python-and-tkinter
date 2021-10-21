import tkinter as tk
from tkinter.constants import END
import tkinter.font as fnt

#window settings
root = tk.Tk()
root.title('ATM')
root.geometry('800x600')
root.resizable(0, 0)
root.configure(bg="#f2c65e")

digit_code = '1234'
balance_value = '1,200,000'

def root_function():
    digit_code_input_value = digit_code_input.get()
    if digit_code_input_value == digit_code:
        def balance():
            general_commands_area.destroy()
            balance_label = tk.Label(text='your balance : ' + balance_value, bg="#f2c65e",font = fnt.Font(size = 28), padx=200, pady=200)
            balance_label.grid(row=2, column=2)
        
        def withdraw():
            
            def success_withdraw():
                balance_value_withdraw_massage = withdraw_input.get()
                withdraw_items.destroy()
                withdraw_suuccess_massage = tk.Label(text='withdraw successfuly', bg='#f2c65e',font = fnt.Font(size = 28), padx=140, pady=50).grid(row=0, column=2)
                withdraw_suuccess_massage2 = tk.Label(text='your withdraw amount : '+balance_value_withdraw_massage, bg='#f2c65e',font = fnt.Font(size = 28), padx=140, pady=50).grid(row=1, column=2)
             
            withdraw_items = tk.LabelFrame(root, bg="#f2c65e", padx=10, pady=10, borderwidth=0)
            withdraw_items.grid()               
            general_commands_area.destroy()
            balance_in_withdraw = tk.Label(withdraw_items,text='your balance now : ' + balance_value,bg="#f2c65e",font = fnt.Font(size = 28),padx=150, pady=50).grid(row=0, column=2)
            withdraw_value_lable = tk.Label(withdraw_items,text='enter your withdraw amount',bg="#f2c65e",font = fnt.Font(size = 28),padx=150, pady=50).grid(row=1, column=2)
            withdraw_input = tk.Entry(withdraw_items,borderwidth=5, font=("default", 30))
            withdraw_input.grid(row=2, column=2, padx=100, pady=100)
            withdraw_button = tk.Button(withdraw_items,text='withdraw', padx=20, pady=10, command=success_withdraw).grid(row=3, column=2)

        def send():

            def success_send():
                send_items.destroy()
                send_suuccess_massage = tk.Label(text='send successfuly', bg='#f2c65e',font = fnt.Font(size = 25), padx=280, pady=20).grid(row=0, column=2)

            general_commands_area.destroy()
            send_items = tk.LabelFrame(root, bg="#f2c65e", padx=10, pady=10, borderwidth=0)
            send_items.grid()
            send_account_number = tk.Entry(send_items, borderwidth=5, font=("default", 25))
            send_account_label = tk.Label(send_items, text='Enter the desired card number',bg="#f2c65e",font = fnt.Font(size = 28),padx=140, pady=20)
            send_amount_label = tk.Label(send_items,text="enter send amount",bg='#f2c65e',font = fnt.Font(size = 28), padx=140, pady=20)
            send_amount = tk.Entry(send_items,borderwidth=5, font=("default", 25))
            send_account_accept = tk.Button(send_items ,text='send', padx=20, pady=10, command=success_send)
            
            send_account_label.grid(row=1,columnspan=2)
            send_account_number.grid(row=2,columnspan=2)
            send_amount_label.grid(row=3,columnspan=2)
            send_amount.grid(row=4,columnspan=2)
            send_account_accept.grid(row=5,columnspan=2, pady=20)
            
        
        digit_code_area.destroy()
        general_commands_area = tk.LabelFrame(root, bg="#f2c65e", padx=10, pady=10, borderwidth=0)
        general_commands_area.grid()
        balance_btn = tk.Button(general_commands_area, text='balance', padx=65, pady=30, bg="#f2c65e", borderwidth=0, font = fnt.Font(size = 18), command=balance).grid(row=0, column=0, padx=0, pady=20)
        withdraw_btn = tk.Button(general_commands_area, text='withdraw', padx=65, pady=30, bg="#f2c65e", borderwidth=0, font = fnt.Font(size = 18), command=withdraw).grid(row=0, column=4, padx=260, pady=20)
        send_btn = tk.Button(general_commands_area, text='send', padx=65, pady=30, bg="#f2c65e", borderwidth=0, font = fnt.Font(size = 18), command=send).grid(row=2, column=0, padx=0, pady=20)
        
    else:
        print('none')
        digit_code_input.delete(0, END)
        
    
    
digit_code_area = tk.LabelFrame(root, bg="#f2c65e", borderwidth=0)
digit_code_area.grid(pady=120, padx=155)

digit_code_label = tk.Label(digit_code_area, text='please enter your digit_code', padx=40, pady=10)
digit_code_input = tk.Entry(digit_code_area, borderwidth=5, font=("default", 30))
digit_code_button = tk.Button(digit_code_area,text="next" ,padx=20,pady=10,command=root_function)

digit_code_label.grid(row=1, columnspan=2, padx=40, pady=20)
digit_code_input.grid(row=2, columnspan=2, padx=40, pady=20)
digit_code_button.grid(row=3, columnspan=2, padx=40, pady=20) 

root.mainloop()
