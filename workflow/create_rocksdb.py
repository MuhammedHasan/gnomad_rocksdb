from tqdm import tqdm
import rocksdb
from kipoiseq.extractors import MultiSampleVCF


batch_size = snakemake.params['batch_size']
db = rocksdb.DB(snakemake.output['db'],
                rocksdb.Options(create_if_missing=True))

for vcf in snakemake.input['vcfs']:
    print('Processing %s' % vcf)
    vcf = MultiSampleVCF(vcf)

    for batch in tqdm(vcf.batch_iter(batch_size=batch_size)):
        batch_writer = rocksdb.WriteBatch()

        for v in batch:
            if v.info['AC'] > 0:
                af = v.info['AF']
                batch_writer.put(bytes(str(v), 'utf-8'),
                                 bytes(str(af), 'utf-8'))

        db.write(batch_writer)
