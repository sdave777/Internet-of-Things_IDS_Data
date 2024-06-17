# IoT Intrusion Detection System Dataset

Looking at this dataset, it may have potential to correlate variables such as duration of activity and size of file transfers, port usage and protocol. More to come.

This dataset shows typical behavior for malicious activity as compared to benign. This will help us understand adversarial patterns when internet of things (IoT) devices are targeted. 

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
