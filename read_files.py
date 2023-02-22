import os,json,shutil

class ReadFiles:
    """
    dat fileやjson fileの読み込みを行う
    """
    
    def dat_read_file(self,dir_name,file_name):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__),dir_name,file_name)),"r") as f:
            fn = f.readline()
            fn = fn.replace('\n','')
        return fn

    def dat_write_file(self,output,dir_name,file_name):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__),dir_name,file_name)),"w") as f:
            print(output,file=f)

    #jsonの読み込みはここで行う
    def json_input(self,dir_name,file_name):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__),dir_name,file_name)),'r') as f:
                d = json.load(f)
        return d

    #書き込みはここで行う
    def json_output(self,output,dir_name,file_name):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__),dir_name,file_name)),'w') as f:
            json.dump(output, f, indent = 2, ensure_ascii=False)

    def abs_file_path(self):
        fn =os.path.abspath(os.path.dirname(__file__))
        return fn

    def file_number(self,file_name):
        number = file_name.replace('.json','')
        idx = number.find('_')
        number = number[idx+1:]
        number = int(''.join(number))
        return number
    
    def file_name_only(self,file_name):
        number = file_name.replace('.json','')
        idx = number.find('_')
        name = number[:idx]
        name = ''.join(name)
        return name

    def file_copy(self,folder_name,next_folder):
        for file_name in os.listdir(folder_name):
            source = os.path.join(folder_name, file_name)
            destination = os.path.join(next_folder,file_name)
            shutil.copy2(source,destination)
            print('copied ',file_name)