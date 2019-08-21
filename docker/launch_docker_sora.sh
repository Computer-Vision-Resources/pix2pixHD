# Thanks @dustinfreeman for providing the script
# Note:
# 1. pwd must exists
# 2. workdir is just an entry point  

nvidia-docker run -ti --ipc=host --shm-size 11G -v $(pwd):/home/haotian/Projects --workdir=/home/haotian/Projects/ haotianz/vid2vid:cuda9.0 /bin/bash