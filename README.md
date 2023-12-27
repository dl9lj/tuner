# tuner
remote controller for different antenna tuners

Yaesu FC-1000 / FC-800
started with buying a Yaesu Automatic Antenna Tuner FC-1000 w/o control unit. I started with removing the existing controller and made a replacement with an atmega328p and 3 HC595 to control the 21 relays of the FC-1000. I loaded the arduino bootloader to the 328p to use arduino ide for programming. Tuner control via RS232 simple protocol. After that I have used wireless RF24 modules Rx (at the tuner) and Tx (at the pc laptop). I wrote a python script with slider and radio buttons. Best band settimgs were programmed to radio buttons of the script. Later I found out, that my FT-840 has a controller included and I only had to create a cable...

LDG AT-1000 (2003)
is a asymmetric low-pass 1kW antenna tuner with manual control. Automatic does not really work well and the tuner had some issues with internal EMC. But in general it has good L and C components an uses a Allegro 5832 to control the 15 relays. Allegro 5832 has an 3-wire interface similar to SPI (data, clock, strobe). Some housings have a hole for D-SUB9 connector, but I have not found an controller option. I have have removed the connection between 68HC11 and 5832 (chokes L11, L12 and L13) and connected 5832 with wires to a DSUB9 connector (data, clock, strobe, gnd, 12V). 

Christian Coupler (DL3LAC)
is symmetric antenna coupler. The main unit contains only L, C and relays and will be controlled with a control unit via a 25-wire cable. 

