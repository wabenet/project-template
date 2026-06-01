# syntax = wabenet/dodfile-syntax
actions:
  base-image:
    type: base
    name: "debian:stable-slim"

  build-dependencies:
    type: install
    name: "build-essential ca-certificates"

  core-utilities:
    type: install
    name: "git bash curl make"

  protobuf:
    type: eget
    repo: "protocolbuffers/protobuf"
    # Hack, because the protobuf releases have an unusual naming schema for the architecture
    asset: ["{{ archLike `x86_64` `x86_32` `aarch_64` `ppcle_64` `s360_64` }}"]

  buf:
    type: eget
    repo: "bufbuild/buf"
    asset: ["^protoc-gen-buf", "^.tar.gz"]

  golang:
    type: golang
    install:
      - github.com/goreleaser/goreleaser/v2@latest
      - github.com/golangci/golangci-lint/v2/cmd/golangci-lint@latest

  copier:
    type: python
    pip_packages:
      - copier
      - copier-templates-extensions
      - jinja2-time

  codeclimate:
    type: fetch
    source: "https://codeclimate.com/downloads/test-reporter/test-reporter-latest-{{ os }}-{{ arch }}"
    destination: "/bin/cc-test-reporter"

  runner-user:
    type: script
    script: |
      echo "Create user for GitHub Actions"
      groupadd --gid 201 runner
      useradd --uid 1001 --gid 201 --create-home runner

  gopath:
    type: environment
    variables:
      GOPATH: /go
