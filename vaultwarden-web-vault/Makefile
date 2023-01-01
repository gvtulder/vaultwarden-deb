build:
	[ -f bw_web_${VW_WEB_VERSION}.tar.gz ] || wget -O bw_web_${VW_WEB_VERSION}.tar.gz https://github.com/dani-garcia/bw_web_builds/releases/download/${VW_WEB_VERSION}/bw_web_${VW_WEB_VERSION}.tar.gz

install:
	mkdir -p ${DESTDIR}/usr/share/vaultwarden
	tar -f bw_web_${VW_WEB_VERSION}.tar.gz -C ${DESTDIR}/usr/share/vaultwarden -xz

deb:
	dpkg-buildpackage --build=binary --no-sign
