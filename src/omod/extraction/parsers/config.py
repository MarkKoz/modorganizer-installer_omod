from enum import Enum
from kaitaistruct import KaitaiStruct

from .datetime_binary import DateTimeBinary
from .vlq_base128_le import VlqBase128Le

class Config(KaitaiStruct):
    class FileFormat(Enum):
        LZMA = 0
        ZIP = 1

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.omod_version = self._io.read_u1()
        self.name = self._root.String(self._io, self, self._root).value
        self.major_version = self._io.read_s4le()
        self.minor_version = self._io.read_s4le()
        self.author = self._root.String(self._io, self, self._root).value
        self.email = self._root.String(self._io, self, self._root).value
        self.website = self._root.String(self._io, self, self._root).value
        self.description = self._root.String(self._io, self, self._root).value
        self.datetime = DateTimeBinary(self._io).to_datetime()
        self.file_format = self._root.FileFormat(self._io.read_u1())
        self.build_version = self._io.read_s4le()

    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = VlqBase128Le(self._io)
            self.value = (self._io.read_bytes(self.length.value)).decode(
                u"UTF-8")
