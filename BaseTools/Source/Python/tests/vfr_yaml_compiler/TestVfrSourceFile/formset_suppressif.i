typedef struct {
  UINT8   FakeItem;
} FAKE_VARSTORE;


formset
  guid     = { 0x4b47d616, 0xa8d6, 0x4552, { 0x9d, 0x44, 0xcc, 0xad, 0x2e, 0xf, 0x4c, 0xf9 } },
  title    = STRING_TOKEN(0x0002),
  help     = STRING_TOKEN(0x0003),

  suppressif TRUE;
    oneof varid     = FAKE_VARSTORE.FakeItem,
        prompt      = STRING_TOKEN(0x01A0),
        help        = STRING_TOKEN(0x01A1),
        option text = STRING_TOKEN(0x0236), value = 0, flags = RESET_REQUIRED ;
        option text = STRING_TOKEN(0x0236),  value = 1, flags = RESET_REQUIRED;
    endoneof;
  endif;
endformset;