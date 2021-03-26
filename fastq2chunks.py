import os
from Bio import SeqIO

#Def Bash from python
def sh(script):
    os.system(script)


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

print("Running Fastq2Chunks....")

# Define directory for sample file
home_dir = os.getcwd()
test_dir = home_dir + "/test"
sample_file_path = test_dir + "/test.fastq"
test_output_dir = test_dir + "/output"
sh("mkdir test/output")

print("Configuring directories ...")

#Define Output Directory
os.chdir(test_output_dir)

print("Splitting fastq, prepare for a barrage of output...")

#Time to split
record_iter = SeqIO.parse(open(sample_file_path), "fastq")
for i, batch in enumerate(batch_iterator(record_iter, 1000000)):
    filename = "chunk_%i.fastq" % (i + 1)
    with open(filename, "w") as handle:
        count = SeqIO.write(batch, handle, "fastq")
    print("Wrote %i records to %s" % (count, filename))

print("It is done! Celebrate!")
