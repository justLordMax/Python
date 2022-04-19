from morse import EnglishMessage

message = "SOS we have hit an iceberg and need help quickly"
morse_m = EnglishMessage(message)

print(f"Incoming message: {message}")
print(f"    Morse encoded: {morse_m.morse_encoded()}")

