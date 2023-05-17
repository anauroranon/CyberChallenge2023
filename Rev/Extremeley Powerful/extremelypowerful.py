from z3 import *

s = Solver()

a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21 = BitVecs("a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15 a16 a17 a18 a19 a20 a21", 8)

s.add((a12 - a17 + a12 + a8) == 153)
s.add((a10 + a21 + (a19 ^ a2)) == 217)
s.add(((a5 ^ a16) + a16 + a3 + (a0 ^ a16)) == 232)
s.add((a10 + a3 + a3 - a19 + (a19 ^ a0))==328)
s.add((a10 - a8 + a2 - a19) == 74)
s.add((a17 - a1 + a4 + a11 + a17 - a9) == 166)
s.add((a14 + a10 + a18 - a9 + a5 + a10) == 413)
s.add((a5 - a16 + a8 - a12 + a17 - a13 + a11 - a2 + a1 + a21) == 98)
s.add(((a19 ^ a13) + a6 - a13 + a17 - a11 + (a16 ^ a12)) == 85)
s.add((a4 - a16 + (a2 ^ a7)) == 77)
s.add((a8 - a17 + a14 - a3 + (a8 ^ a14) + a5 + a1 + a7 + a10) == 384)
s.add((a4 - a0 + a2 - a4 + a15 - a21 + a17 + a2) == 265)
s.add((a5 - a18 + a17 - a4 + a15 + a2 + a21 - a18 + a7 + a6) == 250)
s.add((a21 - a19 + a7 - a18 + a16 - a21 + (a12 ^ a18)) == 75)
s.add(((a10 ^ a2) + a2 + a7 + a20 + a13 + (a3 ^ a16) + a9 + a6)  == 621)
s.add((a8 - a3 + (a14 ^ a2) + a11 + a0 + a1 - a19) == 283)
s.add((a16 - a14 + (a0 ^ a11) + (a0 ^ a14) + a13 - a19) == 106)
s.add((a19 + a10 + a10 + a19 + a0 - a20 + a3 - a18) == 297)
s.add((a0 - a15 + a20 + a18) == 156) 
s.add((a13 - a8 + a10 - a20 + a3 - a17) == 85)
s.add((a3 - a17 + a19 + a4 + (a12 ^ a17) + a10 - a2)== 160)
s.add((a11 - a21 + a12 - a10) == 36)
s.add(((a18 ^ a19) + a6 - a16 + (a5 ^ a16)) == 102)
s.add((a6 - a13 + (a10 ^ a15) + a21 - a5) == -48)
s.add(((a5 ^ a3) + a12 - a11 + (a6 ^ a4)) == 29)
s.add((a6 - a14 + a9 - a2 + a8 - a15 + a21 - a11) == -109)
s.add((a19 - a7 + a0 + a16 + a11 + a17) == 361)
s.add((a3 + a15 + (a15 ^ a19)) == 296)



print(s.check())
model = s.model()

flag = ""

for v in [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19, a20, a21]:
    flag += chr(model[v].as_long())

print(flag)


