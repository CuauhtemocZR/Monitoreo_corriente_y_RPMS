String sResultado, sEspacios;
int iContador,contadorf;
int iTamanoCadena = 30;
int C2=53;
int mssg=0;
volatile int contador = 0;
void setup() {
   pinMode(C2, OUTPUT);
   Serial.begin(115200);
   attachInterrupt(0,interrupcion0,RISING);
}
void loop() {
  delay(990);
  float I = get_cor(1000);
  float V = get_vol(1000);
  float W=V*I;

  V=V-.65;
  sResultado = String(I) + "|" + String(contador*60) + "|" + String(V) + "|"+ String(W) + "|";
  Serial.println(sResultado); 
  contador = 0; 
  if (Serial.available() > 0)
  {
    mssg = Serial.read(); 
  if(mssg == 'A')
  {
    digitalWrite(C2,HIGH);
    }
  else if(mssg == 'B')
    {
     digitalWrite(C2,LOW);
     } 
   }
}
void interrupcion0()
{
  contador++;       
}
float get_cor(int n_muestras)
{
  float voltajeSensor;
  float corriente=0;
  
  for(int i=0;i<n_muestras;i++)
  {
    voltajeSensor = analogRead(A0) * (5.0 / 1024.0);////lectura del sensor
    corriente=corriente+(voltajeSensor); //Ecuación  para obtener la corriente
  }
  corriente=corriente/n_muestras;
  return(corriente);
}
float get_vol(int n_muestras)
{
  float voltajeSensor2;
  float voltaje=0;
  for(int i=0;i<n_muestras;i++)
  {
    voltajeSensor2 = analogRead(A1) * (25.0 / 1024.0);////lectura del sensor
    voltaje=voltaje+(voltajeSensor2); 
  }
  voltaje=voltaje/n_muestras;
  return(voltaje);
}

