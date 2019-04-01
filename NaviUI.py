#Ugyen Dorji, udorji@uci.edu, 83628422


#------Navigation User Interface------
import MapQuestAPI
import NaviClasses
MQ=MapQuestAPI
NC=NaviClasses


def run_ui():
    result=MQ.get_result(MQ.build_directions_url())
    has_errors=MQ.error_check(result)
    if has_errors==False:
        MQ.run_calcs(result)
    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    

if __name__=='__main__':
    run_ui()
    
    
    
