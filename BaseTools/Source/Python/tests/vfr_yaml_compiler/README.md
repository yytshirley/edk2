# Unit testing of vfrcompiler


## Test points
- Unit testing and system testing are implemented in the test_Vfrcompiler.py test file.

    Each test case in the testing class is independent and all test cases are executed 
    sequentially, achieving system testing.
- The parsing test of G4 file syntax in VfrCompiler has been implemented in file test_vfr_syntax.py.

## Pytest
- install: pip install pytest

## Run test
- cd edk2\BaseTools\Source\Python\tests
- Execute the following command on the terminal
> pytest vfr_yaml_compiler