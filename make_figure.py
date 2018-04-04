import matplotlib.pyplot as plt
import codecs

def parse_datfile(fname):
    with codecs.open(fname, "r") as f:
        line = f.readline().strip()
        if (line[:9] != "Variables"):
            print("Wrong format! No variables defined!")
            return
        
        
        # Get var names
        var_names = []
        while(True):
            _a = line.find('"') + 1
            _b = line[_a+1:].find('"') + _a + 1
            if(_a == 0):
                break
            var_names.append(line[_a:_b])
            line = line[_b+1:]
#        print(var_names)
        
        data = {}
        for line in f:
            if (line[:6] == "Zone T"):
                _a = line.find('"') + 1
                _b = line[_a+1:].find('"') + _a + 1
                label = line[_a:_b]
                data[label] = [[] for i in range(len(var_names))]
            elif (line.strip() == ''):

                continue
            else:
                row = line.split()
                for i in range(len(var_names)):
                    data[label][i].append(float(row[i]))

        return var_names, data

def make_img_multi(path, fname):
    plt.figure(figsize = (5, 3))
    
    #plt.title('category classifier, limit=600')

    axes = plt.gca()
    ymin = 33
    ymax = 55
    #axes.set_xlim([1,10])
    axes.set_ylim([ymin, ymax])
    
    var_names, data = parse_datfile(path+fname)
    
    plt.xlabel(var_names[0])
    plt.ylabel(var_names[1])
    
    name = fname[:fname.find('.dat')]
#    print(name)
    imgname = path + name + '.png'
    for key in data:
        if(max(data[key][1]) >= ymin):
            x = data[key][0]
            y = data[key][1]
            plt.plot(x, y, '-o', linewidth=1.0, markersize=2.5, label=key)
    
    plt.legend(bbox_to_anchor=(1.05, 0.9, 0.0, 0.0), loc=2)
    

    
    plt.grid(
             alpha = 0.4,
             linestyle = '--',
             linewidth = 0.2,
             color = 'black',
             )
    
    plt.savefig(imgname, dpi=600, bbox_inches = 'tight')
#    plt.show()


def make_img_single(path, fname):
    plt.figure(figsize = (6, 3))
    
    #plt.title('category classifier, limit=600')
    
    var_names, data = parse_datfile(path+fname)
    
    plt.xlabel(var_names[0])
    plt.ylabel(var_names[1])
    
    name = fname[:fname.find('.dat')]
    imgname = path + name + '.png'
    for key in data:
        x = data[key][0]
        y = data[key][1]
        plt.plot(x, y, '-o', linewidth=1.0, markersize=2.5, label=key)

    
    plt.grid(
             alpha = 0.4,
             linestyle = '--',
             linewidth = 0.2,
             color = 'black',
             )
    
    plt.savefig(imgname, dpi=600, bbox_inches = 'tight')
#    plt.show()

#%%



path = 'schaeffler/'
#make_img_multi(path, 'accuracy_averaged.dat')

make_img_single(path, 'par_size.dat')



