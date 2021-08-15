#!/usr/bin/env python3

import os
import subprocess

def choose_window(halign: str = "center",
                  valign: str = "center",
                  font: str = "'Droid Sans':100",
                  bgcolor: str = "rgba(50, 50, 50, 0.7)",
                  textcolor: str = "rgba(255, 255, 255, 1)",
                  chars: str = "wertdf") -> int:
    
    path = os.path.expanduser("~/.cargo/bin/wmfocus")

    winid = subprocess.check_output([path,
                                     "--print-only",
                                     "--halign", str(halign),
                                     "--valign", str(valign),
                                     "--font", str(font),
                                     "--bgcolor", str(bgcolor),
                                     "--textcolor", str(textcolor),
                                     "--chars", str(chars),
                                     "--fill",
                                     "--exit-keys", "Control_L+g"
                                     ])
    return int(winid, 16)
