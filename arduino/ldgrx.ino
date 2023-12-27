/*
* DL9LJ 2023-04-10
* Receiver for LDG AT-1000 Tuner
*                
* RF24 according to Dejan Nedelkovski, www.HowToMechatronics.com
* 
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN

const byte address[6] = "00001";
const int SCK_PIN = 4; // Clock pin
const int MOSI_PIN = 5; // Data out pin
const int SS_PIN = 6; // Slave select pin
const int STROBE = 3; // Strobe
byte cap = 0;
byte ind = 0;


void setup() {
  SPI.begin();
  SPI.setDataMode(SPI_MODE0);
  
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_LOW); // MIN
  radio.startListening();
  pinMode(SCK_PIN, OUTPUT);
  pinMode(MOSI_PIN, OUTPUT);
  pinMode(SS_PIN, OUTPUT);
  pinMode(STROBE, OUTPUT);
}

void loop() {

      
  if (radio.available()) {
    char text[32] = "";
    radio.read(&text, sizeof(text));
    Serial.println(text);

    switch(text[0]) {

        case 0x31:
         cap = text[3] - 0x30;
         cap = cap + (text[2] - 0x30)*10;
         cap = cap + (text[1] - 0x30)*100;
         break;

        case 0x32:
         ind = text[3] - 0x30;
         ind = ind + (text[2] - 0x30)*10;
         ind = ind + (text[1] - 0x30)*100;
         break;

        default: 
        break;
        }
      
    digitalWrite(SS_PIN, LOW);
    digitalWrite(STROBE, LOW);

    for (int i = 0; i < 15; i++) {
    // Send the current bit
      digitalWrite(MOSI_PIN, 0);
    
    // Pulse the clock
      digitalWrite(SCK_PIN, HIGH);
      digitalWrite(SCK_PIN, LOW);
    }

    for (int i = 0; i < 7; i++) {
    // Send the current bit
      digitalWrite(MOSI_PIN, bitRead(cap, i));
    
    // Pulse the clock
      digitalWrite(SCK_PIN, HIGH);
      digitalWrite(SCK_PIN, LOW);
    }

    for (int i = 0; i < 2; i++) {
    // Send the current bit
      digitalWrite(MOSI_PIN, 0);
    
    // Pulse the clock
      digitalWrite(SCK_PIN, HIGH);
      digitalWrite(SCK_PIN, LOW);
    }

    for (int i = 0; i < 7; i++) {
    // Send the current bit
      digitalWrite(MOSI_PIN, bitRead(ind, i));
    
    // Pulse the clock
      digitalWrite(SCK_PIN, HIGH);
      digitalWrite(SCK_PIN, LOW);
    }

      digitalWrite(MOSI_PIN, 0);
    
    // Pulse the clock
      digitalWrite(SCK_PIN, HIGH);
      digitalWrite(SCK_PIN, LOW);

     digitalWrite(SS_PIN, HIGH);
     digitalWrite(STROBE, LOW);
     digitalWrite(STROBE, HIGH);
     digitalWrite(STROBE, HIGH);
     digitalWrite(STROBE, LOW);
  }

}
