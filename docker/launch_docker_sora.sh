# Thanks @dustinfreeman for providing the script
#!/bin/bash
nvidia-docker run -ti --ipc=host --shm-size 11G -v ~/Projects/pix2pixHD --workdir=/pix2pixHD haotianz/vid2vid:CUDA9-py35 /bin/bash