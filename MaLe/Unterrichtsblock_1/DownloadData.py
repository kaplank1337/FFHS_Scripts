from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    tarball_path = Path("datasets/housing/datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets/housing/datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
    with tarfile.open(tarball_path) as housing_tarball:
        housing_tarball.extractall(path="datasets/housing/datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing = load_housing_data()