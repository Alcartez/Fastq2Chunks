import os

def sh(script):
    os.system(script)

#Define Directories
home = os.getcwd()
extract_reads_dir = home + "/paeruginosa-reads" 
print("Setting up sample files for you ...")

#Download and Unzip Sample files
sh("wget https://resources.qiagenbioinformatics.com/testdata/paeruginosa-reads.zip?_ga=2.268135246.1349443116.1616491052-1182821402.1616491052")
sh("unzip paeruginosa-reads.zip?_ga=2.268135246.1349443116.1616491052-1182821402.1616491052")
print("Successfully downloaded and unzipped...")

#Append Sample to Single Fastq
os.chdir(extract_reads_dir)
sh("cat SRR396636.sra_1.fastq >> test.fastq")
sh("cat SRR396636.sra_2.fastq >> test.fastq")
sh("cat SRR396637.sra_1.fastq >> test.fastq")
sh("cat SRR396637.sra_2.fastq >> test.fastq")
print("test.fastq successfully created...")

#Move test.fastq to test directory
os.chdir(home)
sh("mkdir test")
sh("mv paeruginosa-reads/test.fastq test/")
sh("rm -R paeruginosa-reads/")
sh("rm -R paeruginosa-reads.zip?_ga=2.268659889.1349443116.1616491052-1182821402.1616491052;")
print("Sample files successfully downloaded and extracted ...")
print("Please delete 'paeruginosa-reads.zip?_ga=2.268135246.1349443116.1616491052-1182821402.1616491052' , if it still exists")
print("Apologies for the inconvenience...")
print("Just Run fastq2chunks.py to split it into chunks...")

