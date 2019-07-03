from options.test_options import TestOptions
from demo.pix2pix import Pix2PixConverter

source = "demo/images/test_pose.jpg"

def main():
    opt = TestOptions().parse(save=False)
    model = Pix2PixConverter(opt)

    path_of_synthesized_image = model.convert(source)
    print(path_of_synthesized_image)

if __name__ == '__main__':
    main()
