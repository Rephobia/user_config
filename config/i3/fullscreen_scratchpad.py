from i3ipc import Connection, Con


if __name__ == "__main__":

    i3 = Connection()

    def _is_scratchpad(con: Con) -> bool:
        return con.window and con.parent.type != 'dockarea' and con.workspace().name == '__i3_scratch'

    for con in i3.get_tree():

        if _is_scratchpad(con):
            con.command("fullscreen")
            break

    i3.command("scratchpad show")
