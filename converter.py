from models.pix2pixHD_model import Pix2PixHDModel
from data.base_dataset import get_params, get_transform
from options.test_options import TestOptions
import util.util as util

from PIL import Image
import torch

# Converter class
# ---------------
# Wrapper around Pytorch model providing simple interface
# For new models, write a new converter

class Converter():
    def __init__(self):
        pass

    def convert(self, paths):
        pass

class Pix2PixConverter(Converter):

    def __init__(self):
        opt = TestOptions().parse(save=False)

        opt.name        = "pose2human_640p_g4_HW"
        opt.loadSize    = 640
        opt.label_nc    = 0
        opt.no_instance = True
        opt.nThreads    = 1 
        opt.batchSize   = 1 
        opt.no_flip     = True  # no flip

        self.opt = opt
        self.model = Pix2PixHDModel()
        self.model.initialize(opt)

        if opt.verbose: print(self.model)


    def convert(self, pose_path):
        # Converts image
        # Returns path of image

        A = Image.open(pose_path)
        params = get_params(self.opt, A.size)
        transform_A = get_transform(self.opt, params)
        A_tensor = transform_A(A.convert('RGB'))
        A_shaped_tensor = A_tensor.unsqueeze(0)
        
        generated = self.model.inference(A_shaped_tensor, inst=None, image=None)
        np_image = util.tensor2im(generated.data[0])
        neural_image = Image.fromarray(np_image)

        return neural_image
