import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # initialize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set the number of columns
        self.cols = 2

        # add widgets
        self.add_widget(Label(text = "Name: "))
        # add input boxes
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        # add widgets
        self.add_widget(Label(text = "Gender: "))
        # add input boxes
        self.gender = TextInput(multiline = False)
        self.add_widget(self.gender)

        # add widgets
        self.add_widget(Label(text = "Age: "))
        # add input boxes
        self.age = TextInput(multiline = False)
        self.add_widget(self.age)

        # create submit button
        self.submit = Button(text = "Submit", font_size = 32)
        # bind the button
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    #
    def press(self, instance):
        name = self.name.text
        gender = self.gender.text
        age = self.age.text

        # print(f'Hello {name}, you are {gender}, and your age is {age}!')
        # print the final information onto the GUI instead of terminal
        self.add_widget(Label(text = f'Hello {name}, you are {gender}, and your age is {age}!'))

        # clear the input boxes upon submission
        self.name.text = ""
        self.gender.text = ""
        self.age.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()
