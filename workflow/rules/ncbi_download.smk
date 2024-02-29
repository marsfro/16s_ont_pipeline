#configfile: "../config/config.yaml"

from snakemake.remote.NCBI import RemoteProvider as NCBIRemoteProvider
NCBI = NCBIRemoteProvider(email=config["ncbi_user_address"])
import os


rule all:
    input:
        NCBI.remote("PRJNA687773.fasta", db="nuccore")
    run:
        outputName = os.path.basename("test.fasta")
        shell("mv {input} {outputName}")