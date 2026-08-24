# Auftrag 02 – Fragenkatalog

Diese Fragen dienen dem mündlichen Nachweis der Stufen 3 und 4 gemäss
[Kompetenzmatrix](../../08-kompetenznachweise/lb2/kompetenzmatrix-lb2.md).

**Für Lernende:** Der Katalog ist offen einsehbar. Arbeiten Sie die Antworten vor der Abgabe
durch — im Selbststudium, mit der Fachliteratur oder mit KI-Unterstützung gemäss
[ki-nutzung.md](../../ki-nutzung.md). Entscheidend ist, dass Sie im Gespräch frei und in
eigenen Worten antworten können.

**Für die Lehrperson:** Eine Frage zufällig ziehen. Der Erwartungshorizont nennt, was fallen
muss. Der Hinweis wird nur gegeben, wenn ohne ihn keine Antwort kommt — dann ist Stufe 3
erreichbar, Stufe 4 nicht mehr.

---

### 1

**Frage:** Was ist eine Security Group in AWS, und worin unterscheidet sie sich von der
Windows-Firewall auf Ihrem Server?

**Erwartungshorizont:** Filter auf Netzwerkebene vor der Instanz; wirkt unabhängig vom
Betriebssystem; beide Ebenen müssen den Verkehr erlauben, damit eine Verbindung zustande kommt.

**Hinweis:** Sie haben zwei Hürden hintereinander. Was passiert, wenn nur eine davon offen ist?

---

### 2

**Frage:** Welche Ports haben Sie in Ihrer Security Group geöffnet, und wofür jeweils?

**Erwartungshorizont:** Eigene Konfiguration korrekt genannt; jeder Port einem Dienst zugeordnet
(z. B. RDP, DNS, LDAP, Kerberos); keine Ports ohne erklärbaren Zweck.

**Hinweis:** Gehen Sie Ihre Regelliste durch und fragen Sie sich bei jeder Zeile: Welcher
Dienst würde ohne sie nicht funktionieren?

---

### 3

**Frage:** Was ist das Risiko, wenn RDP auf Port 3389 für `0.0.0.0/0` freigegeben ist, und
welche Alternative gäbe es?

**Erwartungshorizont:** Der Port ist weltweit erreichbar und wird automatisiert angegriffen;
Passwortangriffe innerhalb kurzer Zeit; Alternative: Einschränkung auf die eigene öffentliche
IP oder Zugang über einen Jump Host.

**Hinweis:** Rechnen Sie damit, dass ein offener Port im Internet innerhalb von Minuten
gefunden wird. Was folgt daraus?

---

### 4

**Frage:** Ihre EC2-Instanz hat eine private und eine öffentliche IP-Adresse. Wofür wird
welche verwendet?

**Erwartungshorizont:** Private Adresse für die Kommunikation innerhalb der AWS-Umgebung und
für AD-interne Dienste; öffentliche Adresse für den Zugriff von aussen; im Betriebssystem
selbst ist nur die private konfiguriert.

**Hinweis:** Schauen Sie mit `ipconfig` nach, welche der beiden der Server überhaupt kennt.

---

### 5

**Frage:** Warum kann sich die öffentliche IP-Adresse nach einem Stopp der Instanz ändern, und
wie verhindert man das?

**Erwartungshorizont:** Standardmässig wird die Adresse dynamisch zugewiesen und beim Stoppen
freigegeben; feste Zuordnung über eine reservierte Adresse (Elastic IP).

**Hinweis:** AWS gibt die Adresse zurück in den Pool. Es gibt eine Möglichkeit, sie für sich zu
behalten.

---

### 6

**Frage:** Was ist der Unterschied zwischen «Stop» und «Terminate» bei einer EC2-Instanz?

**Erwartungshorizont:** Stop hält die Instanz an, das Volume bleibt bestehen und ein Neustart
ist möglich; Terminate löscht die Instanz und standardmässig auch das Root-Volume — die Daten
sind weg.

**Hinweis:** Eine der beiden Aktionen können Sie rückgängig machen. Die andere nicht.

---

### 7

**Frage:** Was ist ein Snapshot oder Backup Ihrer Umgebung wert, und wann erstellen Sie ihn?

**Erwartungshorizont:** Absicherung gegen eigene Fehlkonfiguration; sinnvoll vor grösseren
Eingriffen und am Ende eines Arbeitstags; im Modul ausdrücklich Eigenverantwortung.

**Hinweis:** Denken Sie an den Moment, in dem eine GPO Ihre Umgebung unbrauchbar macht.

---

### 8

**Frage:** Stimmen die Werte in Ihrer AWS-Umgebung noch mit Ihrer Planung aus Auftrag 01
überein? Zeigen Sie eine Stelle.

**Erwartungshorizont:** Abgleich kann konkret gezeigt werden; Abweichungen sind bewusst und in
der Planung nachgeführt.

**Hinweis:** Öffnen Sie Ihr Planungssheet neben der AWS-Konsole und vergleichen Sie eine
Zeile.

---

### 9

**Frage:** Warum ist es wichtig, dass Ihre Hostnamen und IP-Adressen eindeutig sind, obwohl
jeder in einer eigenen Umgebung arbeitet?

**Erwartungshorizont:** Nachweis der Eigenständigkeit bei der Abgabe; Vermeidung von
Verwechslungen bei gemeinsamer Fehlersuche; in der Praxis Voraussetzung für Zusammenschaltung.

**Hinweis:** Bei der Abgabe muss erkennbar sein, dass es Ihre Umgebung ist. Woran?

---

### 10

**Frage:** Ihre Umgebung verursacht laufend Kosten. Was passiert, wenn Sie die Instanzen über
die Ferien laufen lassen, und was können Sie dagegen tun?

**Erwartungshorizont:** Kosten fallen pro Laufzeit an, das Guthaben ist begrenzt; Instanzen
stoppen statt laufen lassen; Bewusstsein, dass Speicher auch im gestoppten Zustand kostet.

**Hinweis:** Sie zahlen für zwei verschiedene Dinge. Nur eines davon hört beim Stoppen auf.
