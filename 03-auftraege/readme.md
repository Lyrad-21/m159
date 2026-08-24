# AD-Aufträge (LB2)

Die Aufträge sind in zwei Blöcke gegliedert: Die Aufträge 01–09 bauen die lokale
Active-Directory-Umgebung auf und sind von Cloud-Diensten unabhängig. Die Aufträge 10–13
integrieren diese Umgebung in die Cloud.

Bewertet wird nach der [Kompetenzmatrix LB2](../08-kompetenznachweise/lb2/kompetenzmatrix-lb2.md).

> [!NOTE]
>
> Die Aufträge werden der Reihe nach umgesetzt, beginnend mit Nr. 01. Ausgenommen sind die
> Aufträge 05 und 06, die gegebenenfalls übersprungen werden können.

<hr>

## Block 1 – Lokale Umgebung

| # | Auftrag | Beschreibung |
| --- | --- | --- |
| 01 | [Planung](01-planung) | Erstellen einer detaillierten Projektplanung inklusive Definition aller relevanten Parameter und Nachweis der Cloud-Bereitschaft. |
| 02 | [Initial Setup](02-initial-setup) | Grundinstallation und Konfiguration der AWS-Umgebung gemäss Planung, inklusive IP-Adressen, Hostnames, Ports und Standardeinstellungen. |
| 03 | [Gesamtstruktur (erster DC) & Client](03-neue-gesamtstruktur-und-client) | Einrichtung des ersten Domain Controllers, Join des Clients zur Domäne und Umsetzung aller definierten Zusatzanforderungen. |
| 04 | [Freigaben Laufwerke Berechtigungen](04-freigaben-laufwerke-berechtigungen) | Anlegen der benötigten Gruppen und Benutzer, Zuweisung und Test der NTFS- und Freigabeberechtigungen sowie Umsetzung von ABE und Group-Nesting-Konzept. |
| 05 | [AWS Managed Microsoft AD](05-aws-managed-microsoft-ad) | Einrichtung von AWS Managed Microsoft AD, Konfiguration der Ports und Aufbau eines funktionierenden Trusts mit Sicherheitsdokumentation. **Wählbare Alternative:** [Variante B – Moderner IdP mit Authentik](05-aws-managed-microsoft-ad/variante-b-authentik-idp.md) (LDAP-Anbindung ans AD, ohne kostenpflichtiges Managed AD). |
| 06 | [RSAT & Admin Center V2](06-rsat-admin-center-v2) | Installation der RSAT-Tools, Einrichtung des Windows Admin Centers für interne und externe Administration unter Berücksichtigung von Sicherheitsmassnahmen. |
| 07 | [DIT & GPOs](07-dit-gpos) | Erstellung einer korrekten Domänenstruktur (DIT) und Umsetzung der definierten GPO-Aufgaben gemäss Anforderungen. |
| 08 | [Suche im Directory](08-suche-im-directory) | LDAP-Bind und LDAP-Suche verstehen, verschachtelte Suchfilter aufbauen und in einer Anwendung einpflegen. Entscheid über das Dienstkonto einer Applikationsanbindung. |
| 09 | [Identity Management & PowerShell Debugging](09-automation-und-debugging) | Ein fehlerhaftes Skript für den automatisierten Benutzerimport analysieren, reparieren und um eine Sicherheitsprüfung erweitern. |

## Block 2 – Cloud-Integration

| # | Auftrag | Beschreibung | Variante B |
| --- | --- | --- | --- |
| 10 | [MS Entra ID & MS Entra Connect](10-ms-entra-id-ms-entra-connect) | Active-Directory-Umgebung mit Entra Connect verbinden, Objekte synchronisieren und den Hybrid Join durchführen. | [Zweiter DC & Replikation](10-ms-entra-id-ms-entra-connect/variante-b-zweiter-dc-replikation.md) |
| 11 | [Servergespeicherte Benutzerprofile](11-servergespeicherte-benutzerprofile) | Einrichtung von Roaming Profiles, Folder Redirection und FS-Logix. | nicht nötig – cloud-unabhängig |
| 12 | [Netzlaufwerk to Azure Migration](12-netzlaufwerk-to-azure-migration) | Einrichtung eines Azure Storage Accounts mit File Share und Anbindung über Key oder Entra ID/AD-Integration ohne zusätzliche Authentifizierung. | [AWS S3 Backup](12-netzlaufwerk-to-azure-migration/variante-b-aws-s3.md) |
| 13 | [SSO Python App](13-sso-python-app) | Einrichtung und Test einer Python-Webanwendung mit Single Sign-On über Entra ID und verschiedenen Authentifizierungsverfahren. | [IIS & Kerberos](13-sso-python-app/variante-b-iis-kerberos.md) |

<hr>

## Varianten B – Absicherung gegen Cloud-Ausfälle

Die Aufträge in Block 2 hängen an Microsoft-Cloud-Diensten. Erfahrungsgemäss scheitert die
Aktivierung von Azure for Students oder Entra ID bei einzelnen Lernenden aus Gründen, die
ausserhalb ihres Einflusses liegen.

Für diesen Fall gibt es **Varianten B**: cloud-unabhängige Ausweichaufträge, die nach denselben
vier Stufen bewertet werden. Sie sind kein Ersatz zweiter Klasse, sondern ein gleichwertiger
Weg zum Kompetenznachweis.

**Voraussetzung für den Wechsel:**

1. Der Fehlschlag ist mit einem Screenshot belegt (Fehlermeldung oder Ablehnung bei der
   Aktivierung).
2. Die Lehrperson gibt den Wechsel frei.

Der dokumentierte Fehlschlag gehört zur Abgabe — die Analyse eines Fehlers ist selbst eine
Leistung und zählt auf das Kompetenzfeld H (Testen) ein.

> [!IMPORTANT]
>
> Prüfen Sie Ihren Cloud-Zugang bereits in [Auftrag 01](01-planung). Wer erst an Tag 7
> feststellt, dass sein Tenant nicht funktioniert, verliert Zeit, die sich nicht mehr aufholen
> lässt.

## Eigene Ideen

Vorschläge für neue Aufträge sind willkommen:
[99-idee-fuer-eigene-aufgaben.md](99-idee-fuer-eigene-aufgaben.md)
