# Gnomad Rocksdb

Fast look up interface allel frequency of variants from gnomad with rocksdb.

## Installation

```
conda install -c conda-forge python-rocksdb
pip install git+https://github.com/MuhammedHasan/gnomad_rocksdb.git
```

## Download database

Download rocksdb for gnomad
```console
gnomad_rocksdb_download --version {version} --db_path {output_path}
```

Supported version (4.1)

## Usage

```py
from gnomad_rocksdb import GnomadMafDB

db = GnomadMafDB(db_path)

db.get('17:1000:A>C')
# 0.001

db.get('chr17:1000:A>C')
# 0.001

db['17:1000:A>C']
# 0.001

'17:1000:A>C' in db
# True
```

## Create Database

```console
pip install tqdm snakemake more_itertools
# modify workflow/config.yaml
python -m snakemake -j 1
```
