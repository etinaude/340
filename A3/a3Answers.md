recheck!
ALL OF ONE
ALL OF TWO

# 340 A3

UPI: enau831

ID: 768485633

Name: Etienne Naude

## Question 1 2

16 blocks
4 KiB blocks size
4 Byte block number
4 \* 8 = 32 bit

### 1a

16 \* 4096 =
65,536 bytes

### 1b

262,144

(16 \* 4096)\*2 =
131,072 bytes

### 1c

(16 \* 4096)\*2+
(16 \* 4096)^2 =
4,295,098,368 bytes

### 1d

17,592,186,044,416 bytes

(16 \* 4096)\*2+
(16 \* 4096)^2+
(16 \* 4096)^3 =
281,479,271,809,024 bytes

(2^32)\*4096 =
17,592,186,044,416 bytes

17,592,186,044,416 bytes < 281,479,271,809,024 bytes

since the block number restricts the size most thats the limit

### 1e

4

4 = 18,447,025,552,981,360,000 bytes
3 = 281,479,271,809,024 bytes
aim = 1,152,921,504,606,846,976 bytes

### 1f

2

first block ends at 4096

4050+100 goes over 4096 the next block needs to be accessed as well.

### 1g

2

4,259,820 + 100 extends past the end of the block (block ends at 4,259,840)

### 1h

2

4,263,900 + 100 extends past 4,263,936 therefor uses 2
4,263,936

### 1i

assume overwrites everything

1221
ends at 9,259,820

### 1j

append

### 1k

## Question 2 7

Intel core i5-10120u

Nearly all 64bit processors are backwards compatible with 32bit addresses. This is because many programs don't need to use the whole 32-bit address space, let alone th 64-bit one.

They need to be reprogrammed to take advantage of the full 64-bit address space this is especially relevant for operating systems, which needs to allocate virtual to real addresses.

## Question 3 3

16GB

8KB
1MB

\_ \_ _ 1MB _ \_ \_ ... 1MB ...

bit map
16 000 chunks
(16GB/8KB)/8=
250,000 byte

32

## Question 4 6

4,398,046,511,104 bytes

2^32 \* 1024
not realistic at all. Most programmes wont need it.

## Question 5 6

5000151 \* 0.0001 + 151 \* .99

649.5051ns

## Question 6 0

## Question 7 8

40 seconds

1ns normal
2,000,000ns pf

60

time per fault\* faults = (4 \* 10 ^ 10)ns (40s)
there for there are 60s - 40s = 20s of non errors.
so there are (2\*10^10) non error instructions

2.0e+4 \* 2.0e+6 =
4.0e+10

half the errors

1.0e+4 \* 2.0e+6 =
(2.0e+10)ns (20s)

20s (faults) + 20s (normal running) + 10,000ns =
40,000,000,000+10,000ns = 40,000,010,000 = 40 seconds

## Question 8

### 8a FIFO

|     | 1   | 2   | 3   | 4   | 5   | 4   | 3   | 2   | 1   | 6   | 7   | 1   | 2   | 3   | 7   | 5   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | `=` | `=` | `=` | 5   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | 2   | `=` | `=` | `=` | `=` |
| 0   | `=` | 2   | `=` | `=` | `=` | `=` | `=` | `=` | 1   | `=` | `=` | `=` | `=` | 3   | `=` | `=` | `=` |
| 0   | `=` | `=` | 3   | `=` | `=` | `=` | `=` | `=` | `=` | 6   | `=` | `=` | `=` | `=` | `=` | 5   | `=` |
| 0   | `=` | `=` | `=` | 4   | `=` | `=` | `=` | `=` | `=` | `=` | 7   | `=` | `=` | `=` | `=` | `=` | 1   |

### 8b LRU

|     | 1   | 2   | 3   | 4   | 5   | 4   | 3   | 2   | 1   | 6   | 7   | 1   | 2   | 3   | 7   | 5   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | `=` | `=` | `=` | 5   | `=` | `=` | `=` | 1   | `=` | `=` | `=` | `=` | `=` | `=` | 5   | `=` |
| 0   | `=` | 2   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | 1   |
| 0   | `=` | `=` | 3   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | 7   | `=` | `=` | `=` | `=` | `=` | `=` |
| 0   | `=` | `=` | `=` | 4   | `=` | `=` | `=` | `=` | `=` | 6   | `=` | `=` | `=` | 3   | `=` | `=` | `=` |

### 8c LFU

|     | 1   | 2   | 3   | 4   | 5   | 4   | 3   | 2   | 1   | 6   | 7   | 1   | 2   | 3   | 7   | 5   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | `=` | `=` | `=` | 5   | `=` | `=` | `=` | 1   | 6   | 7   | 1   | 2   | 3   | 7   | 5   | 1   |
| 0   | `=` | 2   | `=` | `=` | `=` | `=` | `=` | +   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` |
| 0   | `=` | `=` | 3   | `=` | `=` | `=` | +   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` |
| 0   | `=` | `=` | `=` | 4   | `=` | +   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` |

### 8d optimal

|     | 1   | 2   | 3   | 4   | 5   | 4   | 3   | 2   | 1   | 6   | 7   | 1   | 2   | 3   | 7   | 5   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | `=` | `=` | `=` | 5   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` |
| 0   | `=` | 2   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | 6   | 7   | `=` | `=` | `=` | `=` | `=` | `=` |
| 0   | `=` | `=` | 3   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` | 2   | 3   | `=` | `=` | `=` |
| 0   | `=` | `=` | `=` | 4   | `=` | `=` | `=` | `=` | 1   | `=` | `=` | `=` | `=` | `=` | `=` | `=` | `=` |
