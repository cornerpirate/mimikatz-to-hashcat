# mimikatz-to-hashcat
Simple script to convert the output of mimikatz !lsadump::cache to hashcat format

# The problem

Mimikatz prints information out in a format that is not directly consumable by hashcat. 
We must parse the output to find the number of iterations, the username (without domain), and the user's hash.
Then print those out in the format:

```
$DCC2$<iterations>#<username>#<hash>
```
# Usage

After running mimikatz you copy/paste the output into a file.
Then pass that file as an argument to the python script like this:

```bash
python3 mimikatz-to-hashcat.py <mimikatz_output>
```

Copy/paste the output and save it into a file which can then be easily consumed by Hashcat.
