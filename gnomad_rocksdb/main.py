import rocksdb
import wget
import click
import tarfile


db_url = {
    '2.1.1': 'https://sandbox.zenodo.org/record/988430/files/gnomad_rocksdb_2.1.1.tar.gz?download=1'
}


@click.command()
@click.option('--version', help='Gnomad version (currently 2.1.1, 3.1.2 supported)')
@click.option('--db_path', help='Path to download database')
def cli(version, db_path):

    if version not in db_url:
        raise(f'Version {version} is not supported.')

    print('Downloading database...')
    download_path = db_path + '_backup.tar.gz'
    wget.download(db_url[version], out=download_path)

    print('Unzipping database...')
    file = tarfile.open(download_path)
    backup_dir = db_path + '_backup/'
    file.extractall(backup_dir)
    file.close()

    print('Storing database...')
    backup = rocksdb.BackupEngine(backup_dir + 'backup/')
    backup.restore_latest_backup(db_path, db_path)


if __name__ == '__main__':
    cli()
