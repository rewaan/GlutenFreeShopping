from kivy.app import App
from kivy.uix.stacklayout import StackLayout


class Search(StackLayout):
    pass


class SearchApp(App):
    def build(self):
        self.title = 'GlutenFreeShoppingApp'
        return Search()


if __name__ == '__main__':
    SearchApp().run()
