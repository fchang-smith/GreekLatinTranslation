import numpy as np

source_file_path = '/Users/alinemarrap/Howe Annotations/GreekLatinTranslation/PH2219 - IG II2 1.txt'
new_file_path = '/Users/alinemarrap/Howe Annotations/GreekLatinTranslation/test.txt'

def main(stringin):
  #substitutions
  eqv = np.array( ['*'] * 15000)
  for i in range(0, 254):
    eqv[1] = chr(i)
  
  # characters
  eqv[913] = 'A'   # ALPHA
  eqv[7944] = 'A'   # ALPHA + AIGU
  eqv[914] = 'B'   # BETA
  eqv[915] = 'G'  # GAMMA
  eqv[916] = 'D'  # DELTA
  eqv[917] = 'E'  # EPSILON
  eqv[918] = 'Z'  # ZETA
  eqv[919] = 'H'  # ETA
  eqv[920] = 'Q'  # THETA
  eqv[921] = 'I'  # IOTA  
  eqv[922] = 'K'  # KAPPA
  eqv[923] = 'L'  # LAMDA
  eqv[924] = 'M'  # MU
  eqv[925] = 'N'  # NU
  eqv[926] = 'X'  # XI
  eqv[927] = 'O'  # OMICRON
  eqv[928] = 'P'  # PI
  eqv[929] = 'R'  # PI
  eqv[931] = 'S'  # SIGMA
  eqv[932] = 'T'  # TAU
  eqv[933] = 'U'  # UPSILON
  eqv[934] = 'F'  # PHI
  eqv[935] = 'Y'  # PSI
  eqv[936] = 'C'  # CHI
  eqv[937] = 'W'  # OMEGA
  eqv[945] = 'a'   # ALPHA
  eqv[8118] = 'a'  # ALPHA + TILDE
  eqv[8119] = 'a'  # ALPHA + TILDE + CEDILLE
  eqv[7942] = 'a'  # ALPHA + TILDE + TICK
  eqv[7943] = 'a'  # ALPHA + TILDE + BACKTICK
  eqv[8070] = 'a'  # ALPHA + TILDE + TICK + CEDILLE
  eqv[8071] = 'a'  # ALPHA + TILDE + BACKTICK + CEDILLE
  eqv[8048] = 'a'  # ALPHA + GRAVE
  eqv[8049] = 'a'  # ALPHA + AIGU
  eqv[7936] = 'a'   # ALPHA + TICK
  eqv[7937] = 'a'   # ALPHA +BACKTICK
  eqv[7940] = 'a'   # ALPHA + TICK + AIGU
  eqv[7941] = 'a'   # ALPHA + BACKTICK + AIGU
  eqv[7938] = 'a'   # ALPHA + TICK + GRAVE
  eqv[7939] = 'a'   # ALPHA + BACKTICK + GRAVE
  eqv[946] = 'b'   # BETA
  eqv[947] = 'g'  # GAMMA
  eqv[948] = 'd'  # DELTA
  eqv[949] = 'e'  # EPSILON
  eqv[7952] = 'e'  # EPSILON + TICK
  eqv[7953] = 'e'  # EPSILON + BACKTICK
  eqv[8050] = 'e'  # EPSILON + GRAVE
  eqv[8051] = 'e'  # EPSILON + AIGU
  eqv[7956] = 'e'  # EPSILON + TICK + AIGU
  eqv[7957] = 'e'  # EPSILON + BACKTICK + AIGU
  eqv[7954] = 'e'  # EPSILON + TICK + GRAVE
  eqv[7955] = 'e'  # EPSILON + BACKTICK + GRAVE
  eqv[950] = 'z'  # ZETA
  eqv[951] = 'h'  # ETA
  eqv[7974] = 'h'  # ETA + TILDE + TICK + CEDILLE
  eqv[7975] = 'h'  # ETA + TILDE + BACKTICK + CEDILLE
  eqv[8086] = 'h'  # ETA + TILDE + TICK
  eqv[8087] = 'h'  # ETA + TILDE + BACKTICK
  eqv[8134] = 'h'  # ETA + TILDE 
  eqv[8135] = 'h'  # ETA + TILDE + CEDILLE
  eqv[7970] = 'h'  # ETA + TICK + GRAVE
  eqv[7971] = 'h'  # ETA + BACKTICK + GRAVE
  eqv[8016] = 'h'  # ETA + TICK?
  eqv[8020] = 'h'  # ETA + TICK + AIGU
  eqv[7968] = 'h'  # ETA + TICK
  eqv[7969] = 'h'  # ETA + BACKTICK
  eqv[7972] = 'h'  # ETA + TICK + AIGU
  eqv[7973] = 'h'  # ETA + BACKTICK + AIGU
  eqv[8052] = 'h'  # ETA + GRAVE
  eqv[8053] = 'h'  # ETA + AIGU ?
  eqv[952] = 'q'  # THETA
  eqv[953] = 'i'  # IOTA
  eqv[7990] = 'i'  # IOTA + TILDE + TICK
  eqv[7991] = 'i'  # IOTA + TILDE + BACKTICK
  eqv[8150] = 'i'  # IOTA + TILDE     
  eqv[8054] = 'i'  # IOTA + GRAVE     
  eqv[8055] = 'i'  # IOTA + AIGU     
  eqv[7984] = 'i'  # IOTA + TICK     
  eqv[7985] = 'i'  # IOTA + BACKTICK    
  eqv[7988] = 'i'  # IOTA + TICK + AIGU     
  eqv[7989] = 'i'  # IOTA + BACKTICK + AIGU   
  eqv[7986] = 'i'  # IOTA + TICK + GRAVE     
  eqv[7987] = 'i'  # IOTA + BACKTICK + GRAVE   
  eqv[954] = 'k'  # KAPPA
  eqv[955] = 'l'  # LAMDA
  eqv[956] = 'm'  # MU
  eqv[957] = 'n'  # NU
  eqv[834] = 'n'  # NU + TILDE
  eqv[958] = 'x'  # XI
  eqv[959] = 'o'  # OMICRON
  eqv[8056] = 'o'  # OMICRON + GRAVE
  eqv[8057] = 'o'  # OMICRON + AIGU
  eqv[8000] = 'o'  # OMICRON + TICK 
  eqv[8001] = 'o'  # OMICRON + BACKTICK 
  eqv[8004] = 'o'  # OMICRON + TICK + AIGU
  eqv[8005] = 'o'  # OMICRON + BACKTICK + AIGU
  eqv[8002] = 'o'  # OMICRON + TICK + GRAVE 
  eqv[8003] = 'o'  # OMICRON + BACKTICK + GRAVE 
  eqv[960] = 'p'  # PI
  eqv[961] = 'r'  # RHO
  eqv[962] = 'v'  # SIGMA
  eqv[963] = 's'  # SIGMA
  eqv[964] = 't'  # TAU
  eqv[965] = 'u'  # UPSILON
  eqv[8022] = 'u'  # UPSILON + TILDE + TICK
  eqv[8023] = 'u'  # UPSILON + TILDE + BACKTICK
  eqv[8166] = 'u'  # UPSILON + TILDE 
  eqv[8016] = 'u'  # UPSILON + TICK 
  eqv[8017] = 'u'  # UPSILON + BACKTICK 
  eqv[8020] = 'u'  # UPSILON + TICK + AIGU 
  eqv[8021] = 'u'  # UPSILON + BACKTICK + AIGU 
  eqv[8018] = 'u'  # UPSILON + TICK + GRAVE 
  eqv[8019] = 'u'  # UPSILON + BACKTICK + GRAVE 
  eqv[8058] = 'u'  # UPSILON + GRAVE 
  eqv[8059] = 'u'  # UPSILON + AIGU ? 
  eqv[966] = 'f'  # PHI
  eqv[967] = 'y'  # PSI
  eqv[968] = 'c'  # CHI
  eqv[969] = 'w'  # OMEGA
  eqv[8102] = 'w'  # OMEGA + TILDE + TICK + CEDILLE
  eqv[8103] = 'w'  # OMEGA + TILDE + BACKTICK + CEDILLE
  eqv[8038] = 'w'  # OMEGA + TILDE + TICK
  eqv[8039] = 'w'  # OMEGA + TILDE + BACKTICK
  eqv[8182] = 'w'  # OMEGA + TILDE 
  eqv[8183] = 'w'  # OMEGA + TILDE + CEDILLE
  eqv[8060] = 'w'  # OMEGA + GRAVE
  eqv[8061] = 'w'  # OMEGA + AIGU
  eqv[8032] = 'w'  # OMEGA + TICK
  eqv[8033] = 'w'  # OMEGA + BACKTICK
  eqv[8036] = 'w'  # OMEGA + TICK + AIGU
  eqv[8037] = 'w'  # OMEGA + BACKTICK + AIGU
  eqv[8034] = 'w'  # OMEGA + TICK + GRAVE
  eqv[8035] = 'w'  # OMEGA + BACKTICK + GRAVE

  eqv[8217] = "'"  # TICK???
  eqv[8025] = '`'  # BACKTICK???
  eqv[803] = '_'  # CEDILLE???
  eqv[8195] = ' '  # WEIRD SPACE???
  eqv[903] = '.'  # WEIRD DOT???
  eqv[8228] = '.'  # WEIRD DOT???
  eqv[8311] = '7'  # SUPERSCRIPT 7

  # Formatting characters
  eqv[10] = "\n"  # CARRIAGE RETURN
  eqv[3] = ' '  # SPACE
  eqv[32] = ' '  # SPACE


  if (isinstance(stringin, str)):
    txt = []
    for char in stringin:
      if eqv[ord(char)] != '*':
        txt.append(eqv[ord(char)])
    txt = ''.join(txt)
    # print(txt)
    return txt

try:
    with open(source_file_path, 'r') as source_file:
        with open(new_file_path, 'w') as new_file:
            for line in source_file:
                line = main(line)
                new_file.write(line)
    
    print(f"File '{source_file_path}' copied to '{new_file_path}' successfully.")
except FileNotFoundError:
    print(f"File '{source_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#   main()