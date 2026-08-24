# Auftrag 09: Identity Management & PowerShell Debugging

## Ressourcen

- [Bewertungskriterien](../../08-kompetenznachweise/lb2/kompetenzmatrix-lb2.md)
- [Fragenkatalog für den mündlichen Nachweis](fragen.md)
- [import-users.ps1](import-users.ps1) – das fehlerhafte Skript

## 1. Einleitung & Szenario
In modernen IT-Infrastrukturen werden Identitäten (User) selten manuell erstellt. 
Die Synchronisation zwischen HR-Systemen und dem Active Directory erfolgt meist über Skripte oder spezialisierte Tools. 
Bevor Daten in Cloud-Systeme (wie MS Entra ID) synchronisiert werden können, müssen sie lokal im Active Directory sauber aufbereitet werden.

**Szenario:**
Die IT-Abteilung hat von einem ehemaligen Lernenden ein Skript geerbt, das den User-Import aus einer CSV-Datei automatisieren soll.
Leider wurde das Skript nie stabil fertiggestellt. Es enthält sowohl **Syntaxfehler**, **logische Fehler** als auch **Konfigurationsfehler**, 
die verhindern, dass es in Ihrer Umgebung läuft.

Ihre Aufgabe ist es, dieses "Legacy-Skript" zu debuggen, zu reparieren und an Ihre Laborumgebung anzupassen.

## 2. Lernziele
* Fehlermeldungen in der PowerShell lesen, verstehen und beheben.
* Bestehenden Code analysieren und logische Lücken schliessen.
* Den Umgang mit dem Active Directory Modul vertiefen.
* Grundverständnis für automatisierte User-Lifecycle-Prozesse entwickeln.

---

## 3. Vorbereitung der Umgebung
Bevor Sie mit dem Debugging beginnen, müssen die Rahmenbedingungen im Active Directory stimmen. Das Skript setzt eine spezifische Struktur voraus:

1. **AD-Struktur anlegen:** * Öffnen Sie "Active Directory Users and Computers" (`dsa.msc`).
    * Erstellen Sie direkt unter Ihrer Domain-Wurzel (z.B. `DC=it-tbz,DC=local`) eine neue Organisationseinheit (OU) namens **User**.
    * Erstellen Sie innerhalb der OU `User` drei weitere OUs: **IT**, **Marketing** und **Support**.
2. **Datenquelle:** Erstellen Sie auf Ihrem Domain Controller (DC) einen Ordner `C:\Temp\`.
3. **CSV-Datei:** Erstellen Sie darin eine Datei namens `mitarbeiter.csv` mit folgendem Inhalt (verwenden Sie exakt dieses Format):
   ```csv
   Vorname,Nachname,Abteilung
   Hans,Muster,IT
   Petra,Beispiel,Marketing
   Lars,Lustig,Support
   

## 4. Das defekte Skript ("Legacy Code")

Kopieren Sie den folgenden Code [import_users.ps1](import-users.ps1) in die PowerShell ISE auf Ihrem DC und speichern Sie ihn als import_users.ps1.

**Achtung**: Dieses Skript ist absichtlich fehlerhaft. Das Ausführen wird mehrere Fehlermeldungen produzieren. Es dient als Basis für Ihre Debugging-Arbeit.

## 5. Arbeitsauftrag

### Teil A: Analyse & Debugging
Identifizieren und korrigieren Sie die Fehler im Skript, damit der Import reibungslos funktioniert. Dokumentieren Sie Ihre Korrekturen in einem kurzen Log. Achten Sie besonders auf folgende Punkte:

1. **Trennzeichen-Konflikt:** Das Skript erwartet ein anderes Trennzeichen (-Delimiter), als in Ihrer CSV-Datei verwendet wird. Passen Sie eines von beiden an.

2. **String-Handling:** In PowerShell müssen Objekt-Eigenschaften (wie $row.Vorname) innerhalb von Anführungszeichen speziell umschlossen werden (Sub-Expression Operator $()), damit sie korrekt als Text aufgelöst werden. Finden Sie alle betroffenen Stellen im Skript.

3. **AD-Pfade:** Korrigieren Sie die Distinguished Names (DC=..., DC=...) im Skript, damit sie exakt zu Ihrem tatsächlichen Domainnamen passen.

4. **Passwort-Konvertierung:** Das Skript nutzt den falschen Befehl, um ein Passwort für den New-ADUser Befehl vorzubereiten. Recherchieren Sie den korrekten Befehl (ConvertTo-... statt ConvertFrom-...).

5. **OU-Logik:** Stellen Sie sicher, dass der Pfad in der Variable $targetOU exakt der Struktur entspricht, die Sie in Punkt 3 angelegt haben.

### Teil B: Funktionale Erweiterung
Erweitern Sie das Skript um eine wichtige Sicherheitsprüfung:

* Bevor ein User angelegt wird, soll das Skript mit Get-ADUser prüfen, ob der berechnete sAMAccountName bereits im Active Directory existiert.

* Falls der User existiert: Geben Sie eine gelbe Warnmeldung in der Konsole aus und überspringen Sie diesen Eintrag.

* Falls der User nicht existiert: Legen Sie den User an und geben Sie eine grüne Erfolgsmeldung aus.

## 6. Abgabe-Kriterien

1. Fehlerprotokoll: Eine Liste der korrigierten Fehler (Was war das Problem? Wie haben Sie es gelöst?).

2. Funktionierendes Skript: Ihr finaler, lauffähiger PowerShell-Code.

3. Erfolgsnachweis: Ein Screenshot Ihrer AD-Konsole (dsa.msc), auf dem die drei neu erstellten User in ihren jeweiligen Abteilungs-OUs (IT, Marketing, Support) zu sehen sind.