# Crypac

Crypac is a tool for packing and encrypting private cryptocurrency assets like private keys and seeds

## Table of contents
1. [Installation](#installation)
2. [Example usage](#usage)
    1. [Packing, encrypting, decrypting, unpacking](#example1)
    2. [Preparing and packing wif(base58)](#example2)
    3. [Preparing and packing bip39(mnemonic seed phrase)](#example3)
3. [Help](#help)

## Installation <a name="installation" />
```
python3 setup.py install
```

## Usage <a name="usage" />
Below are a few examples on how to use crypac

### Packing, encrypting, decrypting, unpacking <a name="example1" />
```
crypac pack \
--dot 4a404cb38c0c1929213c4a33d8ac564ec5c04ade8beb8dd18c5c11fdaf5afc0f \
--eth 64ec5c04ade8beb8dd18c5c11fdaf5afc0f39363bf6a6feefae6a1860d2e61c1 \
--eth 322393e47927ac31e06981a482a70b02519cf3873a7d2923ad4a53a6bd25abcd > pac

xxd pac
00000000: 0464 ec5c 04ad e8be b8dd 18c5 c11f daf5  .d.\............
00000010: afc0 f393 63bf 6a6f eefa e6a1 860d 2e61  ....c.jo.......a
00000020: c104 3223 93e4 7927 ac31 e069 81a4 82a7  ..2#..y'.1.i....
00000030: 0b02 519c f387 3a7d 2923 ad4a 53a6 bd25  ..Q...:})#.JS..%
00000040: abcd 054a 404c b38c 0c19 2921 3c4a 33d8  ...J@L....)!<J3.
00000050: ac56 4ec5 c04a de8b eb8d d18c 5c11 fdaf  .VN..J......\...
00000060: 5afc 0f                                  Z..

crypac pack --dot 5d70c9715012cd3ced029c0b6381dd6a284cce0f3f83d4e0a22c17bc843e9dd5 >> pac

xxd pac
00000000: 0464 ec5c 04ad e8be b8dd 18c5 c11f daf5  .d.\............
00000010: afc0 f393 63bf 6a6f eefa e6a1 860d 2e61  ....c.jo.......a
00000020: c104 3223 93e4 7927 ac31 e069 81a4 82a7  ..2#..y'.1.i....
00000030: 0b02 519c f387 3a7d 2923 ad4a 53a6 bd25  ..Q...:})#.JS..%
00000040: abcd 054a 404c b38c 0c19 2921 3c4a 33d8  ...J@L....)!<J3.
00000050: ac56 4ec5 c04a de8b eb8d d18c 5c11 fdaf  .VN..J......\...
00000060: 5afc 0f05 5d70 c971 5012 cd3c ed02 9c0b  Z...]p.qP..<....
00000070: 6381 dd6a 284c ce0f 3f83 d4e0 a22c 17bc  c..j(L..?....,..
00000080: 843e 9dd5                                .>..

cat pac | crypac unpack
ETH 64ec5c04ade8beb8dd18c5c11fdaf5afc0f39363bf6a6feefae6a1860d2e61c1
ETH 322393e47927ac31e06981a482a70b02519cf3873a7d2923ad4a53a6bd25abcd
DOT 4a404cb38c0c1929213c4a33d8ac564ec5c04ade8beb8dd18c5c11fdaf5afc0f
DOT 5d70c9715012cd3ced029c0b6381dd6a284cce0f3f83d4e0a22c17bc843e9dd5

cat pac | crypac encrypt "P4$$word" > pac.enc

xxd pac.enc
00000000: 95b6 a307 8afc cfe9 4ffb a53e b7fa 615d  ........O..>..a]
00000010: f599 ac3a d07b 3c24 b44e 745d cf93 e240  ...:.{<$.Nt]...@
00000020: d491 d320 84bb 8b3e ae28 b34e 8843 b15a  ... ...>.(.N.C.Z
00000030: 1591 eb61 ded4 fa31 89aa 592b 7dd3 fa27  ...a...1..Y+}..'
00000040: 9a2c bc92 2f85 5d56 6a05 1985 4113 de2c  .,../.]Vj...A..,
00000050: 752b dcf2 3535 e7fe 8f64 5cc0 1d4a f718  u+..55...d\..J..
00000060: 13f5 657e 5a22 c8df 7533 3bf9 051e b39c  ..e~Z"..u3;.....
00000070: ba37 bc5a 8b31 f1f4 8ba4 90b1 9f6b 22f6  .7.Z.1.......k".
00000080: 49e3 0346 959e d0a2 4574 89d8 e98a c00d  I..F....Et......

cat pac.enc | crypac decrypt "P4$$word" | crypac unpack
ETH 64ec5c04ade8beb8dd18c5c11fdaf5afc0f39363bf6a6feefae6a1860d2e61c1
ETH 322393e47927ac31e06981a482a70b02519cf3873a7d2923ad4a53a6bd25abcd
DOT 4a404cb38c0c1929213c4a33d8ac564ec5c04ade8beb8dd18c5c11fdaf5afc0f
DOT 5d70c9715012cd3ced029c0b6381dd6a284cce0f3f83d4e0a22c17bc843e9dd5
```

### Preparing and packing wif(base58) <a name="example2" />

```
crypac convert base58 5JquJyTAucte3F25QGMyovp5VSzzhPmuVqGHg67igTJikcFr3Je
80875d8f49faf8df4568b38220458d89f3a0cba1e0c5a665d27112411771d711e8aad53fef

crypac pack --btc 80875d8f49faf8df4568b38220458d89f3a0cba1e0c5a665d27112411771d711e8aad53fef > pac

xxd pac 
00000000: 0325 8087 5d8f 49fa f8df 4568 b382 2045  .%..].I...Eh.. E
00000010: 8d89 f3a0 cba1 e0c5 a665 d271 1241 1771  .........e.q.A.q
00000020: d711 e8aa d53f ef                        .....?.

cat pac | crypac unpack
BTC 80875d8f49faf8df4568b38220458d89f3a0cba1e0c5a665d27112411771d711e8aad53fef

crypac convert --reverse base58 80875d8f49faf8df4568b38220458d89f3a0cba1e0c5a665d27112411771d711e8aad53fef
5JquJyTAucte3F25QGMyovp5VSzzhPmuVqGHg67igTJikcFr3Je
```

### Preparing and packing bip39(mnemonic seed phrase) <a name="example3" />

```
crypac convert bip39 rug manage involve element need city iron churn jacket neutral master flock
bd10ddd8a3d93c52dd914677129e22ac

crypac pack --sol bd10ddd8a3d93c52dd914677129e22ac > pac

xxd pac
00000000: 0210 bd10 ddd8 a3d9 3c52 dd91 4677 129e  ........<R..Fw..
00000010: 22ac                                     ".

cat pac | crypac unpack
SOL bd10ddd8a3d93c52dd914677129e22ac

crypac convert --reverse bip39 bd10ddd8a3d93c52dd914677129e22ac
rug manage involve element need city iron churn jacket neutral master flock
```

## Help <a name="help" />
```
usage: crypac [-h] [--verbose {DEBUG,INFO,WARNING,ERROR}] {pack,unpack,encrypt,decrypt,convert} ...

Process some integers.

positional arguments:
  {pack,unpack,encrypt,decrypt,convert}

optional arguments:
  -h, --help            show this help message and exit
  --verbose {DEBUG,INFO,WARNING,ERROR}
```

## Pack
```
usage: crypac pack [-h] [--xdg hex] [--sol hex] [--btc hex] [--eth hex] [--dot hex]

optional arguments:
  -h, --help  show this help message and exit
  --xdg hex
  --sol hex
  --btc hex
  --eth hex
  --dot hex
```

## Unpack
unpacks data from stdin

## Convert
Converting bip39 mnemonics and wif to hex for packing
```
usage: crypac convert [-h] [--reverse] {base58,bip39} ...

positional arguments:
  {base58,bip39}

optional arguments:
  -h, --help      show this help message and exit
  --reverse
```
