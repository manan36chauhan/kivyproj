from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.tooltip import MDTooltip
from kivy_garden.mapview import MapView
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (340, 550)

helpstr = '''
#:import get_hex_from_color kivy.utils.get_hex_from_color
ScreenManager:
    WelcomeScreen:
    UsernameScreen:
    DOB:
    MainScreen:
    SecondScreen:
    MapScreen:
    RegiScreen:
    ChatScreen:
    MediScreen:
    
<MediScreen>:
    
    name : 'mediscreen'
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title : "Medicines"
            anchor_title: "center"
            md_bg_color: app.theme_cls.disabled_hint_text_color
            
        
        
    MDFloatingActionButton:
        icon:'location-exit'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '35dp'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'sscreen'


<ChatScreen>:
    name : 'chatscreen'
    MDFloatingActionButton:
        icon:'location-exit'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '35dp'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'sscreen'
            
    MDTextField:
        id:username_text_fied
        pos: self.pos
        size: self.size
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
    
    MDFloatingActionButton:
        icon:'location-exit'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '35dp'
        pos: self.pos
        
    
        
<RegiScreen>:

    name : 'regiscreen'
    FloatLayout:
        Image:
            source: "newimg.jpg"
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1
            opacity: 0.6     
    
    
    MDCard :
        orientation : 'vertical'
        size_hint : None,None
        size : 400,500
        pos_hint : {"center_x":.5,"center_y":.5}
        elevation : 15
        md_bg_color : [35/255,49/255,48/255,0.5]
        padding : 20
        spacing : 30
        MDLabel :
            text : "SIGN-UP"
            font_style : "Button"
            font_size : 40
            halign : "center"
            size_hint_y : None
            height : self.texture_size[1]
            padding_y : 30
        MDTextFieldRound :
            hint_text : "username"
            size_hint_x : None
            icon_right : "account"
            width : 270
            font_size : 20
            pos_hint : {"center_x":.5}
            normal_color : [35/255,49/255,48/255,1]
            color_active : [1,1,1,1]
        MDTextFieldRound : 
            hint_text : "user-id"
            size_hint_x : None
            icon_right : "account"
            width : 270
            font_size : 20
            pos_hint : {"center_x":.5}
            normal_color : [35/255,49/255,48/255,1]
            color_active : [1,1,1,1]
        MDTextFieldRound : 
            hint_text : "password"
            password : True
            size_hint_x : None
            icon_right : "eye-off"
            width : 270
            font_size : 20
            pos_hint : {"center_x":.5}
            normal_color : [35/255,49/255,48/255,1]
            color_active : [1,1,1,1]
        MDTextFieldRound : 
            hint_text : "confirm-password"
            size_hint_x : None
            password : True
            icon_right : "eye-off"
            width : 270
            font_size : 20
            pos_hint : {"center_x":.5}
            normal_color : [35/255,49/255,48/255,1]
            color_active : [1,1,1,1]
        MDTextFieldRound : 
            hint_text : "mobile number"
            size_hint_x : None
            icon_right : "phone"
            width : 270
            font_size : 20
            pos_hint : {"center_x":.5}
            normal_color : [35/255,49/255,48/255,1]
            color_active : [1,1,1,1]
        MDRoundFlatButton :
            text : "SIGN-UP"
            font_size : 15
            pos_hint : {"center_x":.5}
            theme_text_color : "Custom"
            text_color : [3,2,1,1]
            
        MDRoundFlatButton :
            text : "LOGIN"
            font_size : 15
            pos_hint : {"center_x":.5}
            theme_text_color : "Custom"
            text_color : [3,2,2,1]
            on_press:
                root.manager.current = 'usernamescreen'
            

    
<WelcomeScreen>:
    
    name : 'welcomescreen'

    
    ScrollView:
        MDList:
            text:"idealist"    
    FloatLayout:
        Image:
            source: "newimg.jpg"
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1
            opacity: 0.6       
    
    MDLabel:
        text:'Welcome to Emedicare'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_y':0.65}
        tooltip_text: "hi i am pyhthon"
        pos_hint: {"center_x": .5, "center_y": .5}

            
    MDFloatingActionButton:
        icon:'medical-bag'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '35dp'
        pos_hint: {'center_x':0.5,'center_y':0.32}
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'

    MDProgressBar:
        value:30
        pos_hint:{'center_y' : 0.02}
<UsernameScreen>
           
    name:'usernamescreen'
    FloatLayout:
        Image:
            source: "newimg.jpg"
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1  
            opacity: 0.5
    
    MDCard :
        orientation : 'vertical'
        size_hint : None,None
        size : 400,500
        pos_hint : {"center_x":.5,"center_y":.5}
        elevation : 15
        md_bg_color : [35/255,49/255,48/255,0.5]
        padding : 20
        spacing : 30
        MDLabel :
            text : "user-login"
            font_style : "Button"
            font_size : 35
            halign : "center"
            size_hint_y : None
            height : self.texture_size[1]
            padding_y : 30
        
        MDTextFieldRound:
            id:username_text_fied
            pos_hint: {'center_x':0.5,'center_y':0.6}
            size_hint_x : None
            width: 270
            font_size: 20
            hint_text: "color_mode = 'accent'"
            color_mode: 'accent'
            hint_text : 'username'
            helper_text: 'Required'
            normal_color : [38/255,49/255,48/255,1]
            color_active : [2,2,2,2]
            helper_text_mode: 'on_error'
            icon_right: 'account'
            icon_right_color: app.theme_cls.primary_color
            required : True
        MDTextFieldRound:
            id:password_text_fied
            pos_hint: {'center_x':0.5,'center_y':0.51}
            size_hint_x: None
            width : 270
            font_size : 20
            password: True
            hint_text : 'password'
            helper_text: 'Required'
            normal_color : [38/255,49/255,48/255,1]
            color_active : [2,2,2,2]
            helper_text_mode: 'on_error'
            icon_right: 'eye-off'
            icon_right_color: app.theme_cls.primary_color
            required : True
        MDFloatingActionButton:
            icon:'account-plus'
            md_bg_color:app.theme_cls.primary_color
            pos_hint: {'center_x':0.5,'center_y':0.35}
            user_font_size: '50sp'
            on_press: app.check_username()
        MDRoundFlatButton:
            text : 'SIGN-UP'
            icon:'account'
            font_size : 15
            md_bg_color: [38/255,49/255,48/255,1]
            user_font_size : '35dp'
            pos_hint: {'center_x':0.8,'center_y':0.35}
            on_press:
                root.manager.current = 'regiscreen'
                   
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'dob'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:60
        pos_hint: {'center_y':0.02}
                
<MapScreen>:
    name:'mapscreen'
    FloatLayout:
    MapView:
        lon: 72.1592
        lat: 21.7730
        zoom: 11
        
    MDFloatingActionButton:
        icon:'location-exit'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '35dp'
        pos_hint: {'center_x':0.85,'center_y':0.2}
        on_press:
            root.manager.current = 'sscreen'

    
<DOB>:
    name:'dob'
    FloatLayout:
        Image:
            source: "newimg.jpg"
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1 
            opacity: 0.6        
    MDLabel:
        text:'Date of Birth'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y':0.75} 
    MDRaisedButton:
        id:date_picker
        text:'Date Picker'
        user_font_size : '70sp'
        pos_hint : {'center_x':0.5,'center_y':0.6}
        on_press:
            app.show_date_picker()
    MDFloatingActionButton:
        icon:'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'usernamescreen'
    MDFloatingActionButton:
        id: second_disabled
        disabled: True
        icon:'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'mainscreen'

<MainScreen>:
    name : 'mainscreen'
    FloatLayout:
        Image:
            source: "newimg.jpg"
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1 
            opacity: 0.6        
    MDLabel:
        id:profile_name
        text:'main screen'
        font_style : 'H2'
        halign : 'center'
        pos_hint : {'center_y':0.7}
        
    MDFloatingActionButton:
        icon:'medical-bag'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '35dp'
        pos_hint: {'center_x':0.8,'center_y':0.18}
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
            
    MDFloatingActionButton:
        icon:'account'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '45dp'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press:
            root.manager.current = 'sscreen'
            root.manager.transition.direction = 'left'
        
<SecondScreen>:

    name : 'sscreen'

    MDBottomNavigation:
        panel_color: .3, .3, .3, 1

        MDBottomNavigationItem:
            name: 'home'
            text: 'Home'
            icon: 'home'
            Image:
                source: "newimg.jpg"
                allow_stretch: True
                keep_ratio: False
                size_hint: 1, 1 
                opacity: 0.2
            ScrollView:
                MDGridLayout:
                    cols:1
                    adaptive_height:True
                    padding: dp(30),dp(180)
                    spacing: dp(340)
                    
                    MDLabel:
                        text:'Home'
                        font_style: 'H4'
                        halign: 'center'
                        pos_hint: {'center_y':0.8}
                    
                    MDCard:
                        orientation: 'vertical'
                        
                        size: "280dp", "180dp"
                        pos_hint: {"center_x": .5, "center_y": .7}
                        elevation: 14
                        BoxLayout:
                            id: box
                            size_hint_y: None
                            height: dp(150)
                            FitImage:
                                source: "image.jpg"
                        MDLabel:
                            text: "Medication"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        TwoLineIconListItem:
                            text: "Find suitable medicines"
                            on_press: root.manager.current = 'mediscreen'
                            md_bg_color : [35/255,49/255,48/255,0.5]
                
                            IconLeftWidget:
                                icon: "medical-bag"


                    MDCard:
                        orientation: 'vertical'
                        
                        size: "280dp", "180dp"
                        pos_hint: {"center_x": .2, "center_y": .7}
                        elevation: 14
                        BoxLayout:
                            id: box
                            size_hint_y: None
                            height: dp(150)
                            FitImage:
                                source: "image2.jpg"
                            
                        MDLabel:
                            text: "Ask Doctor"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        TwoLineIconListItem:
                            text: "Doctors Contact info"
                            on_press: root.manager.current = 'chatscreen'
                            secondary_text:
                                "[color=%s]Mobile[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
        
                            IconLeftWidget:
                                icon: "phone"
                    

                    MDCard:
                        orientation: 'vertical'
                        size: "280dp", "180dp"
                        pos_hint: {"center_x": .2, "center_y": .3}
                        elevation: 14
                        BoxLayout:
                            id: box
                            size_hint_y: None
                            height: dp(150)
                            FitImage:
                                source: "image3.jpg"
                        MDLabel:
                            text: "Laboratories"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        TwoLineIconListItem:
                            text: "Find Laboratories"
                            on_press: root.manager.current = 'mapscreen'
                            secondary_text:
                                "[color=%s]In map[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
                            IconLeftWidget:
                                icon: "map-marker"

                    MDCard:
                        orientation: 'vertical'
                        
                        size: "280dp", "180dp"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        elevation: 14
                        BoxLayout:
                            id: box
                            size_hint_y: None
                            height: dp(150)
                            FitImage:
                                source: "image4.jpg"
        
                        MDLabel:
                            text: "Health care Products"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        TwoLineIconListItem:
                            text: "Find suitable Healthcare Products"
                            md_bg_color : [35/255,49/255,48/255,0.5]
                
                            IconLeftWidget:
                                icon: "medical-bag"
        
                          
        
                    MDCard:
                        orientation: 'vertical'
                        
                        size: "280dp", "180dp"
                        pos_hint: {"center_x": .8, "center_y": .3}
                        elevation: 14
                        BoxLayout:
                            id: box
                            size_hint_y: None
                            height: dp(150)
                            FitImage:
                                source: "heltips.jpg"
                        MDLabel:
                            text: "Health Tips"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        TwoLineIconListItem:
                            text: "(050)-123-45-67"
                            secondary_text:
                                "[color=%s]Mobile[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
        
                            IconLeftWidget:
                                icon: "phone"
        
                        TwoLineIconListItem:
                            text: "kivydevelopment@gmail.com"
                            secondary_text:
                                "[color=%s]Work[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
        
                            IconLeftWidget:
                                icon: "email"
        
        
                    MDCard:
                        orientation: 'vertical'
                        
                        size: "280dp", "180dp"
                        pos_hint: {"center_x": .8, "center_y": .5}
                        elevation: 14
                        BoxLayout:
                            id: box
                            size_hint_y: None
                            height: dp(130)
        
                            FitImage:
                                source: "gym.jpg"
        
                        MDLabel:
                            text: "Gym & Yoga"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
        
                        TwoLineIconListItem:
                            text: "(050)-123-45-67"
                            secondary_text:
                                "[color=%s]Mobile[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
        
                            IconLeftWidget:
                                icon: "phone"
        
                        TwoLineIconListItem:
                            text: "kivydevelopment@gmail.com"
                            secondary_text:
                                "[color=%s]Work[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
        
                            IconLeftWidget:
                                icon: "email"

        MDBottomNavigationItem:
            name: 'account'
            text: 'account'
            icon: 'account'
            Image:
                source: "newimg.jpg"
                allow_stretch: True
                keep_ratio: False
                size_hint: 1, 1 
                opacity: 0.2
            
        MDBottomNavigationItem:
            name: 'dashbrd'
            text: 'dashboard'
            icon: 'monitor-dashboard'
            Image:
                source: "newimg.jpg"
                allow_stretch: True
                keep_ratio: False
                size_hint: 1, 1 
                opacity: 0.2
            
            MDLabel:
                text:'Dashboard'
                font_style: 'H4'
                halign: 'center'
                pos_hint: {'center_y':0.8}
                
            MDTextField:
                id:username_text_fied
                pos_hint: {'center_x':0.5,'center_y':0.6}
                size_hint: (0.4,0.1)
                hint_text : 'username'
                helper_text: 'Required'
                helper_text_mode: 'on_error'
                icon_right: 'account'
                
        
            MDTextField:
                id:name_text_fied
                pos_hint: {'center_x':0.5,'center_y':0.5}
                size_hint: (0.4,0.1)
                hint_text : 'name'
                helper_text: 'Required'
                helper_text_mode: 'on_error'
                icon_right: 'account'
                
                
            MDRaisedButton:
                id:date_picker
                text:'Date of birth'
                user_font_size : '70sp'
                pos_hint : {'center_x':0.5,'center_y':0.4}
                on_press:
                    app.show_date_picker()
                
            MDTextField:
                id:username_text_fied
                pos_hint: {'center_x':0.5,'center_y':0.3}
                size_hint: (0.4,0.1)
                hint_text : 'Extra'
                helper_text: 'Required'
                helper_text_mode: 'on_error'
                icon_right: 'account'

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'About Us'
            icon: 'settings'
            Image:
                source: "newimg.jpg"
                allow_stretch: True
                keep_ratio: False
                size_hint: 1, 1 
                opacity: 0.2
            
            ScrollView:
                MDGridLayout:
                    cols:1
                    adaptive_height:True
                    padding: dp(30),dp(220)
                    spacing: dp(65)
                    
                    MDLabel:
                        text:'About Us'
                        font_style: 'H4'
                        pos_hint: {'center_y':0.5}
            
                    
                    MDCard:
                        id: card
                        orientation: "vertical"
                        size_hint: .6, None
                        elevation: 14
                        pos_hint: {"center_x": .5, "center_y": .5}
        
                        BoxLayout:
                            id: box
                            size_hint_y: None
                            height: dp(150)
        
                            FitImage:
                                source: "manan.jpg"
        
                        TwoLineIconListItem:
                            text: "(+91)-740-533-5998"
                            secondary_text:
                                "[color=%s]Manan G Chauhan[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
        
                            IconLeftWidget:
                                icon: "phone"
                        TwoLineIconListItem:
                            text: "chauhanmanan98@gmail.com"
                            secondary_text:
                                "[color=%s]Work[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
        
                            IconLeftWidget:
                                icon: "email"
        
        
                    MDCard:
                        id: card
                        orientation: "vertical"
                        size_hint: .5, None
                        elevation: 14
                        height: self.minimum_height
                        pos_hint: {"center_x": .5, "center_y": .8}
        
                        BoxLayout:
                            id: box
                            size_hint_y: None
                            height: dp(150)
        
                            FitImage:
                                source: "dhruv.jpg"
        
                        TwoLineIconListItem:
                            text: "+91 78020 16834"
                            secondary_text:
                                "[color=%s]Dhruv A Pandya[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
        
                            IconLeftWidget:
                                icon: "phone"
                        TwoLineIconListItem:
                            text: "dhruvpandya81@gmail.com"
                            secondary_text:
                                "[color=%s]Work[/color]" \
                                % get_hex_from_color(app.theme_cls.primary_color)
        
                            IconLeftWidget:
                                icon: "email"


   

    MDFloatingActionButton:
        icon:'medical-bag'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '35dp'
        pos_hint: {'center_x':0.8,'center_y':0.2}
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'left'

   
    
   

 
    
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Welcome to Emedicare'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation:5
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "manan.jpg"
                MDLabel:
                    text: "User"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "chauhanmanan98gmail.com"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Profile"
                                on_press:
                                    root.manager.current = 'usernamescreen'
                                    
                                IconLeftWidget:
                                    icon: "face-profile"



                            OneLineIconListItem:
                                text: "Upload"

                                IconLeftWidget:
                                    icon: "upload"


                            OneLineIconListItem:
                                text: "Logout"

                                IconLeftWidget:
                                           
'''

class RegiScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass

class MapScreen(Screen):
    pass


class UsernameScreen(Screen):
    pass


class DOB(Screen):
    pass


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass

class ChatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 2

class MediScreen(Screen):
    pass



class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(UsernameScreen(name='usernamescreen'))
sm.add_widget(DOB(name='dob'))
sm.add_widget(MainScreen(name='main_screen'))
sm.add_widget(SecondScreen(name='sscreen'))
sm.add_widget(MapScreen(name='mapscreen'))
sm.add_widget(RegiScreen(name='regisceen'))
sm.add_widget(ChatScreen(name='chatscreen'))
sm.add_widget(MediScreen(name='mediscreen'))

class NewApp(MDApp):
    def build(self):
        self.title = "E-Medicare"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        self.strng = Builder.load_string(helpstr)
        return self.strng

    def check_username(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username_text_fied.text
        self.password_text = self.strng.get_screen('usernamescreen').ids.password_text_fied.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Invalid Username', text="Please input a valid username", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

        else:
            self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False

    def close_username_dialogue(self, obj):
        self.dialog.dismiss()

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date, year=1999, month=1, day=1, )
        date_dialog.open()

    def get_date(self, date):
        self.dob = date
        self.strng.get_screen('dob').ids.date_picker.text = str(self.dob)
        self.strng.get_screen('dob').ids.second_disabled.disabled = False

        # Storing of DATA
        self.store.put('UserInfo', name=self.username_text, password=self.password_text, dob=str(self.dob))
        self.username_changer()

    def username_changer(self):
        self.strng.get_screen('mainscreen').ids.profile_name.text = f"Welcome {self.store.get('UserInfo')['name']}"

    def on_start(self):
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.username_changer()
                self.strng.get_screen('mainscreen').manager.current = 'mainscreen'

        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'


NewApp().run()
