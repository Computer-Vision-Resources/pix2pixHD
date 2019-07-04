from options.test_options import TestOptions
from converter import Pix2PixConverter

source = "game_assets/test_pose.jpg"

def main():
    model = Pix2PixConverter()
    path_of_synthesized_image = model.convert(source)
    print(path_of_synthesized_image)

if __name__ == '__main__':
    main()
