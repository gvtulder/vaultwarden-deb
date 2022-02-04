build:
	# [ -f output/vaultwarden ] || ./docker-image-extract vaultwarden/server:1.24.0-alpine
	# ./build-in-docker.sh
	echo OK

install:
	mkdir -p ${DESTDIR}/etc
	mkdir -p ${DESTDIR}/usr/bin
	mkdir -p ${DESTDIR}/var/lib/vaultwarden
	mkdir -p ${DESTDIR}/var/lib/vaultwarden/data
	mkdir -p ${DESTDIR}/var/log/vaultwarden
	cp target/release/vaultwarden ${DESTDIR}/usr/bin/vaultwarden
	cp vaultwarden.env ${DESTDIR}/etc/vaultwarden.env

deb:
	dpkg-buildpackage --build=binary --no-sign
