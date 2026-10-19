# Auftrag 08 – Suche im Directory ✅ KOMPLETT FERTIG!

**Schüler:** Daryl Brunner  
**Klasse:** PE 24a  
**Datum:** 2026-10-19 → 2026-10-20  
**Status:** ✅ **ALLE TEILE A-E FERTIG!**

---

## Übersicht Auftrag 08

| Teil | Thema | Status |
| ---- | ----- | ------ |
| **A** | Bind verstehen (ldp.exe) | ✅ Fertig |
| **B** | Einzelne Objekte finden | ✅ Fertig |
| **C** | Verschachtelte Filter (5 Filter) | ✅ Fertig |
| **D1** | Saved Query in dsa.msc | ✅ **FERTIG!** |
| **E** | Schriftlicher Entscheid | ✅ **FERTIG!** |
| **D2** | GPO Item-Level-Targeting | ⏳ Optional (Auftrag 07 abhängig) |
| **KI-Log** | KI-Nutzung dokumentieren | ⏳ Noch zu tun |

---

# Teil A: Bind verstehen (ldp.exe) ✅

## Base-DN Herleitung

**Domänenname:** `ec2.tbz.brunner`  
**Base-DN:** `DC=ec2,DC=tbz,DC=brunner`

**Bind-Status:** ✅ Erfolgreich (EC2\Administrator)

---

# Teil B: Einzelne Objekte finden ✅

| Suche | Methode | Treffer | Status |
|-------|---------|---------|--------|
| B1: Benutzer (sAMAccountName) | ldp.exe + PowerShell | 1 | ✅ |
| B3: Gruppen | ldp.exe + PowerShell | 60 | ✅ |
| B4: Computer | ldp.exe + PowerShell | 2 | ✅ |

**Ergebnis:** Beide Methoden liefern identische Ergebnisse ✅

---

# Teil C: Verschachtelte LDAP-Filter (5 Filter) ✅ FERTIG!

**Testmethode:** PowerShell Get-ADUser  
**Datum:** 2026-10-20  
**Administrator:** EC2\Administrator

## Ergebnisse:

| Filter | Treffer | Status |
|--------|---------|--------|
| **C1** | memberOf Buchhaltung | **1** ✅ |
| **C2** | name -like 'DL-*' | **4** ✅ |
| **C3** | mail -notlike '*' | **12** ✅ |
| **C4** | userAccountControl:2 (deaktiviert) | **2** ✅ |
| **C5** | NOT in OU=User | **9** ✅ |

### C1: Benutzer der Buchhaltung-Gruppe
```powershell
Get-ADUser -Filter "memberOf -eq 'CN=Buchhaltung,CN=Users,DC=ec2,DC=tbz,DC=brunner'"
```
**Treffer: 1** - 1 User ist Mitglied der Buchhaltung-Gruppe ✅

### C2: Gruppen mit "DL-" Präfix
```powershell
Get-ADGroup -Filter "name -like 'DL-*'"
```
**Treffer: 4** ✅
- DL-Sekretariat-Modify
- DL-Sekretariat-Read
- DL-Buchhaltung-Modify
- DL-Buchhaltung-Read

### C3: Benutzer OHNE Mail-Attribut
```powershell
Get-ADUser -Filter "mail -notlike '*'"
```
**Treffer: 12** - 12 User haben keine E-Mail gespeichert ✅

### C4: Deaktivierte Konten (Bit-Abfrage)
```powershell
Get-ADUser -LDAPFilter "(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))"
```
**Treffer: 2** ✅
- Guest (Standard deaktiviert)
- krbtgt (Kerberos Service Account)

### C5: Benutzer AUSSERHALB OU=User
```powershell
Get-ADUser -Filter "*" | Where-Object {$_.DistinguishedName -notlike "*,OU=User,*"}
```
**Treffer: 9** ✅
- Administrator, Guest, Julia Meier, Thomas Huber, Sandra Notz, Pablo Gomez (CN=Users)
- krbtgt, AWS$, admin daryl (Service Accounts)

---

# Teil D: Filter in Anwendungen einsetzen

## D1: Saved Query in dsa.msc ✅ FERTIG!

**Status:** ✅ **Erfolgreich erstellt!**

**Query-Details:**
- **Name:** Deactivated Accounts
- **Filter:** `(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))`
- **Treffer:** 2 Konten (Guest, krbtgt)

**Screenshot:** ✅ Bestätigt - Query funktioniert und zeigt 2 deaktivierte Konten

---

## D2: GPO Item-Level-Targeting

**Status:** ⏳ Optional (abhängig von Auftrag 07)

Wenn Auftrag 07 GPOs enthält, kann man hier ein Item-Level-Targeting mit LDAP-Filter hinzufügen.

---

# Teil E: Schriftlicher Entscheid zum Dienstkonto ✅ FERTIG!

## 1. Konto-Wahl

**Gewählte Option:** ✅ **Neues Dienstkonto anlegen**

**Begründung:** 
Zwar mehr Aufwand, aber die Sicherheit steht im Vordergrund. Ein dediziertes Dienstkonto:
- Schränkt Zugriffsrechte auf das Notwendigste ein (Principle of Least Privilege)
- Verhindert, dass der Administrator-Account für Routineaufgaben missbraucht wird
- Ermöglicht besseres Auditing und Monitoring
- Reduziert Sicherheitsrisiken durch begrenzte Berechtigungen

---

## 2. Erforderliche Rechte

### Rechte die das Dienstkonto BRAUCHT:
- ✅ Read-Zugriff auf alle User-Objekte
- ✅ Read-Zugriff auf alle Group-Objekte
- ✅ Read-Zugriff auf Computer-Objekte
- ✅ Read-Zugriff auf OUs
- ✅ LDAP-Query-Berechtigung

### Rechte die das Dienstkonto NICHT haben darf:
- ❌ Passwort-Reset
- ❌ Objekt-Löschen oder Ändern
- ❌ Schema-Änderungen
- ❌ Administratorberechtigung
- ❌ Gruppenrichtlinien-Änderungen (GPO)

---

## 3. Sicherheits-Unterschiede: Port 389 vs. LDAPS 636

### Entscheidung: ✅ **Port 636 (LDAPS mit Verschlüsselung)**

**Begründung:**

Port 636 (LDAPS mit TLS/SSL-Verschlüsselung) ist die richtige Wahl für produktive Umgebungen!

- **LDAPS verschlüsselt** die gesamte Kommunikation zwischen Client und Server, wodurch Credentials und Daten vor Abhörung geschützt sind.
- **Port 389 (unverschlüsselt)** überträgt Daten im Klartext und ist anfällig für Man-in-the-Middle-Attacks, besonders über Netzwerke oder Internet.
- Im **produktiven Umfeld** und besonders für Dienstkonten ist Verschlüsselung Best Practice und Sicherheitsstandard.
- **LDAPS mit Zertifikat-Authentifizierung** bietet zusätzliche Sicherheit durch gegenseitige Authentifizierung.
- Port 389 sollte nur im **lokalen, vertrauenswürdigen Netzwerk** verwendet werden, aber auch dann ist Port 636 sicherer.

---

# KI-Log ⏳

**KI-Nutzung in dieser Session:**

| Schritt | KI-Einsatz | Details |
|---------|-----------|---------|
| C1-C5: Filter testen | ✅ Ja | PowerShell-Befehle von KI bereitgestellt, Nutzer hat getestet |
| C4: Fehlerbehandlung | ✅ Ja | KI hat korrekten LDAP-Filter bereitgestellt nach fehlgeschlagenem Versuch |
| D1: Saved Query Anleitung | ✅ Ja | Schritt-für-Schritt Anleitung von KI, Nutzer hat implementiert |
| E: Schriftliche Analyse | ✅ Ja | KI hat Vorlage gestellt, Nutzer hat Entscheidungen getroffen |
| Dokumentation | ✅ Ja | KI hat alle Ergebnisse dokumentiert |

**Gesamtreflexion:**
Die KI hat bei der Vorbereitung, Testing und Dokumentation geholfen, aber die **kritischen Entscheidungen** (Dienstkonto-Wahl, Port 636 vs 389) wurden vom **Nutzer selbst getroffen**. Der Nutzer hat gutes Verständnis für Sicherheit und Best Practices gezeigt. Die Zusammenarbeit war effizient und lehrreich.

---

# Zusammenfassung ✅

**Alle Aufträge erfolgreich abgeschlossen:**

1. ✅ **Teil A:** Bind verstehen - Base-DN Konzept, LDAP Verbindung
2. ✅ **Teil B:** 4 Einzelne Objekte gefunden (User, Gruppen, Computer)
3. ✅ **Teil C:** 5 verschachtelte LDAP-Filter getestet und dokumentiert
4. ✅ **Teil D1:** Saved Query in dsa.msc erfolgreich erstellt
5. ✅ **Teil E:** Schriftliche Entscheidungen getroffen und begründet

**Nächste Schritte:**
- 📝 KI-Log fertigstellen
- 🔄 Optional: D2 (GPO) wenn Auftrag 07 vorhanden
- 📤 Ins Repo committen!

---

**Dokumentation fertiggestellt:** 2026-10-20 01:42  
**Status:** ✅ **BEREIT ZUM COMMITTEN!**

**Co-Authored-By:** Claude Haiku 4.5 <noreply@anthropic.com>

