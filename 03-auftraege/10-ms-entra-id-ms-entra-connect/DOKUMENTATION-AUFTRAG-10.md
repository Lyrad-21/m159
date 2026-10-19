# Auftrag 10: MS Entra ID & MS Entra Connect - Dokumentation

**Datum:** 2026-10-19  
**Status:** ✅ **FERTIG**  
**Bearbeiter:** Daryl Leon Brunner

---

## 📋 Aufgabenbeschreibung

Konfiguration von Microsoft Entra ID und Entra Connect Sync zur Synchronisierung einer On-Premises Active Directory (EC2) mit Microsoft Entra ID in einer Hybrid-Umgebung.

---

## ✅ Ergebnisse

### **Synchronisierung erfolgreich!**

**Status:** Alle 3 Test-User wurden erfolgreich von EC2 AD zu Entra ID synchronisiert.

#### **Synchronisierte User:**
- ✅ **Hans Muster** (HMuster@ec2.tbz.brunner) → Entra ID
- ✅ **Petra Beispiel** (PBeispiel@ec2.tbz.brunner) → Entra ID
- ✅ **Lars Lustig** (LLustig@ec2.tbz.brunner) → Entra ID

**Beweis:** Screenshot aus Azure Entra Admin Center zeigt alle 3 User mit Status "On-premises sy..." = **Yes**

---

## 🔧 Durchgeführte Schritte

### **1. Entra Connect Installation**
- ✅ Microsoft Entra Connect Sync heruntergeladen
- ✅ Installation auf ADMINCTR01 durchgeführt
- ✅ Alle erforderlichen Komponenten installiert

### **2. Konfiguration - Express Settings**
- ✅ Azure AD Admin Account erstellt (im Tenant)
- ✅ EC2 AD Admin Credentials eingegeben (EC2\Administrator)
- ✅ Single Sign-On aktiviert

### **3. Konfiguration - Detailed Setup**

#### **User Sign-In**
- ✅ **Password Hash Synchronization** ausgewählt (WICHTIG!)
- ✅ Benutzer können sich mit on-premises Passwörtern anmelden

#### **Connect to Microsoft Entra ID**
- ✅ Azure Admin Account authentifiziert
- ✅ Verbindung zu Entra ID hergestellt

#### **Connect Directories**
- ✅ EC2 Active Directory verbunden
- ✅ Domain: `ec2.tbz.brunner`
- ✅ Forest: `ec2.tbz.brunner`

#### **Domain and OU Filtering**
- ✅ "Sync all domains and OUs" aktiviert
- ✅ Alle User und OUs werden synchronisiert

#### **Identifying Users**
- ✅ "Users are represented only once across all directories"
- ✅ "Let Azure manage the source anchor"

#### **Filter Users and Devices**
- ✅ "Synchronize all users and devices" aktiviert
- ✅ Keine Filterung erforderlich

#### **Optional Features**
- ✅ **Password hash synchronization** aktiviert (KRITISCH!)
- ✅ Andere Features nicht nötig

### **4. Synchronisierung gestartet**
- ✅ "Start the synchronization process when configuration completes" ✓
- ✅ Installation durchgeführt
- ✅ Erste Synchronisierung automatisch gestartet

### **5. Validierung**
- ✅ Azure Entra Admin Center → Users
- ✅ Alle 3 User sind dort mit Status "On-premises sy..." = Yes
- ✅ Synchronisierung funktioniert! ✅

---

## 🔑 Wichtige Erkenntnisse

### **Password Hash Synchronization ist KRITISCH!**
- ✅ Ermöglicht SSO (Single Sign-On)
- ✅ User können sich mit AD-Passwörtern bei Entra ID anmelden
- ✅ Für Auftrag 13 (SSO Python App) erforderlich!

### **Domain-Problem gelöst**
- ❌ Anfangs: `ec2.tbz.brunner` war nicht als Custom Domain in Entra ID registriert
- ✅ Lösung: "Continue without matching all UPN suffixes to verified domains" angekreuzt
- ℹ️ Custom Domain kann später hinzugefügt werden (braucht DNS-Verification)

### **Azure Admin Account**
- ✅ Neuer User im Tenant erstellt (statt externer Gast)
- ✅ Global Admin Rechte vergeben
- ✅ Login funktioniert ohne Probleme

---

## 📊 Konfigurationsdetails

### **Entra Connect Server**
- **Hostname:** ADMINCTR01
- **Betriebssystem:** Windows Server 2022
- **Entra Connect Version:** Latest (installiert 2026-10-19)

### **On-Premises AD**
- **Domain:** ec2.tbz.brunner
- **Forest:** ec2.tbz.brunner
- **Admin Account:** EC2\Administrator

### **Entra ID Tenant**
- **Tenant:** brunnerdarylgmail.onmicrosoft.com
- **Admin Account:** admin-entra-connect@brunnerdarylgmail.onmicrosoft.com
- **Synchronization Method:** Password Hash Sync

---

## 🧪 Test-Ergebnisse

### **Synchronisierung validiert:**

```
Azure Entra Admin Center → Users
───────────────────────────────────
11 users found

Display name          | User principal name              | On-premises sy...
──────────────────────┼──────────────────────────────────┼───────────────
✅ Hans Muster       | HMuster@brunner...               | YES
✅ Petra Beispiel    | PBeispiel@brunner...             | YES
✅ Lars Lustig       | LLustig@brunner...               | YES
```

**Alle User synchronisiert!** ✅

---

## 📝 Befehle für späteren Einsatz

### **Synchronisierung manuell triggern (PowerShell auf ADMINCTR01):**

```powershell
# Modul laden (nach PowerShell Neustart)
Import-Module ADSync

# Delta Sync starten
Start-ADSyncSyncCycle -PolicyType Delta

# Initial Sync starten (komplett)
Start-ADSyncSyncCycle -PolicyType Initial

# Sync Status prüfen
Get-ADSyncConnectorRunStatus
```

### **Sync Service Manager öffnen:**
```
Start → "Synchronization Service Manager"
```

---

## 🎯 Nächste Schritte

### **Auftrag 13: SSO Python App** 🚀
- Python App starten
- Entra ID SSO testen
- User sollten sich ohne Passwortprompt anmelden können
- Video-Beweis erforderlich

### **Optional: Custom Domain hinzufügen**
- `ec2.tbz.brunner` als Custom Domain zu Entra ID hinzufügen
- DNS-Verification durchführen
- User können sich direkt mit `username@ec2.tbz.brunner` anmelden

---

## 📸 Beweis-Screenshots

1. **Azure Entra Admin Center - Users-Liste** ✅
   - Zeigt alle 3 synchronisierten User
   - Status "On-premises sy..." = YES für alle User
   - Proof der erfolgreichen Synchronisierung

---

## ✨ Zusammenfassung

| Punkt | Status |
|-------|--------|
| **Entra Connect Installation** | ✅ Fertig |
| **AD-zu-Entra Verbindung** | ✅ Fertig |
| **Password Hash Sync** | ✅ Aktiviert |
| **User-Synchronisierung** | ✅ 3/3 Users OK |
| **Validierung in Azure Portal** | ✅ Bestätigt |
| **Dokumentation** | ✅ Fertig |

---

## 🎓 Lerneffekte

- ✅ Hybrid Identity Management mit Entra Connect
- ✅ Password Hash Synchronization für SSO
- ✅ On-Premises AD Integration mit Cloud
- ✅ User-Management in Hybrid-Umgebungen
- ✅ Troubleshooting von Entra Connect Installationen

---

**Auftrag 10: ABGESCHLOSSEN** ✅

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
