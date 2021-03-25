import os
from Bio import SeqIO

#BeepBopNoises
home_dir = os.getcwd()
fastq2split_dir = home + "/fastq2split"
test_dir = fastq2split_dir + "/test"
sample_file_path = test_dir + "/test.fastq"

record_iter = SeqIO.parse(open(sample_file_path), "fastq")
for i, batch in enumerate(batch_iterator(record_iter, 10000)):
    filename = "group_%i.fastq" % (i + 1)
    with open(filename, "w") as handle:
        count = SeqIO.write(batch, handle, "fastq")
    print("Wrote %i records to %s" % (count, filename))
