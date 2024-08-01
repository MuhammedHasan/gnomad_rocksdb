import pytest
from gnomad_rocksdb import GnomadMafDB, gnomad_rocksdb_download


@pytest.fixture
def gnomad_maf_db(tmp_path):
    db_path = str(tmp_path / 'test_db')
    gnomad_rocksdb_download('_test', db_path)
    return GnomadMafDB(db_path)


def test_GnomadMafDB_get(gnomad_maf_db):
    it = gnomad_maf_db.db.iterkeys()
    it.seek_to_first()

    variants = list(it)
    v = variants[0].decode("utf-8")

    assert gnomad_maf_db[v] < 1
    assert gnomad_maf_db['chr' + v] < 1
    assert v in gnomad_maf_db
