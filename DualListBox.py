#!/usr/bin/python

############################################## About Author #########################################
# Created by: Alsamman M. Alsamman                                                                  #
# Emails: smahmoud [at] ageri.sci.eg or A.Alsamman [at] cgiar.org or SammanMohammed [at] gmail.com  #
# License: MIT License - https://opensource.org/licenses/MIT                                        #
# Disclaimer: The script comes with no warranty, use at your own risk                               #
# This script is not intended for commercial use                                                    #
#####################################################################################################

# kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
# Widget
from kivy.uix.widget import Widget
# scrollview
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

class BoxItem(BoxLayout):
    ItemLabel = StringProperty()
    SubAdd = StringProperty()
    pass

class DualListBox(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # add 100 buttons to the TargetBox
        for i in range(100):
            self.ids.TargetBox.add_widget(BoxItem(ItemLabel=str(i), SubAdd="+", size_hint_y=None, height=40))
        # add 100 buttons to the SourceBox
        for i in range(100):
            self.ids.SourceBox.add_widget(BoxItem(ItemLabel=str(i), SubAdd="+", size_hint_y=None, height=40))


class DualListWindow(App):
    def build(self):
        return DualListBox()

if __name__ == '__main__':
    DualListWindow().run()