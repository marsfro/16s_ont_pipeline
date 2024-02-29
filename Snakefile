import os

#min_version("6.7.0")

configfile: "../config/config.yaml"

data_dir = config["data_location"]
output_dir = config["output_location"]
log_dir = config["log_location"]

# read samples paths from config
#include: "rules/commons.smk"

# rule all:
#     input:
#         # ncbi_download rule
#         expand("./example_samples/{sample}_fastqc.html", sample=SAMPLES),

#################################################################
###################### rule definitions #########################
#################################################################

include: "rules/ncbi_download.smk"

#include: "rules/quality_control.smk"

#include: "rules/trimming.smk"