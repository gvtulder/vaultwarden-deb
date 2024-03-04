import datetime
import glob
import re
import os.path
from distutils.version import LooseVersion


# generates the index page for the repository


DEBIAN_RELEASES = {
    "bookworm": { "version": 12 },
    "bullseye": { "version": 11 },
    "buster": { "version": 10 },
}
ARCHITECTURES = [ "amd64" ]

IGNORED_PATHS = set([ "by-hash", "index.html", "404.html" ])


def get_version(filename):
    m = re.match(".+_([^_]+)_[^_]+\.deb", filename)
    if m:
        return m[1]
    else:
        return filename


latest_versions = {}
for release in DEBIAN_RELEASES:
    for arch in ARCHITECTURES:
        latest_versions[(release, arch)] = [
            sorted(glob.glob(f"dists/{release}/main/binary-{arch}/{package}_*.deb"), key=get_version)[-1]
            for package in ("vaultwarden", "vaultwarden-web-vault")
        ]


print("""
<!doctype html>
<html>
  <head><title>Vaultwarden deb repository</title>
  <style type="text/css">
body {
  font-family: sans-serif;
  font-size: 14px;
}
a {
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}

.latest-releases {
  padding: 0;
  margin: 0;
}
.latest-releases th,
.latest-releases td {
  padding: 5px 8px;
  margin: 0;
  text-align: left;
  font-size: 14px;
}
.latest-releases .current th,
.latest-releases .current td {
  background: #eee;
}
.latest-releases .arch {
  font-weight: normal;
}

.all-files,
.all-files li,
.all-files ul {
  margin: 0;
  padding: 3px 0;
  text-indent: 0;
  list-style: none;
}
.all-files > li {
  margin-right: 60px;
}
.all-files li li {
  margin-left: 25px;
}
  </style>
</head>
<body>
<h1>Vaultwarden deb repository</h1>
<p>
This repository contains deb packages of Vaultwarden, a Bitwarden-compatible API server written in Rust. They can be installed in Debian or Ubuntu.
</p>
<p>
See the <a href="https://github.com/gvtulder/vaultwarden-deb/">GitHub repository</a> for more information.
</p>

<hr>

<h2>Latest release</h2>
<table class="latest-releases">
""")


for idx, ((release, arch), files) in enumerate(latest_versions.items()):
    print('  <tr class="current">')
    print(f'    <th class="release">Debian {DEBIAN_RELEASES[release]["version"]} ({release})</th>')
    print(f'    <th class="arch">{arch}</th>')
    for file in files:
        print(f'    <td><a href="{file}">{os.path.basename(file)}</a></td>')
    print("  </tr>")


print("""
</table>
<p>
Repository updated on """ + datetime.datetime.now().strftime('%Y.%m.%d') + """.
</p>

<hr>

<h2>Installing the repository</h2>
""")


for release, info in DEBIAN_RELEASES.items():
    print("""
<p>To install Vaultwarden and add this repository, run this for Debian """ + f'{info["version"]} ({release})' + """:</p>
<pre>
wget -qO- https://vaultwarden-deb.pages.dev/dists/""" + release + """/install.sh | sudo bash
sudo apt update
sudo apt install vaultwarden
</pre>
""")

print("""
<hr>

<h2>All files</h2>
<ul class="all-files">
""")


def print_file_tree(path=".", indent=""):
    with os.scandir(path) as it:
        for entry in sorted(it, key=lambda e: (e.is_dir(), e.name)):
            if entry.name in IGNORED_PATHS:
                pass
            elif entry.is_dir():
                print(f'{indent}<li>{entry.name}')
                print(f'{indent} <ul>')
                print_file_tree(entry.path, indent + "  ")
                print(f'{indent} </ul>')
                print(f"{indent}</li>")
            else:
                print(f'{indent}<li><a href="{entry.path}">{entry.name}</a></li>')


print_file_tree()


"""
  <li><a href="vaultwarden-deb-repo-keyring.asc">vaultwarden-deb-repo-keyring.asc</a></li>
  <li><a href="vaultwarden-deb-repo-keyring.gpg">vaultwarden-deb-repo-keyring.gpg</a></li>
  <li>
    bookworm (12)
    <ul>
      <li><a href="dists/bookworm/InRelease">InRelease</a></li>
      <li><a href="dists/bookworm/Release">Release</a></li>
      <li><a href="dists/bookworm/Release.gpg">Release.gpg</a></li>
      <li>
        binary-amd64
        <ul>
          <li><a href="dists/bookworm/InRelease">InRelease</a></li>
          <li><a href="dists/bookworm/Release">Release</a></li>
          <li><a href="dists/bookworm/Release.gpg">Release.gpg</a></li>
          <li><a href="dists/bookworm/InRelease">InRelease</a></li>
          <li><a href="dists/bookworm/Release">Release</a></li>
          <li><a href="dists/bookworm/Release.gpg">Release.gpg</a></li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    bookworm (12)
    <ul>
      <li><a href="dists/bookworm/InRelease">InRelease</a></li>
      <li><a href="dists/bookworm/Release">Release</a></li>
      <li><a href="dists/bookworm/Release.gpg">Release.gpg</a></li>
      <li>
        binary-amd64
        <ul>
          <li><a href="dists/bookworm/main/binary-amd64/vaultwarden_1.28.0-1_amd64.deb">vaultwarden_1.28.0-1_amd64.deb</a></li>
          <li><a href="dists/bookworm/main/binary-amd64/vaultwarden_1.28.1-1_amd64.deb">vaultwarden_1.28.1-1_amd64.deb</a></li>
          <li><a href="dists/bookworm/main/binary-amd64/vaultwarden_1.29.0-1_amd64.deb">vaultwarden_1.29.0-1_amd64.deb</a></li>
          <li><a href="dists/bookworm/main/binary-amd64/vaultwarden_1.29.1-1_amd64.deb">vaultwarden_1.29.1-1_amd64.deb</a></li>
          <li><a href="dists/bookworm/main/binary-amd64/vaultwarden_1.29.2-1_amd64.deb">vaultwarden_1.29.2-1_amd64.deb</a></li>
          <li><a href="dists/bookworm/main/binary-amd64/vaultwarden_1.30.0-1_amd64.deb">vaultwarden_1.30.0-1_amd64.deb</a></li>
          <li><a href="dists/bookworm/main/binary-amd64/vaultwarden_1.30.1-1_amd64.deb">vaultwarden_1.30.1-1_amd64.deb</a></li>
        </ul>
      </li>
    </ul>
  </li>
"""

print("""
</ul>

</html>
""")
