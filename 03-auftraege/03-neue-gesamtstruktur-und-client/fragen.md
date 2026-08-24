# Auftrag 03 – Fragenkatalog

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

**Frage:** Wenn Sie einen Server zum Domain Controller heraufstufen — was passiert dabei mit
dem DNS?

**Erwartungshorizont:** DNS-Rolle wird mit installiert; AD-integrierte Zone entsteht; der DC
trägt seine Dienste selbst als Einträge ein.

**Hinweis:** Schauen Sie in Ihrer DNS-Konsole nach, welche Zone nach der Promotion neu da war.

---

### 2

**Frage:** Woher weiss ein frisch gejointer Client überhaupt, welcher Server sein Domain
Controller ist?

**Erwartungshorizont:** Über DNS; SRV-Records (`_ldap._tcp.dc._msdcs.<domain>`); der Client
fragt den DNS-Server, nicht das Netz per Broadcast.

**Hinweis:** Es steht nirgends fest verdrahtet — der Client fragt jemanden. Wen fragt er?

---

### 3

**Frage:** Wozu dient die Reverse-Lookup-Zone, und was funktioniert ohne sie nicht mehr?

**Erwartungshorizont:** Auflösung IP → Name über PTR-Einträge; ohne sie liefert `nslookup` auf
eine IP keinen Namen; betrifft vor allem Diagnose und Protokollierung, nicht die
Grundfunktion der Anmeldung.

**Hinweis:** Denken Sie an die Richtung. Eine Zone löst Namen zu Adressen auf — was macht die
andere?

---

### 4

**Frage:** Was passiert im Hintergrund, wenn ein Client der Domäne beitritt?

**Erwartungshorizont:** Ein Computerkonto wird im AD angelegt; der Client erhält ein eigenes
Kennwort und baut damit einen sicheren Kanal zum DC auf; der Computer wird selbst zu einem
Objekt mit Rechten.

**Hinweis:** Schauen Sie in `dsa.msc` nach, was nach dem Join zusätzlich existiert, das vorher
nicht da war.

---

### 5

**Frage:** Warum darf am Client nicht der Router oder ein öffentlicher DNS-Server wie 8.8.8.8
als bevorzugter DNS eingetragen sein?

**Erwartungshorizont:** Diese Server kennen die interne Zone nicht; ohne SRV-Auflösung findet
der Client keinen DC; die Anmeldung scheitert oder fällt auf zwischengespeicherte
Anmeldedaten zurück.

**Hinweis:** Verbindung zum Internet hätte der Client damit. Was genau kann 8.8.8.8 trotzdem
nicht beantworten?

---

### 6

**Frage:** Erklären Sie den Unterschied zwischen Domäne, Struktur (Tree) und Gesamtstruktur
(Forest). Was davon haben Sie in Ihrer Umgebung aufgebaut?

**Erwartungshorizont:** Domäne als Verwaltungs- und Replikationseinheit; Tree als
zusammenhängender Namensraum; Forest als äusserste Grenze mit gemeinsamem Schema; eigene
Umgebung korrekt eingeordnet.

**Hinweis:** Sie haben bei der Promotion zwischen mehreren Optionen gewählt. Welche war es,
und was hat sie erzeugt?

---

### 7

**Frage:** In der Bewertung steht, NSLOOKUP müsse «in beide Richtungen» funktionieren. Welche
zwei Richtungen sind gemeint, und welcher Eintragstyp wird jeweils abgefragt?

**Erwartungshorizont:** Name → IP über A-Eintrag; IP → Name über PTR-Eintrag; letzterer setzt
die Reverse-Lookup-Zone voraus.

**Hinweis:** Sie haben beide Abfragen für die Abgabe gemacht. Was haben Sie jeweils
eingetippt?

---

### 8

**Frage:** Erklären Sie Ihr RDP-Konzept: Wer darf von wo auf welche Systeme zugreifen, und
warum haben Sie es so festgelegt?

**Erwartungshorizont:** Nachvollziehbare Begründung der eigenen Festlegung; Bewusstsein, dass
ein direkt aus dem Internet erreichbarer RDP-Port ein Angriffsziel ist; Einschränkung auf
Gruppen oder Herkunftsadressen.

**Hinweis:** Stellen Sie sich vor, Ihr RDP-Port wäre offen im Internet erreichbar. Was würde
innerhalb weniger Stunden passieren?

---

### 9

**Frage:** Was unterscheidet einen Domänenadministrator von einem lokalen Administrator, und wo
ist das jeweilige Konto gespeichert?

**Erwartungshorizont:** Lokales Konto in der lokalen Kontendatenbank, nur auf diesem einen
Rechner gültig; Domänenkonto im Verzeichnis auf dem DC, domänenweit gültig.

**Hinweis:** Melden Sie sich gedanklich an einem Rechner an, der gerade keine Verbindung zum
DC hat. Welches der beiden Konten funktioniert dort noch?

---

### 10

**Frage:** Ein Client kann die Domäne nicht finden. Welche drei Dinge prüfen Sie zuerst, und in
welcher Reihenfolge?

**Erwartungshorizont:** Sinnvolle Reihenfolge vom Einfachen zum Komplexen: DNS-Eintrag des
Clients, Erreichbarkeit des DC, Zeitabweichung; Begründung der Reihenfolge.

**Hinweis:** Zwei der drei Punkte lassen sich in unter einer Minute prüfen. Fangen Sie damit
an.
