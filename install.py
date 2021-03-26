import os

def sh(script):
    os.system(script)

home = os.getcwd()
fastq2split_dir = home + "/Fastq2Chunks"
extract_reads_dir = fastq2split_dir + "/paeruginosa-reads" 
sh("mkdir fastq2split")
os.chdir(fastq2split_dir)
#sh("wget https://resources.qiagenbioinformatics.com/testdata/paeruginosa-reads.zip?_ga=2.268135246.1349443116.1616491052-1182821402.1616491052")
sh("unzip paeruginosa-reads.zip?_ga=2.268135246.1349443116.1616491052-1182821402.1616491052")
os.chdir(extract_reads_dir)
sh("cat SRR396636.sra_1.fastq >> test.fastq")
sh("cat SRR396636.sra_2.fastq >> test.fastq")
sh("cat SRR3906637.sra_1.fastq >> test.fastq")
sh("cat SRR396637.sra_2.fastq >> test.fastq")
os.chdir(fastq2split_dir)
sh("mkdir test")
sh("mv paeruginosa-reads/test.fastq test/")
sh("rmdir -r paeruginosa-reads")
sh("rm paeruginosa-reads.zip?_ga=2.268659889.1349443116.1616491052-1182821402.1616491052")
os.chdir(home)
