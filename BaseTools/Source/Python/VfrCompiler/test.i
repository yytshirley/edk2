#line 1 "e:\\code\\client\\lunarlake\\Intel\\Features\\BluetoothPkg\\BluetoothConnectionManagerDxe\\BluetoothConnectionManager.vfr"
#line 1 "e:\\code\\client\\lunarlake\\Build\\LunarLakeBoardPkg\\DEBUG_VS2017\\X64\\BluetoothPkg\\BluetoothConnectionManagerDxe\\BluetoothConnectionManagerDxe\\DEBUG\\BluetoothConfigDxeStrDefs.h"





























































extern unsigned char BluetoothConfigDxeStrings[];





























#line 93 "e:\\code\\client\\lunarlake\\Build\\LunarLakeBoardPkg\\DEBUG_VS2017\\X64\\BluetoothPkg\\BluetoothConnectionManagerDxe\\BluetoothConnectionManagerDxe\\DEBUG\\BluetoothConfigDxeStrDefs.h"

#line 95 "e:\\code\\client\\lunarlake\\Build\\LunarLakeBoardPkg\\DEBUG_VS2017\\X64\\BluetoothPkg\\BluetoothConnectionManagerDxe\\BluetoothConnectionManagerDxe\\DEBUG\\BluetoothConfigDxeStrDefs.h"
#line 1 "e:\\code\\client\\lunarlake\\Intel\\Features\\BluetoothPkg\\BluetoothConnectionManagerDxe\\BluetoothConnectionManager.vfr"




















#line 1 "e:\\code\\client\\lunarlake\\intel\\features\\bluetoothpkg\\bluetoothconnectionmanagerdxe\\BluetoothConnectionManagerHii.h"






























#line 32 "e:\\code\\client\\lunarlake\\intel\\features\\bluetoothpkg\\bluetoothconnectionmanagerdxe\\BluetoothConnectionManagerHii.h"

#line 22 "e:\\code\\client\\lunarlake\\Intel\\Features\\BluetoothPkg\\BluetoothConnectionManagerDxe\\BluetoothConnectionManager.vfr"
#line 1 "e:\\code\\client\\lunarlake\\intel\\features\\bluetoothpkg\\bluetoothconnectionmanagerdxe\\BluetoothConnectionManagerVfr.h"









































































#line 75 "e:\\code\\client\\lunarlake\\intel\\features\\bluetoothpkg\\bluetoothconnectionmanagerdxe\\BluetoothConnectionManagerVfr.h"

#line 23 "e:\\code\\client\\lunarlake\\Intel\\Features\\BluetoothPkg\\BluetoothConnectionManagerDxe\\BluetoothConnectionManager.vfr"

formset
  guid     = { 0x4f4ef7f0, 0xaa29, 0x4ce9, { 0xba, 0x41, 0x64, 0x3e, 0x1, 0x23, 0xa9, 0x9f }},
  title    = STRING_TOKEN(0x0002),
  help     = STRING_TOKEN(0x0003),

  
  
  
  form formid = 0x0002,
       title  = STRING_TOKEN(0x0005);

    text
      help   = STRING_TOKEN(0x0006),
      text   = STRING_TOKEN(0x0007),
        text   = STRING_TOKEN(0x0008);

    string
              questionid = 0x6002,
              prompt   = STRING_TOKEN(0x000A),
              help     = STRING_TOKEN(0x0009),
              flags    = INTERACTIVE,
              minsize  = 2,
              maxsize  = 19,
    endstring;

    subtitle text = STRING_TOKEN(0x0004);

    goto 0x0003,
      prompt = STRING_TOKEN(0x0010),
      help   = STRING_TOKEN(0x0011),
      flags   = INTERACTIVE,
      key     = 0x6001;
  endform;


  
  
  
  form formid = 0x0003,
       title  = STRING_TOKEN(0x0012);

    label 0x1500;
    label 0x15FF;

    subtitle text = STRING_TOKEN(0x0004);

    subtitle text = STRING_TOKEN(0x0013);

    label 0x1200;
    label 0x12FF;

    
    
    
    action
             questionid = 0x6003,
             prompt   = STRING_TOKEN(0x0004),
             help     = STRING_TOKEN(0x0004),
             flags    = INTERACTIVE,
             config   = STRING_TOKEN(0x0004),
             refreshguid = { 0xF5E655D9, 0x02A6, 0x46f2, {0x9E, 0x76, 0xB8, 0xBE, 0x8E, 0x60, 0xAB, 0x22} },
    endaction;

    subtitle text = STRING_TOKEN(0x0014);

    label 0x1300;
    label 0x13FF;

  endform;

  
  
  
  form formid = 0x0004,
       title  = STRING_TOKEN(0x001C);

  grayoutif TRUE;

    text
      help   = STRING_TOKEN(0x0009),
      text   = STRING_TOKEN(0x000A),
        text   = STRING_TOKEN(0x000B);

    text
      help   = STRING_TOKEN(0x0006),
      text   = STRING_TOKEN(0x0007),
        text   = STRING_TOKEN(0x000F);

    text
      help   = STRING_TOKEN(0x000C),
      text   = STRING_TOKEN(0x000D),
        text   = STRING_TOKEN(0x000E);

    subtitle text = STRING_TOKEN(0x0004);

    text
      help   = STRING_TOKEN(0x001E),
      text   = STRING_TOKEN(0x001D);

    label 0x1400;
    label 0x14FF;

  endif;

  endform;

endformset;

