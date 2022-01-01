openapi-generator generate \
    -i swagger.json \
    -g python \
    -o ./client \
    --additional-properties packageName=kalshi,projectName=kalshi
