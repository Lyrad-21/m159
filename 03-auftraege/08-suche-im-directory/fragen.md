# Auftrag 08 – Fragenkatalog

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

**Frage:** Was passiert bei einem LDAP-Bind, und warum steht er am Anfang jeder Abfrage?

**Erwartungshorizont:** Anmeldung am Verzeichnis mit einer Identität; das Verzeichnis
entscheidet danach, welche Objekte und Attribute überhaupt sichtbar sind; ohne Bind kein
oder nur anonymer Zugriff.

**Hinweis:** Bevor Sie fragen dürfen, muss klar sein, wer fragt. Warum ist das wichtig?

---

### 2

**Frage:** Was ist der Base-DN, und wie leitet er sich aus Ihrem Domainnamen ab?

**Erwartungshorizont:** Einstiegspunkt der Suche im Verzeichnisbaum; jeder Teil des
Domainnamens wird zu einer `DC=`-Komponente; eigener Base-DN korrekt genannt.

**Hinweis:** Nehmen Sie Ihren Domainnamen und zerlegen Sie ihn an den Punkten.

---

### 3

**Frage:** Was bewirkt der Scope einer LDAP-Suche, und was ändert sich zwischen One Level und
Subtree?

**Erwartungshorizont:** Legt die Suchtiefe ab dem Base-DN fest; One Level nur die direkte
Ebene darunter, Subtree den gesamten Teilbaum; Auswirkung am eigenen Ergebnis erklärbar.

**Hinweis:** Sie haben beides ausprobiert und unterschiedliche Trefferzahlen erhalten. Woher
kam der Unterschied?

---

### 4

**Frage:** Zeigen Sie einen Ihrer verschachtelten Filter und erklären Sie ihn Klammer für
Klammer.

**Erwartungshorizont:** Präfixnotation verstanden: Operator steht vor den Bedingungen; `&`, `|`
und `!` korrekt benannt; jede Teilbedingung erklärt.

**Hinweis:** Fangen Sie ganz aussen an. Welches Zeichen steht direkt nach der ersten Klammer,
und was bedeutet es?

---

### 5

**Frage:** Wie prüft man in einem LDAP-Filter ein einzelnes Bit innerhalb eines Attributs, und
wozu braucht man das?

**Erwartungshorizont:** Über eine besondere Vergleichsregel (Bitmaske) statt eines
Gleichheitsvergleichs; nötig, weil `userAccountControl` mehrere Zustände in einer Zahl
zusammenfasst — etwa deaktiviert oder Passwort läuft nie ab.

**Hinweis:** Das Attribut enthält eine einzige Zahl, in der mehrere Aussagen gleichzeitig
stecken. Ein Gleichheitsvergleich hilft da nicht weiter.

---

### 6

**Frage:** Was genau würde bei einem einfachen Bind über Port 389 durch das Netz gehen, und was
ändert LDAPS daran?

**Erwartungshorizont:** Anmeldename und Passwort unverschlüsselt lesbar; LDAPS verschlüsselt
die gesamte Verbindung über TLS; Port 636 statt 389.

**Hinweis:** Stellen Sie sich jemanden vor, der den Netzwerkverkehr mitliest. Was hätte er
nach Ihrem Bind?

---

### 7

**Frage:** Welche Rechte braucht das Dienstkonto der Firewall tatsächlich, und welche
ausdrücklich nicht?

**Erwartungshorizont:** Nur Lesezugriff auf die benötigten Objekte und Attribute; kein
Schreibrecht, keine administrativen Rechte; eigene Festlegung begründet.

**Hinweis:** Die Firewall will Benutzer finden. Muss sie dafür irgendetwas verändern können?

---

### 8

**Frage:** Warum gibt man einer Applikation nicht einfach ein Domänenadmin-Konto als
Bind-Konto?

**Erwartungshorizont:** Das Passwort liegt in der Konfiguration der Applikation und ist damit
so gut geschützt wie diese; eine kompromittierte Applikation gäbe volle Kontrolle über die
Domäne; Prinzip der geringsten Rechte.

**Hinweis:** Fragen Sie sich, wo dieses Passwort danach gespeichert ist — und wer dort
hinkommt.

---

### 9

**Frage:** Wie haben Sie nachgewiesen, dass Ihr Filter nicht nur zufällig das richtige Ergebnis
geliefert hat?

**Erwartungshorizont:** Gegentest mit einem bewusst angelegten Objekt, das knapp nicht passen
darf; Nachweis, dass es korrekt ausgeschlossen wird.

**Hinweis:** Ein Filter, der alle drei vorhandenen Benutzer findet, ist noch kein guter Filter.
Was fehlt zum Beweis?

---

### 10

**Frage:** Wo haben Sie Ihren Filter produktiv eingepflegt, und wie haben Sie geprüft, dass er
dort wirklich greift?

**Erwartungshorizont:** Gespeicherte Abfrage und GPO-Zielgruppenadressierung genannt;
Wirksamkeitsnachweis mit einem passenden **und** einem nicht passenden Benutzer.

**Hinweis:** Dass eine Einstellung bei jemandem ankommt, ist die halbe Prüfung. Was ist die
andere Hälfte?
