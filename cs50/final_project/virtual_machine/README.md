# Virtual Machine Translator 

This Python program converts intermediate ".vm" language (as specified by the HACK computer in the Nand2Tetris course) to ".asm" assembly code (also specified by the HACK computer).

## Getting Started 

There are no dependencies other than a working version of Python.

To run the vm_translator: 

If individual file:

```
$> cd projectdirectory
$> python vm_translator/vm_translator.py tests/type_of_test/testfile.vm
```

If directory: 

```
$> cd projectdirectory 
$> python vm_translator/vm_translator.py tests/type_of_test/
```

## Tests 

To run the tests, first, download the VMemulator and CPUemulator from the [nand2tetris software page](http://www.nand2tetris.org/software.php)

See the [VM emulator instructions](http://www.nand2tetris.org/tutorials/PDF/VM%20Emulator%20Tutorial.pdf) and the [CPU emulator instructions](http://www.nand2tetris.org/tutorials/PDF/CPU%20Emulator%20Tutorial.pdf) to learn how to test your newly created .asm file

## License 

This project is licensed under the MIT License, and the Nand2Tetris suite is also under the MIT License 

