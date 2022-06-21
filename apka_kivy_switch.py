from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder

kvstring = Builder.load_string ('''
<MyLayout>:
    BoxLayout:
        orientation: "horizontal"
        size: root.width, root.height

    Label:
        id: my_label
        font_size: 30
        color: '#00FFCE'
        text: ""

    Switch:
        id: my_switch
        active: True
        disabled: False
        font_size: 30
        on_active: root.switch_click(self, self.active)
''')




# Designate Our .kv design file
#Builder.load_file('switch.kv')


def function_1(income):

    word='CAR'+' '+income
    return (word)

def function_2(income):

    word='HOUSE'+' '+income
    return (word)


class MyLayout(Widget):
    def switch_click(self, switchObject, switchValue):
        print(switchValue)
        return (switchValue)


class SayHello(App):

    def build(self):

        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        #self.window.rows = 10
        self.window.size_hint = (0.9, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}




        # label widget
        self.greeting = Label(
                        text= "Input text to process",
                        font_size= 30,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(

                    multiline= False,
                    padding_y= (10,10),
                    size_hint= (1, 0.5)
                    )
        #print('to jest user',self.user)
        self.window.add_widget(self.user)

        self.switch=MyLayout()
        self.window.add_widget(self.switch)



        self.greeting2 = Label(
            text="Input number",
            font_size=30,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting2)

        self.user2 = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )

        self.window.add_widget(self.user2)


        # button widget
        self.button = Button(
                      text= "Process",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',

                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)



        return self.window



    def callback(self, instance):
        # change label text to "Hello + user name!"

        income=str(self.user.text)
        if bool(self.switch==True):
            outcome=function_1(income)
        else:
            outcome = function_2(income)

        self.greeting.text = "Processed text"
        self.user.text=outcome





# run Say Hello App Calss
if __name__ == "__main__":

    SayHello().run()


