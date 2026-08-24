# Auftrag 05 – Fragenkatalog

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

**Frage:** Was ist eine Vertrauensstellung, und was wird dadurch konkret möglich?

**Erwartungshorizont:** Eine Domäne akzeptiert die Authentifizierung der anderen; Benutzer der
einen Domäne können auf Ressourcen der anderen zugreifen, ohne dort ein zweites Konto zu
haben.

**Hinweis:** Ohne Trust bräuchte jede Person zwei Konten. Was erspart die Vertrauensstellung?

---

### 2

**Frage:** Welche Richtung hat Ihr Trust, und wer kann sich dadurch wo anmelden?

**Erwartungshorizont:** Eigene Konfiguration korrekt genannt; Verständnis, dass die
Vertrauensrichtung der Zugriffsrichtung entgegengesetzt verläuft.

**Hinweis:** Wer vertraut, gibt Zugriff. Zeichnen Sie zwei Kästchen und einen Pfeil.

---

### 3

**Frage:** Welche Ports braucht ein Trust, und welcher Dienst steckt jeweils dahinter?

**Erwartungshorizont:** Mindestens Kerberos, LDAP und DNS genannt und den zugehörigen Ports
zugeordnet; Bewusstsein, dass es mehrere sind und nicht nur einer.

**Hinweis:** Gehen Sie Ihre Security-Group-Regeln durch, die Sie für den Trust ergänzt haben.

---

### 4

**Frage:** Was ist der Unterschied zwischen AWS Managed Microsoft AD und dem Domain Controller,
den Sie selbst auf einer EC2-Instanz installiert haben?

**Erwartungshorizont:** Beim Managed AD betreibt AWS die DCs, Patching und Verfügbarkeit;
dafür kein Domänenadmin-Zugriff und eingeschränkte Eingriffsmöglichkeiten; beim eigenen DC
volle Kontrolle und volle Verantwortung.

**Hinweis:** Fragen Sie sich, was Sie auf dem Managed AD **nicht** tun dürfen, was auf Ihrem
eigenen DC selbstverständlich wäre.

---

### 5

**Frage:** Warum ist es riskant, die Trust-Ports gegen das Internet zu öffnen, und was haben
Sie stattdessen getan?

**Erwartungshorizont:** Verzeichnisdienste sind hochwertige Angriffsziele; Einschränkung auf
die Gegenstelle statt auf alle Adressen; eigene Massnahme benannt und dokumentiert.

**Hinweis:** Die Gegenstelle hat eine bekannte Adresse. Warum sollte irgendjemand sonst diese
Ports erreichen dürfen?

---

### 6

**Frage:** Was bedeutet es, dass eine Vertrauensstellung transitiv ist?

**Erwartungshorizont:** Vertrauen wird weitergereicht: Vertraut A dem B und B dem C, so gilt es
auch zwischen A und C; nicht jeder Trust-Typ ist transitiv.

**Hinweis:** Denken Sie an «der Freund meines Freundes». Gilt das immer?

---

### 7

**Frage:** Ihr Trust funktioniert. Kann ein Benutzer der anderen Domäne nun automatisch auf
Ihre Freigaben zugreifen?

**Erwartungshorizont:** Nein — der Trust ermöglicht nur die Authentifizierung; die
Autorisierung fehlt noch, es müssen Berechtigungen vergeben werden.

**Hinweis:** Es gibt zwei Schritte: erkennen, wer jemand ist, und entscheiden, was er darf.
Welchen davon löst der Trust?

---

### 8

**Frage:** Wie haben Sie nachgewiesen, dass der Trust wirklich funktioniert und nicht nur
angelegt ist?

**Erwartungshorizont:** Aktive Prüfung, etwa über die Validierung in den Domänenwerkzeugen oder
einen Zugriffstest mit einem Konto der Gegenseite; nicht nur die Anzeige des Trust-Objekts.

**Hinweis:** Ein Eintrag in der Konsole beweist nur, dass Sie ihn erstellt haben. Was beweist,
dass er trägt?

---

### 9

**Frage:** Warum haben Sie DNS zwischen den beiden Umgebungen konfigurieren müssen, damit der
Trust zustande kommt?

**Erwartungshorizont:** Jede Seite muss die Domänencontroller der anderen über deren
SRV-Einträge finden; ohne Namensauflösung über die Domänengrenze scheitert der Aufbau;
Weiterleitung oder bedingte Weiterleitung eingerichtet.

**Hinweis:** Bevor zwei Domänen einander vertrauen können, müssen sie einander erst einmal
finden. Womit?

---

### 10

**Frage:** In welcher realen Situation würde eine Firma eine Vertrauensstellung einrichten
statt die Domänen zusammenzulegen?

**Erwartungshorizont:** Nachvollziehbares Beispiel, etwa nach einer Firmenübernahme, bei
getrennter Verwaltungshoheit oder bei unterschiedlichen Sicherheitsanforderungen.

**Hinweis:** Denken Sie an zwei Firmen, die zusammenarbeiten müssen, aber nicht dieselbe
IT-Abteilung haben.
