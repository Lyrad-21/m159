# Auftrag 13 – Variante B: Single Sign-On mit IIS & Kerberos

> [!IMPORTANT]
>
> Dies ist die **Ausweichvariante** zu [Auftrag 13](readme.md). Sie bearbeiten diese Variante
> nur dann, wenn Ihr Entra-ID-Tenant nachweislich nicht zur Verfügung steht.
>
> **Voraussetzungen für den Wechsel:**
>
> 1. Sie belegen den Fehlschlag mit einem Screenshot (Fehlermeldung oder Ablehnung bei der
>    Aktivierung von Azure for Students bzw. Entra ID).
> 2. Die Lehrperson gibt den Wechsel frei.
>
> Der dokumentierte Fehlschlag ist Teil Ihrer Abgabe. Variante B wird nach denselben vier
> Stufen bewertet wie Variante A.
>
> **Kompetenzfelder:** identisch mit Variante A (B und C). Für das Feld C (LDAP als Protokoll)
> ist diese Variante sogar die stärkere, weil Kerberos näher am Protokoll liegt als der
> OAuth-Flow der Python-App.

## 1. Einleitung & Szenario
Single Sign-On (SSO) ist der Kern moderner Benutzerfreundlichkeit. Ein Benutzer meldet sich einmal an seinem PC an und hat danach Zugriff auf alle Webdienste, ohne erneut ein Passwort eingeben zu müssen. Da die Azure-Integration entfällt, implementieren Sie die klassische Methode: **Integrated Windows Authentication (IWA)** via Kerberos.

**Szenario:**
Die Geschäftsleitung wünscht ein internes Web-Portal (Intranet). Dieses Portal soll nur für Domänen-Benutzer zugänglich sein und diese automatisch erkennen, ohne dass ein Login-Fenster erscheint.

## 2. Lernziele
* Installation und Absicherung des Internet Information Servers (IIS).
* Verständnis von Authentifizierungs-Methoden (Anonymous vs. Windows Auth).
* Konfiguration von Browser-Sicherheitszonen für SSO.
* Berechtigungssteuerung auf Web-Ebene via AD-Gruppen.

---

## 3. Vorbereitung der Umgebung
1. **Server-Rolle:** Installieren Sie auf Ihrem DC (oder einem Member-Server) die Rolle **Web Server (IIS)**.
2. **Features:** Stellen Sie sicher, dass unter `Web Server > Security` das Feature **Windows Authentication** mit installiert wird.
3. **Content:** Erstellen Sie unter `C:\inetpub\wwwroot\` eine einfache `index.html` mit dem Inhalt: "Willkommen im geschützten Intranet der [Ihre Firma]!".

---

## 4. Konfiguration (Der "SSO-Weg")
In dieser Aufgabe gibt es kein fertiges Skript. Sie müssen die Konfiguration direkt im **IIS Manager (`inetmgr`)** vornehmen.

**Vorgehensweise:**
* Navigieren Sie zur "Default Web Site".
* Öffnen Sie den Bereich **Authentication**.
* Deaktivieren Sie "Anonymous Authentication".
* Aktivieren Sie "Windows Authentication".

---

## 5. Arbeitsauftrag

### Teil A: Absicherung & Test
1. **Initialer Test:** Versuchen Sie von Ihrem **Windows 10 Client** die Adresse `http://[Name-Ihres-DC]` aufzurufen.
2. **Die Hürde:** Wahrscheinlich erscheint ein Login-Fenster oder ein Fehler. Analysieren Sie, warum der Browser die Identität noch nicht automatisch sendet.
3. **SSO-Aktivierung:** Konfigurieren Sie die Internetoptionen auf dem Client (oder via GPO), damit Ihr Server zur Zone **Lokales Intranet** gehört. Testen Sie erneut. Erscheint die Seite nun ohne Passwortabfrage?

### Teil B: Autorisierung (Security)
Das Portal soll nur für eine bestimmte Gruppe zugänglich sein.
* Erstellen Sie im AD eine Sicherheitsgruppe `G_Intranet_Users`.
* Fügen Sie Ihren Test-User hinzu.
* Konfigurieren Sie im IIS die **Authorization Rules** (oder NTFS-Berechtigungen auf die HTML-Datei) so, dass nur Mitglieder dieser Gruppe die Seite sehen dürfen. Testen Sie dies mit einem User, der nicht in der Gruppe ist.

---

## 6. Abgabe-Kriterien
1. **Funktions-Nachweis:** Ein Screenshot vom Browser des Windows 10 Clients, der die Webseite zeigt, ohne dass ein Anmeldefenster erscheint.
2. **Konfigurations-Nachweis:** Ein Screenshot der IIS-Authentifizierungs-Einstellungen.
3. **Sicherheits-Nachweis:** Ein Screenshot der Fehlermeldung (401 Unauthorized), wenn ein nicht berechtigter User versucht, die Seite aufzurufen.