# Auftrag 08: Suche im Directory

## Ressourcen

- [Bewertungskriterien](../../08-kompetenznachweise/lb2/kompetenzmatrix-lb2.md)
- [Fragenkatalog für den mündlichen Nachweis](fragen.md)
- [KI-Nutzung im Modul](../../ki-nutzung.md)
- Werkzeuge auf dem DC: `ldp.exe`, `dsa.msc`, PowerShell (`Get-ADUser`, `Get-ADObject`), `ldifde`
- [Theorie LDAP](../../02-unterrichtsressourcen/03-fachliteratur-tutorials/ldap)

---

## 1. Szenario

Ihre Firma beschafft eine neue Firewall. Der Hersteller-Support meldet sich mit einer knappen
Anforderung:

> «Damit sich Ihre Mitarbeitenden am VPN anmelden können, brauchen wir von Ihnen einen
> Bind-DN mit Passwort, den Base-DN Ihres Verzeichnisses und einen Suchfilter, der genau die
> Benutzer zurückgibt, die VPN benutzen dürfen. Aktive Konten, keine gesperrten.»

Damit stehen Sie vor der Aufgabe, die jede Applikationsanbindung an ein Active Directory
verlangt: Sie müssen wissen, **wie ein Verzeichnis abgefragt wird**, nicht nur, wie man Objekte
im grafischen Werkzeug anklickt.

---

## 2. Lernziele

- Sie können erklären, was bei einem LDAP-Bind und einer LDAP-Suche passiert.
- Sie können den Base-DN und den DN einzelner Objekte aus Ihrer Struktur herleiten.
- Sie können einzelne Objekte über einen LDAP-Suchfilter gezielt finden.
- Sie können verschachtelte Suchfilter mit UND, ODER und NICHT aufbauen.
- Sie können einen Suchfilter in einer Anwendung einpflegen, sodass er dort wirksam wird.
- Sie können begründen, mit welchen Rechten ein Dienstkonto für die Anbindung ausgestattet wird.

---

## 3. Voraussetzungen

Sie haben die Aufträge 03, 04 und 07 abgeschlossen. In Ihrem AD existieren also eine
OU-Struktur, Benutzer und Gruppen. Die Suchen dieses Auftrags beziehen sich auf **Ihre eigene
Struktur** — nicht auf ein Beispiel aus der Anleitung.

---

## Teil A – Verstehen, was ein Bind ist

Öffnen Sie auf dem DC `ldp.exe`.

1. Verbinden Sie sich über **Connection → Connect** mit Ihrem DC auf Port `389`.
2. Führen Sie **Connection → Bind** aus, zuerst mit der Option «Bind as currently logged on user».
3. Öffnen Sie **View → Tree** und bestätigen Sie den vorgeschlagenen Base-DN.

Notieren Sie in Ihrer Dokumentation:

- Welchen Base-DN schlägt `ldp.exe` vor, und wie leitet er sich aus Ihrem Domainnamen ab?
- Was hat der Bind gemacht — und was wäre passiert, wenn Sie ihn übersprungen hätten?
- Wählen Sie einen Ihrer Benutzer und schreiben Sie dessen vollständigen DN auf.

> [!NOTE]
>
> `ldp.exe` ist kein Werkzeug für den Alltag, sondern zum Verstehen. Sie sehen darin die
> Roh-Antwort des Verzeichnisses, ohne dass eine Oberfläche sie für Sie aufbereitet.

---

## Teil B – Einzelne Objekte finden

Lösen Sie die folgenden Suchen. Die Filter sind **nicht** vorgegeben — das ist die Aufgabe.

| # | Gesucht |
| --- | --- |
| B1 | Ein bestimmter Benutzer, gesucht über seinen Anmeldenamen |
| B2 | Alle Benutzer einer einzelnen Abteilungs-OU |
| B3 | Alle Gruppen Ihrer Domain |
| B4 | Alle Computerkonten Ihrer Domain |

Führen Sie jede Suche **auf zwei Wegen** aus und halten Sie beide Ergebnisse fest:

1. in `ldp.exe` über **Browse → Search** (Base-DN, Scope, Filter)
2. in der PowerShell mit `Get-ADUser -LDAPFilter` bzw. `Get-ADObject -LDAPFilter`

> [!TIP]
>
> Der Scope entscheidet mit über das Ergebnis. Probieren Sie bei B2 bewusst `One Level` und
> `Subtree` aus und erklären Sie den Unterschied an Ihrem eigenen Resultat.

---

## Teil C – Verschachtelte Suchfilter

Jetzt kombinieren Sie Bedingungen. Alle Filter beziehen sich auf Ihre Umgebung.

| # | Gesucht |
| --- | --- |
| C1 | Alle Benutzer der Abteilung Buchhaltung, die Mitglied einer bestimmten Gruppe sind |
| C2 | Alle Gruppen, deren Name mit einem bestimmten Präfix beginnt |
| C3 | Alle Benutzer, bei denen ein bestimmtes Attribut **nicht** gesetzt ist |
| C4 | Alle **deaktivierten** Benutzerkonten |
| C5 | Alle aktiven Benutzer **ausserhalb** einer bestimmten OU |

Zu C4: Der Status eines Kontos steckt als einzelnes Bit im Attribut `userAccountControl`. Ein
normaler Vergleich genügt hier nicht — recherchieren Sie, wie LDAP eine Bit-Abfrage formuliert.

Dokumentieren Sie pro Suche: den Filter, die Anzahl Treffer und einen Screenshot des Resultats
aus Ihrer Umgebung.

> [!IMPORTANT]
>
> Ein Filter, der zufällig das erwartete Resultat liefert, ist noch nicht richtig. Prüfen Sie
> gegen: Legen Sie ein Testobjekt an, das **knapp nicht** passen darf, und weisen Sie nach, dass
> Ihr Filter es korrekt ausschliesst.

---

## Teil D – Den Filter in einer Anwendung einpflegen

Ein Filter ist erst dann etwas wert, wenn eine Anwendung ihn benutzt. Setzen Sie ihn an zwei
Stellen produktiv ein:

**D1 – Gespeicherte Abfrage**
Legen Sie in `dsa.msc` unter **Saved Queries** eine Abfrage an, die Ihren Filter aus C4
verwendet. Ergebnis: Die Lehrperson kann jederzeit mit einem Klick alle deaktivierten Konten
sehen.

**D2 – Bedingte Zuweisung per GPO**
Erweitern Sie eine Ihrer GPOs aus Auftrag 07 um eine **Zielgruppenadressierung
(Item-Level-Targeting)** vom Typ **LDAP Query**, sodass eine Einstellung nur bei Benutzern
greift, die Ihrem Filter entsprechen. Weisen Sie nach, dass sie bei einem passenden Benutzer
ankommt und bei einem nicht passenden ausbleibt.

---

## Teil E – Der Entscheid: Dienstkonto für die Firewall

Die Firewall braucht ein Konto, mit dem sie sich am Verzeichnis anmeldet. Treffen Sie diesen
Entscheid und **begründen Sie ihn schriftlich**:

1. **Welches Konto?** Ein bestehender Administrator, ein eigenes Dienstkonto oder ein
   anonymer Zugriff? Was spricht jeweils dagegen?
2. **Welche Rechte** braucht dieses Konto tatsächlich, um Ihren Filter auszuführen — und
   welche ausdrücklich nicht?
3. **Port 389 oder 636?** Was genau ginge bei einem einfachen Bind über Port 389 durch das
   Netz, und was ändert LDAPS daran?

Es gibt hier nicht die eine richtige Antwort. Bewertet wird, ob Ihre Begründung trägt.

> [!TIP]
>
> Im Ereignisprotokoll Ihres DC unter **Directory Service** finden Sie Hinweise auf ungesicherte
> Bind-Vorgänge. Ein Blick dorthin schärft Ihre Argumentation.

---

## KI-Einsatz in diesem Auftrag

Die LDAP-Filtersyntax ist ein Paradebeispiel für sinnvollen KI-Einsatz: Die Regeln sind
kompakt, aber unintuitiv, und Ihr Verzeichnis sagt Ihnen sofort, ob Sie richtig liegen.

Empfohlenes Vorgehen: Filter selbst entwerfen, ausführen, und erst bei Abweichung die KI zur
Erklärung heranziehen — nicht umgekehrt.

```text
Ich habe folgenden LDAP-Suchfilter geschrieben: [Ihr Filter].
Ziel: [was er finden soll].
Erkläre mir Schritt für Schritt, welche Objekte dieser Filter zurückgibt.
Sage mir nicht, ob er richtig ist — ich will es selbst beurteilen.
```

```text
Erkläre mir, wie LDAP eine Bit-Abfrage auf ein Attribut formuliert.
Nenne mir die Regel, nicht den fertigen Filter für meinen Fall.
```

Halten Sie Ihren KI-Einsatz gemäss [ki-nutzung.md](../../ki-nutzung.md) in `ki-log.md` fest.
Die Spalte «Wie verifiziert» füllt sich hier von selbst: Der Filter liefert die erwarteten
Objekte oder eben nicht.

---

## Abgabe-Kriterien

1. **Teil A**: Base-DN mit Herleitung, DN eines eigenen Benutzers, Erklärung des Bind-Vorgangs
2. **Teil B**: 4 Suchen, je über beide Wege, mit Resultat aus Ihrer Umgebung
3. **Teil C**: 5 Filter mit Trefferzahl und Screenshot, dazu der Gegentest aus dem Hinweis
4. **Teil D**: Screenshot der gespeicherten Abfrage und Nachweis, dass die GPO-Zuweisung bei
   einem passenden Benutzer greift und bei einem nicht passenden ausbleibt
5. **Teil E**: schriftliche Begründung zu Konto, Rechten und Port
6. **`ki-log.md`** mit Reflexion
