meta:
  id: config
  title: OMOD Config
  application: Oblivion Mod Manager
  license: MIT
  ks-version: 0.8
  encoding: UTF-8
  endian: le
  ks-opaque-types: true
  imports:
    - /common/vlq_base128_le
seq:
  - id: omod_version
    type: u1
  - id: name
    type: string
  - id: major_version
    type: s4
  - id: minor_version
    type: s4
  - id: author
    type: string
  - id: email
    type: string
  - id: website
    type: string
  - id: description
    type: string
  - id: datetime
    type: DateTimeBinary
  - id: file_format
    type: u1
    enum: file_format
  - id: build_version
    type: s4
types:
  string:
    seq:
      - id: length
        type: vlq_base128_le
      - id: value
        type: str
        size: length.value
enums:
  file_format:
    0: lzma
    1: zip
