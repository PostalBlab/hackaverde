SEND_NFC_TAG_PREFIX = b"\x00\x50\x20\x00\x0A\x00\x12\x21\x01"
SEND_NFC_TAG_SUFFIX = b"\x00"

DEBUG_NFC_TAG = b"\x04\xD5\xFF\xA6" \
                    b"\x1A\xC9\x55\x80" \
                    b"\x06\x48\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\xAA\x96\x64\x4B" \
                    b"\x05\xAA\x96\x41" \
                    b"\x32\x78\xAA\xB5" \
                    b"\x5F\x50\x05\xAA" \
                    b"\xB6\x41\x46\x96" \
                    b"\x37\x6E\x5A\x2D" \
                    b"\x23\x01\x0F\x00" \
                    b"\x06\x01\xAB\x13" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x7E\x00\x00\x00"

GRIND_AND_BREW_NFC_TAG = b"\x04\xF7\xA3\xD8" \
                    b"\xC2\xA7\x50\x80" \
                    b"\xB5\x48\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\xAA\xA0\x64\x4B" \
                    b"\x05\xAA\xA0\x41" \
                    b"\x46\x55\xAA\xB2" \
                    b"\x5F\x50\x05\xAA" \
                    b"\xB2\x41\x46\x87" \
                    b"\x37\x5A\x5A\x2D" \
                    b"\x23\x05\x0F\x00" \
                    b"\x06\x01\x32\x0C" \
                    b"\x00\x01\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\xFC\x00\x00\x00"

ROAST_ONLY_NFC_TAG = b"\x04\xE2\xEB\x85" \
                    b"\xC2\xA7\x50\x80" \
                    b"\xB5\x48\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\xAA\xA0\x64\x4B" \
                    b"\x05\xAA\xA0\x41" \
                    b"\x46\x58\xAA\xB2" \
                    b"\x5F\x50\x05\xAA" \
                    b"\xB2\x41\x46\x8C" \
                    b"\x37\x6E\x5A\x2D" \
                    b"\x23\x02\x0F\x00" \
                    b"\x06\x01\x89\x12" \
                    b"\x00\x01\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x8E\x00\x00\x00"

COFFEE_CHANGER_BADGE_NFC_TAG = b"\x04\xD5\xFF\xA6" \
                    b"\x1A\xC9\x55\x80" \
                    b"\x06\x48\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\xAA\x96\x64\x4B" \
                    b"\x05\xAA\x96\x41" \
                    b"\x32\x78\xAA\xA2" \
                    b"\x5F\x50\x05\xAA" \
                    b"\xB6\x41\x46\x96" \
                    b"\x37\x6E\x5A\x2D" \
                    b"\x23\x01\x0F\x00" \
                    b"\x06\x01\xAB\x13" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x7E\x00\x00\x00"

AIRFILTER_MULTI_USE_NFC_TAG = b"\x04\x71\x32\xCF" \
                    b"\x4A\xCF\x59\x80" \
                    b"\x5C\x48\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\xAA\x96\x64\x4B" \
                    b"\x05\xAA\x96\x41" \
                    b"\x32\x78\xAA\xAC" \
                    b"\x5F\x50\x05\xAA" \
                    b"\xB8\x41\x46\x96" \
                    b"\x37\x6E\x5A\x2D" \
                    b"\x23\x0F\x0F\x00" \
                    b"\x06\x01\x84\x6E" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x05\x00\x00\x00"

ADVENTURE_14_SLOW_NFC_TAG = b"\x04\x7F\xFB\x08" \
                    b"\xC2\xA7\x50\x80" \
                    b"\xB5\x48\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\xAA\xB8\x4B\x4B" \
                    b"\x00\xAA\xB8\x32" \
                    b"\x46\x5A\xAA\xB6" \
                    b"\x4B\x5A\x00\xAA" \
                    b"\xB6\x32\x46\x64" \
                    b"\x3C\x46\x5A\x2D" \
                    b"\x32\x01\x2D\x00" \
                    b"\x05\x01\x2C\x6E" \
                    b"\x02\x58\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\xA1\x00\x00\x00"

ADVENTURE_4_QUICKIE_NFC_TAG = b"\x04\x46\x19\xD3" \
                    b"\xC2\xA7\x50\x85" \
                    b"\xB0\x48\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\xAA\xB4\x4B\x4B" \
                    b"\x00\xAA\xB4\x32" \
                    b"\x46\x4B\xAA\xAE" \
                    b"\x4B\x5A\x00\xAA" \
                    b"\xAE\x32\x46\x5A" \
                    b"\x3C\x6E\x5A\x14" \
                    b"\x14\x05\x2D\x00" \
                    b"\x05\x01\x94\x01" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x00\x00\x00\x00" \
                    b"\x8B\x00\x00\x00"