SNAPSHOT=$1
# Read the first three lines from key.txt
read -r huggingface_token
read -r key_id
read -r access_key <"key.txt"
echo "$huggingface_token\n$key_id\n$access_key"

echo -e "$huggingface_token\nn" | huggingface-cli login 
echo -e "$key_id\n$access_key\n\n\n\n" | aws configure

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
