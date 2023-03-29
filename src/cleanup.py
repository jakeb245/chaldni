import os


if __name__ == '__main__':
    freq_fname = "/Users/jakebuchanan/code/chladni/data/freq_list.txt.txt"

    freq_list = []
    with open(freq_fname, 'r') as file:
        for line in file.readlines():
            line = line.rstrip('\n')
            freq_list.append(line)

    fit_dir = "/Users/jakebuchanan/code/chladni/ReverseFit/images/"
    for freq in freq_list:
        for fname in os.listdir(fit_dir):
                fname = fname[0:-4]
                fsplit = fname.split('_')
                if freq in fsplit[0]:
                    if fsplit[0].endswith('.'):
                        print(fname+'.png', fit_dir+fname.replace(freq+'.', freq)+'.png')
                        os.rename(fit_dir+fname+'.PNG', fit_dir+fname.replace(freq+'.', freq)+'.PNG')
