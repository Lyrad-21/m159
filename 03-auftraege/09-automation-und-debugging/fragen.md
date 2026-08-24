# Auftrag 09 – Fragenkatalog

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

**Frage:** Warum legt man Benutzerkonten in der Praxis per Skript an statt von Hand?

**Erwartungshorizont:** Grosse Stückzahlen und wiederkehrende Vorgänge; einheitliche
Namensgebung und Attribute; Nachvollziehbarkeit und Wiederholbarkeit; weniger Tippfehler.

**Hinweis:** Denken Sie an einen Lehrbetrieb, der im August vierzig Lernende gleichzeitig
aufnimmt.

---

### 2

**Frage:** Einer der Fehler im Skript betraf das Trennzeichen. Wie hat sich dieser Fehler
geäussert, und wie haben Sie ihn gefunden?

**Erwartungshorizont:** Die CSV wurde nicht korrekt in Spalten zerlegt, die Felder blieben leer
oder enthielten die ganze Zeile; Erkennung über die Ausgabe der eingelesenen Daten.

**Hinweis:** Was hätten Sie sehen müssen, wenn Sie sich nach dem Import einfach den Inhalt der
Variablen hätten ausgeben lassen?

---

### 3

**Frage:** Warum muss man in PowerShell innerhalb einer Zeichenkette `$($row.Vorname)`
schreiben und nicht einfach `$row.Vorname`?

**Erwartungshorizont:** Ohne die Klammern wird nur die Variable ersetzt und der Punkt als Text
behandelt; der Teilausdrucksoperator erzwingt die Auswertung des gesamten Ausdrucks.

**Hinweis:** Probieren Sie beides aus und schauen Sie sich an, was ohne Klammern in der Ausgabe
landet.

---

### 4

**Frage:** Wozu dient `ConvertTo-SecureString`, und warum akzeptiert `New-ADUser` kein
gewöhnliches Passwort als Text?

**Erwartungshorizont:** Wandelt Text in ein geschütztes Objekt um, das nicht im Klartext im
Speicher steht; das Cmdlet verlangt diesen Typ bewusst, um den Umgang mit Passwörtern
abzusichern.

**Hinweis:** Der Parameter erwartet einen bestimmten Datentyp. Warum wohl nicht einfach eine
Zeichenkette?

---

### 5

**Frage:** Was ist der `sAMAccountName`, und was passiert, wenn er bereits vergeben ist?

**Erwartungshorizont:** Eindeutiger Anmeldename innerhalb der Domäne, historisch auf 20 Zeichen
begrenzt; ein Duplikat führt zum Fehler beim Anlegen; deshalb braucht es eine Prüfung oder eine
Namensregel.

**Hinweis:** Ihre Firma stellt eine zweite Person namens Hans Muster ein. Was tut Ihr Skript?

---

### 6

**Frage:** Wie prüft Ihr Skript, ob ein Benutzer bereits existiert, und warum ist diese Prüfung
wichtiger als sie aussieht?

**Erwartungshorizont:** Abfrage mit `Get-ADUser` vor dem Anlegen, mit Fehlerbehandlung; ohne
Prüfung bricht das Skript ab oder erzeugt unklare Zustände; Wiederholbarkeit ohne Schaden.

**Hinweis:** Was passiert, wenn Sie Ihr Skript versehentlich zweimal laufen lassen?

---

### 7

**Frage:** Ihr Skript bricht mitten im Import ab, nachdem zwei von fünf Benutzern angelegt
wurden. Was ist jetzt das Problem, und wie geht man damit um?

**Erwartungshorizont:** Halbfertiger Zustand, der weder vollständig noch leer ist; erneuter Lauf
muss die bestehenden überspringen können; Protokollierung, um den Stand zu erkennen.

**Hinweis:** Genau dafür ist die Prüfung aus der vorherigen Frage da. Warum?

---

### 8

**Frage:** Woher stammen die Benutzerdaten in einem echten Betrieb, und was versteht man unter
einem User-Lifecycle-Prozess?

**Erwartungshorizont:** Aus einem führenden System, meist der Personaladministration;
Lebenszyklus von Eintritt über Wechsel bis Austritt; besonders der Austritt muss zuverlässig
zum Sperren führen.

**Hinweis:** Das Anlegen ist der einfache Teil. Welcher Schritt wird in der Praxis am
häufigsten vergessen?

---

### 9

**Frage:** Welche Attribute setzt Ihr Skript, und welche wären in einem echten Betrieb
zusätzlich nötig?

**Erwartungshorizont:** Eigene gesetzte Attribute korrekt genannt; sinnvolle Ergänzungen wie
Mailadresse, Abteilung, Vorgesetzte oder Personalnummer; Bezug zur späteren Auswertbarkeit.

**Hinweis:** Denken Sie an Auftrag 08: Wonach wollten Sie dort filtern, und woher kämen diese
Werte?

---

### 10

**Frage:** Im Skript steht ein Passwort im Klartext. Was ist daran problematisch, und wie löst
man es besser?

**Erwartungshorizont:** Jeder mit Lesezugriff auf das Skript kennt das Passwort; landet über
Git in der Versionsgeschichte; besser sind Zufallspasswörter mit erzwungener Änderung bei der
ersten Anmeldung oder eine geschützte Ablage.

**Hinweis:** Ihr Skript liegt in Ihrem Repository. Wer kommt dort überall hin — auch in die
Vergangenheit?
