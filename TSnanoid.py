#tested on Python 3.9.6
#built using ChatGPT3.5
#this generates a timestamped 12 digit nanoid using CrockfordBase32 alphabet
#only numbers and uppercase letters are used
#and the letters O, I, L, or U are omitted to reduce ambiguity
#need to install nanoid first via pip

import nanoid
import time

def generate_nanoid_with_timestamp(size=12):
    if size <= 0:
        raise ValueError("Size must be a positive integer.")

    # Get the current timestamp in seconds and convert to hexadecimal
    # make it uppercase
    # Strip leading zeroes.
    # the side effect is how far into the future the code can be used without modifications is reduced.
    timestamp_hex = hex(int(time.time()))[2:].upper()
    # will probably need to prepend a "0X" to convert back to an ISO 8601 timestamp

    # This will generate a 12 digit nanoid
    nanoid_without_timestamp = nanoid.generate('012345689ABCDEFGHJKMNPQRSTVWXYZ',12)
    # Concatenate the timestamp prefix and nanoid
    timestamp_nanoid = timestamp_hex + nanoid_without_timestamp

    # if you prefer having the output in the form timestamp-nanoid uncomment the next line
    #ts_nanoid_with_dashes = timestamp_hex +'-'+ nanoid_without_timestamp
    # split into groups of 4 characters separated by hyphens
    # comment out the next line if you want timestamp-nanoid
    ts_nanoid_with_dashes = '-'.join(timestamp_nanoid[i:i+4] for i in range(0, len(timestamp_nanoid), 4))

    return ts_nanoid_with_dashes

# Example usage
ts_nanoid = generate_nanoid_with_timestamp()
print(ts_nanoid)


#Collision probability calculator https://zelark.github.io/nano-id-cc/
#For a 12 digit nanoid with the CrockfordBase32 alphabet
# if nanoids were created 1000/second, the probability of a 1% collision 
# 125 million IDs or ~1day
# collision risk is further reduced bc of the timestamp prefix incrementing each second.
