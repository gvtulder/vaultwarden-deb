#!/bin/bash
# download the repository files for Cloudflare Pages
set -e
set -x

wget https://github.com/gvtulder/vaultwarden-deb/releases/download/apt-get/repo.tar.gz
tar xzvf repo.tar.gz

cd repo/

cat <<EOF >> index.html
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
<pre>
EOF

find -type f >> index.html

cat <<EOF >> index.html
</pre>
</html>
EOF

