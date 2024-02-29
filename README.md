##Install

conda install -n base -c conda-forge mamba  

mamba create -c conda-forge -c bioconda -n 16s_ont snakemake

conda activate 16s_ont


##Usage:

from dir /workflow:

snakemake --snakefile Snakefile --config folder="/path/to/fastq" min_len=50 qc=10 -c 16 --use-conda


###Requirements:

 - Porechope  # remove adaptors
https://github.com/rrwick/Porechop
pip3 install git+https://github.com/rrwick/Porechop.git


 - Nanofilt # trimming based on quality and length
https://github.com/wdecoster/nanofilt     


- Centrifuge:

https://github.com/infphilo/centrifuge

git clone https://github.com/infphilo/centrifuge
cd centrifuge
make
sudo make install prefix=/usr/local

- Download database for Centrifuge:

https://data.mendeley.com/datasets/tt5ntb4zyv/1

wget https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/tt5ntb4zyv-1.zip
unzip tt5ntb4zyv-1.zip


- Write the path to the database in the file ../config/config.yaml

centrifuge_db: "/path/to/NCBI_202207"





