import os
from Bio import SeqIO

#Define Batch iterator
def batch_iterator(iterator, batch_size):
    entry = True 
    while entry:
        batch = []
        while len(batch) < batch_size:
            try:
                entry = next(iterator) #for Python2 iterator.next()
            except StopIteration:
                entry = None
            if entry is None:
                break
            batch.append(entry)
        if batch:
            yield batch


# Define directory for sample file
home_dir = os.getcwd()
fastq2split_dir = home_dir + "/fastq2split"
test_dir = fastq2split_dir + "/test"
sample_file_path = test_dir + "/test.fastq"
print("Configuring directories ...")
test_output_dir = test_dir + "/output"

#Define Output Directory
os.chdir(test_output_dir)

#Time to split
record_iter = SeqIO.parse(open(sample_file_path), "fastq")
for i, batch in enumerate(batch_iterator(record_iter, 10000)):
    filename = "chunk_%i.fastq" % (i + 1)
    with open(filename, "w") as handle:
        count = SeqIO.write(batch, handle, "fastq")
    print("Wrote %i records to %s" % (count, filename))
