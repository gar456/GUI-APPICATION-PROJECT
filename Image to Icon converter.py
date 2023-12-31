from tkinter import *

App = Tk()
App.title('Image to Icon Converter')


def open_img():
    from PIL import Image
    from tkinter import filedialog
    global img

    App.img_dir = filedialog.askopenfilename(initialdir='C:', title='Select icon image', filetypes=(
    ('PNG Images', '*.png'), ('JPG Images', '*.jpg'), ('All files', '*.*')))

    img = Image.open(App.img_dir)


def convt_img():
    from PIL import Image

    img.save(f'{ico_name.get()}.ico', format='ICO', sizes=[(ico_size.get(), ico_size.get())])

    success = Toplevel()
    success.title('Success')

    msg = Label(success, text='Conversion completed')
    msg.pack()

    success.mainloop()
def preview():
    prev = Toplevel()
    prev.title('Icon preview')
    prev.iconbitmap(f'{ico_name.get()}.ico')

    prev_lbl = Label(prev, text='Checkout your icon!')
    prev_lbl.pack()

    prev.mainloop()

chooseL = Label(App, text='Select your image:')
chooseL.grid(row=0, column=0, pady=10)

chooseB = Button(App, text='Choose', command=open_img)
chooseB.grid(row=0, column=1, pady=10)

sizeL = Label(App, text='Select a size for the icon')
sizeL.grid(row=1, column=0, pady=10)

ico_size = IntVar()
sizes_Options = [16, 24, 32, 48, 64, 128, 255]
ico_size.set(32)
size_menu = OptionMenu(App, ico_size, *sizes_Options)
size_menu.grid(row=1, column=1, pady=10)

fnameL = Label(App, text='Enter the icon name: ')
fnameL.grid(row=2, column=0, pady=10)

ico_name = Entry(App)
ico_name.grid(row=2, column=1, pady=10)

convB = Button(App, text='Convert', command=convt_img)
convB.grid(row=3, column=0, pady=10)

prevB = Button(App, text='Preview', command=preview)
prevB.grid(row=3, column=1, pady=10)

App.mainloop()
