SNAPSHOT=$1
# Read the first three lines from key.txt
read -r huggingface_token
read -r key_id
read -r access_key < "key.txt"
echo "$huggingface_token\n$key_id\n$access_key"

directory="wets/wet_path/$SNAPSHOT"

# Check if directory exists
if [ -d "$directory" ]; then
  echo "Directory already exists: $directory"
else
  # Create the directory
  mkdir -p "$directory"
  echo "Directory created: $directory"
fi

wget https://data.commoncrawl.org/crawl-data/CC-MAIN-$SNAPSHOT/wet.paths.gz -O wets/wet_path/$SNAPSHOT/wet.paths.gz
echo -e "$huggingface_token\nn" | huggingface-cli login 
echo -e "$key_id\n$access_key\n\n\n\n" | aws configure