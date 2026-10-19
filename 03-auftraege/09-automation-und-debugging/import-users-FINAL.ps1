# FINALES REPARIERTES SKRIPT: User-Import aus CSV
# Alle Fehler behoben + Existenzprüfung hinzugefügt
# Domain korrigiert: ec2.tbz.brunner
Import-Module ActiveDirectory

$csvPath = "C:\Temp\mitarbeiter.csv"
$users = Import-CSV $csvPath -Delimiter ","  # FEHLER 1 BEHOBEN: ; zu ,

foreach ($row in $users) {

    $sAMAccountName = $row.Vorname.Substring(0,1) + $row.Nachname
    $userPrincipalName = "$sAMAccountName@ec2.tbz.brunner"  # DOMAIN KORRIGIERT
    $targetOU = "OU=$($row.Abteilung),OU=User,DC=ec2,DC=tbz,DC=brunner"  # FEHLER 3 BEHOBEN + DOMAIN KORRIGIERT

    # FEHLER 4 BEHOBEN: Existenzprüfung hinzugefügt (Teil B)
    $userExists = Get-ADUser -Filter "sAMAccountName -eq '$sAMAccountName'" -ErrorAction SilentlyContinue

    if ($userExists) {
        Write-Host "⚠️  User '$sAMAccountName' existiert bereits! Übersprungen." -ForegroundColor Yellow
        continue
    }

    Write-Host "✓ Erstelle User: $sAMAccountName in OU: $($row.Abteilung)" -ForegroundColor Green

    # FEHLER 2 BEHOBEN: ConvertFrom- zu ConvertTo- geändert
    # FEHLER 5 BEHOBEN: String-Expansion mit $() verbessert
    New-ADUser -Name "$($row.Vorname) $($row.Nachname)" `
               -SamAccountName $sAMAccountName `
               -UserPrincipalName $userPrincipalName `
               -Path $targetOU `
               -AccountPassword (ConvertTo-SecureString "Schule123" -AsPlainText -Force) `
               -Enabled $true

    Write-Host "✓ User '$sAMAccountName' erfolgreich erstellt!" -ForegroundColor Green
}

Write-Host "`n=== Import abgeschlossen ===" -ForegroundColor Cyan
