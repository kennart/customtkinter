'''
THIS PROGRAM IS MADE BY KENNART
and MODIFIED BY PAWAN SIR (https://www.youtube.com/@CID_Official)
'''
from one import Admin
import image_utils
import customtkinter
from CTkMessagebox import CTkMessagebox


class App(customtkinter.CTk):

    customtkinter.set_appearance_mode('dark')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.admin = Admin(self)
##        self.admin.withdraw()

        self.geometry('800x500+230+90')
        self.after(1, lambda: self.state('zoomed'))
        

        self.columnconfigure(1, weight=1, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')


        self.user_name = customtkinter.CTkEntry(self, width=220,
                                                height=32, font=('Sans', 14),
                                                placeholder_text='Enter your username')
        self.user_name.grid(row=1, column=1, padx=(0, 0), pady=(0, 260))
        self.user_name.focus()


        self.user_pass = customtkinter.CTkEntry(self, width=220,
                                                height=32, show='****', font=('Sans', 14),
                                                placeholder_text='Enter your password')
        self.user_pass.grid(row=1, column=1, padx=(0, 0), pady=(0, 165))


        self.data_modify = customtkinter.CTkButton(master=self, 
                                                   text='Login',
                                              width=80, height=26, corner_radius=4,
                                              hover_color=('gray70', 'gray30'),
                                              command=self.sup)
        self.data_modify.grid(row=1, column=1, padx=(0, 0), pady=(3, 0))



        self.lock_image = customtkinter.CTkLabel(master=self, text="", 
                                            image=image_utils.get_ctk_image(icon='user', size=75))
        self.lock_image.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), sticky='s')
        



    def sup(self):
        msg = CTkMessagebox(title='Home', message='Login to Admin dashboard', 
            option_1='Yes', option_2='No')
        if msg.get() == 'Yes':
            self.withdraw()
            self.admin.deiconify()
            
        else:
            return

        

def Main():
    mm = App()
    
    mm.title('main_window')
    mm.mainloop()


if __name__ == "__main__":
    app = Main()

