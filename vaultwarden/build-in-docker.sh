#!/bin/bash
set -e
set -x

SOURCE_URL=https://github.com/dani-garcia/vaultwarden/archive/refs/tags/${VW_SERVER_VERSION}.tar.gz
if [[ $DEBIAN_TARGET_VERSION == buster ]] ; then
  RUST_IMAGE=rust:1.79-${DEBIAN_TARGET_VERSION}
else
  RUST_IMAGE=rust:1.80-${DEBIAN_TARGET_VERSION}
fi

# download latest source
wget -O vaultwarden.tar.gz $SOURCE_URL

# build docker image
docker build --build-arg rust_image=$RUST_IMAGE -t vaultwarden .

# extract files
docker create --name vw vaultwarden
docker cp vw:/out .
docker rm vw
docker image rm vaultwarden

mv out/vaultwarden_*.deb .

