from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
#import random






class DemoApplication(MDApp):

    def build(self):
        global screen
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "700"



        button1 = MDRectangleFlatButton(text="button1",pos_hint={'center_x':0.5, 'center_y':0.3},on_release=self.btnfc)
        button2 = MDRectangleFlatButton(text="button2",pos_hint={'center_x':0.5, 'center_y':0.5})
        button3 = MDRectangleFlatButton(text="button3",pos_hint={'center_x':0.5, 'center_y':0.7},on_release=self.btn)

        screen.add_widget(button1)
        screen.add_widget(button2)
        screen.add_widget(button3)

        return screen


    def btnfc(self,obj):
        button4 = MDRectangleFlatButton(text="button4",pos_hint={'center_x':0.5, 'center_y':0.9})
        screen.add_widget(button4)
        print("pressed")

    def btn(self,obj):
        button5 = MDRectangleFlatButton(text="button5",pos_hint={'center_x':0.5, 'center_y':0.1})

        screen.add_widget(button5)







DemoApplication().run()
