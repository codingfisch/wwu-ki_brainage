# wwu-ki_brainage
Tutorial for brain age prediction using convolutional neural networks (CNN)

Training and evaluation is done using fastai_scans (https://github.com/renato145/fastai_scans), a fastai extension to work with 3d medical images.

# Installation 

1.) Create a new conda environment, install Python 3.6 and activate it
```
conda create -n fastba python=3.6; conda activate fastba
```
2.) Install pip inside the environment
```
conda install pip
```
3.) Install the package inside this conda environment using pip (replace USER with your username and CONDA_DIR with .conda for Anaconda or miniconda for miniconda)
```
/home/USER/CONDA_DIR/envs/fastba/bin/pip install git+git://github.com/codingfisch/wwu-ki_brainage.git
```
4.) Install the bcolz package using conda
```
conda install -c anaconda bcolz
```

Optional (if you have a RTX 30 series graphics card): Reinstall newest Pytorch + Cudatoolkit 
```
conda install pytorch torchvision torchaudio cudatoolkit -c pytorch
```

