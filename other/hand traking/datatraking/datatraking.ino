#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "hall wifi";
const char* password = "Fibrus123";

WebServer server(80);

// Store only the latest number received
int latestNumber = 0;

// Serve the main page
void handleRoot() {
  String html = R"rawliteral(
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset='UTF-8'>
      <title>ESP32 Latest Number</title>
      <style>
        body { font-family: monospace; background: #222; color: #0f0; display:flex; justify-content:center; align-items:center; height:100vh; }
        #number { font-size: 6em; }
      </style>
    </head>
    <body>
      <div id="number">0</div>
      <script>
        async function fetchNumber() {
          const response = await fetch('/number');
          const text = await response.text();
          document.getElementById('number').textContent = text;
        }
        setInterval(fetchNumber, 100); // refresh every 100ms
        fetchNumber();
      </script>
    </body>
    </html>
  )rawliteral";

  server.send(200, "text/html", html);
}

// Serve the latest number
void handleNumber() {
  server.send(200, "text/plain", String(latestNumber));
}

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected!");
  Serial.print("ESP32 IP Address: ");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.on("/number", handleNumber);
  server.begin();
}

void loop() {
  server.handleClient();

  // Read Serial input line by line
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim(); // remove whitespace

    if (input.length() > 0) {
      latestNumber = input.toInt(); // convert string to int
      Serial.print("Latest Number: ");
      Serial.println(latestNumber);
    }
  }
}
