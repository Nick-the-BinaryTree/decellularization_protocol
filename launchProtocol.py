# https://www.tutorialspoint.com/simple-registration-form-using-python-tkinter

import os
import subprocess
from tkinter import *


TITLE_FONT = font=('Helvetica', 14, 'bold')
PADDING_Y = 12

window=Tk()
window.title("Decellularization Protocol")
window.geometry('640x800')

Label(window, text='Note: all times are in seconds (ex: 3 minutes is "180")').grid(row=0, column=0)

Label(window, text="Step Four", font=TITLE_FONT).grid(row=1, column=0, pady=PADDING_Y)
Label(window, text="Number of hypertonic buffer washes:").grid(row=2, column=0)
stepFourInput1 = Entry(window)
stepFourInput1.grid(row=2, column=1)
Label(window, text="Hypertonic buffer wash duration:").grid(row=3, column=0)
stepFourInput2 = Entry(window)
stepFourInput2.grid(row=3, column=1)

Label(window, text="Step Five", font=TITLE_FONT).grid(row=4, column=0, pady=PADDING_Y)
Label(window, text="Nuclease solution treatment duration:").grid(row=5, column=0)
stepFiveInput1 = Entry(window)
stepFiveInput1.grid(row=5, column=1)

Label(window, text="Step Six", font=TITLE_FONT).grid(row=6, column=0, pady=PADDING_Y)
Label(window, text="Hypotonic Tris-HCl wash duration:").grid(row=7, column=0)
stepSixInput1 = Entry(window)
stepSixInput1.grid(row=7, column=1)

Label(window, text="Step Seven", font=TITLE_FONT).grid(row=8, column=0, pady=PADDING_Y)
Label(window, text="Triton X-100 treatment duration:").grid(row=9, column=0)
stepSevenInput1 = Entry(window)
stepSevenInput1.grid(row=9, column=1)

Label(window, text="Step Eight", font=TITLE_FONT).grid(row=10, column=0, pady=PADDING_Y)
Label(window, text="dH20 wash duration:").grid(row=11, column=0)
stepEightInput1 = Entry(window)
stepEightInput1.grid(row=11, column=1)
Label(window, text="dH20 rewash interval:").grid(row=12, column=0)
stepEightInput2 = Entry(window)
stepEightInput2.grid(row=12, column=1)
Label(window, text='Ex: entering "259200" and "43200" means').grid(row=13, column=0)
Label(window, text='"wash once every 12 hrs for 3 days."').grid(row=14, column=0)

Label(window, text="Step Nine", font=TITLE_FONT).grid(row=15, column=0, pady=PADDING_Y)
Label(window, text="Peracetic acid sterilization duration:").grid(row=16, column=0)
stepNineInput1 = Entry(window)
stepNineInput1.grid(row=16, column=1)

Label(window, text="Step Ten", font=TITLE_FONT).grid(row=17, column=0, pady=PADDING_Y)
Label(window, text="PBS and dH20 wash duration:").grid(row=18, column=0)
stepTenInput1 = Entry(window)
stepTenInput1.grid(row=18, column=1)
Label(window, text="Number of PBS and dH20 washes:").grid(row=19, column=0)
stepTenInput2 = Entry(window)
stepTenInput2.grid(row=19, column=1)

Label(window, text="Cross-Protocol", font=TITLE_FONT).grid(row=20, column=0, pady=PADDING_Y)
Label(window, text="Time to fill container:").grid(row=21, column=0)
crossProtocolInput1 = Entry(window)
crossProtocolInput1.grid(row=21, column=1)
Label(window, text="Time to empty container:").grid(row=22, column=0)
crossProtocolInput2 = Entry(window)
crossProtocolInput2.grid(row=22, column=1)


def submit():
    def declare_var(name, value):
        return 'const unsigned int ' + name + ' = ' + value + ';'

    new_file = open('decellularization_protocol.ino', 'w')
    new_file.write(declare_var('NUMBER_HYPERTONIC_BUFFER_WASHES', stepFourInput1.get()))
    new_file.write('\n')

    template_file = open(os.path.join('resources', 'template_decellularization_protocol.ino'))
    new_file.write(template_file.read())
    new_file.close()
    template_file.close()
    # print(subprocess.check_output(['ls']))

Button(window, text="Submit", command=submit).grid(row=23, column=0, pady=PADDING_Y)
window.mainloop()
