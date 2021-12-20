# Based on vaultwarden Dockerfile

# e.g., rust:1.55-buster
ARG rust_image

FROM ${rust_image} AS build

# Debian-based builds support multidb
ARG DB=sqlite,mysql,postgresql

# Build time options to avoid dpkg warnings and help with reproducible builds.
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    TZ=UTC \
    TERM=xterm-256color \
    CARGO_HOME="/root/.cargo" \
    USER="root"

# Create CARGO_HOME folder and don't download rust docs
RUN mkdir -pv "${CARGO_HOME}" \
    && rustup set profile minimal

# Install DB packages
RUN apt-get update \
    && apt-get install -y \
        --no-install-recommends \
        libmariadb-dev \
        libpq-dev \
        build-essential \
        debhelper \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copies the complete project
# To avoid copying unneeded files, use .dockerignore
COPY . .
RUN tar -xzv --strip-component=1 -f vaultwarden.tar.gz

# Make sure that we actually build the project
RUN touch src/main.rs

# Build the project
RUN cargo build --features ${DB} --release

# Build the deb package
RUN make deb
RUN mkdir /out
RUN cp /*.deb /out

