#Don't forget to put a star
import itertools
import hashlib

original_hash = 'your hash code'
count = 0
modes =['utf-8','utf-16','utf-32']
emoji_start = 0x1F600
emoji_end = 0x1F64F
#output_file = "hashed.txt"
#with open(output_file, 'w') as f:
for mode in modes:
    all_unicode_chars = [chr(i) for i in range(1, 1114112) if i < 55296 or i > 57343 and i < emoji_start or i > emoji_end]
    for length in range(1,33):
        for combination in itertools.product(all_unicode_chars, repeat=length):
            string = ''.join(combination).encode(mode)
            hashed = hashlib.sha256(string).hexdigest()
            count += 1
            print(" try count :",count)
                #f.write(f"{hashed} : {string}\n")
            if hashed == original_hash:
                print(f"Matching string found: {string}")
                break
        else:
            continue 
        break 
    else:
        print("No matching string found.")
