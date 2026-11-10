
#
#	This origranne started on 2025-02-14 system argumants for insterment identifaction control and selection
#


import sys
import pyvisa as visa
import re                                                                                   #   REGEX has use case for selecting multiple commands through further selectivity

#Parentage is a cimeric mix of ossicTest-06.py and Info2012CGrab-02.py with the later being used as the bases of information analysis 

def InstraSel(con):
    for I in range(len(con)):                                                               #  gathers all the insterments and Identifys them

        #who=rm.open_resource(con[I])
        
        
        who = int(Resource.open_resource(con[I]).query( "*IDN?" ).find(sys.argv[1]))
        if who >= 0:                                                                       #  confirms the location of a insterment and sets it 
            Inst = Resource.open_resource(con[I])
            print("",Inst.query("*IDN?"))
            return(Inst)
        elif who <= -1:
            print("error no match found with",(sys.argv[1]))
        else:
            print("ERROR in InstraSel function this should not Appeaer ever")
            sys.exit(0)
    Comb=""
    for I in range(len(con)):                                                               #  gathers all the insterments and Identifys and taks note of there 
        InstrID=Resource.open_resource(con[I])
        InstrName=Resource.open_resource(con[I]).query( "*IDN?" )
        Comb=InstrID,InstrName                                                              #   and taks note of the Identies of the insterment to a list which i can access 
    print("Combined list = ",Comb)
def InstraComplie(con):
    for I in range(len(con)):                                                               #  attempting the above slightly diffently (above is Identy the add to list)

        InstrID=Resource.open_resource(con[I])
        InstrName=Resource.open_resource(con[I]).query( "*IDN?" )
        Comb=InstrID+" # "+InstrName
    print("Combined list = ",Comb)
        


Resource = visa.ResourceManager()					                                        #   List Resources 
con = Resource.list_resources() 	                                                        #   Con for connection (Singular as its currently only for singular device at the moment)
print(Resource.list_resources() ) 			                                                #   Print listed Resources

INST = InstraSel(con)

sys.exit(0)
match sys.argv[2]:
    case ("Tektronic"):
        osc.write(' POS')
        print("TEKtronics picked")
    case  ("rohde-schwarz"):
        print("R&S picked")
    case _:
        print("Device Not Recognised")
