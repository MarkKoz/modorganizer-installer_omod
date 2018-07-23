from kaitaistruct import KaitaiStruct

from .vlq_base128_le import VlqBase128Le

class Manifest(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.files = []
        i = 0

        while not self._io.is_eof():
            self.files.append(self._root.File(self._io, self, self._root))
            i += 1

    class File(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = self._root.FileName(self._io, self, self._root)
            self.crc = self._io.read_u4le()
            self.size = self._io.read_u8le()

    class FileName(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = VlqBase128Le(self._io)
            self.name = (self._io.read_bytes(self.length.value)).decode(
                u"UTF-8")
