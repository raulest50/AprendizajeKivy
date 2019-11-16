import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.event import EventDispatcher # para manejar eventos o listeners de los widgets y eventos temporizados

from cryptography.fernet import Fernet




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

class EncriptarApp(App):

    def build(self):
        pass


if __name__ == '__main__':
    EncriptarApp().run()


#C:\Users\Raul Alzate\PycharmProjects\venvKivy\share\kivy-examples\demo\kivycatalog