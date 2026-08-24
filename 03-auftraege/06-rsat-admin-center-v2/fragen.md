# Auftrag 06 – Fragenkatalog

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

**Frage:** Was sind die RSAT-Tools, und warum installiert man sie auf einem Arbeitsplatz statt
sich auf dem Domain Controller anzumelden?

**Erwartungshorizont:** Verwaltungswerkzeuge für Serverrollen auf einem Client; jede Anmeldung
am DC ist ein Risiko und hinterlässt Anmeldedaten auf dem Server; Verwaltung aus der Distanz
ist der Normalfall.

**Hinweis:** Überlegen Sie, was auf einem Server zurückbleibt, nachdem sich ein Administrator
dort interaktiv angemeldet hat.

---

### 2

**Frage:** Was ist ein Jump Host, und welches Problem löst er?

**Erwartungshorizont:** Ein einzelner, besonders abgesicherter Einstiegspunkt; nur er ist von
aussen erreichbar, alle weiteren Systeme nur über ihn; reduziert die Angriffsfläche auf ein
System.

**Hinweis:** Statt zehn Türen nach draussen gibt es eine — und die wird bewacht.

---

### 3

**Frage:** Welchen Weg von aussen haben Sie für die Administration gewählt, und warum diesen?

**Erwartungshorizont:** Eigene Lösung korrekt beschrieben (direkt via HTTPS oder über Jump
Host); Begründung berücksichtigt Erreichbarkeit und Risiko.

**Hinweis:** Sie hatten mehrere Möglichkeiten. Was hat den Ausschlag gegeben?

---

### 4

**Frage:** Warum ist ein selbstsigniertes Zertifikat für das Windows Admin Center in einer
Produktivumgebung problematisch?

**Erwartungshorizont:** Keine überprüfbare Vertrauenskette; Browser warnt, Benutzer gewöhnen
sich ans Wegklicken; ein zwischengeschalteter Angreifer wäre nicht erkennbar.

**Hinweis:** Die Verschlüsselung funktioniert. Was funktioniert nicht?

---

### 5

**Frage:** Welche Konten sollten sich am Admin Center anmelden dürfen, und welche
ausdrücklich nicht?

**Erwartungshorizont:** Nur dedizierte administrative Konten; keine Standardbenutzerkonten und
keine gemeinsam genutzten Konten; Nachvollziehbarkeit setzt personenbezogene Konten voraus.

**Hinweis:** Nach einem Vorfall wollen Sie wissen, wer was getan hat. Was setzt das voraus?

---

### 6

**Frage:** Was bedeutet das Prinzip der geringsten Rechte, und wo haben Sie es in diesem
Auftrag angewendet?

**Erwartungshorizont:** Nur so viele Rechte wie zur Aufgabe nötig; konkrete eigene Umsetzung
benannt, etwa bei Konten, Portfreigaben oder Zugriffsquellen.

**Hinweis:** Suchen Sie in Ihrer Konfiguration die Stelle, an der Sie bewusst weniger erlaubt
haben, als möglich gewesen wäre.

---

### 7

**Frage:** Sie haben den Domain Controller aus dem AWS Managed AD zur Verwaltung hinzugefügt.
Was war dafür nötig, und was können Sie dort trotzdem nicht tun?

**Erwartungshorizont:** Erreichbarkeit und passende Anmeldedaten der verwalteten Domäne; kein
vollwertiger Domänenadmin-Zugriff, weil AWS die Kontrolle über die DCs behält.

**Hinweis:** Beim Managed AD gibt AWS bestimmte Rechte grundsätzlich nicht ab.

---

### 8

**Frage:** Was würden Sie protokollieren, um administrative Zugriffe später nachvollziehen zu
können?

**Erwartungshorizont:** Anmeldungen an den Verwaltungssystemen, Änderungen an Konten und
Gruppen, Zugriffe von aussen; Bewusstsein, dass Protokolle nur nützen, wenn sie auch
ausgewertet werden.

**Hinweis:** Ein Protokoll, das niemand liest, hat schon manche Firma nicht gerettet.

---

### 9

**Frage:** Ein Kollege schlägt vor, RDP auf dem DC einfach für alle freizugeben, das sei
praktischer. Wie argumentieren Sie dagegen?

**Erwartungshorizont:** Direkte Erreichbarkeit des wichtigsten Systems aus dem Internet;
automatisierte Angriffe; Kompromittierung des DC bedeutet Kompromittierung der gesamten
Domäne; Alternative aufzeigen statt nur ablehnen.

**Hinweis:** Was ist der DC im Vergleich zu jedem anderen Server in Ihrer Umgebung?

---

### 10

**Frage:** Sie übergeben Ihre Umgebung an eine Nachfolgerin. Welche Angaben zur Administration
muss sie zwingend von Ihnen bekommen?

**Erwartungshorizont:** Zugangswege und deren Einschränkungen, verwendete Konten und ihre
Rechte, Besonderheiten der Absicherung; Bewusstsein, dass Passwörter nicht in die
Dokumentation gehören.

**Hinweis:** Alles, was sie sonst durch Ausprobieren herausfinden müsste — ausser dem einen,
was Sie ihr auf anderem Weg geben.
