# Use Ubuntu as base and install Hugo
FROM ubuntu:22.04

# Set the working directory
WORKDIR /src

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    git \
    ca-certificates \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Hugo extended version (latest)
RUN wget https://github.com/gohugoio/hugo/releases/download/v0.146.0/hugo_extended_0.146.0_linux-amd64.deb \
    && dpkg -i hugo_extended_0.146.0_linux-amd64.deb \
    && rm hugo_extended_0.146.0_linux-amd64.deb

# Create a non-root user
RUN useradd -m -s /bin/bash hugo
USER hugo

# Expose Hugo's development server port
EXPOSE 1313

# Default command to serve the site
CMD ["hugo", "server", "--bind", "0.0.0.0", "--buildDrafts", "--buildFuture"]