# Auftrag 13 – Fragenkatalog

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

**Frage:** Beschreiben Sie Schritt für Schritt, was beim Login über Ihre App passiert
(OIDC-Ablauf).

**Erwartungshorizont:** Die App leitet zum IdP (Entra ID) weiter, der Benutzer meldet sich dort
an, der IdP ruft die Callback-URL mit einem Code/Token auf, die App erhält daraus ein Token und
kennt damit die Identität — ohne das Passwort je zu sehen.

**Hinweis:** Zwischen App und Entra ID gibt es mehrere Weiterleitungen. Wer meldet sich wo an?

---

### 2

**Frage:** Wozu dienen Client ID, Client Secret und Tenant ID, und wo gehören sie hin?

**Erwartungshorizont:** Sie identifizieren und authentifizieren die App gegenüber Entra ID; das
Secret ist vertraulich und gehört in die `.env` (nicht in den Code/das Repo), Client- und
Tenant-ID benennen App und Verzeichnis.

**Hinweis:** Welcher der drei Werte ist geheim, und wo darf er auf keinen Fall landen?

---

### 3

**Frage:** Warum führte der Aufruf über `127.0.0.1` statt `localhost` zu einem Redirect-URI-
Mismatch?

**Erwartungshorizont:** Die in Entra ID registrierte Redirect-URI muss exakt mit der
aufgerufenen übereinstimmen; `127.0.0.1` und `localhost` gelten als verschiedene URIs.

**Hinweis:** Wie genau muss die aufgerufene Adresse mit der registrierten übereinstimmen?

---

### 4

**Frage:** Worin unterscheiden sich Ihre drei Login-Tests: manuelle Anmeldung, token-basiertes
SSO und Kerberos-/WIA-SSO?

**Erwartungshorizont:** Manuell = Passwort eingeben; token-basiert = bereits an Entra ID
angemeldet, deshalb ohne erneute Passworteingabe; Kerberos/WIA = domain-/hybrid-joined Client
meldet sich über die Windows-Anmeldung ohne Prompt an.

**Hinweis:** Bei welchem Test tippen Sie ein Passwort, bei welchen nicht — und warum?

---

### 5

**Frage:** Was ist eine Redirect-/Callback-URI und warum ist sie sicherheitsrelevant?

**Erwartungshorizont:** Die Adresse, an die der IdP nach dem Login den Code/das Token
zurückschickt; die Registrierung erlaubter URIs verhindert, dass Tokens an fremde Ziele
umgeleitet werden.

**Hinweis:** Was könnte passieren, wenn ein Angreifer eine eigene Rücksprungadresse
unterschieben könnte?

---

### 6

**Frage:** Warum darf das Client Secret nicht ins Git-Repository, und wie haben Sie es
geschützt?

**Erwartungshorizont:** Es ist ein Geheimnis, mit dem sich die App ausgibt; im Repo wäre es
öffentlich. Schutz über `.env` und `.gitignore` (bzw. es nicht einchecken).

**Hinweis:** Wer könnte das Secret lesen, wenn es im Repo läge — und was damit tun?

---

### 7

**Frage:** Was erhält die App vom IdP nach erfolgreichem Login, und was macht sie damit?

**Erwartungshorizont:** Ein ID-/Access-Token mit Claims zur Identität; die App vertraut dem IdP
und wertet das Token aus, statt selbst Passwörter zu prüfen.

**Hinweis:** Die App sieht das Passwort nie. Was bekommt sie stattdessen?

---

### 8

**Frage:** Wie unterscheidet sich modernes OIDC/OAuth-SSO von klassischem Kerberos-SSO?

**Erwartungshorizont:** OIDC ist token-basiert und läuft über HTTP/Web mit einem IdP; Kerberos
ist ticket-basiert und läuft im AD/LAN über den KDC. Beide erreichen SSO, aber über
verschiedene Wege.

**Hinweis:** Welches Verfahren funktioniert auch für eine Web-App im Internet, welches eher im
Firmennetz?

---

### 9

**Frage:** Warum funktioniert das Kerberos-/WIA-SSO nur, wenn der Client domain-/hybrid-joined
ist und der richtige (öffentliche) UPN verwendet wird?

**Erwartungshorizont:** WIA nutzt die bestehende Windows-Anmeldung; ohne Domänen-/Hybrid-Join
gibt es keine nutzbare Kerberos-Identität, und der Benutzer muss unter dem öffentlichen UPN
existieren, damit die Zuordnung stimmt.

**Hinweis:** Woher nimmt der Browser bei WIA die Identität, ohne dass Sie etwas eingeben?

---

### 10

**Frage:** In welcher realen Situation bindet man eine eigene Web-App an einen IdP an, statt eine
eigene Benutzerverwaltung zu bauen?

**Erwartungshorizont:** Nachvollziehbares Beispiel: kein eigenes Passwort-Handling nötig,
zentrales SSO und MFA, einheitliche Konten über viele Anwendungen, höhere Sicherheit.

**Hinweis:** Was muss die App alles *nicht* mehr selbst tun, wenn der IdP den Login übernimmt?
