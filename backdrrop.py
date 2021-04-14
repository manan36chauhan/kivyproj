from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.factory import Factory
from kivymd.uix.label import MDLabel

from kivymd.app import MDApp


Builder.load_string(
    '''
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget


<ItemBackdropFrontLayer@TwoLineAvatarListItem>

    icon: "android"

    IconLeftWidget:
        icon: root.icon


<MyBackdropFrontLayer@ItemBackdropFrontLayer>
    backdrop: None
    text: "Lower the front layer"
    secondary_text: " by 30 %"
    icon: "transfer-down"
    on_press: root.backdrop.open(-Window.height / 2)
    pos_hint: {"top": 1}
    _no_ripple_effect: True

    
<MyBackdropBackLayer@Image>
    size_hint: .8, .8
    source: "gym.jpg"
    pos_hint: {"center_x": .5, "center_y": .6}
'''
)

# Usage example of MDBackdrop.
Builder.load_string(
    '''
<Emedicare>
    
    MDFlatButton:
        text: 'MDFLATBUTTON'
        theme_text_color: 'Custom'
        text_color: 0, 0, 1, 1
        pos_hint_x: 250
        
    MDToolbar:
        title: 'Bottom Navigation'
        md_bg_color:.2,.2,.2,1
        specific_text_color:1,1,1,1
        
    
        
    MDLabel:
        text: 'Python'
        
    
    MDBackdrop:
        id: backdrop
        left_action_items: [['menu', lambda x: self.open()]]
        title: "Emedicare"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Menu:"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer
        MDLabel:
            text: 'Python'
        
        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
'''
)


class Emedicare(Screen):
    pass


class TestBackdrop(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Emedicare()


TestBackdrop().run()
