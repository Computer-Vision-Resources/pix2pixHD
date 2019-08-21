# Install nvidia-driver >= 384
# Use `addtional driver` in `Software & Updates`, need reboot

# Install CUDA 9.0
# CUDA 9 requires gcc 6
sudo apt install gcc-6
sudo apt install g++-6
# downoad one of the "runfile (local)" installation packages from cuda toolkit archive 
wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run
# make the download file executable
chmod +x cuda_9.0.176_384.81_linux-run 
sudo ./cuda_9.0.176_384.81_linux-run --override
# answer following questions while installation begin
	# You are attempting to install on an unsupported configuration. Do you wish to continue? y
	# Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 384.81? n
	# Install the CUDA 9.0 Toolkit? y
# setup your paths
echo 'export PATH=/usr/local/cuda-9.0/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
sudo bash -c "echo /usr/local/cuda/lib64/ > /etc/ld.so.conf.d/cuda.conf"
sudo ldconfig

# Install cudnn 7
# Download 3 .deb files from https://developer.nvidia.com/rdp/cudnn-download
sudo dpkg -i libcudnn7_7.0.5.15–1+cuda9.0_amd64.deb
sudo dpkg -i libcudnn7-dev_7.0.5.15–1+cuda9.0_amd64.deb
sudo dpkg -i libcudnn7-doc_7.0.5.15–1+cuda9.0_amd64.deb
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH'
source ~/.bashrc

# Final check
nvidia-smi
nvcc -V

pip3 install cffi tqdm scipy scikit-image colorama==0.3.7 setproctitle pytz dominate requests