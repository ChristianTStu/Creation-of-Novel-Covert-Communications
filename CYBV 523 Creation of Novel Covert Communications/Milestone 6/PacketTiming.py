from scapy.all import *
from pandas import Series
from scipy.stats import entropy

# Function to calculate entropy
def calcEntropy(data):
    b = bytearray(data)
    s = Series(b)
    counts = s.value_counts()
    return entropy(counts)

# Entropy threshold
entropyThreshold = 2.5

# Global variables to store timing and size information
last_packet_time = None
time_intervals = []
total_size = 0
packet_count = 0

# Function to process payloads, timing, and size
def processPayloadsAndTiming(p):
    global last_packet_time, time_intervals, total_size, packet_count

    # Check if the packet has a TCP layer and a Raw layer
    if p.haslayer(TCP) and p.haslayer(Raw):
        # Calculate the entropy of the payload
        e = calcEntropy(p[Raw].load)

        # Get the current packet time
        current_time = p.time

        # If this is not the first packet, calculate the time difference
        if last_packet_time is not None:
            time_diff = current_time - last_packet_time
            time_intervals.append(time_diff)
            print(f"Time since last TCP packet: {time_diff} seconds")

        # Update the last packet time
        last_packet_time = current_time

        # Calculate and print the size of the packet
        packet_size = len(p)
        print(f"Size of this TCP packet: {packet_size} bytes")
        total_size += packet_size
        packet_count += 1

        # Check entropy and size for potential encryption
        if e >= entropyThreshold and len(p[Raw].load) % 16 == 0:
            print("Potentially encrypted data detected with entropy %f" % e)
            print("\t%s" % p[Raw].load.hex())

# Function to calculate and print average time interval and average packet size
def printAverageMetrics():
    if time_intervals:
        average_time = sum(time_intervals) / len(time_intervals)
        print(f"Average time interval between packets: {average_time} seconds")
    else:
        print("No packets captured.")

    if packet_count > 0:
        average_size = total_size / packet_count
        print(f"Average size of TCP packets: {average_size:.2f} bytes")
    else:
        print("No TCP packets captured.")

# Start sniffing packets, set count to 0 for no limit
sniff(offline="C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Creation of Novel Covert Communications/Milestone 6/WireShark Traffic Capture/EncryptedChannel.pcapng", prn=processPayloadsAndTiming, count=0)

# After sniffing, print the average time interval and packet size
printAverageMetrics()
