var hash = '\x37\x3c\x30\x6c\x3c\x6e\x69\x30\x33\x3c\x6c\x3c\x6c\x3c\x33\x3e\x35\x3c\x62\x60\x3e\x64\x6b\x3e\x6a\x3b\x33\x6e\x30\x3e\x3e\x6f\x39\x6e\x30\x60\x6e\x6b\x33\x39';
var padding = '\x39\x6f\x23\x6a\x7a\x51\x24\x3d\x57\x38\x73\x4e\x3e\x6e\x3f\x6b\x49\x58\x75\x49\x4d\x37\x73\x68\x36\x20\x57\x69\x6c\x62\x44\x50\x78\x60\x31\x26\x59\x46\x35\x7a';
var xor = '\x64\x5b\x63\x6e\x3f\x6b\x2b\x71\x6a\x65\x29\x2f\x4e\x7c\x74\x2e\x77\x6b\x47\x72\x5d\x72\x4f\x2b\x6b\x39\x62\x3d\x32\x79\x2c\x7d\x40\x5a\x79\x62\x3a\x38\x70\x6c\x61\x32\x27\x36\x25\x64\x6e\x29';
var transpose = [0x0, 0x15, 0x0, 0x22, 0x4, 0x9, 0x17, 0x1e, 0xe, 0x5, 0x1d, 0x4, 0x18, 0x16, 0x8, 0x14, 0x1f, 0x11, 0x26, 0x23, 0xf, 0x1, 0xd, 0x6, 0xc, 0x1a, 0x19, 0x1b, 0x21, 0xa, 0x7, 0x10, 0x20, 0x1c, 0x3, 0x13, 0x25, 0x24, 0x12, 0x27];

function check(str) {
    var i = 0;
    while (str.length < 0x28) str += padding[i++ % paddding.length];

    var chars = str.split('');
    for (i=0; i < chars.length; i++) chars[transpose[i]] = str[i];
    for (i=0; i < chars.length; i++) chars[i] = String.fromCharCode(chars[i].charCodeAt(0) ^ (xor.charCodeAt(i) & 0xf));
 
    return chars.join('') == hash;
}

check("3f3939527e73ad93b73b070bb12cde1292bbcde5") // true but wrong

check("5f3949527e73ad93b73b070bb12cde1292bbcde5") // also true, correct (bruteforced)
