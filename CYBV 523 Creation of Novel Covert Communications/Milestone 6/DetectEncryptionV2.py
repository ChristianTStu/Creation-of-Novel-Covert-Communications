from scapy.all import *
from pandas import Series
from scipy.stats import entropy

def calcEntropy(data):
    # Convert the packet data to a bytearray for entropy calculation
    b = bytearray(data)
    # Create a pandas Series from the bytearray
    s = Series(b)
    # Count the occurrence of each byte value in the data
    counts = s.value_counts()
    # Calculate and return the entropy of the data
    return entropy(counts)

# Define an entropy threshold to identify potentially encrypted data
entropyThreshold = 2.5

def processPayloads(p):
    # Check if the packet has a Raw layer containing the actual data
    if not p.haslayer(Raw):
        return
    # Extract the payload from the Raw layer
    load = p[Raw].load
    # Calculate the entropy of the payload
    e = calcEntropy(load)
    # Check if the entropy is above the threshold and the data length is a multiple of 16
    # AES (used in the encryption script) works in 16-byte blocks, so encrypted data is likely to be a multiple of 16
    if e >= entropyThreshold and len(load) % 16 == 0:
        print("Potentially encrypted data detected with entropy %f" % e)
        # Print the hexadecimal representation of the payload
        print("\t%s" % load.hex())
    return

# Start sniffing packets from a specified file (e.g., a pcapng file)
# The 'prn' parameter specifies the function to be called for each packet
sniff(offline="EncryptedChannel.pcapng", prn=processPayloads)
