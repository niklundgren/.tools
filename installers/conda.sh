# Grab latest miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh

# Activate conda
source ~/.bashrc

# Update conda and install pip
conda update conda
conda install pip

# (optional) create and activate an environment
conda create -n develop python pandas scikit-learn jupyter
source activate py3
