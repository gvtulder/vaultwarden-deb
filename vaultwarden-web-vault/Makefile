build:
	[ -f bw_web_v2.25.0.tar.gz ] || wget -O bw_web_v2.25.0.tar.gz https://github.com/dani-garcia/bw_web_builds/releases/download/v2.25.0/bw_web_v2.25.0.tar.gz

install:
	mkdir -p ${DESTDIR}/var/lib/vaultwarden
	tar -f bw_web_v2.25.0.tar.gz -C ${DESTDIR}/var/lib/vaultwarden -xz

deb:
	dpkg-buildpackage --build=binary --no-sign
