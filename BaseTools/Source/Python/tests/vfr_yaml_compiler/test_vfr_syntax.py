## @file
# Test the parser rules for the Python version of Vfr generated through Antlr4.
#

import pytest
import sys
import os
from antlr4 import *

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from VfrCompiler.IfrTree import IfrTreeNode
from VfrCompiler.IfrPreProcess import PreProcessDB
from VfrCompiler.VfrSyntaxParser import VfrSyntaxParser
from VfrCompiler.VfrSyntaxVisitor import VfrSyntaxVisitor
from VfrCompiler.VfrSyntaxLexer import VfrSyntaxLexer
from VfrCompiler.IfrPreProcess import Options

from VfrCompiler.IfrFormPkg import (
    gFormPkg,
    gVfrVarDataTypeDB,
    gVfrDefaultStore,
    gVfrDataStorage,
    gIfrFormId,
)


class TestVfrcompilFunc:
    def setup_class(self):
        # self.Cmd = CmdParser()
        self.Options = Options()
        self.VfrRoot = IfrTreeNode()
        self.PreProcessDB = PreProcessDB(self.Options)

    def test_VfrDataStructDefinition(self):
        """
        Test Struct Definition
        """
        structInput = [
            'VfrFuncSrc/struct.i',
        ]
        exceptOutput = [
            {
                "structName": 'VLAN_CONFIGURATION',
                "elementNode": [
                    ['UINT16', 'VlanId'],
                    ['UINT8', 'Priority'],
                    ['UINT8', 'VlanList']
                ]
            },
        ]
        for index in range(len(structInput)):
            InputStream = FileStream(structInput[index])
            VfrLexer = VfrSyntaxLexer(InputStream)
            VfrStream = CommonTokenStream(VfrLexer)
            VfrParser = VfrSyntaxParser(VfrStream)
            self.Visitor = VfrSyntaxVisitor(
                self.PreProcessDB, self.VfrRoot, self.Options.OverrideClassGuid
            )
            self.Visitor.visit(VfrParser.vfrDataStructDefinition())
            DataTypeList = gVfrVarDataTypeDB.DataTypeList
            exp = exceptOutput[index]
            assert exp['structName'] == DataTypeList.TypeName

            i = 0
            element = DataTypeList.Members
            while element:
                assert exp['elementNode'][i][1] == element.FieldName
                assert exp['elementNode'][i][0] == element.FieldType.TypeName
                element = element.Next
                i += 1

    def test_VfrDataUnionDefinition(self):
        pass

    def test_VfrFormSetDefinition(self):
        """
        Test formset format.
        """
        formsetList = [
            'VfrFuncSrc/formset.i',
        ]
        exceptOutput = [
            """
                0E A7 16 D6 47 4B D6 A8 52 45 9D 44 CC AD 2E 0F 4C F9 02 00 03 00 01 71 99 03 93 45 85 04 4B B4 5E 32 EB 83 26 04 0E 
                5C 06 00 00 00 00 
                5C 06 00 00 01 00 
                24 2E 16 D6 47 4B D6 A8 52 45 9D 44 CC AD 2E 0F 4C F9 66 66 3C 45 49 53 43 53 49 5F 43 4F 4E 46 49 47 5F 49 46 52 5F 4E 56 44 41 54 41 00 
                01 86 01 00 04 00 
                1C 90 06 00 07 00 01 01 66 66 00 00 04 04 DF 00 
                29 02 
                02 87 3A 00 00 00 00 
                29 02 
                0F 0F 0E 00 0E 00 0E 01 00 00 FF FF 04 02 00 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 00 90 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 FF FF 
                02 87 3A 00 00 00 00 
                29 02 
                0F 0F 10 00 11 00 16 01 00 00 FF FF 04 05 00 
                02 87 3A 00 00 00 00 
                29 02 
                0F 0F 12 00 12 00 10 01 00 00 FF FF 04 04 00 
                02 87 3A 00 00 00 00 
                29 02 
                29 02 
                01 86 02 00 05 00 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 00 30 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 FF FF 
                29 02 
                01 86 04 00 12 00 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 00 40 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 FF FF 
                0C 8F 3B 00 3B 00 11 01 00 00 FF FF 04 00 00 
                29 02 
                0C 8F 3C 00 3C 00 12 01 00 00 FF FF 04 00 00 
                29 02 
                29 02 
                01 86 05 00 10 00 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 00 50 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 FF FF 
                0C 8F 3B 00 3B 00 14 01 00 00 FF FF 04 00 00 
                29 02 
                0C 8F 3C 00 3C 00 15 01 00 00 FF FF 04 00 00 
                29 02 
                29 02 
                01 86 03 00 0F 00 
                1C 90 08 00 09 00 01 00 66 66 C0 01 01 00 0C 00 
                29 02 
                02 87 3A 00 00 00 00 
                29 02 
                05 91 13 00 14 00 02 00 66 66 D8 01 00 10 00 02 00 
                09 07 15 00 10 00 00 
                09 07 16 00 00 00 01 
                09 07 17 00 00 00 02 
                29 02 
                02 87 3A 00 00 00 00 
                29 02 
                05 91 18 00 19 00 1C 01 66 66 D9 01 04 10 00 02 00 
                09 07 1A 00 00 00 00 
                09 07 1B 00 00 00 01 
                09 07 1C 00 00 00 02 
                29 02 
                02 87 3A 00 00 00 00 
                29 02 
                07 91 0A 00 0B 00 03 00 66 66 DA 01 00 10 00 10 00 
                29 02 
                07 94 0C 00 0D 00 04 00 66 66 DC 01 00 11 64 00 20 4E 00 00 
                5B 07 00 00 01 E8 03 
                29 02 
                02 87 3A 00 00 00 00 
                29 02 
                1C 90 3D 00 3E 00 1E 01 66 66 3A 0B 04 06 0C 00 
                29 02 
                02 87 3A 00 00 00 00 
                29 02 
                0A 82 
                12 06 1C 01 02 00 
                06 8E 2C 00 2C 00 02 01 66 66 DE 01 04 00 
                29 02 
                29 02 
                0A 82 
                12 86 1C 01 01 00 
                12 06 1C 01 02 00 
                16 02 
                29 02 
                19 82 
                12 06 02 01 01 00 
                1C 90 21 00 24 00 03 01 66 66 E0 01 04 07 0F 00 
                29 02 
                1C 90 22 00 24 00 04 01 66 66 00 02 04 07 0F 00 
                29 02 
                1C 90 23 00 24 00 05 01 66 66 20 02 04 07 0F 00 
                29 02 
                29 02 
                29 02 
                0A 82 
                12 06 1C 01 02 00 
                02 87 3A 00 00 00 00 
                29 02 
                29 02 
                0A 82 
                12 86 1C 01 02 00 
                12 06 02 01 00 00 
                16 02 
                29 02 
                06 8E 2D 00 2D 00 05 00 66 66 DF 01 00 00 
                29 02 
                29 02 
                0A 82 
                12 86 1C 01 02 00 
                12 06 05 00 01 00 
                16 02 
                29 02 
                1C 90 25 00 26 00 0C 01 66 66 40 02 04 04 DF 00 
                29 02 
                1C 90 27 00 28 00 06 01 66 66 00 04 04 00 FF 00 
                29 02 
                07 94 29 00 29 00 06 00 66 66 FE 05 00 11 00 00 FF FF 00 00 
                29 02 
                1C 90 2A 00 2B 00 0D 01 66 66 00 06 04 01 14 00 
                29 02 
                29 02 
                0A 82 
                12 06 1C 01 02 00 
                02 87 3A 00 00 00 00 
                29 02 
                29 02 
                05 91 1D 00 1E 00 1D 01 66 66 2A 06 00 10 00 01 00 
                09 07 1F 00 00 00 01 
                09 07 20 00 10 00 00 
                29 02 
                0A 82 
                12 86 1D 01 01 00 
                17 02 
                29 02 
                05 91 2E 00 2F 00 07 00 66 66 2B 06 00 10 00 01 00 
                09 07 30 00 00 00 00 
                09 07 31 00 10 00 01 
                29 02 
                29 02 
                0A 82 
                12 86 1D 01 01 00 
                17 02 
                29 02 
                1C 90 32 00 32 00 07 01 66 66 2C 06 04 00 7E 00 
                29 02 
                1C 90 33 00 34 00 08 01 66 66 2A 07 04 0C 10 00 
                29 02 
                29 02 
                0A 82 
                12 86 1D 01 01 00 
                17 02 
                12 06 07 00 01 00 
                17 02 
                16 02 
                29 02 
                1C 90 35 00 35 00 09 01 66 66 4C 07 04 00 7E 00 
                29 02 
                1C 90 36 00 34 00 0A 01 66 66 4A 08 04 0C 10 00 
                29 02 
                29 02 
                0A 82 
                46 02 
                1C 90 3F 00 3F 00 08 00 66 66 54 0B 00 00 60 00 
                29 02 
                1C 90 43 00 43 00 09 00 66 66 14 0C 00 00 60 00 
                29 02 
                1C 90 40 00 40 00 0A 00 66 66 D4 0C 00 00 60 00 
                29 02 
                1C 90 41 00 41 00 0B 00 66 66 94 0D 00 00 60 00 
                29 02 
                1C 90 42 00 42 00 0C 00 66 66 54 0E 01 00 60 00 
                29 02 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 00 60 
                5F 15 35 17 0B 0F A0 87 93 41 B2 66 53 8C 38 AF 48 CE 00 FF FF 
                29 02 
                02 87 3A 00 00 00 00 
                29 02 
                0C 8F 38 00 39 00 0F 01 00 00 FF FF 04 00 00 
                29 02 
                0F 0F 37 00 37 00 0D 00 00 00 FF FF 00 01 00 
                29 02 
                29 02 
            """,
        ]
        for index in range(len(formsetList)):
            InputStream = FileStream(formsetList[index])
            VfrLexer = VfrSyntaxLexer(InputStream)
            VfrStream = CommonTokenStream(VfrLexer)
            VfrParser = VfrSyntaxParser(VfrStream)
            self.Visitor = VfrSyntaxVisitor(
                self.PreProcessDB, self.VfrRoot, self.Options.OverrideClassGuid
            )
            self.Visitor.visit(VfrParser.vfrProgram())
            formSetObj = self.Visitor.Root.Child[0]
            ExceptSrc = [i.strip() for i in exceptOutput[index].split('\n') if
                         i.strip()]
            Buffer = list()
            Buffer.append(formSetObj.Buffer)
            for ch in formSetObj.Child:
                if ch.Buffer != None:
                    Buffer.append(ch.Buffer)
                    for sc in ch.Child:
                        if sc.Buffer != None:
                            Buffer.append(sc.Buffer)
                            for c in sc.Child:
                                if c.Buffer != None:
                                    Buffer.append(c.Buffer)
            for i in range(len(Buffer)):
                for j in range(len(Buffer[i])):
                    print('i: ', i, j)
                    exp = Buffer[i][j]
                    src = int([s for s in ExceptSrc[i].split(' ') if s][j], 16)
                    assert Buffer[i][j] == int(ExceptSrc[i].split(' ')[j], 16)

    def test_VfrPragmaPackDefinition(self):
        pass

    def test_PragmaPackShowDef(self):
        pass


if __name__ == '__main__':
    pytest.main(['-v', 'test_vfr_syntax.py'])
