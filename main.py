from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from datetime import date

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDLabel:
        text: "SCHOOL OF AYGODA"
        text: "Grade 11B Group project"
        text: "Group Members: Kalkidan, Temesgn, Feven, Bethelhem Ketema, Yonatan, Edlawit"
              
        halign: 'center'
        size_hint_y: None
        height: "48dp"
        theme_text_color: "Primary"
        pos_hint: {"top": 1}

    MDBoxLayout:
        orientation: 'horizontal'
        padding: "10dp"

        MDLabel:
            text: "Day:"
            size_hint_x: None
            width: "50dp"

        MDTextField:
            id: day_field
            hint_text: "Enter Day"
            size_hint_x: None
            width: "100dp"

    MDBoxLayout:
        orientation: 'horizontal'
        padding: "10dp"

        MDLabel:
            text: "Month:"
            size_hint_x: None
            width: "50dp"

        MDTextField:
            id: month_field
            hint_text: "Enter Month"
            size_hint_x: None
            width: "100dp"

    MDBoxLayout:
        orientation: 'horizontal'
        padding: "10dp"

        MDLabel:
            text: "Year:"
            size_hint_x: None
            width: "50dp"

        MDTextField:
            id: year_field
            hint_text: "Enter Year"
            size_hint_x: None
            width: "100dp"

    MDRaisedButton:
        text: "Calculate Age"
        pos_hint: {"center_x": .5}
        on_release: app.calculate_age()

    MDLabel:
        id: result_label
        halign: 'center'
'''


class AgeCalculatorApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def calculate_age(self):
        today = date.today()
        birth_day = int(self.root.ids.day_field.text)
        birth_month = int(self.root.ids.month_field.text)
        birth_year = int(self.root.ids.year_field.text)

        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

        self.root.ids.result_label.text = f"Your age is: {age}"


if __name__ == '__main__':
    AgeCalculatorApp().run()
