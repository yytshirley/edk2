# Unit testing of vfrcompiler

## Project Repo link
[edk2](https://github.com/yytshirley/edk2.git)

## Environmental 
- clone edk2 repo
- Checkout branch to Phase1PyVfrCompile
- run build

## Pytest
- install: pip install pytest

## Run test
- cd edk2\BaseTools\Source\Python\tests
- open pytest.ing and Modify the parameters that need to be used
```
python_files =
    # test_split.py
    test_Vfrcompiler.py

    # Before performing yaml testing, please perform vfr testing first,
    # as yaml testing depends on the output file after vfr testing
    #test_YamlCompiler.py

This parameter selects the test file.
```

- run pytest in cmd