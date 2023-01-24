# imports
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
import math

from pygame import display


# set app size
Window.size = (800, 300)

# define main class
class MainApp(MDApp):
    ang_mod = ''
    answer = ''
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.accent_palette = 'Blue'
        return Builder.load_file('design.kv')
    def equals(self):
        # get what on screen
        prior = self.root.ids.my_label.text

        # for math error
        try:
            # evaluate it
            answer = eval(prior)
            # update screen
            self.root.ids.my_label.text = str(answer)
        except:
            self.root.ids.my_label.text = f'Error'    
    def setting(self,instance, mod):
        self.ang_mod = mod
        # deactivate other mod
        if mod =='Rad':
            self.root.ids.rad_mod.md_bg_color= (123/255, 192/255, 67/255,1)
            self.root.ids.deg_mod.md_bg_color= (254/255, 138/255, 113/255,1)
        if mod =='Deg':
            self.root.ids.rad_mod.md_bg_color= (254/255, 138/255, 113/255,1)
            self.root.ids.deg_mod.md_bg_color= (123/255, 192/255, 67/255,1)
    # clear screen
    def clear(self):
        self.root.ids.my_label.text = '0'
    # show last answer
    def show_answer(self):
        if self.answer == '':
            # default value
            self.root.ids.my_label.text = '0'
        else:
            # show answer
            self.root.ids.my_label.text = self.answer    
    # show on screen
    def display_fun(self, instance, butt):
        # get what on screen
        prior = self.root.ids.my_label.text
        # no zeros on left
        if prior =='0':
            prior=''
        # conditional block for display
        if butt == 'x!':
            self.root.ids.my_label.text = f'{prior}!'

        elif butt == '(':
            self.root.ids.my_label.text = f'{prior}('

        elif butt == ')':
            self.root.ids.my_label.text = f'{prior})'

        elif butt == '%':
            self.root.ids.my_label.text = f'{prior}%'

        elif butt == 'Inv':
            self.root.ids.my_label.text = f'{prior}1/'

        elif butt == 'sin':
            self.root.ids.my_label.text = f'{prior}sin('

        elif butt == 'ln':
            self.root.ids.my_label.text = f'{prior}ln('

        elif butt == '7':
            self.root.ids.my_label.text = f'{prior}7'

        elif butt == '8':
            self.root.ids.my_label.text = f'{prior}8'

        elif butt == '9':
            self.root.ids.my_label.text = f'{prior}9'

        elif butt == '÷':
            self.root.ids.my_label.text = f'{prior}/'

        elif butt == 'π':
            if prior =='':
                self.root.ids.my_label.text = f'{prior}{round(math.pi,2)}'    
            else:    
                self.root.ids.my_label.text = f'{prior}*{round(math.pi,2)}'

        elif butt == 'cos':
            self.root.ids.my_label.text = f'{prior}cos('

        elif butt == 'log':
            self.root.ids.my_label.text = f'{prior}log('

        elif butt == '4':
            self.root.ids.my_label.text = f'{prior}4'

        elif butt == '5':
            self.root.ids.my_label.text = f'{prior}5'

        elif butt == '6':
            self.root.ids.my_label.text = f'{prior}6'

        elif butt == 'x':
            self.root.ids.my_label.text = f'{prior}*'

        elif butt == 'e':
            self.root.ids.my_label.text = f'{prior}e'
                        
        elif butt == 'tan(':
            self.root.ids.my_label.text = f'{prior}tan('

        elif butt == '√':
            self.root.ids.my_label.text = f'{prior}√'
                        
        elif butt == '1':
            self.root.ids.my_label.text = f'{prior}1'
                        
        elif butt == '2':
            self.root.ids.my_label.text = f'{prior}2'

        elif butt == '3':
            self.root.ids.my_label.text = f'{prior}3'

        elif butt == '-':
            self.root.ids.my_label.text = f'{prior}-'
            
        elif butt == 'Exp':
            self.root.ids.my_label.text = f'{prior}Exp'

        elif butt == '^':
            self.root.ids.my_label.text = f'{prior}**'

        elif butt == '0':
            self.root.ids.my_label.text = f'{prior}0'
            
        elif butt == '.':
            self.root.ids.my_label.text = f'{prior}.'

        elif butt == '+':
            self.root.ids.my_label.text = f'{prior}+'

            
            
                                    
# run main app
if __name__ == '__main__':
    MainApp().run()