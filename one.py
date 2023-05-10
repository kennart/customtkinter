import sys
import move
import customtkinter
from tkinter import NSEW
from CTkMessagebox import CTkMessagebox



class Admin(customtkinter.CTkToplevel):
    customtkinter.set_appearance_mode('dark')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('800x500+230+90')


        if sys.platform.startswith("win"):
            self.after(1, lambda: self.state("zoomed"))
        else:
            CTkMessagebox(title='Platform', message='Platform not supported for windows',
                      icon='warning')


        self.columnconfigure((1,2), weight=1, uniform='a')
        self.rowconfigure(0, weight=1, uniform='a')


        self.left_frame = customtkinter.CTkFrame(master=self, border_color='gray25', 
                                            border_width=0.8, corner_radius=8)
        self.left_frame.grid(row=0, column=0, padx=(10,0), ipadx=(10), 
                             pady=(10, 20), sticky=NSEW)
        self.left_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)



        self.data_modify = customtkinter.CTkButton(master=self.left_frame, 
                                                   text='Back to homepage',
                                              width=80, height=26, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.back_command)
        self.data_modify.grid(row=0, column=0, padx=(0, 0), pady=(3, 0))


    def back_command(self):
        msg = CTkMessagebox(title='Home', message='Are you sure togo home', 
          option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            self.withdraw()
            move.App()
        else:
            return



# def main():
#     root = customtkinter.CTk()
#     aa = Admin(root)
#     aa.title('Admin Panel')
#     aa.geometry('500x500')
#     aa.mainloop()

# if __name__ == '__main__':
#     main()