
#
#	This origranne started on 2025-02-14 system argumants for insterment identifaction control and selection
#


import sys
import pyvisa as visa
import re                                                                                   #   REGEX has use case for selecting multiple commands through further selectivity

#Parentage is a cimeric mix of ossicTest-06.py and Info2012CGrab-02.py with the later being used as the bases of information analysis 

def InstraSel(con):
    for I in range(len(con)):                                                               #  gathers all the insterments and Identifys them

        try :
            
            print( "\n Is this in list", I,"insterment is",con[I])
            
            print("who you =",Resource.open_resource(con[I]).query( "*IDN?" ))
            
            if I >= len(con):
                print("ERROR ",sys.argv[1],"end of list, Item was not found")
                sys.exit(0)
            else:
                who = int(Resource.open_resource(con[I]).query( "*IDN?" ).find(sys.argv[1]))
                
            if who >= 0:                                                                        #   confirms the location of the insterments
                Inst = Resource.open_resource(con[I])
                print("Match")
                return(Inst)
            else:
                print("ERROR ",sys.argv[1],"not found in list did it respond, Please be more seletive")
                print("Matchs are based on the first device that a match is noted on ")
                #sys.exit(1)
            
        except:
            print("no response form/no match",con[I])
        
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
