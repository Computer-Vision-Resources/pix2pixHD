from kivy.app         import App
from kivy.core.window import Window
from kivy.clock       import Clock
from kivy.uix.widget  import Widget
from kivy.uix.image   import Image

from converter import Pix2PixConverter
import pickle

with open("table-tennis-data/densepose_result.pkl", "rb") as f:
    dp = pickle.load(f , encoding="latin1")
    print(dp[0])

pkl_root = "/Projects/esper_haotian/esper/app/data/image/densepose_HW/"
data_root = "table-tennis-data/JZ/test_A/"
image = "densepose_65_34779_JZ.jpg"
initial_image = data_root + image_path


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

    def on_touch_down(self, *ignore):
        self.convert()



class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()

        # Add background image, set window size
        self.background = Sprite(source='game_assets/background.jpg')
        self.size = self.background.size
        self.add_widget(self.background)

        # Initialize model
        self.model = Pix2PixConverter()

        # Create player
        initial_image = "game_assets/test_pose.jpg"
        self.player = NeuralImage(source=initial_image, model=self.model)
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
