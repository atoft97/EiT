import random
from datetime import datetime

def main():

	#Add Firebase Config here
    #firebase_config = dict()

    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()

    f = open("skriveFile.txt", "a")

    f.write("ny kjoring")
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()


    counters = [0,0,0,0]
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            #print(line)
            splitted = line.split(":")
            #print(splitted)
            plantDict = {splitted[0]: splitted[1]}
            #print(plantDict)

            plant = {'time':time.time(), splitted[0]:splitted[1]}
            #f.write(str(line) + "\n")
            #db.push(plant)
            timestamp = str(datetime.now())
            moist = float(splitted[1])
            data=dict(
                timestamp=timestamp,
                #soliMoisture=float(splitted[1])
                soilMoisture=moist
            )
            print(data)
            f.write(str(splitted[0]) +"," + str(data) +"\n")
            #print(random.uniform(0,1))
            #print(type(random.uniform(0,1)))
            #print(float(splitted[1]))
            #print(type(float(splitted[1])))
            print("plant" + splitted[0])
            plantNumber = int(splitted[0])
            counters[plantNumber] += 2
            #try:
            if (counters[plantNumber]>=60):
                counters[plantNumber] = 0
                db.child("plants").child("plant" + splitted[0]).child("log").push(data)
            db.child("plants").child("plant" + splitted[0]).child("latest").set(data)
            #except:
            #    print("feil")
    f.close()

main()