#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include "ESPAsyncWebServer.h"
#include <LittleFS.h>
#include <DNSServer.h>
#include <stdlib.h>
#include <Preferences.h>

AsyncEventSource events("/events");
AsyncWebServer server(80);

Preferences preferences;

IPAddress apIP(8, 8, 8, 8);
IPAddress netMsk(255, 255, 255, 0);

DNSServer dnsServer;

void config_ap_response()
{
  server.serveStatic("/", LittleFS, "/").setDefaultFile("index.html").setCacheControl("max-age=30");
  server.onNotFound([](AsyncWebServerRequest *request)
                    {
                          Serial.println(request->url());
                          if (request->url().endsWith(F(".js"))) {
                            Serial.println(F("js file"));                          
                          }
                          Serial.println("NOT FOUND " + request->url());                          
                          Serial.println(F("Redirect to AP Point"));
                          request->send(LittleFS, "/index.html", String(), false); });
}

void setup_ap()
{
  Serial.println(F("Starting AP!"));
  WiFi.softAP("robo");

  Serial.println(F("Gateway IP address: "));
  Serial.println(WiFi.softAPIP());
  dnsServer.setErrorReplyCode(DNSReplyCode::NoError);
  dnsServer.start(53, "*", apIP);
}

void setup_littlefs()
{
  Serial.println(F("Configure Littlefs.."));
  if (!LittleFS.begin())
  {
    Serial.println(F("LittleFS beginn FAILED!"));
  }
}

void setup()
{
  Serial.begin(9600);
  delay(1000);

  setup_littlefs();
  setup_ap();

  Serial.println(F("Looping.."));
}

void loop()
{
  dnsServer.processNextRequest();
}