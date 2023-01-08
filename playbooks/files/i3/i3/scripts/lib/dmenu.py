#!/usr/bin/env python3

"""
Module wrapper for dmenu
"""

import subprocess

class Dmenu:
    @staticmethod
    def show_values(values: list, dmenu_cmd: str = "dmenu") -> str:
        """
        Call dmenu with values.
        """
        cmd = subprocess.Popen(dmenu_cmd,
                               shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stdout, _ = cmd.communicate("\n".join(values).encode("utf-8"))

        return stdout.decode("utf-8").strip("\n")
