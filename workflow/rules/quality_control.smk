rule fastQC1:
    input:
        trimmed1=os.path.join(config['Results'],"raw/{sample}_1.fastq")
    output:
        html=os.path.join(config['Results'],"fastQC/raw/{sample}_1.html"),
        zip=os.path.join(config['Results'],"raw/trimmed/{sample}_1.zip")
    threads: 4
    wrapper:
        "0.35.0/bio/fastqc"


rule fastQC2:
    input:
        trimmed2=os.path.join(config['pipeline_result'],"trimmed/{sample}_2.fastq"),
    output:
        html=os.path.join(config['pipeline_result'],"fastQC/trimmed/{sample}_2.html"),
        zip=os.path.join(config['Results'],"fastQC/trimmed/{sample}_2.zip")
    threads: 4
    wrapper:
        "0.35.0/bio/fastqc"

rule fastQC3:
    input:
        trimmed2=os.path.join(config['pipeline_result'],"mapping/{sample}_2.fastq"),
    output:
        html=os.path.join(config['pipeline_result'],"fastQC/mapping/{sample}_2.html"),
        zip=os.path.join(config['Results'],"fastQC/mapping/{sample}_2.zip")
    threads: 4
    wrapper:
        "0.35.0/bio/fastqc"


rule multiQC:
    input:
        expand(os.path.join(config['Results'],"fastQC/mapping/{sample}_1.html"), sample =list(samples.index)),
        expand(os.path.join(config['Results'],"fastQC/trimmed/{sample}_2.html"), sample =list(samples.index)),
        expand(os.path.join(config['Results'],"Prokka/{sample}/{sample}.gff"), sample =list(samples.index)),
        expand(os.path.join(config['Results'],"QUAST/{sample}/report.txt"), sample =list(samples.index))
    output:
        os.path.join(config['Results'],"multiqc/multiqc.html")
    wrapper:
        "0.35.0/bio/multiqc"
