#!/bin/bash -e

aws configure --profile s3-sync-action <<-EOF > /dev/null 2>&1
${AWS_ACCESS_KEY_ID}
${AWS_SECRET_ACCESS_KEY}
${AWS_REGION}
text
EOF

aws s3 sync $1 $2 --profile s3-sync-action --endpoint-url $AWS_S3_ENDPOINT --no-progress

aws configure --profile s3-sync-action <<-EOF > /dev/null 2>&1
null
null
null
text
EOF

