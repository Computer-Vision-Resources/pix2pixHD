# Thanks @dustinfreeman for providing the script
#!/bin/bash

# nvidia-docker build -f docker/Dockerfile -t cristobal/pix2pix .

nvidia-docker run -ti --ipc=host --shm-size 11G --workdir=/home/cristobal/p2p-haotian -v $(pwd):/home/cristobal/p2p-haotian cristobal/pix2pix /bin/bash
