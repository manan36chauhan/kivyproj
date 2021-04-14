import kivy
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.app import App
from kivy.graphics import Line


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:

            Color(1, 0, 0, .5, mode='rgba')
            self.rect = Rectangle(pos=(300,300), size=(100,100))


    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        print("Mouse move", touch)


class Myapp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    Myapp().run()
