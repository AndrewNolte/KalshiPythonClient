openapi-generator generate \
    -i swagger.json \
    -g python \
    -o ./client.py \
    --additional-properties=packageName=kalshi