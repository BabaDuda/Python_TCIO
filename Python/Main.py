## Import Libraries
import pyads
import time

## Variables and Instructions
AMSNETID = "192.168.1.66.1.1"
boolOutTest = True;
incrementTest = 0;
plc = pyads.Connection(AMSNETID, 27905)
plc.open()
print(f"Connected?: {plc.is_open}")
print(f"Local Address? : {plc.get_local_address()}")
print(plc.read_state())

while True:
##    testInt = plc.read_by_name("Term 6 (EL3102).AI Standard Channel 1.Value", pyads.PLCTYPE_INT)
##    testbool = plc.read_by_name('Term 2 (EL1014).Channel 1.Input', pyads.PLCTYPE_BOOL)
##    print('Boolean input is ', testbool, ', ', 
##          'Integer Value is ', testInt, sep='', end='                   \r')
    time.sleep(0.5)
    incrementTest = incrementTest + 500
    if incrementTest > 32767:
        incrementTest = 0
    boolOutTest = not boolOutTest
    print('Boolean Output is ',  boolOutTest, ', Output Integer Value is ', incrementTest, sep='', end='                   \r')  
    plc.write_by_name("Term 3 (EL2014).DIG Outputs.Channel 1.Output", boolOutTest, pyads.PLCTYPE_BOOL)
    plc.write_by_name("Term 7 (EL4102).Channel 1.Output", incrementTest, pyads.PLCTYPE_INT)