# Auftrag 04 – Fragenkatalog

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

**Frage:** Ein Benutzer greift über das Netz auf eine Freigabe zu. Welche Berechtigung gilt,
wenn Freigabe- und NTFS-Rechte unterschiedlich sind?

**Erwartungshorizont:** Die restriktivere von beiden gewinnt; beim lokalen Zugriff greift nur
NTFS; in der Praxis Freigabe grosszügig, NTFS präzise.

**Hinweis:** Sie müssen durch zwei Türen. Welche bestimmt, wie weit Sie kommen?

---

### 2

**Frage:** Wofür steht AGDLP, und was bedeutet jeder einzelne Buchstabe?

**Erwartungshorizont:** Account → Global Group → Domain Local Group → Permission; Benutzer in
globale Gruppen, diese in domänenlokale, und nur diese erhalten Berechtigungen.

**Hinweis:** Vier Buchstaben, vier Stationen. Am Anfang steht ein Benutzer, am Ende ein Recht.

---

### 3

**Frage:** Warum vergibt man Berechtigungen nicht direkt an einzelne Benutzer?

**Erwartungshorizont:** Nicht skalierbar und nicht nachvollziehbar; bei Personalwechsel müssten
alle Ordner angefasst werden; über Gruppen genügt eine Mitgliedschaftsänderung.

**Hinweis:** Stellen Sie sich vor, eine Mitarbeiterin wechselt die Abteilung. Wie viele
Stellen müssen Sie anfassen?

---

### 4

**Frage:** Was bewirkt Access Based Enumeration, und was sieht ein Benutzer mit und ohne diese
Einstellung?

**Erwartungshorizont:** Ordner, auf die keine Leseberechtigung besteht, werden ausgeblendet
statt nur gesperrt; ohne ABE sieht man alles und erhält beim Öffnen eine Fehlermeldung.

**Hinweis:** Ohne ABE erfährt ein Benutzer, dass es einen Ordner «Geschäftsleitung» gibt. Mit
ABE nicht.

---

### 5

**Frage:** Zeigen Sie eine Ihrer Gruppen. Welchen Gruppenbereich hat sie, und warum diesen?

**Erwartungshorizont:** Eigene Gruppe korrekt eingeordnet; global für Benutzerbündelung,
domänenlokal für Berechtigungsvergabe; Begründung passt zum AGDLP-Konzept.

**Hinweis:** Schauen Sie in die Eigenschaften der Gruppe. Dort stehen Bereich und Typ.

---

### 6

**Frage:** Was passiert mit den NTFS-Berechtigungen einer Datei, wenn Sie sie innerhalb
desselben Laufwerks verschieben — und was, wenn Sie sie kopieren?

**Erwartungshorizont:** Verschieben innerhalb eines Volumes behält die bestehenden
Berechtigungen; Kopieren erzeugt ein neues Objekt, das die Rechte des Zielordners erbt.

**Hinweis:** Beim einen Vorgang entsteht etwas Neues, beim anderen wird nur ein Verweis
umgehängt.

---

### 7

**Frage:** Was ist Vererbung bei NTFS-Berechtigungen, und wann würden Sie sie bewusst
unterbrechen?

**Erwartungshorizont:** Unterordner übernehmen die Rechte des übergeordneten Ordners;
Unterbrechung dort, wo ein Bereich abweichend geschützt werden muss; erhöht die Komplexität
und sollte die Ausnahme bleiben.

**Hinweis:** In den erweiterten Sicherheitseinstellungen gibt es dafür eine Schaltfläche. Was
tut sie mit den bestehenden Einträgen?

---

### 8

**Frage:** Ein Benutzer ist in zwei Gruppen: eine erlaubt Vollzugriff, die andere verweigert
Schreibrechte. Was gilt?

**Erwartungshorizont:** Ein ausdrückliches Verweigern setzt sich gegen ein Erlauben durch;
deshalb wird Verweigern in der Praxis nur sehr gezielt eingesetzt.

**Hinweis:** Eine der beiden Berechtigungsarten ist stärker als die andere. Welche, und warum
ist das gefährlich?

---

### 9

**Frage:** Wie haben Sie überprüft, dass Ihre Berechtigungen tatsächlich so greifen wie geplant?

**Erwartungshorizont:** Test mit einem echten Benutzerkonto der jeweiligen Gruppe, nicht als
Administrator; sowohl erlaubter als auch verweigerter Zugriff getestet.

**Hinweis:** Als Administrator kommen Sie überall hin. Was sagt Ihnen dieser Test also?

---

### 10

**Frage:** Ihre Firma stellt eine Person ein, die in zwei Abteilungen arbeitet. Was müssen Sie
in Ihrem Gruppenkonzept tun — und was ausdrücklich nicht?

**Erwartungshorizont:** Aufnahme in beide globalen Gruppen; keine neuen Berechtigungen auf
Ordnern setzen und keine Sonderrechte am Benutzer selbst.

**Hinweis:** Wenn Ihr Konzept sauber ist, ist die Antwort erstaunlich kurz.
