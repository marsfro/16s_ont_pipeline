import os
from snakemake.shell import shell
import read_config

# Read config.yaml
config = read_config.get_config()

# output folder
output_folder = config["raw_data_location"]
os.makedirs(output_folder, exist_ok=True)

# download using curl
sh_file = f"download_file.sh"
shell(f"curl -o {output_folder}/{sh_file}")

rule files:
    input: 
	"/resources/download_file.sh"
    output:
	"/resources/input_samples/"
    shell: 
	"python download_input_samples.py"  