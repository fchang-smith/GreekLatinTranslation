greekDict = {
    "\u0391": "A", #A
    "\u0392": "B", #B
    "\u0393": "G", #Γ
    "\u0394": "D", #Δ
    "\u0395": "E", #Ε
    "\u0396": "Z", #Ζ
    "\u0397": "H", #Η
    "\u0398": "Q", #Θ
    "\u0399": "I", #Ι
    "\u039a": "K", #Κ
    "\u039b": "L", #Λ
    "\u039c": "M", #Μ
    "\u039d": "N", #Ν
    "\u039e": "X", #Ξ
    "\u039f": "O", #Ο
    "\u03a0": "P", #Π
    "\u03a1": "R", #Ρ
    "\u03a3": "S", #Σ
    "\u03a4": "T", #Τ
    "\u03a5": "Y", #Υ
    "\u03a6": "F", #Φ
    "\u03a7": "C", #Χ
    "\u03a8": "U", #Ψ
    "\u03a9": "W" #Ω
}

def singleLetter(greekLetter):
    return greekDict[greekLetter]

def multiLetter(greekWord):
    parsed = [*greekWord]
    latinWord = ""
    for i in parsed:
        latinWord = latinWord + singleLetter(i)
    return latinWord

word = multiLetter("ΟΦΩ")
print (word) 


