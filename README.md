# ts_nanoid
Generates nanoid with a timestamp prefix

I liked nanoid, ksuid and ulids
Wanted IDs that: 
Have a timestamp prefix so some there was some ability to group and search 
Would be shorter than ulids
Use the Crockford Base32 alphabet
ID is shown in groups of 4 letters separated by dashes for ease of reading off and verifying
For my needs, I don't anticipate collisions given the relatively slow rate of ID generation.

Used ChatGPT3.5 to get most of the coding and tweaked slightly from there.
