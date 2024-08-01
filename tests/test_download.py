from click.testing import CliRunner
from gnomad_rocksdb import GnomadMafDB
from gnomad_rocksdb.main import cli_gnomad_rocksdb_download


def tests_download_gnomad(tmp_path, script_runner):
    runner = CliRunner()
    result = runner.invoke(cli_gnomad_rocksdb_download, f'--version _test --db_path {str(tmp_path)}')
    assert result.exit_code == 0

    db_download = GnomadMafDB(str(tmp_path))
    it = db_download.db.iterkeys()
    it.seek_to_first()
    assert len(list(it)) > 0