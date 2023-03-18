# Function to get all the divisors of the given number
def getDivisors(number):
    divisors = []

    for d in range(2, number):
        if number % d == 0:
            divisors.append(d)
    
    return divisors

# Function to find the tuples in the text and returns the number of tuples and
# a list with the divisors of all the tuples

def getTuples(list):
    frequency = [] # WIll contain the divisors 
    count = 0 # WIll contain the number of tuples
    i = 0

    while i < len(list):
        elt = list[i:i+3] # Takes three elements at time
        long = len(elt)

        if long == 3: # If it is not 3 we are at the end of the list
            for j in range (i+1, len(list)): # Search in the list if there is the same pattern
                if list[i:i+long] == list[j:j+long]: # If two pairs of three characters are the same, we check if other characters of this two pairs are the same
                    while list[i:i+long] == list[j:j+long]:
                        long = long+1
                    long = long-1

                    elt = list[i:i+long] # A tuple
                    diff = j - i # Distance between the two pairs of equal chars

                    frequency.extend(getDivisors(diff)) # Add the divisors to the list
                    count = count + 1 # Number of equal found tuples
                    j = j + long + 1 
            i = i + long - 3 + 1
        else :
            i = i + 1
        return count, frequency

# Count each divisor and sort divisors in descending order.
# The returning list will have the divisors and the number of times that divisor appears in the list
# You need hand reasoning to guess the key
def countOcc(frequency):
    d={}

    for elt in frequency:
        if elt in d:
            d[elt] += 1
        else:
            d[elt] = 1
    
    return sorted(d.items(), key = lambda x: x[1], reverse=True)

if __name__ == "__main__": 
    ciphertext = "XSIQNFKAHPPCTINAWLPSTOCCSOICSHYENFHWPOKESQEFOCIEEHVWGHVNMYWOERZNMLRZNBXUERIOARGRSXYZTOKEHMCHUSZUHPBSYSRNSCSTNFSOVPEWGKRSMYJCEQVIRDEFQWEIEFRHVZZTALWGHDVRWPHSQPPTLPWOICPAVOGCQSFFGSEFYSJFIWMLGVVCECXOJOJAAZVYBTXRILXWZDFRXLRQRWESECHWAWRNLTWHBFPIXHEGNBFRKLRWPQFHICIBGOEDWJWHRARTMNACEYFFPPKWFZRTMZRSAQFMTLWGVBXTLPGWIWCAROTSAOCLEHXVRVZSXZVMBTKHIOVOSHZNKZJHUSTAVEEWFIEKRZABOIKTLPGOEHRIXDIZSDIOZTHSFOEEBNIZYSETKWMACGVIRESHUSVTLYSZBUZCEWEBQZZNKFMGGWTSMEYOGWFNSQPOGSDEHTIJNZJAVOMBVOZNXSIQNFKAXSIFRWJTLPQCQSINMKMBTCWCICXOVBEOVXWOARKHIUYFVRZCEWAWFRFMXSEHPCETETRGRZVMIYXGBTKHICSANBTARZRWPOCTVLHWGWFNXSIPLNRNXTRSBBVTLPFCYCXNIDIXHFZSTCYRRBTEEYHHUSKHSFKVGCWTLPKZBGJAXZVGBTKHINEHNZRNGZYFGQLLXFVSOIKAFZZSNZCTLPPCPOCJYCMRVQRLIWEPBFRTMZRCSHYEWLVRVBZARNYGGCDSQLHSOMJAVOMBVOEMYYMQVDRLPLACASEOXLFZRDIOZTWWBBFFXSIQBRVIWELOGWKGEGIRNIXHXPVGNBUSSYWHUSJAQPMBUSIIXLRQRFZGLEWOFKVLPTXOYGFDINPOESUTLLXFNDVCSFPROSIEGZQDRBJEHELFBIXHQLVFVOXESYPMVTKHIHSANBNHSHEGEOGEHLKFRSUTSXEFEMYEVCEDVGKAROIJRBZFWSIRVRKHINSRRRVCPLVSQHYAXELSEOGIWEWHVZCHEOXCRWKHICTOLOCAVRITVBVTSELSFSEAXPSFUOMELTWTBCKCYESTSVZSGSSWPSZFWSIRVREOXLKFRSKOQLVFLVZMLPLOQHFGMGIVRFRDSHVMGVRTWFMHRRYEVDSQVOCSXLXIFGFTLLXGUSTOYWHANFIYWZQSBBVEPDIOARYEWEMZYVRDXZIWGVVRTLCOYOIGIQMBRHFTLPWSAOKESCLOISYIWQSCGQLTSQJVVGTHSTGSNGNEPWXVRGVPYYMGUAVNXDASESEOXLJTRQKEHMCKUSKHICSFACKTLPACZOEIRBYSFHZORHEGOSKRSELSQHYEGZHSNZJOGLYGRRVLILRCECWAVMSFROKOFPVSZSDBICIRNGFNIZJHUSWIVDXZNKDAOPVGGCJEXFTHUSTOROMHVCEOJCIQVDIOGTXMJVVNHPEZVBXWMELTBFVIKYIFFOJWIWPOFHYEGCMARCWMMDJSNGRNGP"
    cipherlist = list(ciphertext)
    count, frequency = getTuples(cipherlist)
    divisors = countOcc(frequency)

    print("\nDivisors and their frequency:\n  ",divisors)

