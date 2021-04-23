// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  delay(1000*5);
  int sensorValue0 = analogRead(A0);
  int sensorValue1 = analogRead(A1);
  int sensorValue2 = analogRead(A2);
  int sensorValue3 = analogRead(A3);

  //Normalize values to between 0 and 1
  float voltage0 = sensorValue0 / 500;
  float voltage1 = sensorValue1 / 500;
  float voltage2 = sensorValue2 / 500;
  float voltage3 = sensorValue3 / 500;
  
  // print out the value you read:
  Serial.print("0:");
  Serial.println(voltage0);

  Serial.print("1:");
  Serial.println(voltage1);
  
  Serial.print("2:");
  Serial.println(voltage2);
  
  Serial.print("3:");
  Serial.println(voltage3);
}