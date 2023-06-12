# Import charm-crypto library
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair

# Initialize a pairing group
group = PairingGroup('SS512')

# Define a function to convert a file to a GT element
def file_to_GT(filename):
    # Open the file in binary mode and read its content
    with open(filename, 'rb') as f:
        content = f.read()
    # Convert the content to an integer
    num = int.from_bytes(content, 'big')
    # Convert the integer to a GT element
    gt = group.init(GT, num)
    return gt

# Define a function to convert a GT element to a file
def GT_to_file(gt, filename):
    # Convert the GT element to an integer
    num = group.decode(gt)
    # Convert the integer to bytes
    content = num.to_bytes((num.bit_length() + 7) // 8, 'big')
    # Write the bytes to a file in binary mode
    with open(filename, 'wb') as f:
        f.write(content)

# Test the functions with an example file
# Assume there is a file named 'example.txt' in the current directory
gt = file_to_GT('example.txt')
print(gt) # Print the GT element
GT_to_file(gt, 'output.txt') # Write the GT element to a new file named 'output.txt'
# Check if the original file and the new file are identical
with open('example.txt', 'rb') as f1, open('output.txt', 'rb') as f2:
    print(f1.read() == f2.read()) # Print True if they are identical
