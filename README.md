# IoT Intrusion Detection System Dataset

Looking at this dataset, it may have potential to correlate variables such as duration of activity and size of file transfers, port usage and protocol.

This dataset shows typical behavior for malicious activity as compared to benign. This will help us understand adversarial patterns when internet of things (IoT) devices are targeted. 

The dataset actually shows a need for this organization to concentrate on fundamentals, and I will demonstrate that.

## Description

17 fields, representing, 	"id.orig_h, id.orig_p, id.resp_h, id.resp_p, proto, service, duration, orig_bytes, resp_bytes, conn_state, missed_bytes	history, orig_pkts, orig_ip_bytes,	resp_pkts, resp_ip_bytes, label"

Translated, that's the origin IP address and port for the first two, responding IP address and port, then protocol, the rest are self explanatory, history appears to contain hash values, and the labels are "benign" or "malicious".

The quantitative values are the duration, bytes, and number of packets values. The labels will likely be converted into binary conditions and correlated/summed as well.

There are null values that may need to be cleaned or altered, but the data seems correct.

It is raw data, though it has a summary that explains it will require further reprocessing; it notes the string data types and the integer values, suggesting a binary setting for the "malicious" or "benign" labels.

## Avenues of Inquiry

Successful obfuscation is an unknown, it is possible that some of the benigns are malicious, however, port usage may provide a good indicator of compromise (IOC) for these situations.

I would also like to correlate the IOCs present for redundancy to assess their usefulness in rule-building situations.

## Value Proposition

This would aid defensive cyber operations (DCO) in tailoring their intrusion detection systems (IDS) towards known threats. It's generally accepted that IOCs such as IP addresses and hash values are of limited use, but an analysis of the behavioral patterns shown in the data should provide tactical data that may prove invaluable during an incident.


## Findings

After selecting for labels that equal malicious and plotting those values with an event index count, there appears to be a strong correlation between protocol and malicious activity, moderate correlation with protocol and originating ip address.

![image](https://github.com/sdave777/Internet-of-Things_IDS_Data/assets/132175768/ee4c0e1d-310c-48e9-8842-b351c653b60c)

There are 21220 malicious attempts using the TCP protocol, and only 2 using the UDP protocol. This may be due to the common use of the protocol, or to available tools that tend to prefer TCP over UDP, I will research this further (I should already know this...)

![image](https://github.com/sdave777/Internet-of-Things_IDS_Data/assets/132175768/539e80e4-1f9c-469c-a691-d03b27d74419)


1812 benign UDPs and only 111 benign TCPs

It appears that all activity originates from 192.168.1.195, indicating either a compromised device or server, or this is the simply the NAT address that we are seeing. If the device is compromised, it should be removed and/or, if the resources are available, quarantined and sent to a specialist for forensic analysis. If this an issue with the NAT address, then the following should be done:

![image](https://github.com/sdave777/Internet-of-Things_IDS_Data/assets/132175768/4a80627d-5d8a-4685-a599-6a14fac61621)


Targetted IP addresses:

![image](https://github.com/sdave777/Internet-of-Things_IDS_Data/assets/132175768/6156014c-c47d-4a60-a177-194a112357b9)

Duration of malicious events with connections states:

![image](https://github.com/sdave777/Internet-of-Things_IDS_Data/assets/132175768/99726a4f-28e4-4fd5-b8cc-55eee27712bf)

Duration of malicious events for the most commonly targetted IP address:

![image](https://github.com/sdave777/Internet-of-Things_IDS_Data/assets/132175768/efd5fc49-6154-4ef1-bcce-95024393ad86)

Count of connection states:

![image](https://github.com/sdave777/Internet-of-Things_IDS_Data/assets/132175768/5c9e4855-068e-4992-9778-fde2721bd512)



## Recommendations

Deploy Internal IDS Sensors: Place IDS sensors inside the network, where they can see the original internal IP addresses before NAT occurs. This helps in correlating traffic to specific internal devices.

Monitor Key Network Segments: Position IDS sensors at key points within the network, such as at critical servers or subnet boundaries.

Use of Internal Logs: Correlate IDS alerts with internal logs (firewall logs, DHCP logs) that contain original IP address information. This can help map external traffic back to internal devices.

SIEM Integration: Integrate IDS with a Security Information and Event Management (SIEM) system to aggregate and correlate data from multiple sources, providing a more comprehensive view of the network.

Detailed NAT Logging: Configure NAT devices to log detailed translation information, including internal-to-external IP mappings. These logs can be used to trace back the internal source of traffic.

Session Logging: Maintain detailed logs of sessions, including source and destination IPs, ports, and timestamps, to aid in post-event analysis.

### Sources

https://docs.zeek.org/en/current/scripts/base/protocols/conn/main.zeek.html

ipinfo.io

https://www.barracuda.com/support/glossary/intrusion-detection-system#:~:text=An%20intrusion%20detection%20system%20(IDS,information%20and%20event%20management%20system

https://csrc.nist.gov/glossary/term/industrial_control_system#:~:text=Industrial%20control%20systems%20include%20supervisory,controllers%20to%20control%20localized%20processes

