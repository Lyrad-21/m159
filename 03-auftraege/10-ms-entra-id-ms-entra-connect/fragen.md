# Auftrag 10 – Fragenkatalog

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

**Frage:** Was synchronisiert Entra Connect, und in welche Richtung läuft die Synchronisation?

**Erwartungshorizont:** Benutzer und Gruppen werden vom lokalen AD nach Entra ID abgeglichen;
das On-Prem-AD bleibt die führende Quelle, Entra ID ist das Abbild.

**Hinweis:** Wo legen Sie einen neuen Benutzer an, damit er in beiden Welten erscheint?

---

### 2

**Frage:** Was ist Password Hash Synchronization, und was wird dabei tatsächlich übertragen?

**Erwartungshorizont:** Nicht das Klartextpasswort, sondern ein Hash (des Passwort-Hashes); so
kann sich der Benutzer in der Cloud mit demselben Passwort anmelden wie on-prem.

**Hinweis:** Wandert Ihr Passwort im Klartext in die Cloud? Was sonst?

---

### 3

**Frage:** Warum muss der UPN-Suffix mit einer verifizierten, öffentlichen Domain
übereinstimmen?

**Erwartungshorizont:** Ohne verifizierte Domain landet der Benutzer unter `…onmicrosoft.com`;
ein sauberes SSO und ein einheitlicher Anmeldename brauchen den übereinstimmenden, öffentlichen
UPN.

**Hinweis:** Wie sieht der Anmeldename aus, wenn der Suffix *nicht* matched?

---

### 4

**Frage:** Was ist der Unterschied zwischen einem Initial- und einem Delta-Sync, und wann
brauchen Sie welchen?

**Erwartungshorizont:** Initial gleicht alles ab, Delta nur die Änderungen seit dem letzten
Lauf; Delta läuft automatisch periodisch, Initial stösst man nach grösseren Änderungen manuell
an.

**Hinweis:** Denken Sie an die beiden `Start-ADSyncSyncCycle`-Varianten aus den Ressourcen.

---

### 5

**Frage:** Was ist ein Hybrid Join, und wie unterscheidet er sich von einem reinen Azure AD
Join?

**Erwartungshorizont:** Beim Hybrid Join ist das Gerät gleichzeitig in der lokalen Domäne *und*
in Entra ID registriert; beim reinen Azure AD Join nur in Entra ID, ohne lokale Domäne.

**Hinweis:** In wie vielen Verzeichnissen ist das Gerät jeweils bekannt?

---

### 6

**Frage:** Wie haben Sie nachgewiesen, dass der Hybrid Join funktioniert?

**Erwartungshorizont:** Über `dsregcmd /status`; im Device State stehen sowohl `DomainJoined`
als auch `AzureAdJoined` auf `YES`.

**Hinweis:** Welchen Befehl haben Sie ausgeführt, und auf welche zwei Werte kommt es an?

---

### 7

**Frage:** Ein Benutzer ändert sein Passwort im lokalen AD. Kann er sich sofort in der Cloud mit
dem neuen Passwort anmelden?

**Erwartungshorizont:** Nicht zwingend sofort — die Änderung wird beim nächsten Sync-Zyklus
übertragen; kurze Verzögerung möglich, danach gilt das neue Passwort auch in der Cloud.

**Hinweis:** Was muss zwischen der Änderung und dem Cloud-Login erst noch passieren?

---

### 8

**Frage:** Warum bleibt das lokale AD die führende Quelle, statt Benutzer direkt in Entra ID
anzulegen?

**Erwartungshorizont:** Eine einzige Quelle der Wahrheit vermeidet Duplikate und Konflikte; die
Verwaltung bleibt zentral im AD, Entra ID spiegelt nur.

**Hinweis:** Was passiert, wenn dasselbe Konto an zwei Orten unabhängig gepflegt wird?

---

### 9

**Frage:** Welche Rolle spielt die Gruppenrichtlinie beim Hybrid Join?

**Erwartungshorizont:** Sie sorgt für die automatische Geräteregistrierung in Entra ID (z. B.
über den Service Connection Point / die entsprechende Richtlinie), sodass die Clients ohne
manuelle Einzelanmeldung hybrid werden.

**Hinweis:** Wie werden viele Clients registriert, ohne jeden einzeln von Hand einzurichten?

---

### 10

**Frage:** In welcher realen Situation richtet eine Firma eine Hybrid-Identität ein, statt rein
On-Prem oder rein Cloud zu arbeiten?

**Erwartungshorizont:** Nachvollziehbares Beispiel: bestehendes AD soll bleiben, gleichzeitig
werden Cloud-Dienste (z. B. Microsoft 365) genutzt; Hybrid erlaubt die schrittweise Migration
mit einer Identität.

**Hinweis:** Welche Firma hat schon ein AD, will aber trotzdem Microsoft-365-Dienste nutzen?
