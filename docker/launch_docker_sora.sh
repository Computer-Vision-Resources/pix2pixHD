# Thanks @dustinfreeman for providing the script
#!/bin/bash

# nvidia-docker build -f docker/Dockerfile -t haotianz/pix2pixHD:CUDA9-py35 .

nvidia-docker run -ti --ipc=host --shm-size 11G -v ~/Projects/pix2pixHD --workdir=/pix2pixHD haotianz/vid2vid:CUDA9-py35 /bin/bash