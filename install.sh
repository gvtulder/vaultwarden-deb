# https://wiki.debian.org/DebianRepository/UseThirdParty
# based on code from https://github.com/retorquere/zotero-deb

case `uname -m` in
  "x86_64")
    ;;
  *)
    echo "Vaultwarden is only compiled for the x86_64 architecture"
    exit
    ;;
esac

export GNUPGHOME="/dev/null"

DEBIAN_TARGET_VERSION=bullseye
BASEURL=https://github.com/gvtulder/vaultwarden-deb/releases/download/apt-${DEBIAN_TARGET_VERSION}
RELEASE=./
KEYNAME=vaultwarden-deb-repo-keyring.gpg
GPGKEY=$BASEURL/$KEYNAME
KEYRING=/usr/share/keyrings/$KEYNAME
if [ -x "$(command -v curl)" ]; then
  sudo curl -L $GPGKEY -o $KEYRING
elif [ -x "$(command -v wget)" ]; then
  sudo wget -O $KEYRING $GPGKEY
else
  echo "Error: need wget or curl installed." >&2
  exit 1
fi

sudo chmod 644 $KEYRING

cat << EOF | sudo tee /etc/apt/sources.list.d/vaultwarden-deb-repo.list
deb [signed-by=$KEYRING by-hash=force] $BASEURL $RELEASE
EOF

sudo apt-get clean
