import os
import urllib.request
from tqdm import tqdm



TOKEN = input("Please enter the secret Zenodo review token provided by the authors: ").strip()

DATASETS = {
"Xenium_Proseq_pt1_lesion.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt1_lesion.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt2_lesion.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt2_lesion.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt3_lesion.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt3_lesion.h5ad/content?preview=1&token={TOKEN}", 
"Xenium_Proseq_pt4_lesion.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt4_lesion.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt5_lesion.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt5_lesion.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt2_control.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt2_control.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt3_control.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt3_control.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt4_control.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt4_control.h5ad/content?preview=1&token={TOKEN}",

"Xenium_Proseq_pt1_lesion_neighborhood_261009.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt1_lesion_neighborhood_261009.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt2_lesion_neighborhood_261009.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt2_lesion_neighborhood_261009.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt3_lesion_neighborhood_261009.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt3_lesion_neighborhood_261009.h5ad/content?preview=1&token={TOKEN}", 
"Xenium_Proseq_pt4_lesion_neighborhood_261009.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt4_lesion_neighborhood_261009.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt5_lesion_neighborhood_261009.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt5_lesion_neighborhood_261009.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt2_control_neighborhood_261009.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt2_control_neighborhood_261009.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt3_control_neighborhood.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt3_control_neighborhood_261009.h5ad/content?preview=1&token={TOKEN}",
"Xenium_Proseq_pt4_control_neighborhood_261009.h5ad": f"https://zenodo.org/api/records/23324318/draft/files/Xenium_Proseq_pt4_control_neighborhood_261009.h5ad/content?preview=1&token={TOKEN}"

}

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

def main():
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")

    for filename, url in DATASETS.items():
        output_path = os.path.join(data_dir, filename)
        if os.path.exists(output_path):
            print(f"File already exists: {output_path} (skipping)")
            continue
        
        print(f"Downloading {filename}...")
        try:
            download_url(url, output_path)
            print(f"Successfully downloaded to {output_path}\n")
        except Exception as e:
            print(f"Error downloading {filename}: {e}\n")

if __name__ == "__main__":
    main()

