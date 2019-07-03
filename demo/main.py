from kivy.app         import App
from kivy.core.window import Window
from kivy.clock       import Clock
from kivy.uix.widget  import Widget
from kivy.uix.image   import Image

from pix2pix import Pix2PixConverter


class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.size = self.texture_size


class NeuralImage(Sprite):
    def __init__(self, model=None, **kwargs):
        super(NeuralImage, self).__init__(**kwargs)
        self.model = model
        self.original_source = self.source

    def convert(self):
        path_of_synthesized_image = self.model.convert(self.source)
        self.source = path_of_synthesized_image


class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()

        # Add background image, set window size
        self.background = Sprite(source='images/background.jpg')
        self.size = self.background.size
        self.add_widget(self.background)

        # Initialize model
        from options.test_options import TestOptions
        opt = TestOptions().parse(save=False)
        self.model = Pix2PixConverter(opt)

        # Create player
        self.player = NeuralImage(source='images/test_pose.jpg', model=self.model)
        self.add_widget(self.player)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, *ignore):
        pass


class GameApp(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game


if __name__ == '__main__':
    GameApp().run()
