from pymisp import MISPEvent, MISPObject, PyMISP, ExpandedPyMISP
import urllib.request
import ipaddress

# ---
url_feeds = "https://lists.blocklist.de/lists/443.txt"
misp_key = "4DmF6SMIDAFgCHWPTmZJp9YCzWlIRJMywEDqH8o7"
misp_url = "https://192.168.0.102"
misp_verify_cert = False  # Лучше заменить на путь к сертификату или True, если есть валидный сертификат

# Инициализация MISP
misp = ExpandedPyMISP(misp_url, misp_key, misp_verify_cert)

# ---
event = MISPEvent()
event.info = "Blocklisted IP"
event.analysis = "1"
event.threat_level_id = "1"
event.distribution = "0"
event.add_tag('tip:green')
event.add_tag('ip_blocklist')
event.add_tag('osint:source-type="block-or-filter-list"')

# ---
try:
    blist = urllib.request.urlopen(url_feeds)
    for line in blist:
        ip_str = line.decode("utf-8").strip()
        if not ip_str:
            continue  # Пропускаем пустые строки
        try:
            # Проверяем, что это валидный IP-адрес
            ipaddress.ip_address(ip_str)
            event.add_attribute('ip-dst', ip_str, comment="BlockListed IP by MISP", disable_correlation=False, to_ids=True)
        except ValueError:
            print(f"Skipping invalid IP: {ip_str}")
    blist.close()
except Exception as e:
    print(f"Error fetching blocklist: {e}")

# Сохраняем событие в MISP
try:
    event.published = True
    misp.add_event(event)
    print("Event successfully added to MISP")
except Exception as e:
    print(f"Error adding event to MISP: {e}")