import yaml
import collections

def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath,"r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath,data):
    """Dumps data to a yaml file"""
    with open (filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

if __name__=="__main__":
    #filepath="test.yaml"
    filepath="simple_aal_import.aal"
    data=yaml_loader(filepath)
    print(data)
    
    res_data = {}
    bindKey = ""
    triggerList = []
    scenarioData = []
    for key,val in data.iteritems():
        if "stream" in key:
            scenarioData = data[key]
        if(type(val)==type(dict())):
            for k,v in val.iteritems():
                print key + "=>" + str(k) + "," + str(v)
                if "agent" in key:
                    if k=="group":
                        res_data['binding'] = {v:""}
                        bindKey = v
            for k,v in val.iteritems():
                print key + "=>" + str(k) + "," + str(v)
                if "agent" in key:
                    if k=="path":
                        res_data['binding'][bindKey] = v
                        
        if(type(val)==type(list())):
            for ele in val:
                if(type(ele)==type(dict())):
                    for k,v in ele.iteritems():
                        if(type(v)==type(list())):
                            for _v in v:
                                if(type(_v)==type(dict())):
                                    for _k,_v1 in _v.iteritems():
                                        print key + "=>" + k + "=>" + _k + "," + _v1
                                        #print key + k + _k + _v1
                        else:
                            print key + "=>" + str(k) +"," + str(v)
                            

                            
                else:
                    print key + "=>" + (ele)
                    if "group" in key:
                        res_data['actor'] = val
    
    for sdata in scenarioData:
        sdata = collections.OrderedDict(sdata)
        for key,val in sdata.iteritems():
            print key,val
            if key=="triggers":
                triggerList.append(val[0]['event'])
            elif key=='trigger':
                triggerList.append(val)
                triggerList.append(sdata['method'])
                triggerList.append("emit")
                triggerList.append(sdata['method']+"_done")
            elif val=='event' and 'trigger' not in sdata:
                triggerList.append('actor')
                triggerList.append(sdata['method'])
                triggerList.append("emit")
                triggerList.append(sdata['method']+"_done")

    res_data['scenario']=triggerList
    print(res_data)

    with open("DEWtry2.txt","w") as output:
        for key,val in res_data.iteritems():
            if key=="binding":
                output.write(key + "\n")
                for k,v in val.iteritems():
                    output.write(k + " : "+v)
            elif key=="actor":
                output.write("\n" + key +" : "+ val[0] + "\n")
            else:
                output.write("\n"+key + "\nwhen ")
                for i in range(0,len(res_data[key])):
                    if "done" in res_data[key][i]:
                        output.write(res_data[key][i]+" ")
                        output.write("\nwhen ")
                        for j in range(i+1,len(res_data[key])):
                            output.write(res_data[key][j]+" ")
                        break
                    else:
                        output.write(res_data[key][i]+" ")
                        
                        
                        
                
            




        

    
 