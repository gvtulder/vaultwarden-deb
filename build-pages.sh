#!/bin/bash
# download the repository files for Cloudflare Pages
set -e

mkdir -p repo
./sync-s3.sh s3://${AWS_S3_BUCKET}/ repo/

for release in buster bullseye bookworm ; do
  cp install.sh repo/dists/$release/install.sh
  sed -i 's/DEBIAN_TARGET_VERSION=[a-z]+/DEBIAN_TARGET_VERSION='$release'/' repo/dists/$release/install.sh
  sed -i 's/BASEURL=.\+/BASEURL=https:\/\/vaultwarden-deb.pages.dev/' repo/dists/$release/install.sh
  sed -i 's/RELEASE=.\+/RELEASE="'$release' main"/' repo/dists/$release/install.sh
done

cp 404.html repo/

cd repo/

python ../build-pages-html.py > index.html

