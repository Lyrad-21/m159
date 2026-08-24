# Auftrag 12 – Fragenkatalog

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

**Frage:** Welche drei Identity-based-Access-Varianten gibt es für Azure Files, und warum haben
Sie AD DS gewählt?

**Erwartungshorizont:** AD DS, Microsoft Entra Domain Services und Microsoft Entra Kerberos;
Entra Kerberos funktioniert nur von Windows-Client-OS, Entra DS bringt Zusatzkosten ohne
Vorteil — daher AD DS.

**Hinweis:** Warum scheiden die beiden anderen in Ihrem Szenario praktisch aus?

---

### 2

**Frage:** Was bewirkt `Join-AzStorageAccount`, und warum ist das nötig?

**Erwartungshorizont:** Der Storage Account wird als Computerobjekt im lokalen AD registriert;
erst dadurch kann der lokale KDC ein Kerberos-Ticket für den Zugriff auf den Share ausstellen.

**Hinweis:** Wofür braucht der lokale KDC ein Objekt, für das er ein Ticket ausstellen kann?

---

### 3

**Frage:** Welchen Port braucht der Zugriff auf den Azure File Share, und wie haben Sie ihn
getestet?

**Erwartungshorizont:** SMB über Port 445; getestet mit `Test-NetConnection … -Port 445`.

**Hinweis:** Welches Protokoll steckt hinter einem Netzlaufwerk, und über welchen Port läuft es?

---

### 4

**Frage:** Wozu dient die GPO „Define host name-to-Kerberos realm mappings", und was passiert
ohne sie?

**Erwartungshorizont:** Sie ordnet den Hostnamen `<storageaccount>.file.core.windows.net` dem
korrekten lokalen Realm zu; ohne Mapping sucht der Client im falschen Realm und der KDC findet
kein passendes Computerkonto.

**Hinweis:** Welchen Realm würde der Client ohne Mapping für den Azure-Hostnamen annehmen?

---

### 5

**Frage:** Beschreiben Sie den Ablauf der Authentifizierung, wenn ein Client auf den Share
zugreift.

**Erwartungshorizont:** Der Client fordert beim lokalen KDC ein Kerberos-Ticket für den SPN des
Storage-Account-Objekts an und greift damit per SMB auf den Share zu — ohne separate
Passworteingabe.

**Hinweis:** Wer stellt das Ticket aus, und für welches Objekt?

---

### 6

**Frage:** Was ist der Unterschied zwischen den Share-Rollen (RBAC) und den Datei-/
NTFS-Berechtigungen bei Azure Files?

**Erwartungshorizont:** Die RBAC-Rollen steuern den Zugriff auf Share-Ebene (wer darf lesen/
schreiben), die NTFS-Berechtigungen innerhalb des Shares auf Datei-/Ordnerebene; beide greifen
zusammen (das Restriktivere gewinnt).

**Hinweis:** Es gibt zwei Ebenen — die des Shares und die der einzelnen Dateien. Welche Rolle
wirkt wo?

---

### 7

**Frage:** Welche Rollen haben Sie Sekretariat und Buchhaltung zugewiesen und warum?

**Erwartungshorizont:** Sekretariat „Storage File Data SMB Share Reader" (Read), Buchhaltung
„… Contributor" (Write); Zuweisung nach Bedarf der Abteilung (least privilege).

**Hinweis:** Wer muss nur lesen, wer auch schreiben — und wie heissen die Rollen dazu?

---

### 8

**Frage:** Wie haben Sie getestet, dass Read und Write tatsächlich korrekt greifen?

**Erwartungshorizont:** Mit je einem Benutzer angemeldet: Sekretariat kann lesen, aber nicht
schreiben; Buchhaltung kann schreiben. Ein aktiver Zugriffstest, nicht nur die Rollenanzeige.

**Hinweis:** Eine zugewiesene Rolle in der Konsole beweist noch nicht, dass sie am Share wirkt.
Was beweist es?

---

### 9

**Frage:** Warum ist Microsoft Entra Kerberos in Ihrem Szenario nicht geeignet?

**Erwartungshorizont:** Der Zugriff mit Entra Kerberos ist aktuell nur von
Windows-Client-Betriebssystemen möglich; in Ihrem Setup ist das nicht durchgängig gegeben.

**Hinweis:** Auf welchem Betriebssystemtyp müsste der Zugriff laufen, damit Entra Kerberos
ginge?

---

### 10

**Frage:** In welcher realen Situation migriert eine Firma ein Netzlaufwerk nach Azure Files
statt einen eigenen File Server zu betreiben?

**Erwartungshorizont:** Nachvollziehbares Beispiel: kein eigener File-Server/Backup gewünscht,
Skalierbarkeit, standortübergreifender Zugriff, Integration in eine bestehende
Hybrid-Umgebung.

**Hinweis:** Was spart man sich, wenn der Fileshare in der Cloud statt im eigenen Serverraum
liegt?
