#
_bytes1: list[int] = [1, 2, 3]
_bytearray1: bytearray = bytearray(_bytes1)

_bytes2: list[int] = [1, 2, 3]
_bytearray2: bytearray = bytearray(_bytes2)

_are_they_the_same: bool = _bytearray1 == _bytearray2
print(f"are they the same? {_are_they_the_same}")