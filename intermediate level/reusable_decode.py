from morse import MorseMessage

m = "... --- ... / .-- . / .... .- ...- . / .... .. - / .- -. / .. -.-. . -... . .-.- --. / .- -. -.. / -. . . -.. / .... . .-.. .--. / --.- ..- .. -.-. -.- .-.. -.--"
english_m = MorseMessage(m)

print(english_m.morse_decoded())