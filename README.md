# polymer-tree
[![Build Status](https://travis-ci.org/uehara1414/polymer-tree.svg?branch=master)](https://travis-ci.org/uehara1414/polymer-tree)

Print the custom element tree of a website which built with Polymer.

## Installation
```sh
git clone https://github.com/uehara1414/polymer-tree.git
cd polymer-tree
pip install -r requirements.txt
```

## Usage
```sh
python pt.py <url>
```

For example

```sh
python pt.py http://h4k0bu5.hatu.ga/
http://h4k0bu5.hatu.ga/
└── http://h4k0bu5.hatu.ga/x-app.html
    ├── http://h4k0bu5.hatu.ga/bower_components/polymer/polymer.html
    ├── http://h4k0bu5.hatu.ga/bower_components/iron-flex-layout/iron-flex-layout.html
    ├── http://h4k0bu5.hatu.ga/bower_components/app-layout/app-header-layout/app-header-layout.html
    ├── http://h4k0bu5.hatu.ga/bower_components/app-layout/app-header/app-header.html
    ├── http://h4k0bu5.hatu.ga/bower_components/app-layout/app-scroll-effects/app-scroll-effects.html
    ├── http://h4k0bu5.hatu.ga/bower_components/app-layout/app-toolbar/app-toolbar.html
    ├── http://h4k0bu5.hatu.ga/bower_components/vaadin-combo-box/vaadin-combo-box.html
    ├── http://h4k0bu5.hatu.ga/bower_components/iron-icon/iron-icon.html
    ├── http://h4k0bu5.hatu.ga/bower_components/iron-icons/iron-icons.html
    ├── http://h4k0bu5.hatu.ga/bower_components/iron-ajax/iron-ajax.html
    └── http://h4k0bu5.hatu.ga/bower_components/paper-spinner/paper-spinner.html
```
