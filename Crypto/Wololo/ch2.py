import collections

probability = {
'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127, 'f': 0.022, 'g': 0.020,
'h': 0.061, 'i': 0.070, 'j': 0.002, 'k': 0.008, 'l': 0.040, 'm': 0.024, 'n': 0.067,
'o': 0.075, 'p': 0.019, 'q': 0.001, 'r': 0.060, 's': 0.063, 't': 0.091, 'u': 0.028,
'v': 0.010, 'w': 0.023, 'x': 0.001, 'y': 0.020, 'z': 0.001
}

substitution = {
    'b' : 'i',
    't' : 'a',
    'u' : 'e',
    'i' : 'y',
    'x' : 'b',
    'p' : 'r',
    'v' : 't',
    'k' : 'a'
}

ciphertext = "Tcu xi Unjbpus BB: Vku Tcu xi Obfcs bs t putw-vbnu svptvucd abqux ctnu quauwxjuq hd Ufsunhwu Svlqbxs tfq jlhwbskuq hd Nbepxsxiv. Puwutsuq bf 1999 ixp Nbepxsxiv Zbfqxzs tfq Ntebfvxsk, bv bs vku suexfq ctnu bf vku Tcu xi Unjbpus supbus. Vku Tcu xi Obfcs bs suv bf vku Nbqqwu Tcus tfq exfvtbfs vkbpvuuf jwtdthwu ebabwbgtvbxfs. Jwtdups tbn vx ctvkup pusxlpeus, zkbek vkud lsu vx hlbwq vxzfs, eputvu tpnbus, tfq quiutv vkubp ufunbus. Vkupu tpu ibau kbsvxpbetwwd htsuq etnjtbcfs, zkbek exfsvpbev vku jwtdup vx sjuebtwbguq tfq svxpd-hteouq exfqbvbxfs. Vkupu tpu vkpuu tqqbvbxftw sbfcwu-jwtdup ctnu nxqus, tfq nlwvbjwtdup bs sljjxpvuq."
ciphertext = ciphertext.lower()

def decrypt() : 
    for i in range(len(ciphertext)):
        for k in substitution:
            if ciphertext[i] == k:
                replaced_text = ciphertext.replace(ciphertext[i], substitution[k])
    print(replaced_text)

decrypt()
        
