import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.event import EventDispatcher # para manejar eventos o listeners de los widgets y eventos temporizados


""" this is our custom root widget"""
class LoginScreen(GridLayout):

    # method override to add widgets and define behavior
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Nombre de Usuario', font_size=40))
        self.username = TextInput(multiline=False, font_size=40)
        self.add_widget(self.username)
        self.add_widget(Label(text='Contraseña',font_size=40))
        self.password = TextInput(multiline=False, font_size=40)
        self.add_widget(self.password)
        self.b1 = Button(text='evento 1', font_size=40)
        self.add_widget(self.b1)
        self.b2 = Button(text='evento 2', font_size=40)
        self.add_widget(self.b2)

        self.b1.bind(on_press=self.eventoX)

    """
    funcion que limpia el campo de texto 
    """
    def eventoX(self, obj):
        self.username.text=''




"""
clase para manejar eventos personalizados
"""
class MyEventDispatcher(EventDispatcher):

    def __init__(self):
        self.register_event_type('evento1')
        self.register_event_type('evento2')
        super(MyEventDispatcher, self).__init__(**kwargs)

    def evento1(self, *args):
        print('nothing')

    def evento2(self, *args):
        print('also nothing')

"""
se requiere que la clase base de tu apicacion herede de la clase App de kivy
"""
class MyApp(App):

    def build(self):
        return LoginScreen()



if __name__ == '__main__':
    MyApp().run()