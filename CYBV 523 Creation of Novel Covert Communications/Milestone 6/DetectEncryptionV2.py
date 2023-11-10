from scapy.all import *
from pandas import Series
from scipy.stats import entropy

def calcEntropy(data):
    # Convert data to a bytearray for entropy calculation
    b = bytearray(data)
    s = Series(b)
    counts = s.value_counts()
    return entropy(counts)

# Set an entropy threshold to identify encrypted data
entropyThreshold = 2.5

def processPayloads(p):
    # Check if the packet has a Raw layer
    if not p.haslayer(Raw):
        return
    load = p[Raw].load
    e = calcEntropy(load)
    # Check if entropy is high and data length is a multiple of 16 (AES block size)
    if e >= entropyThreshold and len(load) % 16 == 0:
        print("Potentially encrypted data detected with entropy %f" % e)
        print("\t%s" % load.hex())
    return

# Sniff packets from a file (replace with your pcapng file)
sniff(offline="EncryptedChannel.pcapng", prn=processPayloads)