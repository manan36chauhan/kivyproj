username_input = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    
    size_hint_x:None
    width:300
"""
password_input = """
MDTextField:
    hint_text: "Enter Password"
    helper_text: "or click on forgot Password"
    helper_text_mode: "on_focus"
    icon_right: "android"
    password: True
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""