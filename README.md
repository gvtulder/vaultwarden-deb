# Vaultwarden deb packages

This repository contains deb packages of [Vaultwarden](https://github.com/dani-garcia/vaultwarden), a Bitwarden-compatible API server written in Rust. They can be installed in Debian or Ubuntu.

The files in these packages are extracted from the most recent Docker releases of the upstream [Vaultwarden](https://github.com/dani-garcia/vaultwarden) repository. The binary is statically linked, so it should run on many amd64 systems.

See the [Vaultwarden](https://github.com/dani-garcia/vaultwarden) repository for much more information.

## Contents

The repository provides two packages:

* `vaultwarden`, the main executable, from [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden);
* `vaultwarden-web-vault`, the Bitwarden web vault, from [dani-garcia/vaultwarden](https://github.com/dani-garcia/bw_web_builds).

Use `apt-get install vaultwarden` to install both.

## Installation

To install Vaultwarden and add this repository, run this for Debian 11 (bullseye):
```bash
wget -qO- https://vaultwarden-deb.pages.dev/dists/bullseye/install.sh | sudo bash
sudo apt update
sudo apt install vaultwarden
```

For Debian 10 (buster):
```bash
wget -qO- https://vaultwarden-deb.pages.dev/dists/buster/install.sh | sudo bash
sudo apt update
sudo apt install vaultwarden
```

The packages can also be downloaded manually from the [Releases page](https://github.com/gvtulder/vaultwarden-deb/releases).

## Important configuration

After installation, Vaultwarden needs to be configured. Edit the configuration file at `/etc/vaultwarden.env` to change important settings, such as the port number, the database, and security options.

Vaultwarden is added to `systemd` and can be started and stopped with:
```bash
sudo systemctl status vaultwarden
# to start and stop
sudo systemctl start vaultwarden
sudo systemctl stop vaultwarden
# to start on boot
sudo systemctl enable vaultwarden
```

### Directories

The packages add the following files:
* `/etc/vaultwarden.env`: the configuration file.
* `/usr/bin/vaultwarden`: the Vaultwarden server.
* `/var/lib/vaultwarden/data`: the data directory.
* `/var/lib/vaultwarden/web-vault`: the files for the Bitwarden web vault.
* `/var/log/vaultwarden`: the log file.
