## Install

1. Install Mamba package manager:

```bash

conda install -n base -c conda-forge mamba  
```

2. Create a new conda environment named `16s_ont` and install Snakemake:

```bash

mamba create -c conda-forge -c bioconda -n 16s_ont snakemake
```

3. Activate the `16s_ont` environment:

```bash

conda activate 16s_ont
```


## Usage:

You need activate `16s_ont` environment before every usage

From directory /workflow: or write pathway to Snakefile

```bash

snakemake --snakefile Snakefile --config folder="/home/masha/Artem/Liza/V3-V4/test_tmp" database="bacter" min_len=50 qc=10 max_len=10000 -c 16 --use-conda
```


`folder path` path until directory with raw ont fastq files
`min_len` minimal length of read
`max_len` maximal length of read
`qc minimal` quality of read
`-c` number of threads 
`database` "bacter" , "fungi", "parasites"

You can use several database - for that you need to show pathways to database in
`\16s_ont_pipeline\config\config.yaml` and then use flag `bacter` , `fungi`, `parasites`
or something else you want

- Download database for Centrifuge:

https://data.mendeley.com/datasets/tt5ntb4zyv/1

wget https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/tt5ntb4zyv-1.zip
unzip tt5ntb4zyv-1.zip


- Write the path to the database in the file ../config/config.yaml

centrifuge_db: "/path/to/NCBI_202207"





