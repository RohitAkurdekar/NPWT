#include<WiFi.h>
#include<HTTPClient.h>

#define PIN_LED 2
#define PIN_BUTTON 0
#define DEBOUNCE_DELAY 300

#define GET_DELAY 3000

#define SSID "AK"
#define PASS "diot123456"

#define HOST "http://192.168.77.205:8080"

unsigned long lastDebounceTime = 0;

int numberToSend = 1234;

unsigned long lastGETTime = 0;

bool ledState = false;

void setup() 
{
  // put your setup code here, to run once:

  pinMode(PIN_LED,OUTPUT);
  pinMode(PIN_BUTTON,INPUT);

  Serial.begin(115200);

  Serial.println("\n Connecting to: " + (String)SSID);

  WiFi.begin(SSID,PASS);

  while(WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(1000);
  }

  Serial.println("");
  Serial.print("IP addr: ");
  Serial.println(WiFi.localIP());
  
  Serial.print("MAC addr: ");
  Serial.println(WiFi.macAddress());

  digitalWrite(PIN_LED, HIGH);
  delay(100);
  digitalWrite(PIN_LED, LOW);

  Serial.println("Setup complete..");

}

void loop() 
{
  // put your main code here, to run repeatedly:
  int reading = digitalRead(PIN_BUTTON);

  unsigned long currentTime = millis();

  if((reading == LOW) && ((currentTime - lastDebounceTime) > DEBOUNCE_DELAY))  
  {
    lastDebounceTime = currentTime;
    
    String macAddr = WiFi.macAddress();
    String textToSend = "ESP32 " + macAddr + " value " + (String)numberToSend;

    numberToSend++;    

    Serial.print("button pressed, Sending : ");
    Serial.println(textToSend);    

    postRequest(textToSend);
  }

  currentTime = millis();

  if((currentTime - lastDebounceTime)> GET_DELAY)  
  {
    lastGETTime = currentTime;
    String result = getRequest();

    Serial.print("Return value...");
    Serial.println(result);  

    if(result == "on" && ledState == false)
    {
      ledState = true;
      digitalWrite(PIN_LED, HIGH)      ;      
    }
    else if(result == "off" && ledState == true)
    {
      ledState = false;
      digitalWrite(PIN_LED, LOW)      ;      
    }

  }

}

// -------------- getRequest() ------------------------------------------
String getRequest()
{
  HTTPClient http;

  http.begin(HOST);

  http.addHeader("Content-Type", "text/plain");
  int httpCode = http.GET()  ;
  String  payload = http.getString();

  http.end();

}

// ------------------- postRequest() ------------------------

void postRequest(String message)
{
  HTTPClient http;

  http.begin(HOST);
  http.addHeader("Content-Type", "text/plain");

  int httpCode = http.POST(message)  ;
  String  payload = http.getString();

  Serial.println(httpCode);
  Serial.println(payload);

  http.end();
}