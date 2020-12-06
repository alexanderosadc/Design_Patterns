from abc import ABC, abstractmethod


class ScreenRenderer(ABC):

    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, dict_with_options):
        pass


class UIRenderer(ScreenRenderer):

    def handle(self, dict_with_options):
        if 'screen_resolution' in dict_with_options:
            self._screen_resolution = dict_with_options['screen_resolution']
            print('UI Renderer')

        if self._successor is not None:
            self._successor.handle(dict_with_options)


class ButtonsRenderer(ScreenRenderer):

    def handle(self, dict_with_options):
        if 'position_of_button_x' in dict_with_options and \
                'position_of_button_y' in dict_with_options:
            self._position_of_button_x = dict_with_options['position_of_button_x']
            self._position_of_button_y = dict_with_options['position_of_button_y']
            print('Button Renderer')

        if self._successor is not None:
            self._successor.handle(dict_with_options)

class ButtonTextRenderer(ButtonsRenderer):

    def handle(self, dict_with_options):
        if 'text' in dict_with_options:
            self._button_text = dict_with_options['text']

        if 'font_family' in dict_with_options:
            self._font_family = dict_with_options['font_family']
        else:
            self._font_family = 'Arial'

        if 'text_size' in dict_with_options:
            self._text_size = dict_with_options['text_size']
        else:
            self._text_size = 2

        print('Button Text Renderer')
        if self._successor is not None:
            self._successor.handle(dict_with_options)