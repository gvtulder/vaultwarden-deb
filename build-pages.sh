#!/bin/bash
# download the repository files for Cloudflare Pages
set -e

wget https://github.com/gvtulder/vaultwarden-deb/releases/download/apt-get/repo.tar.gz
tar xzvf repo.tar.gz

for release in buster bullseye ; do
  cp install.sh repo/dists/$release/install.sh
  sed -i 's/DEBIAN_TARGET_VERSION=[a-z]+/DEBIAN_TARGET_VERSION='$release'/' repo/dists/$release/install.sh
  sed -i 's/BASEURL=.\+/BASEURL=https:\/\/vaultwarden-deb.pages.dev/' repo/dists/$release/install.sh
  sed -i 's/RELEASE=.\+/RELEASE="'$release' main"/' repo/dists/$release/install.sh
done

cd repo/

cat <<EOF > index.html
<html>
<head><title>Vaultwarden deb repository</title></head>
<body>
<h1>Vaultwarden deb repository</h1>
<p>
This repository contains deb packages of Vaultwarden, a Bitwarden-compatible API server written in Rust. They can be installed in Debian or Ubuntu.
</p>
<p>
See the <a href="https://github.com/gvtulder/vaultwarden-deb/">GitHub repository</a> for more information.
</p>
<p>
Files:
</p>
<ul>
EOF

find * -type f | sort -u | while read filename ; do
  echo '  <li><a href="'$filename'">'$filename'</a></li>' >> index.html
done

cat <<EOF >> index.html
</ul>
</html>
EOF

