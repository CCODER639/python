# Input binary sequence (with dashes removed)
squence = "100100010001011001100100110010011111011011101100110011111010101101101110101111001001100110010011001011011101001110011111001111100111010110111000010100010110110111010000100111110011111010010"

# Ensure dashes are removed if present
squence = squence.replace("-", "")

# Final sentence to build
sentence = ""

# Total number of 7-bit chunks
num_chunks = len(squence) // 7

for i in range(num_chunks):
    chunk = squence[i * 7:(i + 1) * 7]
    
    # Convert the 7-bit binary string to decimal
    decimal_value = int(chunk, 2)

    # Map 121 to space manually
    if decimal_value == 121:
        letter = " "
    elif 65 <= decimal_value <= 90:
        letter = chr(decimal_value + 32)  # A-Z to a-z
    else:
        letter = " "  # Fallback for unknown characters

    sentence += letter

# Output
print("Decoded letters:", len(sentence))
print("Sentence:", sentence)
