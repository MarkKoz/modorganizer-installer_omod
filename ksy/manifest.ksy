meta:
  id: manifest
  title: OMOD File Manifest
  application: Oblivion Mod Manager
  file-extension: crc
  license: MIT
  ks-version: 0.8
  encoding: UTF-8
  endian: le
  imports:
    - /common/vlq_base128_le
seq:
  - id: files
    type: file
    repeat: eos
types:
  file:
    seq:
      - id: name
        type: file_name
      - id: crc
        type: u4
      - id: size
        type: u8
  file_name:
     seq:
      - id: length
        type: vlq_base128_le
      - id: name
        type: str
        size: length.value
