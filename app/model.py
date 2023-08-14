from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
import plotly.graph_objs as go
from .logger_file import logger

# import plotly.express as px

class Model:
    def __init__(self):
        # Define the SIEM event list
        self.siem_events = []

    def packet_handler(self, packet):
        event = {
        "timestamp": str(packet.time),
        # "event_type": None,  # Set a default value for event_type
        }

        if packet.haslayer(IP):
            event["source_ip"] = packet[IP].src
            event["destination_ip"] = packet[IP].dst
            event["protocol"] = packet[IP].proto
            event["ttl"] = packet[IP].ttl
            event["packet_length"] = len(packet)

        if packet.haslayer(TCP):
            event["source_port"] = packet[TCP].sport
            event["destination_port"] = packet[TCP].dport
            event["tcp_flags"] = packet[TCP].flags
            # Check if it's a HTTP request (commonly on port 80 or 443)
            if packet[TCP].dport == 80 or packet[TCP].dport == 443:
                event["event_type"] = "TCP - HTTP Request"
            # Check if it's a HTTP response (commonly on port 80 or 443)
            elif packet[TCP].sport == 80 or packet[TCP].sport == 443:
                event["event_type"] = "TCP - HTTP Response"
            # Check if it's a DNS query (commonly on port 53)
            elif packet[TCP].dport == 53:
                event["event_type"] = "TCP - DNS Query"
            # Check if it's a DNS response (commonly on port 53)
            elif packet[TCP].sport == 53:
                event["event_type"] = "TCP - DNS Response"            
            elif packet[TCP].dport == 22:
                event["event_type"] = "TCP - SSH"
            elif packet[TCP].dport == 21:
                event["event_type"] = "TCP - FTP"
            elif packet[TCP].dport == 3389:
                event["event_type"] = "TCP - RDP"
            elif packet[TCP].dport == 1433 or packet[TCP].dport == 3306:
                event["event_type"] = "TCP - Database Access"
            # Add more conditions for other TCP-based event types...
            else:
                event["event_type"] = "TCP"

        if packet.haslayer(UDP):
            event["source_port"] = packet[UDP].sport
            event["destination_port"] = packet[UDP].dport
            # Check if it's a DNS query (commonly on port 53)
            if packet[UDP].dport == 53:
                event["event_type"] = "UDP - DNS Query"
            # Check if it's a DNS response (commonly on port 53)
            elif packet[UDP].sport == 53:
                event["event_type"] = "UDP - DNS Response"
            elif packet[UDP].dport == 123:
                event["event_type"] = "UDP - NTP"
            elif packet[UDP].dport == 161:
                event["event_type"] = "UDP - SNMP"
            elif packet[UDP].dport == 67 or packet[UDP].dport == 68:
                event["event_type"] = "UDP - DHCP"
            elif packet[UDP].dport == 161 or packet[UDP].dport == 162:
                event["event_type"] = "UDP - SNMP"
            # Add more conditions for other UDP-based event types...
            else:
                event["event_type"] = "UDP"

        if packet.haslayer(ICMP):
            if packet[ICMP].type == 8:  # ICMP Echo Request (ping)
                event["event_type"] = "ICMP Echo Request"
            elif packet[ICMP].type == 0:  # ICMP Echo Reply
                event["event_type"] = "ICMP Echo Reply"
            # Add more conditions for other ICMP-based event types...
            else:
                event["event_type"] = "ICMP"

        if packet.haslayer(Raw):
            event["payload"] = packet[Raw].load.hex()

        # Add more features as needed...
        self.siem_events.append(event)
        # Check if 15 packets are captured, and stop packet capturing if yes
        if len(self.siem_events) >= 30:
            raise KeyboardInterrupt  # Stop capturing by raising KeyboardInterrupt

    def capture_packets(self, interface):
        # Start packet capturing on the specified network interface
        sniff(iface=interface, prn=self.packet_handler, filter="", store=False)
        logger.info('New packets have been captured')
    
    def get_events_type_data(self):
        event_type_data = {}
        # Prepare data for Plotly chart
        event_types = [event.get("event_type", "Unknown") for event in self.siem_events]
        event_count = len(event_types)
        event_freq = {event: event_types.count(event) for event in set(event_types)}
        # now creating a variable that holds a dictionary data type of the axis values
        event_type_data = {
            "event_freq" : event_freq,
            "x_data" : list(event_freq.keys()),
            "y_data" : list(event_freq.values())
        }

        return event_type_data
    
    def plotly_chart(self):
        # Prepare data for Plotly chart
        data = self.get_events_type_data()
        event_freq = data["event_freq"]

        # Create a bar chart using Plotly graph objects (go)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=data["x_data"], y=data["y_data"]))
        # Customize the layout of the chart
        fig.update_layout(title=f"Event Type Distribution for the last {len(self.siem_events)} network packets captured.",
                        xaxis_title="Event Type",
                        yaxis_title="Count")
        # Set the color of the "Unknown" bar to yellow
        if "Unknown" in event_freq:
            unknown_index = list(event_freq.keys()).index("Unknown")
            colors = ["rgb(243, 188, 36)" if i == unknown_index else "rgba(31,119,180,1)" for i in range(len(event_freq))]
            fig.data[0].marker.color = colors
        chart_html = fig.to_html()
        return chart_html

    # Sample data for demonstration purposes
    sample_events = [
        {
            "id": 1,
            "timestamp": "2023-07-30 12:34:56",
            "source_ip": "192.168.0.1",
            "event_type": "Login Failure",
            "additional": "value of additional",
        },
        {
            "id": 2,
            "timestamp": "2023-07-30 12:40:23",
            "source_ip": "192.168.0.2",
            "event_type": "Malicious Activity",
            "username": "user123",
            "target_ip": "10.0.0.5",
            "status_code": 403,
        },
        # Add more sample events here... this can work
    ]

    welcomeMsg = {"message": "Welcome to the SIEM Tool!"} # default message