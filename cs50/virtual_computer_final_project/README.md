# Nand to Tetris - Build a Computer from First Principles 

## Getting Started 

This directory consists of a basic computer including a hardware chipset (in hdl language), an assembler, and a virtual machine.  To run a program on this "virtual computer," the code must be converted to the Virtual Machine intermediate language.  The VM API is laid out below.

Please note that the elaborate process for using the software written here is intentional.  By following all steps, you will understand the process of "compilation" in great detail.


### Prerequisites

In order to run project files, [download the software suite](http://www.nand2tetris.org/software.php) from the Nand to Tetris website, and have Python 2.7.13 or higher installed on your system.

After installing, you will need two of the tools to successfully run the "maze_game," or any other piece of software written in the Jack programming language (Nand2tetris native language):

1. Compiler (command line tool)
2. CPU Emulator (GUI tool)

### Running a "Jack Program" (see software/maze_game)

1. Create a new directory which contains all the .jack files, and all the [.vm files from the operating system folder.](https://github.com/zachgoll/finance_to_code/tree/master/cs50/virtual_computer_final_project/software/operating_system). 
2. Assuming you have downloaded the prerequisites, from the command line (where "projectdirectory" is the directory you have just created): 

```
$> cd projectdirectory
$> JackCompiler.sh projectdirectory/               // If using Mac 
$> JackCompiler.bat projectdirectory/              // If using Windows
```

This will compile your .jack files into vm files. 

3. Now, you will have to convert all of your .vm files into .hack files.

``` 
$> cd ~/virtual_computer_final_project/software/virtual_machine
$> python vm_translator.py ~/projectdirectory/
```

Please note that in place of "~/projectdirectory/" you will need to supply a full path to the directory which you would like translated.

4. You now have a long .asm file.  To convert this file into machine language which will run on the "Hack" hardware/chipset,  you must use the Assembler. 

``` 
$> cd ~/virtual_computer_final_project/software/Assembler
$> python assembler.py ~/.asmfile

The "~/.asmfile" represents the path to the .asm file that was created from the last step.

5. You now have one enormously long file containing 0's and 1's.  To run this machine code, we will need the CPUEmulator that you downloaded from the Nand2Tetris software suite.  Theoretically, this machine code could be run on a real, physical machine built via the chipset specification in the hardware directory of this repository.  Since this would be awfully tedious to do, go to the command line and open the CPUEmulator.

```
$> CPUEmulator.sh    // If using Mac
$> CPUEmulator.bat   // If using Windows 
```

This should open the emulator.  Now, following the [instructions provided here](http://www.nand2tetris.org/tutorials/PDF/CPU%20Emulator%20Tutorial.pdf), you can run your program!


## License 

The project herein is part of the Nand to Tetris platform, which is licensed under the [Creative Common Attribution-NonCommercial-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-nc-sa/3.0/)

Each project in this repository is original work with the exclusion of the tests. 


## Virtual Machine API 

For those truly curious, the specification for my Virtual Machine implementation is described in [part 1](http://www.nand2tetris.org/lectures/PDF/lecture%2007%20virtual%20machine%20I.pdf) and [part 2](http://www.nand2tetris.org/lectures/PDF/lecture%2007%20virtual%20machine%20I.pdf) of the Nand to Tetris Virtual Machine project.

With just this information, one could theoretically create their own programming language for compilation on top of this virtual machine architecture, and run programs written in this newly created language on the "Hack Computer" as specified in the chipset in this project/repository.  The software for converting the virtual machine code to machine language has been written and provided in this repository.

## Acknowledgements 

Thanks a ton to Shimon Schocken and Noam Nisan, who created this course for the rest of us to learn computing systems from the ground up.  Such a learning experience could not have been made possible without an immense amount of time and effort put towards the creation of the accompanying tools and software.


