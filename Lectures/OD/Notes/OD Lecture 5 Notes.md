---
tags:
  - Notes
links: "[[OD Lecture 5]]"
creation date: 2024-11-09 15:39
modification date: Saturday 9th November 2024 15:40:07
semester: 3
year: 2024
---


---
# OD Lecture 5 Notes

---



# ["Turning the database inside out with Apache Samza" by Martin Kleppmann](https://www.youtube.com/watch?v=fU9hR3kiOK0&t=505s)


## Key Points

- **Speaker:** Martin Kleppmann, author of "Designing Data-Intensive Applications"
- **Topic:** Rethinking database and application architecture, focusing on data consistency and scalability
- **Thesis:** The current database paradigm, centered around shared mutable state, is limiting. A more event-driven approach can lead to better applications.

## Core Concepts

- **Shared Mutable State:** Databases often maintain a single, global state that can be modified by multiple applications. This can lead to complexity and inconsistencies.
- **Event-Driven Architecture:** Applications subscribe to streams of events, allowing for more decentralized and scalable systems.
- **Materialized Views:** Pre-computed caches that can improve query performance.
- **Stream Processing:** Processing data as it flows, enabling real-time analytics and decision-making.

## Benefits of the Event-Driven Approach

- **Improved Data Consistency:** By separating reads and writes, inconsistencies can be reduced.
- **Enhanced Scalability:** Event-driven systems can handle high volumes of data and distributed workloads more efficiently.
- **Better Performance:** Materialized views can optimize query performance.
- **Real-Time Insights:** Stream processing enables timely analysis of data.

## Key Takeaways

- **Rethink Database Design:** The current paradigm may be limiting. Consider event-driven approaches.
- **Leverage Materialized Views:** Improve query performance with pre-computed caches.
- **Embrace Stream Processing:** Process data in real-time for valuable insights.
- **Explore Event-Driven Architecture:** Learn more about this approach for building scalable and consistent applications.


# Real-time Transport Protocol (RTP)

## Overview

- RTP is a network protocol designed for the delivery of audio and video over IP networks
- It's commonly used in communication and entertainment system involve streaming media, including telephony, video conferencing application (e.g., WebRTC), television services and web-based  push to talk features. 
- RTP typically operates on the User Datagram Protocol (UDP), which allows for faster transmission speeds by sacrificing some reliability
- It works alongside the RTP Control Protocol (RTCP) which monitors transmission statistics quality of service and aids in synchronizing multiple media streams.



## Development and Standards

- RTP was developed by the Audio-Video Transport Working Group of the Internet Engineering Task Force (IETF) and was first published in 1996 as RFC 1889, replaced by RFC 3550 in 2003.
- Initial research on audio and video over packet-switched networks dates back to the early 1970s, with significant developments made by the IETF since 1992.
- The design of RTP prioritizes end-to-end, real-time transfer of streaming media, offering features for jitter compensation and detecting packet loss and out-of-order delivery.
- RTP can support data transfer to multiple destinations through IP multicast, making it versatile for various applications.
- RTP is tailored for real-time multimedia applications, which can tolerate some packet loss but require timely data delivery for optimal performance.


## RTP and RTCP Functionality
- RTP protocol facilitates the transfer of real-time multimedia data, including timestamps for synchronization, sequence numbers to detect packet loss and recorder packets and a payload format describing the encoded data
- RTCP provides feedback about quality of service and assists the synchronization of media steams without carrying much bandwidth 
- Each multimedia session consists of an RTP session for data transfer and an assciated RTCP session for control and QoS (Quality of Service) monitoring 
- When establishing an RTP session, signaling protocols such as H.323, SIP, RTSP, or Jingle (XMPP) may be employed to negotiate parameters.
- RTP is predominantly implemented over UDP, but it can also work with other transport protocols like SCTP and DCCP if required reliability is necessary.


## RTP Header and Payload Formats

- RTP packets consist of a minimum 12-byte header that may include optional extensions followed by the RTP payload, which varies according to the specific application's requirements.
- The header includes important fields such as timestamps, sequence numbers, and a Payload Type (PT) field that indicates the codec being used.
- The RTP standard allows for the integration of new multimedia formats without requiring changes to the standard itself, with profiles defining codecs and payload formats.
- Examples of audio payload formats include G.711, G.723, G.726, G.729, GSM, QCELP, MP3, and DTMF. Examples of video payload formats include H.261, H.263, H.264, H.265, and MPEG-1/MPEG-2.
- The specification of MPEG-4 audio/video streams with RTP is detailed in RFC 3016, while RFC 2429 describes H.263 video payloads.

## Auxiliary Protocols and Applications

- RTP is commonly paired with other standards and protocols, such as SIP, Jingle, RTSP, H.225, and H.245, for session initialization and control.
- Encoding standards like H.264, MPEG, and H.263 are also used in RTP applications to define how the payload data is managed.
- An RTP sender captures multimedia information, encodes it, and then frames it into RTP packets with appropriate timestamps and sequence numbers before transmission.
- Receivers interpret these RTP packets, decode the media data as per the specified payload types, and present the streamed content to users.
- The flexibility of RTP allows for varying configurations to meet specific application needs while maintaining necessary performance attributes for real-time streaming.


# Real-time Streaming Protocol (RTSP)

## Overview of RTSP
- Real-time Steaming Protocol is designed for multiplexing and packetizing multimedia transport streams, covering interactive media, video  and audio. 
- RTSP facilitates the control of streaming media servers in entertainment and communication systems, handling commands like play, record, and pause from clients. 
- The protocol establishes and controls media sessions between endpoints, enabling functionalities such as video on demand and voice recording 


## Development and Standardization

- RTSP was developed by RealNetowrks, Netscaple and Columbia University, with the first draft submitted to the IETF  in October 1996
- The initial drafts, culminated in the standardization by the Multiparty Multimedia Session Control Working Group (MMUSIC WG) of the IETF.
- RTSP was published as a Proposed Standard in RFC 2326 in 1998, and RTSP 2.0 was later published in 2016 as RFC 7826, though it is not backwards compatible with its predecessor except in basic version negotiation

## Data Transmission and Compatibility  

- While RTSP does not handle the transmission of streaming data itself, it often works alongside the Real-time Transport Protocol (RTP) and Real-time Control Protocol (RTCP) for media delivery.
- Some vendors may implement proprietary transport protocols, such as RealNetworks' proprietary Real Data Transport (RDT).
- Unlike HTTP, which is stateless, RTSP maintains a session state via identifiers to track concurrent sessions.


## RTSP Control Messages  

- RTSP sends control messages predominantly from client to server, with some commands also sent from the server back to the client.
- The default transport layer port number for RTSP is 554, with UDP rarely used for control requests.
- The ANNOUNCE method exemplifies an RTSP message format, demonstrating the structure of client-server communication regarding session setup.

## RTSP over HTTP and Security  

- Defined by Apple in 1999, RTSP over HTTP interleaves RTP video and audio data within RTSP command connections, using long-running HTTP GET and POST connections.
- RTSP 2.0 introduces several encryption methods for RTSP command messages and RTP media data, including a new secure URL scheme (rtsps://) and reserved port (322).
- As of September 2024, RTSP over HTTPS has been implemented in various devices including ONVIF IP Cameras, and supports encryption for additional security benefits.


# How WebRTC works

## Overview of WebRTC

- WebRTC enables real-time communications (voice, video, and data) directly in web browsers without any plugins or downloads.
- It operates as a media engine with a JavaScript API, facilitating easy usage, despite varying implementations across different browsers.
- Once signaling is complete, WebRTC allows direct peer-to-peer communication between browsers without routing through a web server, differentiating it from traditional client-server architectures.
- This peer-to-peer nature of WebRTC is a defining feature, allowing for more efficient communication compared to standard methods which rely on server mediation.



## Signaling and Media in WebRTC  

- WebRTC employs two types of interactions over the network: signaling and media, which operate through different channels.
- Signaling is conducted over an HTTPS connection or WebSocket, where developers must implement methods for users to find each other and initiate conversations.
- Media transmission occurs over specialized "media channels" using protocols like SRTP for voice and video, and SCTP for data channels, allowing for direct communication following the signaling phase.
- Developers must decide how to manage signaling as it is not built into WebRTC itself, utilizing SDP messages for session initiation.


## Audio and Video Transmission  

- WebRTC predominantly showcases audio and video communication, using codecs to compress and decompress data, aimed at low-latency transmission.
- Media sent through WebRTC must handle potential packet loss efficiently, sometimes foregoing retransmission to maintain responsiveness.
- It employs VoIP techniques for processing media, which can complicate interoperability with existing VoIP services due to its unique implementations.

## Data Channels and NAT Traversal  

- WebRTC also allows the transmission of arbitrary data via data channels, enabling direct messaging between browsers but facing challenges when behind NATs or firewalls.
- Network Address Translation (NAT) complicates peer-to-peer communication, necessitating the use of TURN servers to relay media when direct connection fails.
- It is estimated that 5-20% of sessions may require TURN server use, emphasizing the importance of effective NAT traversal strategies in WebRTC applications.