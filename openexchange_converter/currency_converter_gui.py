from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import currency_converter as ccv


def get_formatted_rate(rate):
    formatted_rate = ccv.get_currency_rate(rate.get().split(' ', 1)[0])
    return formatted_rate


def convert(amount, to_curr, from_curr):
    from_curr_amount = amount.get()
    to_curr_rate = get_formatted_rate(to_curr)
    from_curr_rate = get_formatted_rate(from_curr)
    to_curr_final_value = ccv.convert_currencies(from_curr_amount,
                                                 to_curr_rate,
                                                 from_curr_rate
                                                 )
    messagebox.showinfo('Conversion',
                        '{} {} = {:.2f} {}'.format(amount.get(),
                                                   from_curr.get(),
                                                   to_curr_final_value,
                                                   to_curr.get()
                                                   )
                        )


if __name__ == '__main__':
    window = Tk()
    window.title('OpenExchange Currency Converter')
    window.geometry('450x200')
    values_dict = ccv.get_valid_currencies()
    values = [[k, v] for k, v in values_dict.items()]

    lbl_amount = Label(window, text='Amount')
    lbl_amount.grid(column=0, row=0)
    txt_amount = Entry(window, width=10)
    txt_amount.grid(column=0, row=1)

    lbl_from_curr = Label(window, text='From Currency')
    lbl_from_curr.grid(column=1, row=0)
    combo_from_curr = Combobox(window)
    combo_from_curr['values'] = sorted(values)
    combo_from_curr.current(1)
    combo_from_curr.grid(column=1, row=1)

    lbl_to_curr = Label(window, text='To Currency')
    lbl_to_curr.grid(column=2, row=0)
    combo_to_curr = Combobox(window)
    combo_to_curr['values'] = sorted(values)
    combo_to_curr.current(1)
    combo_to_curr.grid(column=2, row=1)

    btn = Button(window,
                 text='Convert',
                 command=lambda: (convert(amount=txt_amount,
                                          to_curr=combo_to_curr,
                                          from_curr=combo_from_curr
                                          )
                                  )
                 )

    btn.grid(column=1, row=9)

    window.mainloop()
