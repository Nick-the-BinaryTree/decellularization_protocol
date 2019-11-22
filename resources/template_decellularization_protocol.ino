// ***********************************************************************************
// DO NOT EDIT BELOW THIS POINT

// Wire connections to solenoid valves
const int HYPERTONIC_BUFFER_PIN = 13;
const int NUCLEASE_SOLUTION_PIN = 14;
const int HYPOTONIC_TRIS_HCL_SOLUTION_PIN = 16;
const int TRITON_X_100_PIN = 17;
const int dH20_PIN = 18;
const int PERACETIC_ACID_PIN = 19;
const int PBS_PIN = 21;
const int EMPTY_CONTAINER_PIN = 22;
const int ULTRASOUND_TRIGGER_PIN = 23;
const int ULTRASOUND_ECHO_PIN = 24;

double getHeightAboveLiquid() {
  // Clear pin
  digitalWrite(ULTRASOUND_TRIGGER_PIN, LOW);
  delayMicroseconds(2);

  // Send pulse
  digitalWrite(ULTRASOUND_TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(ULTRASOUND_TRIGGER_PIN, LOW);
  
  // Receive return pulse
  long duration = pulseIn(ULTRASOUND_ECHO_PIN, HIGH);

  // Calculate distance in centimeters
  return duration*0.034/2;
}

void fillContainer(int pin) {
  digitalWrite(pin, HIGH);
  while (CONTAINER_HEIGHT - getHeightAboveLiquid() < HEIGHT_TO_SUBMERGE_TISSUE) {
    delay(1);
  }
  digitalWrite(pin, LOW);
}

void halfFillContainer(int pin) {
  digitalWrite(pin, HIGH);
  while (CONTAINER_HEIGHT - getHeightAboveLiquid() < HEIGHT_TO_SUBMERGE_TISSUE/2) {
    delay(1);
  }
  digitalWrite(pin, LOW);
}

void emptyContainer() {
  digitalWrite(EMPTY_CONTAINER_PIN, HIGH);
  while (getHeightAboveLiquid() < CONTAINER_HEIGHT) {
    delay(1);
  }
  digitalWrite(EMPTY_CONTAINER_PIN, LOW);
}

void setup() {                
  // Initialize the digital pins as outputs
  pinMode(HYPERTONIC_BUFFER_PIN, OUTPUT);
  pinMode(NUCLEASE_SOLUTION_PIN, OUTPUT);
  pinMode(HYPOTONIC_TRIS_HCL_SOLUTION_PIN, OUTPUT);     
  pinMode(TRITON_X_100_PIN, OUTPUT);     
  pinMode(dH20_PIN, OUTPUT);     
  pinMode(PERACETIC_ACID_PIN, OUTPUT);     
  pinMode(PBS_PIN, OUTPUT);
  pinMode(EMPTY_CONTAINER_PIN, OUTPUT);
  pinMode(ULTRASOUND_TRIGGER_PIN, OUTPUT);
  pinMode(ULTRASOUND_ECHO_PIN, INPUT);
  
  // Begin protocol
  // Note: "wash" is equivalent to "treat" and "sterilization," they all mean fill the container and wait
  
  // Step four
  for (int i = 0; i < NUMBER_HYPERTONIC_BUFFER_WASHES; i++) {
    fillContainer(HYPERTONIC_BUFFER_PIN);
    delay(HYPERTONIC_BUFFER_WASH_DURATION);
    emptyContainer();
  }
  
  // Step five
  // Does not set temperature to required 37 degrees Celsius
  fillContainer(NUCLEASE_SOLUTION_PIN);
  delay(NUCLEASE_SOLUTION_TREATMENT_DURATION);
  emptyContainer();
  
  // Step six
  fillContainer(HYPOTONIC_TRIS_HCL_SOLUTION_PIN);
  delay(HYPOTONIC_TRIS_HCL_WASH_DURATION);
  emptyContainer();
  
  // Step seven
  fillContainer(TRITON_X_100_PIN);
  delay(TRITON_X_100_TREATMENT_DURATION);
  emptyContainer();
  
  // Step eight
  unsigned long numberOfWashes = ceil(dH20_WASH_DURATION / dH20_REWASH_INTERVAL);
  
  for (int i = 0; i < numberOfWashes; i++) {
    fillContainer(dH20_PIN);
    delay(dH20_REWASH_INTERVAL);
    emptyContainer();
  }
  
  // Step nine
  fillContainer(PERACETIC_ACID_PIN);
  delay(PERACITIC_ACID_STERILIZATION_DURATION);
  emptyContainer();
  
  // Step ten
  for (int i = 0; i < NUMBER_PBS_AND_dH20_WASHES; i++) {
    halfFillContainer(dH20_PIN);
    halfFillContainer(PBS_PIN);
    delay(PBS_AND_dH20_WASH_DURATION);
    emptyContainer();
  }
}

void loop() {}
