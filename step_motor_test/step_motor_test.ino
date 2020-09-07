int pulse_per_rev = 200; // unit ; pulse/rev
int pulse_delay = 1; // unit ; ms
int delay_time = 1000; // unit ; ms
// for linear actuator
int lead = 2; // unit : mm

int PUL = 13;
int DIR = 12;

void setup() {
  pinMode(PUL, OUTPUT);
  pinMode(DIR, OUTPUT);
  Serial.begin(9600);
  Serial.print("Resolution : ");
  Serial.print( float(lead) / float(pulse_per_rev));
  Serial.println("mm/pulse");
}

void loop() {
  
  digitalWrite(DIR, HIGH);
  give_PUL( PUL, pulse_per_rev, pulse_delay, delay_time);

  digitalWrite(DIR, LOW);
  give_PUL( PUL, pulse_per_rev, pulse_delay, delay_time);
}

void give_PUL(int PUL, int pulse_per_rev, int pulse_delay, int delay_time) {

  // Give a Pulse
  for(int i=0; i<pulse_per_rev; i++)
  {
    digitalWrite(PUL, HIGH);
    delay(pulse_delay);
    digitalWrite(PUL, LOW);
    delay(pulse_delay);
  }

  // Give delay time
  delay(delay_time);
}
