import wave

#workaround to convert 16 bit data
def hexstr_to_si(x):
    y = int(x, 16)
    # check sign bit
    if (y & 0x8000) == 0x8000:
        # if set, invert and add one to get the negative value, then add the negative sign
        y = -( (y ^ 0xffff) + 1)
    return y
    
def ByteToHex( byteStr ):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """
    
    # Uses list comprehension which is a fractionally faster implementation than
    # the alternative, more readable, implementation below
    #   
    #    hex = []
    #    for aChar in byteStr:
    #        hex.append( "%02X " % ord( aChar ) )
    #
    #    return ''.join( hex ).strip()        

    return ''.join( [ "%02X " % ord( x ) for x in byteStr ] ).strip()

input_file = "C:/my_python_scripts/test_wav/testwav.wav"
f = wave.open(input_file,'r')
print "nb channels  : ",
print f.getnchannels()
print ("getnchannels: " + str(f.getnchannels()) + "")
print ("getsampwidth: " + str(f.getsampwidth()) + " bytes")
print ("getframerate: " + str(f.getframerate()) + " ")
print ("getnframes: " + str(f.getnframes()) + " ")


if(f.getsampwidth() == 2):
    f.setpos(0)
    for i in range (100):
        s = f.readframes(1); 
        hexstr0 = ByteToHex(s[0])
        hexstr1 = ByteToHex(s[1])        
        sample_i16 = hexstr_to_si(hexstr1+hexstr0)
        print sample_i16
f.close()

