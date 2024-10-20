from enum import IntEnum


class Units(IntEnum):
    Byte = 1
    KB = 1024
    MB = 1024 * KB
    GB = 1024 * MB
    PAGE = 4 * KB

MEM_DATA = [
    0x9A2F13476C05B3A2, 0x3E984FDBA64C8179, 0x6D7BAE908ECCBEF3, 0x48826F1DA5E62317,
    0x1048D952BC3A67E9, 0x5AEC8B6F97F1D023, 0x7B1C3D8A25F699C6, 0x81B6FA3ED597AC0F,
    0x2C5D970F8A1B4E63, 0x4FED3B9C6A78D501, 0xA8BC602F3EFA7D94, 0x74D1A9EC59E6FCA8,
    0xD08C416A3B759F21, 0x672E8A94B1CD2F7E, 0xE45F17B82A60EC19, 0xFA903257E1268CD4,
    0xC5AEDB1F987ABD62, 0x8D6A051BFA43E718, 0x5392F8DFA0CE647B, 0xB240ECB5C3F58A26
]