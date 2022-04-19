from morse import EnglishMessage, MorseMessage

message_string = "hello world"
message = EnglishMessage(message_string)

code_string = message.morse_encoded()

code = MorseMessage(code_string)
decoded = code.morse_decoded()

print(decoded == message_string)