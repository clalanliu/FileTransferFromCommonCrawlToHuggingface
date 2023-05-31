NAME=$1
echo $NAME

while true
do
    pkill -f "python3 $NAME" || echo "Nothing to delete"
    python3 $NAME&
    sleep $2
done