import os
from subprocess import Popen, PIPE


def tests_download_gnomad(tmp_path):

    __import__("pdb").set_trace()

    os.system(f'gnomad_rocksdb_download --version 2.1.1 --db_path {str(tmp_path)}')
    
    __import__("pdb").set_trace()
    
