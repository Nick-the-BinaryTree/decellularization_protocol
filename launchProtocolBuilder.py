# https://www.tutorialspoint.com/simple-registration-form-using-python-tkinter

import os
import subprocess
from tkinter import *

FILE_NAME = 'decellularization_protocol.ino'
MILLISECOND_CONVERSION = '000'
PADDING_Y = 12
TITLE_FONT = font=('Helvetica', 14, 'bold')


window=Tk()
window.title("Decellularization Protocol")
window.geometry('640x800')

Label(window, text='Note: times are in seconds and lengths are in centimeters.').grid(row=0, column=0)

Label(window, text="Step Four", font=TITLE_FONT).grid(row=1, column=0, pady=PADDING_Y)
Label(window, text="Number of hypertonic buffer washes:").grid(row=2, column=0)
stepFourInput1 = Entry(window, textvariable=StringVar(window, '2'))
stepFourInput1.grid(row=2, column=1)
Label(window, text="Hypertonic buffer wash duration:").grid(row=3, column=0)
stepFourInput2 = Entry(window, textvariable=StringVar(window, '600'))
stepFourInput2.grid(row=3, column=1)

Label(window, text="Step Five", font=TITLE_FONT).grid(row=4, column=0, pady=PADDING_Y)
Label(window, text="Nuclease solution treatment duration:").grid(row=5, column=0)
stepFiveInput1 = Entry(window, textvariable=StringVar(window, '14400'))
stepFiveInput1.grid(row=5, column=1)

Label(window, text="Step Six", font=TITLE_FONT).grid(row=6, column=0, pady=PADDING_Y)
Label(window, text="Hypotonic Tris-HCl wash duration:").grid(row=7, column=0)
stepSixInput1 = Entry(window, textvariable=StringVar(window, '72000'))
stepSixInput1.grid(row=7, column=1)

Label(window, text="Step Seven", font=TITLE_FONT).grid(row=8, column=0, pady=PADDING_Y)
Label(window, text="Triton X-100 treatment duration:").grid(row=9, column=0)
stepSevenInput1 = Entry(window, textvariable=StringVar(window, '86400'))
stepSevenInput1.grid(row=9, column=1)

Label(window, text="Step Eight", font=TITLE_FONT).grid(row=10, column=0, pady=PADDING_Y)
Label(window, text="dH20 wash duration:").grid(row=11, column=0)
stepEightInput1 = Entry(window, textvariable=StringVar(window, '259200'))
stepEightInput1.grid(row=11, column=1)
Label(window, text="dH20 rewash interval:").grid(row=12, column=0)
stepEightInput2 = Entry(window, textvariable=StringVar(window, '43200'))
stepEightInput2.grid(row=12, column=1)
Label(window, text='Ex: entering "259200" and "43200" means').grid(row=13, column=0)
Label(window, text='"wash once every 12 hrs for 3 days."').grid(row=14, column=0)

Label(window, text="Step Nine", font=TITLE_FONT).grid(row=15, column=0, pady=PADDING_Y)
Label(window, text="Peracetic acid sterilization duration:").grid(row=16, column=0)
stepNineInput1 = Entry(window, textvariable=StringVar(window, '14400'))
stepNineInput1.grid(row=16, column=1)

Label(window, text="Step Ten", font=TITLE_FONT).grid(row=17, column=0, pady=PADDING_Y)
Label(window, text="Number of PBS and dH20 washes:").grid(row=18, column=0)
stepTenInput1 = Entry(window, textvariable=StringVar(window, '2'))
stepTenInput1.grid(row=18, column=1)
Label(window, text="PBS and dH20 wash duration:").grid(row=19, column=0)
stepTenInput2 = Entry(window, textvariable=StringVar(window, '60'))
stepTenInput2.grid(row=19, column=1)

Label(window, text="Cross-Protocol", font=TITLE_FONT).grid(row=20, column=0, pady=PADDING_Y)
Label(window, text="Height to submerge tissue:").grid(row=21, column=0)
crossProtocolInput1 = Entry(window, textvariable=StringVar(window, '120'))
crossProtocolInput1.grid(row=21, column=1)
Label(window, text="Height of container:").grid(row=22, column=0)
crossProtocolInput2 = Entry(window, textvariable=StringVar(window, '120'))
crossProtocolInput2.grid(row=22, column=1)


def generate():
    def declare_var(name, value):
        return 'const unsigned long ' + name + ' = ' + value + ';\n'

    new_file = open('decellularization_protocol.ino', 'w')
    new_file.write(declare_var('NUMBER_HYPERTONIC_BUFFER_WASHES', stepFourInput1.get()))
    new_file.write(declare_var('HYPERTONIC_BUFFER_WASH_DURATION', stepFourInput2.get()+MILLISECOND_CONVERSION))
    new_file.write(declare_var('NUCLEASE_SOLUTION_TREATMENT_DURATION', stepFiveInput1.get()+MILLISECOND_CONVERSION))
    new_file.write(declare_var('HYPOTONIC_TRIS_HCL_WASH_DURATION', stepSixInput1.get()+MILLISECOND_CONVERSION))
    new_file.write(declare_var('TRITON_X_100_TREATMENT_DURATION', stepSevenInput1.get()+MILLISECOND_CONVERSION))
    new_file.write(declare_var('dH20_WASH_DURATION', stepEightInput1.get()+MILLISECOND_CONVERSION))
    new_file.write(declare_var('dH20_REWASH_INTERVAL', stepEightInput2.get()+MILLISECOND_CONVERSION))
    new_file.write(declare_var('PERACITIC_ACID_STERILIZATION_DURATION', stepNineInput1.get()+MILLISECOND_CONVERSION))
    new_file.write(declare_var('NUMBER_PBS_AND_dH20_WASHES', stepTenInput1.get()))
    new_file.write(declare_var('PBS_AND_dH20_WASH_DURATION', stepTenInput2.get()+MILLISECOND_CONVERSION))
    new_file.write(declare_var('HEIGHT_TO_SUBMERGE_TISSUE', crossProtocolInput1.get()))
    new_file.write(declare_var('CONTAINER_HEIGHT', crossProtocolInput2.get()))

    template_file = open(os.path.join('resources', 'template_'+FILE_NAME))
    new_file.write(template_file.read())
    new_file.close()
    template_file.close()


def upload():
    generate()
    print(subprocess.check_output(['arduino', '--upload', FILE_NAME, '--port', '/dev/ttyUSB*']))


Button(window, text="Generate Script", command=generate).grid(row=23, column=0, pady=PADDING_Y)
Button(window, text="Run on Arduino", command=upload).grid(row=23, column=1, pady=PADDING_Y)

window.mainloop()
