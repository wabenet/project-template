[![copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)
![license](https://img.shields.io/github/license/wabenet/project-template)

# wabenet project template

This repository provides a common template for all other Github projects under
the wabenet umbrella.

## Usage

Projects are templated via [Copier](https://copier.readthedocs.io/en/stable).
It requires additional jinja2 extensions to run. You can install all prerequisites with pip:

```
$ pip install copier copier-templates-extensions jinja2-time
```

To create a new project from this template, run:

```shell
$ copier copy --trust gh:wabenet/project-template <path/to/project>
```

To update your project to the latest version, run:

```shell
$ copier update --trust
```

## license & authors

```text
Copyright 2024 Ole Claussen

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
