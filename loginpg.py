from kivymd.app import MDApp
from kivymd.uix.screen import Screen
import helpers
from kivy.lang import Builder
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton, MDRectangleFlatButton
from kivymd.uix.screen import Screen



class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = Screen()

        # username = MDTextField(
        #     pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #     size_hint_x=None, width=200)

        username = Builder.load_string(helpers.username_input)
        screen.add_widget(username)

        password = Builder.load_string(helpers.password_input)
        screen.add_widget(password)

        btn1 = MDRectangleFlatButton(text='Submit', pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn = MDFloatingActionButton(icon="android",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                     )
        btn2 = MDRectangleFlatButton(text='Cancel', pos_hint={'center_x': 0.620, 'center_y': 0.3})
        btn = MDFloatingActionButton(icon="android",
                                     pos_hint={'center_x': 0.4, 'center_y': 0.3},
                                     )

        screen.add_widget(btn1)
        screen.add_widget(btn2)

        return screen


DemoApp().run()
