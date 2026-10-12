markdown

# Xenium Spatial Profiles of Human Genital Skin during Recurrent HSV-2 Infection

This repository contains the Jupyter Notebooks and reproducible analysis pipeline for our manuscript submitted to *Science Immunology*: **" Keratinocytes spatially segregate neutrophil and T-cell immunity during human HSV-2 ulceration"** (2026).

## ?? Data Availability
Due to GitHub's file size limitations (>100 MB), our processed `.h5ad` AnnData objects are archived securely on **Zenodo** under the DOI: `10.5281/zenodo.23324318`. 

During the peer-review process, these files are set to **Restricted Access**. Reviewers and editors can access the record page directly via our [Zenodo Reviewer Access Link]( https://zenodo.org/records/23324318?preview=1&token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjIzZjI5MWNhLWU4NWEtNDMzYi1hYjkzLTdmM2ZkYzhkMGY1ZCIsImRhdGEiOnt9LCJyYW5kb20iOiIxMzE3NjIxYmVjMGQ5Njk0NGM1NzA0MWZkNDUxNDRjZSJ9.TJ0heZCADdLladQ6apFeh_aBDnf0COMLkdKrX12eljrBgGxc9iyrpA8ayhr3sKkDrLvNkAHob9z8DFx_ZABBrw).

### ?? Dataset Details
The dataset consists of **16 `.h5ad` files** encompassing 10x Xenium single-cell transcriptional profiling (475 genes) across:
* **5 Lesional Skin Biopsies** from individuals with HSV-2 reactivation-induced ulcer disease.
* **3 Matched Control Biopsies** from contralateral control skin.
* Corresponding neighborhood matrices for spatial clustering mapping.

## ?? Getting Started & Replication

You do not need to download the 1.5 GB dataset manually. We have provided an automated script embedded with the secure token to structure your local directory automatically.

### 1. Clone the Repository
```bash
git clone https://github.com
cd Xenium-spatial-skin-HSV2
```

### 2. Set Up Your Environment
We recommend utilizing a clean virtual environment (Conda or venv):
```bash
conda create -n hsv2_spatial python=3.10
conda activate hsv2_spatial
pip install -r requirements_v2.txt
```

### 3. Automatically Fetch the Data Matrices
Run the download script from your terminal to generate the `data/` directory and safely pull down all 16 `.h5ad` files directly from Zenodo's secure API:
```bash
python download_data.py
```

### 4. Run the Analysis
Launch Jupyter Lab or Notebook to run the pipeline sequentially inside the `notebooks/` directory:
```bash
jupyter lab
```

## ?? Contact
For questions or issues regarding the data infrastructure or code reproducibility, please open an issue in this repository or contact the corresponding authors.


