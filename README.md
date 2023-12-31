# tuner
wireless remote control for different antenna tuners

Yaesu FC-1000 / FC-800
started with buying a Yaesu Automatic Antenna Tuner FC-1000 w/o control unit. I started with removing the existing controller and thought about to do a replacement with an atmega328p in combination with 3 HC595 shift register. Interface to a laptop pc via uart. I had this setup running (328p firmware in C). But after working with NRF24L01 modules I decided to do the interface wireless. 328p is no longer required but the 595 board can be used.The 3 HC595 are connected via wires and DSUB9 connector to an externel arduino with NRF24L01 module. I wrote a python script with slider and radio buttons. Best band settings were programmed to radio buttons of the script. Later I found out, that my FT-840 has a controller included and I only need to have a cable... But the new setup is more flexible and can be used with any transceiver. 

LDG AT-1000 (2003)
is a asymmetric low-pass 1kW antenna tuner with manual control. Automatic does not really work well and the tuner had some issues with internal EMC. But in general it has good L and C components an uses an Allegro UCN5832 to control the 15 relays. Allegro UCN5832 has an 3-wire interface similar to SPI (data, clock, strobe). Some housings have a hole for D-SUB9 connector, but I have not found an controller option. I have have removed the connection between MC68HC11 and UCN5832 (chokes L11, L12 and L13) and connected UCN5832 with wires to a DSUB9 connector (data, clock, strobe, gnd, 12V). 

Christian Koppler (DL3LAC)
is a symmetric antenna coupler. The main unit contains only L, C and relays and will be controlled with a control unit via a 25-wire cable (16 pins for relays, 7 pins for 12V, 2 pins spare). I have created an interface board with TI TPIC6B595 driver 2s (2p for inductor relays) and 5V Supply. A arduino uno with NRF24L01 will be connected to this interface for receiving control data from the NRF24L01 transmitter.

The NRF24L01 transmitter will be the same for all 3 antenna tuners. NRF24L01 receiver hardware is equal for Yaesu and Christian Koppler. LDG needs a Strobe signal from pin 3 of the arduino. It is not required to build up 3 receiver but a dedicated receiver for each tuner helps to keep the overview. Each receiver requires a separate arduino firmware. 

Software is written very straight forward (no error correction / udp style). GUI does not show the real state after start (only after pushing the button). After start you have to press the "AllOff" button to set everything to zero/off.Terminal shows the output sequence. 

Additional interface hardware is required for Yaesu and Christian Koppler. The schematics for the Yaesu tuner has an wrong order for the relays connected to pin 12 to 19 (RL11,10,9,8,7,6,5,1_2 would be better). Later I have fixed that mistake with jumper wires. In between I have used a python script with LUT to do the correction  but correction in hardware makes programming easier. U1 of the Christian Koppler interface needs a 2nd TPIC6B595 on top (all pins connected except pin18 (nc)) because current output of a single chip is too weak for driving 4 relays in parallel. The board of the LDG Tuner has already the Allegro UCN5832 shift-register which can directly connected to the external arduino. Please check wiring.txt file for connections (is more recent than the existing schematics).

![J12](pics/gui.png)

#### GUI
- simple GUI with wxPython
- start with "AllOff" and set all buttons to 0
- output data will be printed on the terminal window

![J13](pics/chr_1.jpg)

#### Christian Koppler with remote receiver (Arduino with NRF24L01 module)
- this euro box can be put with some rain protection in the backyard to connect the antenna
- 12V from VRLA battery will be used

![J14](pics/chr_2.jpg)

#### Interface inside the housing
- tuner pcb has a male DSUB25 connector

![J15](pics/chr_3.jpg)

#### Interface board for Christian Koppler
- with 5V supply fot TPIC6B595 components
- 2nd TPIC6B595 is soldered on top of U1 (pin 18 not connected)

![J16](pics/ldg_1.jpg)

#### LDG AT-1000 Tuner
- front view

![J17](pics/ldg_2.jpg)

#### LDG AT-1000 Tuner
- rear view with added DSUB9 female

![J15](pics/ldg_3.jpg)

#### LDG AT-1000 Tuner
- top view
- see wiring to connect Allegro UCN5832

![J18](pics/ldg_4.jpg)

#### LDG AT-1000 Tuner
- small pcb with chokes to connect Allegro UCN5832

![J19](pics/ldg_5.jpg)

#### LDG AT-1000 Tuner
- wiring / connection

![J20](pics/rx1.jpg)

#### Receiver box
- Arduino Uno with NRF24L01 module
- Yaesu and Christian Koppler can use the same hardware (Arduino pins 4,5,6) but need different code
- LDG uses Arduino pins 3,4,5

![J21](pics/rxtx_1.jpg)

#### Receiver and transmitter boxes 
- looking very similar

![J22](pics/tx_1.jpg)

#### Transmitter box
- has USB connector for the connection to a laptop pc
- can also act w/o pc (currently only for testing) 

![J23](pics/yae_1.jpg)

#### Yaesu FC-1000 Antenna Tuner
- top view
- housing can withstand some raindrops

![J24](pics/yae_2.jpg)

#### Yaesu FC-1000 Antenna Tuner
- nice device - 40pin controller were replaced with a small pcp (3 x HC595)
- 3 sections can nearly tune and match any antenna (up to 150W)

![J25](pics/yae_3.jpg)

#### Yaesu FC-1000 interface board
- see wiring

![J26](pics/yae_4.jpg)

#### Yaesu FC-1000 interface board
- error was corrected with jumper wires

