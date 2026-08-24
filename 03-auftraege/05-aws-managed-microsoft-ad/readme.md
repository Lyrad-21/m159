# AWS Managed AD / AD-Trust

> [!WARNING]
>
> **Achtung:** AWS Managed AD kostet etwa 18 $ pro Woche. Daher sollten Sie diesen Auftrag 05 und den daran anschliessenden Auftrag 06 erst ganz am Ende des Moduls durchführen. 

## Ressourcen

- [Bewertungskriterien](../../08-kompetenznachweise/lb2/kompetenzmatrix-lb2.md)
- [Fragenkatalog für den mündlichen Nachweis](fragen.md)
- [01_A_Planung_AD & Cloud Setup Sheet](../01-planung/resources/01-a-planung-ad-cloud-setup-sheet.md)

![Modul_159_Architekturdiagramm](../01-planung/resources/modul-159-architekturdiagramm.drawio.svg)



## AWS Managed AD Domain

> [!IMPORTANT]
>
> Tragen Sie das von Ihnen hier festgelegte Passwort unbedingt bei Ihrer Planung ein.

| Schritte  | Printscreens                  |
| --------- | ----------------------------- |
| Schritt 1 | ![Step1](resources/step1.png) |
| Schritt 2 | ![Step2](resources/step2.png) |
| Schritt 3 | ![Step3](resources/step3.png) |
| Schritt 4 | ![Step4](resources/step4.png) |
| Schritt 5 | ![Step5](resources/step5.png) |

## Ports aus der Planung nochmal sicherstellen

Sofern die Ports wie geplant eingerichtet wurden, kann mit der Einrichtung des Trusts begonnen werden.

## Conditional Forwarders

Damit Ihr Active Directory in EC die AWS-Managed-Domain sehen kann, muss ein sogenannter Conditional Forwarder eingerichtet werden. Normalerweise gehen AD-Abfragen immer an den eigenen DNS-Server des Active Directory. Da wir bei dieser Abfrage jedoch einen DNS-Server ausserhalb von `ec2.meinedomain.corp` abfragen müssen, benötigen wir diese bedingte Weiterleitung.



![Step5](resources/conditionalforwarder.png)

![Step5](resources/dns-server.png)

> [!TIP]
>
> Testen Sie den Conditional Forwader mit nslookup zb mit `nslookup -type=SOA aws.meinedomain.corp`
>

## Trust einrichten

### EC2 AD

Gehen Sie auf Active Directory Domain and Trusts -> Eigenschaften auf Ihre Domain

| Schritte  | Printscreen                               |
| --------- | ----------------------------------------- |
| Schritt 1 | ![Trust-Step1](resources/trust-step1.png) |
| Schritt 2 | ![Trust-Step1](resources/trust-step2.png) |
| Schritt 3 | ![Trust-Step1](resources/trust-step3.png) |
| Schritt 4 | ![Trust-Step1](resources/trust-step4.png) |
| Schritt 5 | ![Trust-Step1](resources/trust-step5.png) |
| Schritt 6 | ![Trust-Step1](resources/trust-step6.png) |
| Schritt 7 | ![Trust-Step1](resources/trust-step7.png) |

### AWS managed AD

| Schritte  | Printscreens                                  |
| --------- | --------------------------------------------- |
| Schritt 1 | ![Trust-Step1](resources/aws-trust-step1.png) |
| Schritt 2 | ![Trust-Step1](resources/aws-trust-step2.png) |
| Schritt 3 | ![add-aws-trust](resources/add-aws-trust.png) |
| Schritt 4 | ![Trust-Step1](resources/aws-trust-step3.png) |



### Trust validieren

Nachdem beide Seiten eingerichtet sind kann die Validierung auf dem EC2 Active Directory gemacht werden

 ![Trust-Step1](resources/validate.png)
