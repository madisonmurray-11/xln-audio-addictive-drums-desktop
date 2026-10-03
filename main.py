"""Xln Audio Addictive Drums Desktop — A local helper for Xln Audio Addictive Drums data folders, config and export files, and photo albums on Windows and macOS."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='xln_audio_addictive_drums_desktop',
        description='A local helper for Xln Audio Addictive Drums data folders, config and export files, and photo albums on Windows and macOS.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Xln Audio Addictive Drums Desktop')
    print('Keep the Xln Audio Addictive Drums data folder tidy before an update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
