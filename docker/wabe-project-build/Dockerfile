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

  golang:
    type: golang
    install:
      - google.golang.org/protobuf/cmd/protoc-gen-go@latest
      - google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
      - github.com/goreleaser/goreleaser@latest
      - github.com/golangci/golangci-lint/v2/cmd/golangci-lint@latest

  copier:
    type: python
    pip_packages:
      - copier
      - copier-templates-extensions
      - jinja2-time

  gopath:
    type: environment
    variables:
      GOPATH: /go
