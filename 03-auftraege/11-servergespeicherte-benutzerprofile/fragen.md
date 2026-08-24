# Auftrag 11 – Fragenkatalog

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

**Frage:** Was ist das Problem mit rein lokalen Profilen, und was lösen servergespeicherte
Profile?

**Erwartungshorizont:** Bei lokalen Profilen liegen die Daten nur auf einem PC; bei einem
Gerätewechsel oder Defekt sind sie weg. Servergespeicherte Profile machen sie an mehreren
Geräten verfügbar.

**Hinweis:** Was passiert mit den Dateien eines Benutzers, wenn er den PC wechselt?

---

### 2

**Frage:** Was ist der Unterschied zwischen einem Roaming Profile und Folder Redirection?

**Erwartungshorizont:** Roaming Profile kopiert das gesamte Profil bei An- und Abmeldung;
Folder Redirection leitet nur bestimmte bekannte Ordner auf eine Freigabe um, ohne alles zu
kopieren.

**Hinweis:** Bei welcher Variante wird bei jeder Anmeldung alles hin- und herkopiert?

---

### 3

**Frage:** Was macht FSLogix anders als klassische Roaming Profiles, und welchen Vorteil bringt
das?

**Erwartungshorizont:** FSLogix legt das Profil als Container (VHD/VHDX) ab und bindet es beim
Login direkt ein, statt zu kopieren; schnellere Anmeldung, weniger Profilkorruption.

**Hinweis:** Wird bei FSLogix noch kopiert, oder wird etwas eingehängt?

---

### 4

**Frage:** Was ist OneDrive Known Folder Move (KFM), und welche Ordner betrifft es?

**Erwartungshorizont:** KFM verschiebt die bekannten Ordner Desktop, Dokumente und Bilder nach
OneDrive for Business und synchronisiert sie in die Cloud.

**Hinweis:** Um welche drei Standardordner geht es typischerweise?

---

### 5

**Frage:** Über welchen Mechanismus haben Sie die OneDrive-KFM-Migration ausgerollt?

**Erwartungshorizont:** Über eine GPO (u. a. „Silently move known folders to OneDrive" plus
Tenant-URL, „Silently configure OneDrive"), verknüpft mit der OU der Testbenutzer.

**Hinweis:** Womit verteilen Sie Einstellungen automatisch an alle Benutzer einer OU?

---

### 6

**Frage:** Warum aktiviert man „Prevent users from redirecting their known folders back to their
PC"?

**Erwartungshorizont:** Damit Benutzer die Umleitung nicht rückgängig machen und Daten wieder
nur lokal ablegen; sichert die Datenkonsistenz und die zentrale Verfügbarkeit.

**Hinweis:** Was könnte ein Benutzer sonst tun, das Ihre Migration wieder aushebelt?

---

### 7

**Frage:** Wie haben Sie nachgewiesen, dass die Synchronisation geräteübergreifend funktioniert?

**Erwartungshorizont:** Datei auf PC1 erstellt, an PC2 mit demselben Benutzer angemeldet und
geprüft, dass sie dort erscheint — und umgekehrt.

**Hinweis:** Ein Test auf nur einem Gerät beweist noch nicht das „Roaming". Was fehlt?

---

### 8

**Frage:** Woher weiss der OneDrive-Client bei der stillen Konfiguration, als welcher Benutzer
er sich anmelden soll?

**Erwartungshorizont:** Über das primäre Windows-Konto der angemeldeten (hybriden/Entra-)
Identität; deshalb funktioniert die automatische Anmeldung ohne manuelle Eingabe.

**Hinweis:** Welche Anmeldung nutzt OneDrive „silently" wieder?

---

### 9

**Frage:** Wo liegen die Profildaten am Ende physisch, und was bedeutet das für Verfügbarkeit
und Abhängigkeiten?

**Erwartungshorizont:** In der Cloud (OneDrive) bzw. auf der Profilfreigabe; überall verfügbar,
aber abhängig von Netzwerk/Internet und dem Tenant/Server.

**Hinweis:** Was brauchen die Clients zwingend, damit die Daten erreichbar sind?

---

### 10

**Frage:** In welcher realen Situation würden Sie FSLogix einsetzen und in welcher eher OneDrive
KFM?

**Erwartungshorizont:** FSLogix bei Terminalserver/VDI mit häufig wechselnden Sessions; OneDrive
KFM für normale Clients, bei denen es vor allem um die bekannten Benutzerordner geht.

**Hinweis:** Wo melden sich viele Benutzer nacheinander auf denselben Servern an?
