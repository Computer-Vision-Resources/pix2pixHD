FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

RUN apt-get update && apt-get install -y rsync htop git openssh-server tmux

RUN apt-get install python3-pip -y
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip3 install --upgrade pip

# Torch and dependencies:
RUN pip install torch torchvision 
RUN pip install cffi tensorboardX
RUN pip install tqdm scipy scikit-image colorama==0.3.7 
RUN pip install setproctitle pytz ipython

# vid2vid dependencies
RUN apt-get install libglib2.0-0 libsm6 libxrender1 -y
RUN pip install dominate requests opencv-python 

# pix2pixHD, required for initializing training
RUN git clone https://github.com/NVIDIA/pix2pixHD /pix2pixHD

# Install apex
WORKDIR /
RUN git clone https://github.com/NVIDIA/apex \
 && cd apex \
 && pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" .

# Install Kivy
RUN pip install cython kivy
RUN git clone https://github.com/kivy/kivent.git kivent
RUN apt-get update && apt-get install -y libgl1-mesa-dev
RUN cd kivent/modules/core && python setup.py build_ext install

# Add user 
RUN useradd -ms /bin/bash cristobal
USER cristobal


