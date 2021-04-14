navigation_helper = """
ScreenManager:

    MenuScreen:
    ProfileScreen:
    ExtraScreen:
    
    
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'profile'
        
    
        
    MDLabel:
        text: 'Hello Tap On login to Go further'
        pos_hint: {'center_x':0.7,'center_y':0.3}
        
    
        
<ProfileScreen>:
    name: 'profile'
    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Python'
            icon: 'language-python'

    MDLabel:
        text: 'Welcome to Profile page'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        
    MDRectangleFlatButton:
        text: 'Extra'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'extra'

<ExtraScreen>:
    name: 'extra'
    MDLabel:
        text: 'extra page'
        pos_hint: {'center_x':0.8,'center_y':0.1}

    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Welcome to Emedicare'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
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
                    source: "mine.jpg"
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

                                IconLeftWidget:
                                    icon: "face-profile"



                            OneLineIconListItem:
                                text: "Upload"

                                IconLeftWidget:
                                    icon: "upload"


                            OneLineIconListItem:
                                text: "Logout"

                                IconLeftWidget:
                                    icon: "logout"
                                
                                    
   
    
    MDTextField:
        hint_text: "Enter Username"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}

        size_hint_x:None
        width:300

    MDTextField:
        hint_text: "Enter Password"
        helper_text: "or click on forgot Password"
        helper_text_mode: "on_focus"
        icon_right: "onepassword"
        password: True
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300

    MDRectangleFlatButton:
        text: "Submit"
        font_size: "18sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: show_data

    MDRectangleFlatButton:
        text: "Cancel"
        font_size: "18sp"
        pos_hint: {'center_x': 0.750, 'center_y': 0.4}
        on_press: root.manager.current = 'menu'
        

            
                    
"""





