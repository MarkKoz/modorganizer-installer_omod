from kaitaistruct import KaitaiStruct

class DateTimeBinary(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.date_data = self._io.read_s8le()

    def to_datetime(self):
        pass

    def _to_datetime_raw(self):
        pass
