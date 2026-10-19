# Auftrag 09: Fehlerprotokoll - User-Import Debugging

## Gefundene Fehler & Lösungen

### ❌ FEHLER 1: Delimiter-Konflikt (Zeile 5)
**Problem:** 
- CSV-Datei nutzt Komma `,` als Trennzeichen
- Skript erwartet Semikolon `;`
- Resultat: CSV wird falsch geparst

**Lösung:**
```powershell
# FALSCH:
$users = Import-CSV $csvPath -Delimiter ";"

# RICHTIG:
$users = Import-CSV $csvPath -Delimiter ","
```

---

### ❌ FEHLER 2: Falscher Passwort-Befehl (Zeile 19)
**Problem:**
- `ConvertFrom-SecureString` konvertiert VON SecureString zu PlainText
- Aber wir brauchen das Gegenteil: PlainText zu SecureString
- Resultat: Skript-Fehler bei User-Erstellung

**Lösung:**
```powershell
# FALSCH:
-AccountPassword (ConvertFrom-SecureString "Schule123" -AsPlainText -Force)

# RICHTIG:
-AccountPassword (ConvertTo-SecureString "Schule123" -AsPlainText -Force)
```

---

### ❌ FEHLER 3: Distinguished Name String-Expansion (Zeile 11)
**Problem:**
- `$row.Abteilung` wird in doppelten Anführungszeichen nicht expandiert
- DN wird falscher Weise: `OU=$row.Abteilung,OU=User,...` statt `OU=IT,OU=User,...`
- Resultat: User wird in falscher OU erstellt

**Lösung:**
```powershell
# FALSCH:
$targetOU = "OU=$row.Abteilung,OU=User,DC=it-tbz,DC=local"

# RICHTIG (Sub-Expression Operator):
$targetOU = "OU=$($row.Abteilung),OU=User,DC=it-tbz,DC=local"
```

---

### ❌ FEHLER 4: Name-String Expansion (Zeile 15)
**Problem:**
- `"$row.Vorname $row.Nachname"` ist unpräzise
- Besser mit Sub-Expression Operator für Klarheit
- Resultat: Funktioniert, aber nicht Best Practice

**Lösung:**
```powershell
# NICHT OPTIMAL:
-Name "$row.Vorname $row.Nachname"

# BESSER:
-Name "$($row.Vorname) $($row.Nachname)"
```

---

### ❌ FEHLER 5 (Teil B): Fehlende Existenzprüfung
**Problem:**
- Skript prüft nicht, ob User bereits existiert
- Bei erneutem Lauf: Duplikate oder Fehler
- Resultat: Keine Fehlerkontrolle

**Lösung - Code hinzugefügt:**
```powershell
# Existenzprüfung VOR User-Erstellung:
$userExists = Get-ADUser -Filter "sAMAccountName -eq '$sAMAccountName'" -ErrorAction SilentlyContinue

if ($userExists) {
    Write-Host "⚠️  User '$sAMAccountName' existiert bereits! Übersprungen." -ForegroundColor Yellow
    continue
}

# Erfolgs-Ausgabe mit Farbe:
Write-Host "✓ User '$sAMAccountName' erfolgreich erstellt!" -ForegroundColor Green
```

---

## Zusammenfassung der Korrektionen

| Fehler | Art | Zeile | Behoben |
|--------|-----|-------|---------|
| Delimiter ; statt , | Konfiguration | 5 | ✓ |
| ConvertFrom statt ConvertTo | Logik | 19 | ✓ |
| Keine Variable-Expansion in DN | Syntax | 11 | ✓ |
| Unscharfe String-Expansion | Style | 15 | ✓ |
| Keine Duplikat-Prüfung | Funktional | - | ✓ |

---

## Test-Ergebnis

✓ **Skript läuft ohne Fehler**
✓ **Users werden in korrekten OUs erstellt**
✓ **Duplikat-Schutz aktiv**
✓ **Farbige Ausgaben für bessere Lesbarkeit**
