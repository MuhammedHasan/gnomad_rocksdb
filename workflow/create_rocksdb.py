from tqdm import tqdm
import gzip
from more_itertools import batched
import rocksdb


batch_size = snakemake.params['batch_size']
db = rocksdb.DB(snakemake.output['db'],
                rocksdb.Options(create_if_missing=True))

def variants(vcf):

    with gzip.open(vcf, 'r') as f:
        for line in tqdm(f):
            line = line.decode('utf-8')

            if line.startswith('#'):
                continue

            variant = line.split('\t')
            chrom = variant[0].replace('chr', '')
            pos = variant[1]
            ref = variant[3]
            alt = variant[4]

            info = variant[7].split(';')
            ac = int(info[0].split('=')[1])
            af = float(info[2].split('=')[1])

            if ac > 0:
                yield f'{chrom}:{pos}:{ref}>{alt}', af
                

for vcf in snakemake.input['vcfs']:
    print('Processing %s' % vcf)

    for batch in batched(variants(vcf), batch_size):
        batch_writer = rocksdb.WriteBatch()

        for variant, af in batch:
            batch_writer.put(bytes(variant, 'utf-8'), bytes(str(af), 'utf-8'))
        db.write(batch_writer)