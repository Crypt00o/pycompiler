from builtins import compile,open
from marshal import dump
from compileall import compile_file,compile_dir
from argparse import ArgumentParser

def compile_source(source_file,optimize_level):
    bytecode = compile(source=open(source_file).read(), filename=source_file,mode='exec',optimize=optimize_level)
    return bytecode

def file_full_compile(source_file,optimize_level):
    compile_file(fullname='source_file',optimize=optimize_level)

def dir_full_compile(source_dir,optimize_level):
    compile_dir(dir=source_dir,optimize=optimize_level)

def write_compiled_code(bytecode,output_file):
    with open(output_file, 'wb') as file :
        dump(bytecode,file)



def parse_args():
    arg_parser=ArgumentParser()
    arg_parser.description="PyCompile For Compile Pyhton Code to native bytecode\n Created By 0xCrypt00o"
    group=arg_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f','--full-compile',dest="full_compile",action='store_true',help="Full Compile This File Source Code and Compile all Modules imported insided it")
    group.add_argument('-d','--dir-full-compile',dest="dir_full_compile",action='store_true',help="Full Compile All Source Code Inside Spefic Dir and Compile all Modules imported insided it")
    group.add_argument('-c',"--compile",dest='normal_compile',action='store_true',help="Compile Source Code Without Compile Imported Modules")
    arg_parser.add_argument("-i",'--input-file',dest="source_file",required=True,help="Path To Source Code File|Dir ")
    arg_parser.add_argument("-o","--optimize",dest="optimize_level",choices=[0,1,2], type=int,default=2,help="level for code optimization ")
    args=arg_parser.parse_args()
    return args

def main():
    try:
        args=parse_args()
        if args.normal_compile:
            write_compiled_code(compile_source(args.source_file,args.optimize_level),"{}.pyc".format(args.source_file))
        elif args.full_compile:
            file_full_compile(args.source_file,args.optimize_level)
        elif args.dir_full_compile:
            dir_full_compile(args.source_file,args.optimize_level)
        print("[+] Compiled Successfully : {}".format(args.source_file))
    except Exception as exception:
        print("[-] Error While Compile {} : {} ".format(args.source_file,exception))

if __name__=="__main__":
    main()
