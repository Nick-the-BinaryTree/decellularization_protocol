const unsigned long NUMBER_HYPERTONIC_BUFFER_WASHES = ;
const unsigned long HYPERTONIC_BUFFER_WASH_DURATION = ;
const unsigned long NUCLEASE_SOLUTION_TREATMENT_DURATION = ;
const unsigned long HYPOTONIC_TRIS_HCL_WASH_DURATION = ;
const unsigned long TRITON_X_100_TREATMENT_DURATION = ;
const unsigned long dH20_WASH_DURATION = ;
const unsigned long dH20_REWASH_INTERVAL = ;
const unsigned long PERACITIC_ACID_STERILIZATION_DURATION = ;
const unsigned long PBS_AND_dH20_WASH_DURATION = ;
const unsigned long NUMBER_PBS_AND_dH20_WASHES = ;
const unsigned long TIME_TO_FILL_CONTAINER = ;
const unsigned long TIME_TO_EMPTY_CONTAINER = ;
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

void emptyContainer() {
  digitalWrite(EMPTY_CONTAINER_PIN, HIGH);
  delay(TIME_TO_EMPTY_CONTAINER);
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
  
  // Begin protocol
  // Note: "wash" is equivalent to "treat" and "sterilization," they all mean fill the container and wait
  
  // Step four
  for (int i = 0; i < NUMBER_HYPERTONIC_BUFFER_WASHES; i++) {
    digitalWrite(HYPERTONIC_BUFFER_PIN, HIGH);
    delay(TIME_TO_FILL_CONTAINER);
    digitalWrite(HYPERTONIC_BUFFER_PIN, LOW);
    delay(HYPERTONIC_BUFFER_WASH_DURATION);
    emptyContainer();
  }
  
  // Step five
  // Does not set temperature to required 37 degrees Celsius
  digitalWrite(NUCLEASE_SOLUTION_PIN, HIGH);
  delay(TIME_TO_FILL_CONTAINER);
  digitalWrite(NUCLEASE_SOLUTION_PIN, LOW);
  delay(NUCLEASE_SOLUTION_TREATMENT_DURATION);
  emptyContainer();
  
  // Step six
  digitalWrite(HYPOTONIC_TRIS_HCL_SOLUTION_PIN, HIGH);
  delay(TIME_TO_FILL_CONTAINER);
  digitalWrite(HYPOTONIC_TRIS_HCL_SOLUTION_PIN, LOW);
  delay(HYPOTONIC_TRIS_HCL_WASH_DURATION);
  emptyContainer();
  
  // Step seven
  digitalWrite(TRITON_X_100_PIN, HIGH);
  delay(TIME_TO_FILL_CONTAINER);
  digitalWrite(TRITON_X_100_PIN, LOW);
  delay(TRITON_X_100_TREATMENT_DURATION);
  emptyContainer();
  
  // Step eight
  unsigned long numberOfWashes = ceil(dH20_WASH_DURATION / dH20_REWASH_INTERVAL);
  
  for (int i = 0; i < numberOfWashes; i++) {
    digitalWrite(dH20_PIN, HIGH);
    delay(TIME_TO_FILL_CONTAINER);
    digitalWrite(dH20_PIN, LOW);
    delay(dH20_REWASH_INTERVAL);
    emptyContainer();
  }
  
  // Step nine
  digitalWrite(PERACETIC_ACID_PIN, HIGH);
  delay(TIME_TO_FILL_CONTAINER);
  digitalWrite(PERACETIC_ACID_PIN, LOW);
  delay(PERACITIC_ACID_STERILIZATION_DURATION);
  emptyContainer();
  
  // Step ten
  for (int i = 0; i < NUMBER_PBS_AND_dH20_WASHES; i++) {
    digitalWrite(dH20_PIN, HIGH);
    digitalWrite(PBS_PIN, HIGH);
    delay(TIME_TO_FILL_CONTAINER/2);
    digitalWrite(dH20_PIN, LOW);
    digitalWrite(PBS_PIN, LOW);
    delay(PBS_AND_dH20_WASH_DURATION);
    emptyContainer();
  }
}

void loop() {}
