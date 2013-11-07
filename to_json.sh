echo "["
sed 's/\"startDate\"/{ &/' | sed 's/\(\"value\".*\),/\1 },/'
# create an empty object so we don't have a problem with trailing ,
echo "{}"
echo "]"
