import scapy.all as scapy

#mac ve ip adresslerini eşleştirmek için arp kullanıcaz ve yayın yapıcaz sinyal yollayarak
#1)arp request, arp paketi oluşturmak ilk aşamamız
#2)broadcast, yayın yapmak
#3)response, gelen cevabı işlemek

arp_request_packet = scapy.ARP(pdst="10.0.2.1/24")
#scapy.ls(scapy.ARP)
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#scapy.ls(scapy.Ether())
combined_packet = broadcast_packet/arp_request_packet
#scapy dilinde bu combined iki paketi birleştirip tek paket haline getirir
(answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
answered_list.summary()
#print(list(answered_list)) bunu da diyebilirsin
