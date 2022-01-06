from click.testing import CliRunner
from gnomad_rocksdb import GnomadMafDB
from gnomad_rocksdb.main import gnomad_rocksdb_download


def tests_download_gnomad(tmp_path, script_runner):
    runner = CliRunner()
    result = runner.invoke(gnomad_rocksdb_download, f'--version _test --db_path {str(tmp_path)}')
    assert result.exit_code == 0

    db_download = GnomadMafDB(str(tmp_path))
    it = db_download.db.iterkeys()
    it.seek_to_first()
    download_variants = list(it)

    db = GnomadMafDB('tests/data/test_db')
    it = db.db.iterkeys()
    it.seek_to_first()
    variant = list(it)

    assert len(download_variants) == len(variant)
