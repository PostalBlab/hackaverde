-- 00 --
00
01
02
03
-- 01 --
04
05
06
07
-- 02 --
08
09
10
11
-- 03 --
12 - OTP, check in bv_check_NFC_data
13 - OTP, check in bv_check_NFC_data
14 - OTP, check in bv_check_NFC_data
15 - OTP, check in bv_check_NFC_data
-- 04 --
16 - with 17
17 - with 18
18 - with 16,17 as parameter of 3d96

    could be first roast phase
19 - if < 14, set to 14, used as parameter bv_set_TIM4_CCR3_to_param1_max_100, FUN_08004236
-- 05 --
20
21 - with 22
22 - with 23
23 - with 21,22 as parameter of 3d96
-- 06 --
24 - FUN_08004236
25 - wird mit 0x14 multipliziert?!
26 - with 27
27 - with 28
-- 07 --
28 - with 26,27 as parameter of 3d96
29 - parameter für bv_set_TIM4_CCR3_to_param1_max_100, FUN_08004236
30
31 - with 33
-- 08 --
32 - with 33
33 - with 31,32 as parameter of 3d96
34 - parameter für bv_set_TIM4_CCR3_to_param1_max_100, FUN_08004236
35 - * 0x14
-- 09 --
36
37
38 - FUN_08004236
39
-- 0A --
40 - gets multiplied by 5 or 10 in 42dc
41 - 2000 0012 wird auf den wert gesetzt, anschließend X > 0x13 || X == 0 => 2000 000c & 0xFDFF
    wenn 0 oder grö0er 0x13 wird 2000000c & 0xfdff gesäubert
         ((((DAT_20000012 != 0) && (DAT_20000012 < 7)) || (DAT_20000012 == 0xf)) || ((DAT_20000012 == 0x12 || (DAT_20000012 == 0x13)))) && ((bVar4 && (DAT_2000000e != 1)))
         validiert zu true bei 1, 2, 3, 4, 5, 6, 15 - 0xF , 18 - 0x12, 19 - 0x13, scheint bei allen tags der fall zu sein

    0x0f definitly resets airfilter counter if it is 0x0f
    0x11 set airfilter to 0x1e which means you need a reset
    0x0a green light, roasting chamber rotating, then blue light
    
    1,2,4,5,f haben die tags die ich habe
42 - *600 <= 20000392
43
-- 0B --
44
45
46 - with 47
47 - merge with 46 in bv_check_NFC
    if both are 0, the tag does not get resetted
-- 0C --
48 - merge mit 49
49 - merge mit 48, wird mit 2000 0396 verglichen
        if (((uint)NFC_TAG_DATA_ARRAY[49] + (uint)NFC_TAG_DATA_ARRAY[48] * 0x100 & 0xffff) == 0) {
            DAT_20000394 = 0
            bv_set_statemachine_flag(4);
            bv_set_2000000f(0x14);
            bVar1 = actuator_shift_values; }
50
51
-- 0D --
52
53
54
55
-- 0E --
56
57
58
59
-- 0F --
60 - crc8 checksum without addr 03
61
62
63





-- 10 -- Mifare stuff
64
65
66
67
-- 11 -- Mifare stuff
68
69
70
71
-- 12 -- Mifare stuff
72
73
74
75
-- 13 -- Mifare stuff
76
77
78
79

