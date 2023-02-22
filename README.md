
# Prepare Environment To Train Torch-ngp




## Step 1: Create conda environment and activate it.

Create conda environment.

```bash
  conda create -n torch-ngp
```
Activate conda environment.
```bash
  conda activate torch-ngp
```


## Step 2: Clone github.

```bash
  git clone --recursive https://github.com/ashawkey/torch-ngp.git
  cd torch-ngp
```


## Step 3: Install packages.

```bash
  pip install -r requirements.txt

  # (optional) upgrade numpy version
  pip install numpy --upgrade

  # (optional) install the tcnn backbone
  pip install git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch
```
To avoid not generating video.

```bash
  pip install imageio[ffmpeg]
```


## Step 4: Build extension (optional).

```bash
  bash scripts/install_ext.sh
  cd raymarching
  python setup.py build_ext --inplace
  pip install .
  cd ..
```
