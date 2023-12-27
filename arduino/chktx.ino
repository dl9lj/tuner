/*
* DL9LJ 2023-04-10
* Transmitter for Christian KopplerLDG AT-1000 Tuner
*                
* RF24 according to Dejan Nedelkovski, www.HowToMechatronics.com
* 
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
* 
*  C / L / L
*  AllOff 0 / 0 / 0
*  Thru 48 / 95 / 29
*  80m 191 / 161 / 28 
*  40m 49 / 176 / 31
*  20m 40 / 128 / 10
*  10m 50 / 192 / 31
*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN

const byte address[6] = "00001";

char text[10];
char i = 0;
int k = 0;
char inchar;


void setup() {

  Serial.begin(9600);
  
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_LOW); // MIN
  radio.stopListening();  
}

void loop() {
    
  if (Serial.available() > 0) {  // check if there is any data available on the serial port
    text[i] = Serial.read();  // read the incoming character
    i++;

    if(i > 3)
    {
      i = 0;
      k = 0;
      radio.write(&text, 4);
    }
  }

  k++;
  if (k > 50000)
  {
    i = 0;
    k = 0;
    text[0] = 0;
    text[1] = 0;
    text[2] = 0;
    text[3] = 0;
  }

}
