# rushi

import os
import subprocess
import click


def list_files():
    os.system("dir")


def list_files_subprocess():
    subprocess.run(["cmd", "/c", "dir"])


@click.command()
@click.argument("name")
def main(name):
    print(f"Hello {name}")
    list_files()
    list_files_subprocess()


if __name__ == "__main__":
    main()