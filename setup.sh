SNAPSHOT=$1

wget https://data.commoncrawl.org/crawl-data/CC-MAIN-2020-05/wet.paths.gz -O wets/wet_path/$SNAPSHOT
huggingface-cli login
aws configure