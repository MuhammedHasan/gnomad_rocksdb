from pathlib import Path
import rocksdb
import pooch
import tarfile



class VariantDB:

    def __init__(self, path, max_open_files=5000):
        options = rocksdb.Options(max_open_files=max_open_files)
        self.db = rocksdb.DB(path, options, read_only=True)

    @staticmethod
    def _variant_to_byte(variant):
        return bytes(str(variant), 'utf-8')

    def _type(self, value):
        raise NotImplementedError()

    def _get(self, variant):
        if variant.startswith('chr'):
            variant = variant.replace('chr', '')
        return self.db.get(self._variant_to_byte(variant))

    def __getitem__(self, variant):
        maf = self._get(variant)
        if maf:
            return self._type(maf)
        else:
            raise KeyError('This variant is not in the db')

    def __contains__(self, variant):
        return self._get(variant) is not None

    def get(self, variant, default=None):
        try:
            return self[variant]
        except KeyError:
            return default


class GnomadMafDB(VariantDB):

    def _type(self, value):
        return float(value)


db_url = {
    '_test': (
        'https://sandbox.zenodo.org/records/90048/files/test_gnomad_rocksdb_4.1.tar.gz?download=1',
        'md5:e1308f459e79d8a1dea4579820525869'
    ),
    '4.1': (
        'https://zenodo.org/records/12785982/files/gnomad_rocksdb_4.1.tar.gz?download=1',
        'md5:6c34e48dd3f1c76ff608ff6959a92974'
    )
}

def gnomad_rocksdb_download(version, db_path):

    if version not in db_url:
        raise(f'Version {version} is not supported.')

    print('Downloading database...')

    download_path = Path(db_path + '_backup.tar.gz')
    url, md5 = db_url[version]
    pooch.retrieve(
        url=url, known_hash=f'md5:{md5}',
        path=download_path.parent, fname=download_path.name
    )

    print('\nUnzipping database...')
    download_path = str(download_path)
    file = tarfile.open(download_path)
    backup_dir = db_path + '_backup/'
    file.extractall(backup_dir)
    file.close()

    print('Storing database...')
    backup = rocksdb.BackupEngine(backup_dir + 'backup/')
    backup.restore_latest_backup(db_path, db_path)

