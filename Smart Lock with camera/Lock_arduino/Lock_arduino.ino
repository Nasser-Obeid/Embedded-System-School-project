int inputPin = 2;
char msg;
void setup() {
  Serial.begin(9600);
  pinMode(inputPin, OUTPUT);     // declare sensor as input
}
 
void loop(){
  digitalWrite(inputPin, HIGH);
  
  if(Serial.available()>0){ 
    msg = Serial.read();
    
    Serial.println("msg recived");
  
     switch(msg){
      case 'A': digitalWrite(inputPin, LOW);
      delay(10000);
      Serial.println("ACCESS GRANTED: Face recognized.");
      digitalWrite(inputPin, HIGH);
      break;
  
      case 'B':
      Serial.println("ACCESSS DENIED: Face not recognized.");
      break;
  
      case 'C':
      Serial.println("ACCESS DENIED: No face detected..");
      break;
      }
// high: locked low: open
  }
}
