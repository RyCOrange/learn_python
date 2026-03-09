# This program validates and expresses which carrier a credit card is from using Luhn's algorithm

cc_number = 0

# Bank of card carrier names to be checked from
card_carriers = {
    "amex": ["34", "37"],
    "master_card": ["51", "52", "53", "54", "55"],
    "visa": ["4"]
}
    
# Convert to a list of integers and reverse order
def checksum(cc_number):
    digits = [int(d) for d in cc_number[::-1]]  # use the parameter, not the outer variable
    total = 0 
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            doubled_digit = digit * 2 # Multiplies odd number digits by 2
            total += doubled_digit - 9 if doubled_digit > 9 else doubled_digit
        else:
            total += digit # Sum evens and odds
    return total


# Compares the first 1 or 2 digits in the card number to the bank of carriers
def detect_carrier(cc_number):
    for carrier, prefixes in card_carriers.items():
        for prefix in prefixes:
            if cc_number.startswith(prefix):
                print(carrier)
                return
    raise ValueError(f"Invalid card number: {cc_number}")

def main():
    cc_number = input("What number: ")
    cleaned = cc_number.replace(" ", "").replace("-", "")

    if checksum(cleaned) % 10 == 0:
        try:
            detect_carrier(cleaned)
        except ValueError as e:
            print(e)
    else:
        print("Invalid card number")

if __name__ == "__main__":
    main()
