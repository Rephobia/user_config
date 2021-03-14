#!/usr/bin/env python3

import os
import subprocess

def choose_window(halign: str = "center",
                  valign: str = "center",
                  font: str = "'Droid Sans':100",
                  bgcolor: str = "#204a87",
                  textcolor: str = "#eeeeec",
                  chars: str = "qweasd") -> int:
    
    path = os.path.expanduser("~/.cargo/bin/wmfocus")

    winid = subprocess.check_output([path,
                                     "--print-only",
                                     "--halign", str(halign),
                                     "--valign", str(valign),
                                     "--font", str(font),
                                     "--bgcolor", str(bgcolor),
                                     "--textcolor", str(textcolor),
                                     "--chars", str(chars),
                                     ])
    return int(winid, 16)
