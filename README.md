# Prerequisites
1. `Windows` or `Linux` machine
2. `Python3` installed

# How to Run

## Windows
When running for the first time execute as administrator file `.\setup-win.bat` in command line. This only needs to be done once.
1. Open command line
2. Run `.\activate-win.bat`
3. Run main program using `.\cluster.py [filename]`, where `[filename]` is a path to the file containing file paths of images to cluster (each in separate line). To see sample input file check out `example\input1.txt` or run `.\cluster.py example\input1.txt`
4. Output file names are `output.html` and `output.txt`
5. After you are done working with the program run `deactivate`

## Linux

When running for the first time execute file `./setup-linux.sh` in command line. This only needs to be done once.
1. Open command line
2. Run `./activate-linux.sh`
3. Run main program using `./cluster.py [filename]`, where `[filename]` is a path to the file containing file paths of images to cluster (each in separate line). To see sample input file check out `example\input1.txt` or run `.\cluster.py example\input1.txt`
4. Output file names are `output.html` and `output.txt`
5.. After you are done working with the program run `deactivate`
