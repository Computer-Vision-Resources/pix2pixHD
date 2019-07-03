from models.pix2pixHD_model import Pix2PixHDModel
from data.base_dataset import get_params, get_transform
from PIL import Image
import util.util as util
import torch

class Pix2PixConverter():

    def __init__(self, opt):
        opt.nThreads = 1    # test code only supports nThreads = 1
        opt.batchSize = 1   # test code only supports batchSize = 1
        opt.no_flip = True  # no flip
        self.opt = opt

        self.model = Pix2PixHDModel()
        self.model.initialize(opt)
        if opt.verbose: print(self.model)


    def convert(self, pose_path):
        # Converts image and returns its path

        A = Image.open(pose_path)
        params = get_params(self.opt, A.size)
        transform_A = get_transform(self.opt, params)
        A_tensor = transform_A(A.convert('RGB'))
        
        generated = self.model.inference(A_tensor, inst=None, image=None)
        neural_image = util.tensor2im(generated.data[0])

        path_elems = pose_path.split(".")
        neural_path = "".join([*path_elems[:-1], "_neural", path_elems[-1]])
        util.save_image(synthesized_image, neural_path)

        return neural_path
