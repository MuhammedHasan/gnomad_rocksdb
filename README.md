# Gnomad Rocksdb

Fast look up interface allel frequency of variants from gnomad with rocksdb.

## Installation

```
conda install -c conda-forge rocksdb python-rocksdb
pip install gnomad_rocksdb
```

## Download database

Download rocksdb for gnomad
```console
gnomad_rocksdb_download --version {version} --db_path {output_path}
```

Supported version (2.1.1, 3.1.2)

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
pip install tqdm kipoiseq snakemake cython cyvcf2
# modify workflow/config.yaml
python -m snakemake -j 1
```
