build:
	[ -f output/vaultwarden ] || ./docker-image-extract vaultwarden/server:1.23.1-alpine

install:
	mkdir -p ${DESTDIR}/etc
	mkdir -p ${DESTDIR}/usr/bin
	mkdir -p ${DESTDIR}/var/lib/vaultwarden
	mkdir -p ${DESTDIR}/var/lib/vaultwarden/data
	mkdir -p ${DESTDIR}/var/log/vaultwarden
	cp output/vaultwarden ${DESTDIR}/usr/bin/vaultwarden
	cp vaultwarden.env ${DESTDIR}/etc/vaultwarden.env

deb:
	dpkg-buildpackage --build=binary --no-sign
