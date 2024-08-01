import click
from gnomad_rocksdb import gnomad_rocksdb_download


@click.command()
@click.option('--version', help='Gnomad version (currently 4.1 supported)')
@click.option('--db_path', help='Path to download database')
def cli_gnomad_rocksdb_download(version, db_path):
    gnomad_rocksdb_download(version, db_path)