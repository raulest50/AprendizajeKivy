import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.event import EventDispatcher # para manejar eventos o listeners de los widgets y eventos temporizados

from cryptography.fernet import Fernet


""" this is our custom root widget"""
class LoginScreen(GridLayout):

    # method override to add widgets and define behavior
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.row_default_height = 100
        self.row_force_default = True
        self.Button_randkey = Button(text='Generar', font_size=30)
        self.TextIn_randkey = TextInput(multiline=False, font_size=30, size_hint_x=None, width=700)
        self.Button_backUp = Button(text='BackUp', font_size=30)
        self.TextIn_route = TextInput(multiline=False, font_size=30, size_hint_x=None, width=700)

        self.add_widget(self.Button_randkey)
        self.add_widget(self.TextIn_randkey)
        self.add_widget(self.Button_backUp)
        self.add_widget(self.TextIn_route)

        self.Button_randkey.bind(on_press=self.ActionButton_randkey)
        self.Button_backUp.bind(on_press=self.ActionButton_backUp)

    def ActionButton_randkey(self, obj):
        self.TextIn_randkey._set_text(Fernet.generate_key())

    def ActionButton_backUp(self, obj):
        key = self.TextIn_randkey.text
        ruta = self.TextIn_route.text
        file = open(ruta, 'rb')
        contenido = file.read()
        #encoded = contenido.encode()
        f = Fernet(key)
        encri = f.encrypt(contenido)
        encriFile = open('encri.txt', 'wb')
        encriFile.write(encri)
        encriFile.close()

        decriFile = open('dencri.txt', 'wb')
        decriFile.write(f.decrypt(encri))
        decriFile.close()
        print(f.decrypt(encri))


"""
se requiere que la clase base de tu apicacion herede de la clase App de kivy
"""


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
