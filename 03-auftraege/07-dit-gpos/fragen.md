# Auftrag 07 – Fragenkatalog

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

**Frage:** Was ist ein Directory Information Tree, und wozu erstellt man ihn, bevor man die
Struktur im AD anlegt?

**Erwartungshorizont:** Grafische Darstellung des logischen Aufbaus des Verzeichnisses;
Strukturfehler fallen auf Papier auf statt später in der produktiven Umgebung; dient
zugleich der Dokumentation.

**Hinweis:** Es ist billiger, ein Kästchen zu verschieben als eine OU mit dreissig Objekten.

---

### 2

**Frage:** Zeigen Sie den DN eines Ihrer Benutzer und lesen Sie ihn vor — von rechts nach
links.

**Erwartungshorizont:** Eigener DN korrekt gelesen; Verständnis, dass er von der Domänenwurzel
bis zum Objekt führt und die Reihenfolge in der Schreibweise umgekehrt ist.

**Hinweis:** Ganz rechts stehen die `DC=`-Teile. Was ist das, und wo führt der Weg von dort
hin?

---

### 3

**Frage:** Warum trennt man in der untersten Ebene Benutzer- und Computerkonten?

**Erwartungshorizont:** Gruppenrichtlinien haben getrennte Bereiche für Benutzer und Computer;
die Trennung erlaubt gezielte Verknüpfung ohne Filter; erhöht die Übersicht.

**Hinweis:** Öffnen Sie eine GPO. In wie viele Hauptbereiche ist sie unterteilt?

---

### 4

**Frage:** In welcher Reihenfolge werden Gruppenrichtlinien angewendet, und was passiert bei
widersprüchlichen Einstellungen?

**Erwartungshorizont:** Lokal, dann Standort, dann Domäne, dann OUs von oben nach unten; die
zuletzt angewendete Einstellung gewinnt; Ausnahmen über Erzwingen oder Vererbung deaktivieren.

**Hinweis:** Vier Ebenen, von der kleinsten Reichweite zur grössten. Und dann von aussen nach
innen.

---

### 5

**Frage:** Warum haben Sie die Passwortrichtlinie in der Default Domain Policy geändert und
nicht in einer eigenen GPO auf einer OU?

**Erwartungshorizont:** Kontorichtlinien wirken für Domänenkonten nur auf Domänenebene; eine
GPO auf einer OU hätte keine Wirkung auf die Domänenkonten; Ausnahmen wären über feingranulare
Kennwortrichtlinien möglich.

**Hinweis:** Probieren Sie es gedanklich durch: Sie setzen die Richtlinie auf einer OU. Was
passiert bei den Benutzern darin?

---

### 6

**Frage:** Was ist der Unterschied zwischen Sicherheitsfilterung und Zielgruppenadressierung?

**Erwartungshorizont:** Sicherheitsfilterung steuert über Berechtigungen, ob die gesamte GPO
für ein Objekt gilt; Zielgruppenadressierung entscheidet innerhalb der GPO für einzelne
Einstellungen; unterschiedliche Granularität.

**Hinweis:** Das eine wirkt auf die ganze Richtlinie, das andere auf eine einzelne Zeile darin.

---

### 7

**Frage:** Was macht ein WMI-Filter, und was ist der Preis dafür?

**Erwartungshorizont:** Wendet die GPO nur an, wenn eine Systemabfrage zutrifft, etwa eine
bestimmte Betriebssystemversion; die Abfrage läuft bei jeder Anwendung und kostet Zeit bei der
Anmeldung.

**Hinweis:** Der Filter muss bei jedem einzelnen Client ausgewertet werden. Was bedeutet das
bei tausend Clients?

---

### 8

**Frage:** Eine Ihrer GPOs greift nicht. Wie gehen Sie vor?

**Erwartungshorizont:** Systematisches Vorgehen: Verknüpfung und Ziel-OU prüfen, Filterung und
Berechtigungen, Benutzer- gegen Computerkonfiguration, dann `gpresult /r` beziehungsweise
`gpresult /h` zur Auswertung.

**Hinweis:** Es gibt einen Befehl, der Ihnen sagt, welche Richtlinien tatsächlich angekommen
sind. Fangen Sie dort an.

---

### 9

**Frage:** Woran entscheiden Sie, ob eine Einstellung in die Computer- oder in die
Benutzerkonfiguration gehört?

**Erwartungshorizont:** Gilt die Einstellung für das Gerät unabhängig davon, wer sich anmeldet,
oder für die Person unabhängig vom Gerät; entsprechend muss die GPO mit der OU der Computer
oder der Benutzer verknüpft sein.

**Hinweis:** Fragen Sie sich: Soll das auch gelten, wenn sich jemand anderes an diesem Rechner
anmeldet?

---

### 10

**Frage:** Warum baut man eine OU-Struktur nicht einfach nach dem Organigramm der Firma?

**Erwartungshorizont:** OUs dienen der Verwaltung und der Richtlinienzuweisung, nicht der
Abbildung von Hierarchien; Organigramme ändern sich häufig; Gruppen bilden Zugehörigkeit ab,
OUs die Administration.

**Hinweis:** Fragen Sie sich, was Sie mit einer OU tun können — und ob eine Umstrukturierung
der Firma daran etwas ändern sollte.
