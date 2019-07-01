# Thanks @dustinfreeman for providing the script
# Note:
# 1. pwd must exists
# 2. workdir is just an entry point  
#!/bin/bash

# nvidia-docker build -f docker/Dockerfile -t haotianz/pix2pixHD:CUDA9-py35 .

nvidia-docker run -ti --ipc=host --shm-size 11G -v $(pwd):/home/haotian/Projects/pix2pixHD --workdir=/home/haotian/Projects/pix2pixHD haotianz/vid2vid:CUDA9-py35 /bin/bash