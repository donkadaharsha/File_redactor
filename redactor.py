import argparse
import glob, os
import os.path
from project1 import main
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    parser.add_argument("--names", action='store_true')
    parser.add_argument("--genders", action='store_true')
    parser.add_argument("--dates", action='store_true')
    parser.add_argument("--phones", action='store_true')
    parser.add_argument("--address", action='store_true')
    parser.add_argument("--stats", type=str)
    
    args = parser.parse_args()
    
    result={}
    summary=""
    if args.input:
        ip_files=args.input
        ip_files_list= glob.glob("*.txt")
    for file in ip_files_list:
        f=open(file, "r")
        document=f.read()

        if args.names:
            result["names"] = main.names(document)[1]
        if args.address:
            result["address"] = main.address(document)[1]
        if args.genders:
            result["genders"] = main.genders(document)[1]
        if args.dates:
            result["dates"] = main.dates(document)[1]
        if args.phones:
            result["phones"] = main.phones(document)[1]
        if args.stats:
            summary += f"The redacted summary report for file '{file}' is:\n{main.statistics(result)}"

            if args.output:  
                cwd = os.getcwd()
                folderpath = os.path.join(cwd, args.output[1:-1])
                filepath = os.path.basename(file) + '.redacted'
                final_path = os.path.join(folderpath, filepath)
                if os.path.isdir(folderpath):
                    final_file = open(final_path,"w", encoding="utf-8")
                else:
                    os.mkdir(folderpath)
                    final_file = open(final_path,"w", encoding="utf-8")
                final_file.write(main.textToUnicode(result, document))
                final_file.close()
    stats_file = args.stats
    if stats_file=="stdout":
        print(summary)
    elif stats_file=="stderr":
        sys.stderr.write(summary)
    else:
        stats = open(stats_file, "w")
        stats.write(summary)
        stats.close()
