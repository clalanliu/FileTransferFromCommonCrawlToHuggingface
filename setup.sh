SNAPSHOT=$1
pip install -r requirements.txt

huggingface_token=$(sed '1q;d' key.txt)
key_id=$(sed '2q;d' key.txt)
access_key=$(sed '3q;d' key.txt)
echo "$huggingface_token\n$key_id\n$access_key"

huggingface-cli login < "$huggingface_token\nn" 
aws configure < "$key_id\n$access_key\n" 

directory="wets/wet_path/$SNAPSHOT"

# Check if directory exists
if [ -d "$directory" ]; then
  echo "Directory already exists: $directory"
else
  # Create the directory
  mkdir -p "$directory"
  echo "Directory created: $directory"
fi

aws s3 cp s3://commoncrawl/crawl-data/CC-MAIN-$SNAPSHOT/wet.paths.gz wets/wet_path/$SNAPSHOT/wet.paths.gz
#wget https://data.commoncrawl.org/crawl-data/CC-MAIN-$SNAPSHOT/wet.paths.gz -O wets/wet_path/$SNAPSHOT/wet.paths.gz
