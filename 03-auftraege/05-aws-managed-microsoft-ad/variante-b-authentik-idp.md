# Auftrag 05 – Variante B: Moderner IdP mit Authentik

> [!IMPORTANT]
>
> Dies ist eine **wählbare Alternative** zu [Auftrag 05 (AWS Managed AD / Trust)](readme.md).
> Statt zwei AD-Welten per Forest Trust zu koppeln, setzen Sie einen modernen Identity Provider
> **vor** Ihr bestehendes AD. Sie bearbeiten **entweder** Variante A **oder** Variante B — nicht
> beide. Der Wechsel wird mit der Lehrperson abgesprochen; Variante B wird nach denselben vier
> Stufen bewertet wie Variante A.
>
> **Warum diese Variante:** kein kostenpflichtiges AWS Managed AD (~18 $/Woche), nur eine
> zusätzliche EC2-Instanz. Und Sie erleben den Kontrast zwischen **klassischem AD-Trust** und
> **moderner Föderation** direkt an Ihrer eigenen Umgebung.
>
> **Kompetenzfelder:** B (Einsatz Directory Service), C (LDAP als Protokoll), G (Datenaustausch).

## Ressourcen

- [Bewertungskriterien](../../08-kompetenznachweise/lb2/kompetenzmatrix-lb2.md)
- [KI-Nutzung im Modul](../../ki-nutzung.md)
- [Planung – AD & Cloud Setup Sheet](../01-planung/resources/01-a-planung-ad-cloud-setup-sheet.md)
- LDAP-Theorie im Modul: [ldap](../../02-unterrichtsressourcen/03-fachliteratur-tutorials/ldap)
- Authentik-Dokumentation: `https://docs.goauthentik.io` (Installation → Docker Compose; Sources → LDAP)

> [!NOTE]
>
> Diese Variante benötigt eine zusätzliche **Linux-EC2-Instanz**. Authentik braucht ab ca. 2 GB
> RAM; prüfen Sie Ihr AWS-Guthaben und stimmen Sie die Instanzgrösse mit der Lehrperson ab.

---

## 1. Szenario

Ihr Active Directory läuft auf Ihren EC2-Domänencontrollern und verwaltet Benutzer und Gruppen.
Nun soll eine moderne Web-Anwendung ein **Single Sign-On** erhalten — ohne dass sie selbst
Benutzer verwaltet. Sie stellen deshalb einen Identity Provider (Authentik) vor Ihr AD:

> «Unsere neue Web-App soll dieselben Logins nutzen wie das AD — aber sie spricht kein Kerberos,
> nur OIDC.»

Das AD bleibt die **führende Quelle**; Authentik übernimmt Login und Föderation.

---

## 2. Lernziele

- Sie können einen Identity Provider self-hosted auf einer eigenen Instanz betreiben.
- Sie können erklären, wie sich ein IdP per LDAP an ein AD anbindet und Benutzer/Gruppen synchronisiert.
- Sie können den Unterschied zwischen unverschlüsseltem LDAP und LDAPS und die Rolle des Zertifikats benennen.
- Sie können begründen, warum das **kein AD-Trust** ist, sondern eine Föderation.
- Sie können Authentifizierung von Autorisierung unterscheiden (Login ≠ App-Zugriff).

---

## Teil A – Authentik bereitstellen (Stufe 1)

1. Stellen Sie eine **Linux-EC2-Instanz** (z. B. Ubuntu Server) in **derselben VPC** wie Ihre DCs
   bereit und tragen Sie sie in Ihre Planung ein (Hostname, IP). Die Security Group muss den DC
   über LDAP/LDAPS erreichen können.
2. Installieren Sie **Docker** und **Docker Compose**.
3. Starten Sie Authentik mit dem offiziellen Docker-Compose gemäss Authentik-Doku
   (Compose-Datei und `.env` herunterladen, `docker compose up -d`). Rufen Sie anschliessend den
   Ersteinrichtungs-Flow (`/if/flow/initial-setup/`) auf und vergeben Sie das Admin-Passwort.

Dokumentieren Sie, **warum** die Authentik-Instanz in dieselbe VPC gehört und welche Ports sie
zum DC benötigt.

---

## Teil B – LDAP Source ans AD anbinden (Stufe 1)

1. Legen Sie **im AD ein dediziertes Bind-/Service-Konto** an (nur Leserechte, **kein**
   Domänenadmin). Begründen Sie, warum least privilege sinnvoll ist.
2. Konfigurieren Sie in Authentik eine **LDAP Source**: Server-URI, Bind-DN und -Passwort,
   **Base DN** (ab welcher OU synchronisiert wird) sowie die User- und Group-Property-Mappings.
3. Lösen Sie die Synchronisation aus und weisen Sie nach, dass Ihre AD-Benutzer und -Gruppen in
   Authentik erscheinen.
4. **Login-Test:** Melden Sie sich in Authentik mit einem **AD-Konto** an. Die Passwortprüfung
   läuft gegen den DC. Belegen Sie den erfolgreichen Login.

> [!TIP]
>
> Prüfen Sie zuerst grob die Erreichbarkeit vom Authentik-Host zum DC (Port 389/636 offen?),
> bevor Sie den Fehler in Authentik suchen.

---

## Teil C – Auf LDAPS härten (Stufe 2)

Einfaches LDAP überträgt den Bind — inklusive Passwort — im Klartext. Stellen Sie die Anbindung
auf **LDAPS (Port 636)** um:

1. Sorgen Sie dafür, dass Ihr DC ein **Zertifikat** für LDAPS besitzt, und binden Sie Authentik
   über `ldaps://…:636` an.
2. Dokumentieren Sie, **warum** LDAPS nötig ist — und beachten Sie: **Ab Windows Server 2025 ist
   LDAP Signing standardmässig erzwungen.** Halten Sie fest, was das für Ihre Anbindung bedeutet.

> [!WARNING]
>
> Für ein Passwort-Rückschreiben von Authentik ins AD ist LDAPS **zwingend**. Über
> unverschlüsseltes LDAP lehnt der DC Passwortänderungen ab.

---

## Teil D – Eine Anwendung anbinden (Stufe 2)

Ein IdP zeigt seinen Wert erst mit einer angebundenen App.

1. Binden Sie **genau eine** Web-Anwendung an Authentik an — per **OIDC oder SAML** (integrierte
   App) oder über den **Application-Proxy** (für eine App ohne eigenes Login).
2. Weisen Sie ein echtes **SSO-Login** nach: Nach der Anmeldung an Authentik gelangen Sie ohne
   zweite Anmeldung in die App.
3. Steuern Sie den Zugriff über eine **AD-Gruppe** (Authentik-Policy auf Gruppenmitgliedschaft).

> [!TIP]
>
> **Optionale Vertiefung:** Zeigen Sie zusätzlich, dass ein Benutzer **ohne** die passende Gruppe
> keinen Zugriff bekommt. Das trennt Authentifizierung (wer bin ich) sauber von Autorisierung
> (was darf ich) — ist für Stufe 2 aber nicht zwingend.

---

## KI-Einsatz in diesem Auftrag

LDAP-Bindungsfehler sind ein gutes Feld für die KI-gestützte Fehlersuche: Die Meldungen sind
kryptisch, aber ihr Wahrheitsgehalt lässt sich direkt am System prüfen.

```text
Meine Authentik-LDAP-Source verbindet sich nicht mit dem DC.
Umgebung: Authentik in Docker auf Ubuntu, DC = Windows Server [Version],
Anbindung über [ldap/ldaps]. Fehlermeldung: [exakte Meldung].
Bereits geprüft: [Port, Bind-DN, Base-DN, ...].
Nenne mir die 5 wahrscheinlichsten Ursachen mit je einem Prüfbefehl. Noch keine Lösung.
```

Halten Sie Ihren KI-Einsatz gemäss [ki-nutzung.md](../../ki-nutzung.md) in `ki-log.md` fest.

> [!IMPORTANT]
>
> Die KI **direkt** an Ihre Umgebung anzubinden (z. B. per MCP an Browser, RDP oder SSH), damit
> sie die Einrichtung selbst ausführt, ist nicht erlaubt — siehe [ki-nutzung.md](../../ki-nutzung.md).

---

## Abgrenzung: Das ist **kein** AD-Trust

Auch wenn beides „Vertrauen" schafft, sind es zwei verschiedene Dinge:

| | AD-Forest-Trust (Variante A) | Authentik-Föderation (Variante B) |
| --- | --- | --- |
| Zwischen | zwei echten Active Directories | AD (Quelle) und einem Web-IdP |
| Protokoll | Kerberos / NTLM | LDAP (Sync) + OIDC/SAML (App) |
| Richtung | gegenseitig möglich (two-way) | einseitig: Authentik liest aus dem AD |
| Wer vertraut wem | Domäne ↔ Domäne | App vertraut dem IdP |

Authentik ist **kein** AD, hat keinen Kerberos-KDC und kann kein Trust-Partner in einer
AD-Vertrauensstellung sein. Es bindet sich per LDAP an und föderiert Anwendungen per Token.

---

## Abgabe-Kriterien

Zur Einordnung in die vier Stufen (Details:
[Kompetenzmatrix](../../08-kompetenznachweise/lb2/kompetenzmatrix-lb2.md)):

- **Stufe 1:** Teil A + B — Authentik läuft, die LDAP Source synchronisiert AD-Benutzer/-Gruppen, Login mit einem AD-Konto ist nachgewiesen.
- **Stufe 2:** Teil C + D — Anbindung über LDAPS mit Zertifikat (Notwendigkeit dokumentiert), eine App per OIDC/SAML/Proxy mit funktionierendem SSO und gruppenbasiertem Zugriff, least-privilege Bind-Konto begründet.
- **Stufe 3/4:** mündlicher Nachweis über den Fragenkatalog unten.
- **`ki-log.md`** mit Reflexion des KI-Einsatzes.

---

## Fragenkatalog (mündlicher Nachweis, Stufen 3/4)

Der Katalog ist offen einsehbar. Arbeiten Sie die Antworten vor der Abgabe durch; im Gespräch
antworten Sie frei und in eigenen Worten. Die Lehrperson zieht eine Frage zufällig.

### 1

**Frage:** Warum bleibt das AD die führende Quelle, obwohl sich alle bei Authentik anmelden?

**Erwartungshorizont:** Authentik synchronisiert **aus** dem AD und prüft Passwörter gegen den
DC; Benutzer/Gruppen werden im AD gepflegt, nicht in Authentik. Die Anbindung ist einseitig.

**Hinweis:** In welche Richtung läuft die Synchronisation, und wo legen Sie einen neuen
Benutzer an?

### 2

**Frage:** Was passiert technisch, wenn sich ein Benutzer mit seinem AD-Konto bei Authentik
anmeldet?

**Erwartungshorizont:** Authentik führt gegen den DC einen LDAP-Bind mit den eingegebenen
Zugangsdaten durch (bzw. prüft das Passwort gegen das AD); erst bei Erfolg ist der Login gültig.

**Hinweis:** Authentik speichert das AD-Passwort nicht selbst. Wen fragt es dann?

### 3

**Frage:** Was ist der Unterschied zwischen LDAP und LDAPS, und warum brauchen Sie für Ihre
Anbindung LDAPS?

**Erwartungshorizont:** LDAP überträgt den Bind im Klartext, LDAPS über TLS (Port 636) mit
Zertifikat; für Passwortübertragung/-rückschreiben und generell aus Sicherheitsgründen ist
Verschlüsselung nötig.

**Hinweis:** Was steht beim Bind mit auf der Leitung, und wer könnte mitlesen?

### 4

**Frage:** Warum ist diese Anbindung **kein** AD-Trust wie zwischen AWS Managed AD und Ihrem AD?

**Erwartungshorizont:** Ein AD-Trust besteht zwischen zwei echten ADs über Kerberos, gegenseitig;
Authentik ist kein AD, bindet sich einseitig per LDAP an und föderiert Apps per OIDC/SAML.

**Hinweis:** Welche Voraussetzung müsste die Gegenseite erfüllen, um Trust-Partner zu sein?

### 5

**Frage:** Was ist in Ihrem Aufbau der Unterschied zwischen Authentifizierung und Autorisierung?

**Erwartungshorizont:** Authentifizierung = Login (wer bin ich, geprüft gegen das AD);
Autorisierung = ob dieses Konto die App sehen darf (über die AD-Gruppe / Authentik-Policy).

**Hinweis:** Ein gültiger Login allein — reicht der schon für den App-Zugriff?

### 6

**Frage:** Warum verwenden Sie ein dediziertes Bind-Konto mit minimalen Rechten statt eines
Admin-Kontos?

**Erwartungshorizont:** Least privilege; das Konto liegt im Klartext/als Secret in Authentik,
bei Kompromittierung wäre der Schaden mit Adminrechten weit grösser; es braucht nur Leserechte.

**Hinweis:** Wo ist dieses Passwort hinterlegt, und was könnte ein Angreifer damit tun?

### 7

**Frage:** Was bewirkt die Base DN Ihrer LDAP Source, und was passiert, wenn Sie sie zu hoch oder
zu tief ansetzen?

**Erwartungshorizont:** Die Base DN bestimmt den Startpunkt der Synchronisation; zu hoch → zu
viele/ungewollte Objekte, zu tief → benötigte Benutzer/Gruppen fehlen.

**Hinweis:** Denken Sie an den Ast im Verzeichnisbaum, ab dem gesucht wird.

### 8

**Frage:** Ihre App spricht OIDC. Was tauscht sie mit Authentik aus, damit ein Login zustande
kommt?

**Erwartungshorizont:** Weiterleitung zum IdP, Anmeldung dort, Rückgabe eines Tokens an die App;
die App vertraut dem IdP (Federation Trust) und wertet das Token aus, statt selbst Passwörter zu
prüfen.

**Hinweis:** Die App sieht das Passwort nie. Was bekommt sie stattdessen von Authentik?

### 9

**Frage:** Ab Windows Server 2025 ist LDAP Signing standardmässig erzwungen. Was bedeutet das für
Ihre Anbindung, und wie sind Sie damit umgegangen?

**Erwartungshorizont:** Unsignierte/unverschlüsselte Binds werden abgelehnt; nötig ist LDAPS bzw.
Signing; eigene Massnahme (Zertifikat, `ldaps://`) benannt.

**Hinweis:** Was hat sich gegenüber älteren Server-Versionen an der Standardeinstellung geändert?

### 10

**Frage:** In welcher realen Situation stellt eine Firma einen IdP wie Authentik vor ihr AD,
statt Anwendungen direkt an AD zu binden?

**Erwartungshorizont:** Nachvollziehbares Beispiel: moderne Web-/Cloud-Apps sprechen OIDC/SAML,
nicht Kerberos/LDAP; ein IdP liefert zentrales SSO, MFA und einheitliche Zugriffssteuerung über
viele Anwendungen.

**Hinweis:** Welche „Sprache" sprechen heutige SaaS- und Web-Anwendungen beim Login?
