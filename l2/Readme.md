# Einführung in Arduino / Nodemcu
---

## Control

<style>
.centerButton {
    width: 100px !important;
    margin: 0 auto;
}
</style>

<a href="#" id="start" class="centerButton" data-role="button" data-theme="b">Start Loop</a>

<a href="#" id="stop" class="centerButton" data-role="button" data-theme="b">Stop Loop</a>


<script>
$("#start").click(function() {
    fetch("/start").then(function(response) {
      return response.json();
    }).then(function(data) {
      console.log(data);
    }).catch(function(err) {
      console.log('Fetch Error :-S', err);
    });
});
$("#stop").click(function() {
    fetch("/stop").then(function(response) {
      return response.json();
    }).then(function(data) {
      console.log(data);
    }).catch(function(err) {
      console.log('Fetch Error :-S', err);
    });
});
</script>

## Einführung in Arduino und NodeMCU

### Was ist Arduino und wofür wird es verwendet?

Arduino ist eine Plattform für Elektronik- und Mikrocontroller-Projekte. Diese Plattform umfasst zum einen die Arduino Elektronik-Hardware-Boards und zum anderen die Arduino Software mit deren Hilfe die Boards programmiert werden können.
Das Geniale an Arduino ist: Die gesamte Plattform ist „open Source“. Das heißt, dass die Schaltpläne und Layouts der Hardware Boards frei zugänglich sind und jeder sie für seine Zwecke verwenden oder modifizieren kann.

### Was ist ein NodeMCU und welche Funktionen bietet es?

Das NodeMCU Entwicklerboard ist ein kleiner, leistungsstarker Mikrocontroller. Es verfügt ähnlich wie ein Arduino-Board über GPIOs (general purpose input/output), also digitale Ein- und Ausgänge und zusätzlich ist ein ESP8266-Modul integriert. Über dieses Modul kann eine Verbindung in WLAN-Netze hergestellt werden.

https://www.elektrotechnik-einfach.de/was-ist-arduino/

### Pin Belegung

<img src='img/nodemcu-pinout-functions.jpg' width="80%" alt="Nodemcu"/>

Quelle: https://www.make-it.ca/nodemcu-details-specifications/

## Ändere den Namen von dem AccessPoint von robo in einem von dir gewählten Namen

* datei main.cpp finden
* code stelle finden und den namen ändern
* in das Plugin "PlatformIO" wechseln (links an der seite, der Armeisenkopf)
* Unter nodemcuv2 -> General -> Upload and Monitor -> Schauen ob der Wifi name geändert wurde

## Verbinde dich mit dem Access Point und starte und stoppe die loop function

Die Buttons start und stop sollten die main loop starten und wieder stoppen. Das kann dir später behilflich sein damit dir der roboter nicht vom tisch fährt


## Mit dem Klebeband irgendwo einen kleinen streifen hinkleben, damit der Roboter diesen folgen kann

Klebeband für die Linienverfolgung vorbereiten:

Schneide ein Stück Klebeband in der gewünschten Länge ab und klebe es auf den Boden.
Achte darauf, dass das Klebeband gerade und gut befestigt ist, um eine klare Linie für den Roboter zu schaffen.
Lasse genügend Platz um das Klebeband herum, damit der Roboter genügend Raum hat, um die Linie zu erkennen und ihr zu folgen.

## Konfiguriere die Sensoren

Der Potentiometer an den Line-Following-Sensoren ermöglicht die Einstellung der Empfindlichkeit, um die Linie genau zu erkennen.
Finde den Potentiometer auf den Sensormodulen. Es sollte ein kleiner Schraubendreher-Schlitz oder ein verstellbarer Widerstand vorhanden sein.
Drehe den Potentiometer im Uhrzeigersinn, um die Empfindlichkeit zu erhöhen, oder gegen den Uhrzeigersinn, um sie zu verringern.
Während du den Potentiometer einstellst, beobachte die Reaktion der Sensoren auf das Klebeband.
Ziel ist es, die Empfindlichkeit so einzustellen, dass der Roboter das Klebeband zuverlässig erkennt und ihm genau folgen kann, ohne von der Linie abzuweichen.

## Implementiere die Logik

Implementiere die Logik in der loop-Funktion in der main.cpp-Datei, um den Roboter dem Klebeband folgen zu lassen.

Die loop-Funktion wird fortlaufend ausgeführt und ist der Hauptarbeitsbereich des Roboters.
In dieser Funktion sollst du den aktuellen Zustand des Roboters aus den Sensorwerten auslesen und entsprechende Aktionen ausführen, um dem Klebeband zu folgen.
Die Sensorwerte werden mit den Schwellenwerten verglichen, um festzustellen, ob der Roboter auf der Linie ist oder nicht.
Basierend auf dem Zustand des Roboters kannst du verschiedene Aktionen ausführen, um auf der Linie zu bleiben. Zum Beispiel die Motoren steuern, Richtungsänderungen vornehmen oder andere relevante Funktionen nutzen.
Es ist wichtig, dass du die Roboterlogik so implementierst, dass der Roboter zuverlässig dem Klebeband folgen kann, ohne davon abzuweichen.

## Montiere die Ränder und teste deine Implementierung

Viel spaß

## Verbesserungsvorschläge / Projekt Forken

### Forken des Projekts:

Gehe zur Projektseite (https://github.com/ApfelPresse/arduino_lp) und klicke auf die Schaltfläche "Fork" oben rechts auf der Seite.
Dadurch wird eine Kopie des Projekts in deinem persönlichen GitHub-Konto erstellt.
Du kannst nun Änderungen an dieser Kopie vornehmen, ohne das originale Projekt zu beeinflussen.
Lokales Repository erstellen:

Klonen des geforkten Projekts auf deinen Computer, indem du den Git-Befehl git clone verwendest oder eine Git-Desktop-Anwendung nutzt.
Gehe in deinem Terminal oder deiner Git-Desktop-Anwendung zum Zielordner und führe den Klonbefehl aus.
Dadurch wird eine lokale Kopie des geforkten Projekts auf deinem Computer erstellt.

### Branch erstellen:

Wechsle in deinem Terminal oder deiner Git-Desktop-Anwendung zum geklonten Projektordner.
Erstelle einen neuen Branch, um deine Änderungen zu isolieren, indem du den Befehl git branch branchname verwendest (ersetze "branchname" durch einen Namen deiner Wahl).
Wechsle zum neuen Branch, indem du den Befehl git checkout branchname verwendest.

### Änderungen machen:

Bearbeite die erforderlichen Dateien 

### Änderungen bestätigen:

Führe den Befehl git status aus, um den Status der geänderten Dateien anzuzeigen.
Füge die geänderten Dateien dem Git-Index hinzu, indem du den Befehl git add dateiname verwendest (ersetze "dateiname" durch den tatsächlichen Dateinamen) oder verwende git add ., um alle geänderten Dateien hinzuzufügen.
Bestätige die Änderungen mit einer aussagekräftigen Commit-Nachricht, indem du den Befehl git commit -m "Nachricht" verwendest (ersetze "Nachricht" durch eine beschreibende Nachricht deiner Änderungen).

### Änderungen hochladen:

Lade deine Änderungen auf deinen Fork des Projekts hoch, indem du den Befehl git push origin branchname verwendest (ersetze "branchname" durch den Namen deines erstellten Branches).
Dadurch werden deine Änderungen in deinem Fork des Projekts auf der Plattform hochgeladen.

### Pull-Request erstellen:

Gehe zur Projektseite deines Forks auf der Plattform und klicke auf die Schaltfläche "Pull Request" oder "New Pull Request".
Vergleiche die Änderungen zwischen deinem Branch und dem Hauptbranch des Originalprojekts.
Überprüfe die Änderungen sorgfältig und füge eine aussagekräftige Beschreibung für den Pull-Request hinzu.
Wenn alles in Ordnung ist, sende den Pull-Request ab.


### Zusammenführen der Änderungen:

Die Projektverwalter können nun deinen Pull-Request überprüfen, Kommentare abgeben und Änderungen anfordern.
Wenn deine Änderungen genehmigt sind, werden sie in den Hauptbranch des Originalprojekts zusammengeführt.
Du kannst den aktualisierten Hauptbranch deines Forks aktualisieren, indem du den Befehl git pull origin main (oder entsprechend) in deinem lokalen Repository ausführst.