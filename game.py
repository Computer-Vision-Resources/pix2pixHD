from kivy.app         import App
from kivy.core.window import Window
from kivy.clock       import Clock
from kivy.uix.widget  import Widget
from kivy.uix.image   import Image
from kivy.core.image  import Image  as CoreImage

from converter import Pix2PixConverter
from io import BytesIO
import pickle

data_root = "table-tennis-data/JZ/test_A/"
pkl_root = "/Projects/esper_haotian/esper/app/data/image/densepose_JZ/"
image_path = "densepose_65_34779_JZ.jpg"

pkl_path = pkl_root + image_path
img_path = data_root + image_path

f_pkl = open("table-tennis-data/densepose_result.pkl", "rb")
dp = pickle.load(f_pkl , encoding="latin1")


class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.size = self.texture_size


class NeuralImage(Sprite):
    def __init__(self, model=None, **kwargs):
        super(NeuralImage, self).__init__(**kwargs)
        self.model = model
        self.has_converted = False

        cond = lambda x: "densepose_path" in x and x["densepose_path"] == pkl_path
        box = list(map(int, list(filter(cond, dp))[0]["crop_box"]))

    def convert(self):
        # image is a PIL image
        image = self.model.convert(self.source)
        data = BytesIO()
        image.save(data, format='png')
        data.seek(0)
        self.texture = CoreImage(BytesIO(data.read()), ext='png').texture

        self.has_converted = True

    def on_touch_down(self, *ignore):
        if (self.has_converted):
            global image_path
            tokens = image_path.split("_")
            tokens[2] = str(int(tokens[2]) + 1)
            image_path = "_".join(tokens)
            self.source = data_root + image_path
            self.has_converted = False
        else:
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
        self.player = NeuralImage(source=img_path, model=self.model)
        self.add_widget(self.player)


class GameApp(App):
    def build(self):
        game = Game()
        Window.size = game.size
        return game


if __name__ == '__main__':
    GameApp().run()
