# Thanks @dustinfreeman for providing the script
#!/bin/bash

# sshfs -o idmap=user haotian@sora.stanford.edu:/home/haotian/Projects ~/mnt_sora/Projects

# start this from ~/mnt_sora
nvidia-docker run -ti --ipc=host --shm-size 32G -v $(pwd):/mnt_sora --workdir=/mnt_sora haotianz/vid2vid:CUDA9-py35 /bin/bash
