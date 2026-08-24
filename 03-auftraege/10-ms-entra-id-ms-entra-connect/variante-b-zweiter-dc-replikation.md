# Auftrag 10 – Variante B: Zweiter Domain Controller & Replikation

> [!IMPORTANT]
>
> Dies ist die **Ausweichvariante** zu [Auftrag 10](readme.md). Sie bearbeiten diese Variante
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
> **Kompetenzfelder:** identisch mit Variante A (G und B). Der Datenaustausch findet hier
> zwischen zwei Instanzen desselben Verzeichnisses statt statt zwischen AD und Entra ID.

## Ressourcen

- [Bewertungskriterien](../../08-kompetenznachweise/lb2/kompetenzmatrix-lb2.md)
- [KI-Nutzung im Modul](../../ki-nutzung.md)
- [RepAdmin-Unterlagen](../../02-unterrichtsressourcen/03-fachliteratur-tutorials/analyse)
- [Standorte](../../02-unterrichtsressourcen/03-fachliteratur-tutorials/basics/4-standorte.pdf)
- Befehle: `repadmin /replsummary`, `repadmin /showrepl`, `repadmin /syncall /AdeP`, `netdom query fsmo`

> [!NOTE]
>
> Diese Variante benötigt eine zusätzliche EC2-Instanz. Prüfen Sie vorher Ihr verbleibendes
> AWS-Guthaben und stimmen Sie die Instanzgrösse mit der Lehrperson ab.

---

## 1. Szenario

Ihre Domäne läuft auf einem einzigen Domain Controller. Die Geschäftsleitung stellt die
naheliegende Frage:

> «Was passiert eigentlich, wenn dieser eine Server ausfällt?»

Die Antwort ist unangenehm: Niemand meldet sich mehr an. Sie bauen deshalb einen zweiten
Domain Controller auf und weisen nach, dass die Verzeichnisdaten zwischen beiden zuverlässig
abgeglichen werden — und dass die Anmeldung den Ausfall eines DC übersteht.

---

## 2. Lernziele

- Sie können erklären, wie Verzeichnisdaten zwischen zwei Directory-Service-Instanzen
  abgeglichen werden.
- Sie können den Zustand der Replikation prüfen und eine Replikation gezielt auslösen.
- Sie können nachweisen, dass eine Änderung tatsächlich übertragen wurde.
- Sie können begründen, wie FSMO-Rollen, Global Catalog und DNS auf zwei DCs verteilt werden.

---

## Teil A – Zweiten Domain Controller aufbauen

1. Stellen Sie eine zweite Windows-Server-Instanz bereit und tragen Sie sie in Ihre Planung ein
   (Hostname, IP, DNS-Einstellungen).
2. Fügen Sie den Server **Ihrer bestehenden Domäne** als zusätzlichen Domain Controller hinzu.
   Achtung: Es entsteht **keine** neue Gesamtstruktur.
3. Prüfen Sie in `dsa.msc` und in der DNS-Konsole, dass der neue DC sichtbar ist.

Dokumentieren Sie, welche DNS-Einstellung der zweite DC bekommt und warum sie sich von der des
ersten unterscheidet.

---

## Teil B – Replikation prüfen

Führen Sie auf beiden DCs aus:

| Befehl | Was Sie damit beantworten |
| --- | --- |
| `repadmin /replsummary` | Gibt es Fehler, und wie alt ist die letzte erfolgreiche Replikation? |
| `repadmin /showrepl` | Mit welchem Partner repliziert dieser DC, und über welche Namenskontexte? |
| `netdom query fsmo` | Welcher DC hält welche Betriebsmasterrolle? |

Halten Sie die Ausgaben fest und erklären Sie in eigenen Worten, was ein **Namenskontext**
(Naming Context) ist und warum es mehrere davon gibt.

---

## Teil C – Den Beweis antreten

Eine fehlerfreie Statusmeldung ist noch kein Nachweis, dass Daten ankommen.

1. Legen Sie auf **DC1** einen Benutzer an, dessen Name eindeutig Ihnen zuzuordnen ist.
2. Prüfen Sie auf **DC2**, ob der Benutzer bereits da ist. Notieren Sie, wie lange es gedauert
   hat.
3. Ändern Sie auf **DC2** ein Attribut dieses Benutzers und erzwingen Sie die Replikation
   zurück auf DC1 mit `repadmin /syncall /AdeP`.
4. Weisen Sie nach, dass die Änderung auf DC1 angekommen ist.

> [!TIP]
>
> Replikation innerhalb eines Standorts passiert nicht sofort, aber auch nicht erst nach
> Stunden. Wenn Sie ungeduldig werden, ist das ein guter Moment, um nachzulesen, wie die
> Änderungsbenachrichtigung zwischen DCs funktioniert.

---

## Teil D – Der Ausfalltest

Jetzt beantworten Sie die Frage aus dem Szenario.

1. Fahren Sie **DC1** kontrolliert herunter.
2. Melden Sie sich am Client mit einem Domänenbenutzer an. Funktioniert es?
3. Prüfen Sie mit `nltest /dsgetdc:<ihre-domain>` oder `echo %LOGONSERVER%`, welcher DC die
   Anmeldung übernommen hat.
4. Starten Sie DC1 wieder und prüfen Sie erneut die Replikation.

Falls die Anmeldung **nicht** funktioniert hat: Das ist kein Misserfolg, sondern der
eigentliche Erkenntnisgewinn. Analysieren Sie die Ursache und dokumentieren Sie sie.

---

## Teil E – Der Entscheid: Verteilung auf zwei DCs

Treffen Sie folgende Entscheide und **begründen Sie sie schriftlich**:

1. **FSMO-Rollen:** Sollen alle fünf Rollen auf DC1 bleiben oder aufgeteilt werden? Was
   passiert bei einem Ausfall des Rolleninhabers — und ist das bei jeder Rolle gleich schlimm?
2. **Global Catalog:** Soll DC2 ebenfalls Global Catalog sein? Was spricht dafür, was dagegen?
3. **DNS:** Warum sollte auch DC2 die DNS-Rolle tragen, und wie müssen die DNS-Einträge der
   Clients dann aussehen?

Auch hier gibt es nicht die eine richtige Antwort. Bewertet wird, ob Ihre Begründung trägt.

---

## KI-Einsatz in diesem Auftrag

Replikationsfehler sind ein gutes Übungsfeld für die Fehlersuche mit KI: Die Meldungen von
`repadmin` sind kryptisch, aber ihr Wahrheitsgehalt lässt sich direkt am System prüfen.

```text
Ich erhalte in repadmin /showrepl folgende Meldung: [exakte Meldung].
Umgebung: zwei DCs derselben Domain, [OS-Version], gleicher Standort.
Ich habe bereits geprüft: [was Sie ausgeschlossen haben].
Nenne mir die 5 wahrscheinlichsten Ursachen, sortiert nach Wahrscheinlichkeit,
und für jede: mit welchem Befehl kann ich sie überprüfen?
Gib mir noch keine Lösung.
```

Halten Sie Ihren KI-Einsatz gemäss [ki-nutzung.md](../../ki-nutzung.md) in `ki-log.md` fest.

---

## Abgabe-Kriterien

1. **Teil A**: Planungseintrag des zweiten DC, Screenshot aus `dsa.msc` mit beiden DCs
2. **Teil B**: Ausgaben der drei Befehle, Erklärung des Begriffs Namenskontext
3. **Teil C**: Nachweis der Replikation in **beide** Richtungen, mit Zeitangabe
4. **Teil D**: Protokoll des Ausfalltests inkl. Anmeldeserver des Clients
5. **Teil E**: schriftliche Begründung zu FSMO, Global Catalog und DNS
6. **`ki-log.md`** mit Reflexion
