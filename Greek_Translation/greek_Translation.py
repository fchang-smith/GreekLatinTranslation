source_file_path = '/Users/fiona/Library/Mobile Documents/com~apple~CloudDocs/PHD/Research:Lab/Howe lab/GreekLatinTranslation/PH2219 - IG II2 1.txt'
new_file_path = '/Users/fiona/Library/Mobile Documents/com~apple~CloudDocs/PHD/Research:Lab/Howe lab/GreekLatinTranslation/PH2219 - IG II2 1_Latin.txt'






def greekProxies(str):
    # Define a dictionary mapping Greek characters (both uppercase and lowercase) to Latin equivalents
    eqv = {
        'Α': 'A', 'Β': 'B', 'Γ': 'G', 'Δ': 'D', 'Ε': 'E', 'Ζ': 'Z', 'Η': 'H',
        'Θ': 'Q', 'Ι': 'I', 'Κ': 'K', 'Λ': 'L', 'Μ': 'M', 'Ν': 'N', 'Ξ': 'X',
        'Ο': 'O', 'Π': 'P', 'Ρ': 'R', 'Σ': 'S', 'Τ': 'T', 'Υ': 'U', 'Φ': 'F',
        'Χ': 'C', 'Ψ': 'Y', 'Ω': 'W',
        'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'h',
        'θ': 'q', 'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x',
        'ο': 'o', 'π': 'p', 'ρ': 'r', 'σ': 's', 'ς': 's', 'τ': 't', 'υ': 'u',
        'φ': 'f', 'χ': 'c', 'ψ': 'y', 'ω': 'w',
        'ά': 'a', 'έ': 'e', 'ή': 'h', 'ί': 'i', 'ό': 'o', 'ύ': 'u', 'ώ': 'w',
        'ϊ': 'i', 'ϋ': 'u', 'ΐ': 'i', 'ΰ': 'u',
        'ἀ': 'a', 'ἁ': 'a', 'ἂ': 'a', 'ἃ': 'a', 'ἄ': 'a', 'ἅ': 'a', 'ἆ': 'a', 'ἇ': 'a',
        'ἐ': 'e', 'ἑ': 'e', 'ἒ': 'e', 'ἓ': 'e', 'ἔ': 'e', 'ἕ': 'e',
        'ἠ': 'h', 'ἡ': 'h', 'ἢ': 'h', 'ἣ': 'h', 'ἤ': 'h', 'ἥ': 'h', 'ἦ': 'h', 'ἧ': 'h',
        'ἰ': 'i', 'ἱ': 'i', 'ἲ': 'i', 'ἳ': 'i', 'ἴ': 'i', 'ἵ': 'i', 'ἶ': 'i', 'ἷ': 'i',
        'ὀ': 'o', 'ὁ': 'o', 'ὂ': 'o', 'ὃ': 'o', 'ὄ': 'o', 'ὅ': 'o',
        'ὐ': 'u', 'ὑ': 'u', 'ὒ': 'u', 'ὓ': 'u', 'ὔ': 'u', 'ὕ': 'u', 'ὖ': 'u', 'ὗ': 'u',
        'ὠ': 'w', 'ὡ': 'w', 'ὢ': 'w', 'ὣ': 'w', 'ὤ': 'w', 'ὥ': 'w', 'ὦ': 'w', 'ὧ': 'w',
        'ᾀ': 'a', 'ᾁ': 'a', 'ᾂ': 'a', 'ᾃ': 'a', 'ᾄ': 'a', 'ᾅ': 'a', 'ᾆ': 'a', 'ᾇ': 'a',
        'ᾐ': 'h', 'ᾑ': 'h', 'ᾒ': 'h', 'ᾓ': 'h', 'ᾔ': 'h', 'ᾕ': 'h', 'ᾖ': 'h', 'ᾗ': 'h',
        'ᾠ': 'w', 'ᾡ': 'w', 'ᾢ': 'w', 'ᾣ': 'w', 'ᾤ': 'w', 'ᾥ': 'w', 'ᾦ': 'w', 'ᾧ': 'w',
        'ᾰ': 'a', 'ᾱ': 'a', 'ᾲ': 'a', 'ᾳ': 'a', 'ᾴ': 'a', 'ᾶ': 'a', 'ᾷ': 'a',
        'ῂ': 'h', 'ῃ': 'h', 'ῄ': 'h', 'ῆ': 'h', 'ῇ': 'h',
        'ῐ': 'i', 'ῑ': 'i', 'ῒ': 'i', 'ΐ': 'i', 'ῖ': 'i', 'ῗ': 'i',
        'ῠ': 'u', 'ῡ': 'u', 'ῢ': 'u', 'ΰ': 'u', 'ῤ': 'r', 'ῥ': 'r',
        'ῤ': 'r', 'ῥ': 'r', 'ῦ': 'u', 'ῧ': 'u', 'ῲ': 'o', 'ῳ': 'o', 'ῴ': 'o', 'ῶ': 'o', 'ῷ': 'o', 'Ἀ': 'A', 
        'ί': 'i', 'ὺ': 'u', 'ὶ': 'i', 'ά': 'a', 'έ': 'e', 'ὰ': 'a', 'ή': 'h', 'ό': 'o', 'ώ': 'o', 'o͂': 'w',
        'ὴ': 'h', 'e͂': 'e', 'o͂': ''
    }

    txt = []
    for char in str:
        if char in eqv:
            txt.append(eqv[char])
        else:
            txt.append(char)
    return ''.join(txt)

# Test the function
# input_text = "Γειά σας, Κόσμε! αβγδε"
# output_text = greekProxies(input_text)
# print(output_text)

try:
    with open(source_file_path, 'r') as source_file:
        with open(new_file_path, 'w') as new_file:
            for line in source_file:
                line = greekProxies(line)
                new_file.write(line)
    
    print(f"File '{source_file_path}' copied to '{new_file_path}' successfully.")
except FileNotFoundError:
    print(f"File '{source_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")