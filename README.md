# RFENet for Retinal Lesion Segmentation

This repository provides the official PyTorch implementation of **RFENet**, a lightweight segmentation framework for CNV (OCT) and CNP (FFA) lesion segmentation.  
For confidentiality reasons, the clinical datasets are not distributed in this repository.

## 1. Requirements

- Python 3.9
- PyTorch (CUDA supported)
- Common dependencies: `albumentations`, `opencv-python`, `numpy`, `pandas`, `scikit-learn`, `tqdm`, `timm`, `mmcv`

> Note: Exact package versions may vary across systems. The code was tested on a CUDA-enabled GPU environment.

## 2. Project Structure

Please organize the dataset in the following format:

./inputs/
└── <DATASET_NAME>/
├── images/
│ ├── xxx.png
│ └── ...
└── masks/
├── xxx.png
└── ...


- `images/`: input images (e.g., OCT B-scans for CNV or FFA images for CNP)
- `masks/`: binary masks with the same file stem as images
- Default image/mask extension is `.png`

## 3. Training

Example (CNV or CNP):

```bash
python train.py \
  --dataset CNV \
  --arch RFENet \
  --loss BCEDiceLoss \
  --epochs 300 \
  --batch_size 16 \
  --lr 1e-4 \
  --scheduler CosineAnnealingLR \
  --min_lr 1e-5 \
  --input_h 512 --input_w 512

The training script will split data into train/val internally (random seed fixed in code).

Best checkpoint is selected by validation IoU and saved to:

models/<EXP_NAME>/model.pth

Logs are saved to:

models/<EXP_NAME>/log.csv

