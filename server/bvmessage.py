
import struct
import binascii
from bvpackages import *

def calcCRC(data):
    crc8 = 0
    #calculate only the crc8 without the "OTP" register
    new_data = data[0:12] + data[16:60]
    for single_byte in new_data:
        crc8 ^= single_byte
        for i in range(0,8):
            if (crc8 & 0x80) != 0:
                crc8 = crc8 << 1 ^ 0x7
            else:
                crc8 = crc8 << 1
            
    return crc8 & 0xff

def get_full_nfc_tag_package(nfc_tag):
    #add prefix and suffix
    package = bytearray(build_package(SEND_NFC_TAG_PREFIX + bytearray(nfc_tag).hex().upper().encode() + SEND_NFC_TAG_SUFFIX))

    #calculate new crc and add it to the array
    new_crc = calcCRC(nfc_tag)
    package[len(SEND_NFC_TAG_PREFIX) + 61 * 2] = (55 if (new_crc >> 4) > 9 else 48) + (new_crc >> 4)
    package[len(SEND_NFC_TAG_PREFIX) + 61 * 2 + 1] = (55 if (new_crc >> 4) > 9 else 48) + (new_crc & 0xf)
    return package

def build_package(message):
    msg = struct.pack(">H", len(message))
    msg += message
    return msg