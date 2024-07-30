import re
import sys

def parse_mimikatz_output(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Extract the iteration count
    iteration_match = re.search(r'\* Iteration is set to default \((\d+)\)', content)
    if not iteration_match:
        raise ValueError("Iteration count not found in the file")
    iterations = iteration_match.group(1)

    # Extract each user block
    user_blocks = re.findall(r'\[NL\$\d+ - .+?\](.+?)MsCacheV2 : ([0-9a-fA-F]+)', content, re.DOTALL)

    # Parse each block to get username and hash
    output_lines = []
    for block in user_blocks:
        user_info = block[0]
        hash_value = block[1]

        # Extract username
        user_match = re.search(r'User\s+:\s+([^\s\\]+)\\([^\s]+)', user_info)
        if user_match:
            username = user_match.group(2)
        else:
            raise ValueError("Username not found in the block")

        # Construct the output line
        output_line = f"$DCC2${iterations}#{username}#{hash_value}"
        output_lines.append(output_line)

    return output_lines

def usage():
    print("Simple script to convert the output of mimikatz !lsadump::cache to hashcat format\n")
    print("Usage: python3 mimikatz-to-hashcat.py <mimikatz_output>")

# Example usage:
if len(sys.argv) != 2:
    usage()
    sys.exit(0)

file_path = sys.argv[1]
output_lines = parse_mimikatz_output(file_path)
for line in output_lines:
    print(line)
