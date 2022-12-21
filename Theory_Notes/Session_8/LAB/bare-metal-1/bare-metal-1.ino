void setup() {
  // put your setup code here, to run once:
  DDRB = 32;

}

void loop() {
  // put your main code here, to run repeatedly:
  PORTB = 32;
  for(long i=0; i<1000000; i++){PORTB = 32;}
  PORTB = 0;
  for(long i=0; i<1000000; i++){PORTB = 0;}

}
