import argparse


def parser() -> argparse.ArgumentParser:
    root_parser = argparse.ArgumentParser(
        prog="lvcli",
        description="LabVIEW application with command line interface",
        )
    root_subparsers = root_parser.add_subparsers(
        title="commands",
        description="list of available commands",
        dest="root_cmd"
    )
    root_subparsers.add_parser(
        name="ping",
        help="ping LabVIEW application"
    )
    root_subparsers.add_parser(
        name="shutdown",
        help="shutdown LabVIEW application"
    )
    gui_parser = root_subparsers.add_parser(
        name="gui",
        help="graphical user interface commands"
    )
    gui_subparsers = gui_parser.add_subparsers(
        title="commands",
        description="list of available GUI commands",
        dest="gui_cmd"
    )
    gui_subparsers.add_parser(
        name="hide",
        help="hide GUI"
    )
    gui_subparsers.add_parser(
        name="show",
        help="show GUI"
    )
    return root_parser
