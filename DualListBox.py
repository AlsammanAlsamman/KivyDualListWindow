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
import re
from kivy.uix.popup import Popup

class BoxItem(BoxLayout):
    ItemLabel = StringProperty()
    ItemSource = ObjectProperty()
    pressed = False
    def on_press(self):
        if not self.pressed:
            self.pressed = True
            # change color to blue
            self.ids.ItemButton.background_color = (0, 0, 1, 1)
        else:
            self.pressed = False
            # change color
            self.ids.ItemButton.background_color = (0.753, 0.753, 0.753, 1)

class DualListBox(Widget):
    # List of the items in the SourceBox for backup  
    SourceList = []
    TargetLabel = StringProperty()
    SourceLabel = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # if the user did not set the TargetLabel
        if not self.TargetLabel:
            self.TargetLabel = 'Target'
        # if the user did not set the SourceLabel
        if not self.SourceLabel:
            self.SourceLabel = 'Source'
                # add 100 buttons to the TargetBox
        # for i in range(100):
        #     self.ids.TargetBox.add_widget(BoxItem(ItemLabel=str(i),  size_hint_y=None, height=40, ItemSource=self.ids.TargetBox))
        #add '99' buttons to the TargetBox
        self.ids.TargetBox.add_widget(BoxItem(ItemLabel=str('1'),  size_hint_y=None, height=40, ItemSource=self.ids.TargetBox))

        # add 100 buttons to the SourceBox
        for i in range(100):
            self.ids.SourceBox.add_widget(BoxItem(ItemLabel=str(i),  size_hint_y=None, height=40, ItemSource=self.ids.SourceBox))
    def MoveItemToTarget(self, SourceBox, TargetBox):
        chicked = {}
        TargetItems = []
        # get all children of the TargetBox
        for child in TargetBox.children:
            TargetItems.append(child.ItemLabel)
        # get all children of the SourceBox
        for child in SourceBox.children:
            # check if the child is pressed
            # if SourceList is empty add all children to the SourceList
            if child.pressed:
                ## add the child to the chicked
                chicked[child.ItemLabel] = child
        # move the chicked to the TargetBox
        for child in chicked.values():
            # # remove the child from the SourceBox
            SourceBox.remove_widget(child)
            # if the item is already exist in the TargetBox
            if child.ItemLabel in TargetItems:
                return
            # # add the child to the TargetBox
            TargetBox.add_widget(child)
            # # change the color of the button
            child.ids.ItemButton.background_color = (0.753, 0.753, 0.753, 1)
            # # change the pressed state
            child.pressed = False
        # remove from the SourceList if it is exist
        for child in chicked.values():
            if child in self.SourceList:
                self.SourceList.remove(child)

    def MoveItemToSource(self, SourceBox, TargetBox):
        chicked = {}
        sourceItems = []
        # get all children of the SourceBox
        for child in SourceBox.children:
            sourceItems.append(child.ItemLabel)

        # get all children of the TargetBox
        for child in TargetBox.children:
            # check if the child is pressed
            if child.pressed:
                ## add the child to the chicked
                chicked[child.ItemLabel] = child
                
        # move the chicked to the SourceBox
        for child in chicked.values():
            # # remove the child from the TargetBox
            TargetBox.remove_widget(child)
            # if the item is already exist in the SourceBox
            if child.ItemLabel in sourceItems:
                return
            # # add the child to the SourceBox
            SourceBox.add_widget(child)
            # # change the color of the button
            child.ids.ItemButton.background_color = (0.753, 0.753, 0.753, 1)
            # # change the pressed state
            child.pressed = False

    def search(self, pattern, SourceBox):
        matched = {}
        # get all children of the SourceBox
        for child in SourceBox.children:
            # save the child in the SourceList
            self.SourceList.append(child)
            # check if the child label match the pattern
            if re.search(pattern, child.ItemLabel):
                ## add the child to the matched
                matched[child.ItemLabel] = child
        # remove all children from the SourceBox
        SourceBox.clear_widgets()
        # add the matched to the SourceBox
        for child in matched.values():
            SourceBox.add_widget(child)

    def UndoSearch(self, SourceBox):
        # if the SourceList is empty
        if len(self.SourceList) == 0:
            return
        # remove all children from the SourceBox
        SourceBox.clear_widgets()
        # add the SourceList to the SourceBox
        for child in self.SourceList:
            SourceBox.add_widget(child)
        # clear the SourceList
        self.SourceList = []

    def AddItemToTarget(self, TargetBox, TargetAdd):
        # if it is not empty
        newItem=""
        newItemText = TargetAdd.text
        if newItemText == '':
            popup = Popup(title='Error', content=Label(text='Please enter a value'), size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            popup.open()
            return
        else:
            # check if the item is already exist
            for child in TargetBox.children:
                if child.ItemLabel == newItemText:
                    popup = Popup(title='Error', content=Label(text='The item is already exist'), size_hint=(None, None), size=(200, 200), auto_dismiss=True)
                    popup.open()
                    return
            # create a new item
            newItem = BoxItem(ItemLabel=newItemText, size_hint_y=None, height=40, ItemSource=TargetBox)
            # add the new item to the SourceBox
            TargetBox.add_widget(newItem)
            # clear the text input
            TargetAdd.text = ''
class DualListWindow(App):

    def build(self):
        return DualListBox()

if __name__ == '__main__':
    DualListWindow().run()