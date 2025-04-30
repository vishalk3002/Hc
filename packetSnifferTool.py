from scapy.all import sniff, IP, TCP, UDP, Raw

def process_packet(packet):
    print("="*60)
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Protocol       : {ip_layer.proto}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print("Protocol Type  : TCP")
            print(f"Source Port    : {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print("Protocol Type  : UDP")
            print(f"Source Port    : {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")

        if Raw in packet:
            print("Payload:")
            print(packet[Raw].load[:100])  # Print up to 100 bytes of payload

def start_sniffing():
    print("Starting packet sniffing... Press Ctrl+C to stop.")
    sniff(filter="ip", prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffing()
