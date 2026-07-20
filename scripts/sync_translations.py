#!/usr/bin/env python3
"""
Detect outdated or missing translations compared to the English version.

This script compares modification times between English documentation files
and their translated counterparts to identify which translations are missing
or need updating. Supports any language folder present at the repo root
(e.g. vi/, zh/, ja/, uk/).

Usage:
    python scripts/sync_translations.py                  # defaults to vi
    python scripts/sync_translations.py --lang zh
    python scripts/sync_translations.py --lang zh --verbose
    python scripts/sync_translations.py --all-langs       # check every known language dir
"""

import argparse
from datetime import datetime
from pathlib import Path

# Language directories that may exist at the repo root. Used by --all-langs
# to discover which ones are actually present without hardcoding elsewhere.
KNOWN_LANGS = ["vi", "zh", "ja", "uk"]


def check_translation_status(
    lang: str, root_path: Path | None = None, verbose: bool = False
) -> tuple[list[dict], list[dict]]:
    """
    Compare modification times between English and translated files.

    Args:
        lang: Language directory name to check (e.g. "vi", "zh", "ja", "uk")
        root_path: Root directory of the repository (default: script parent parent)
        verbose: Print detailed information

    Returns:
        Tuple of (outdated files, not-translated files), each a list of metadata dicts.
    """
    if root_path is None:
        root_path = Path(__file__).parent.parent

    lang_dir_marker = f"{lang}/"

    # Get all English markdown files, excluding every known language directory
    # (not just the one being checked) so cross-language files never leak in.
    excluded_markers = [f"{code}/" for code in KNOWN_LANGS]
    en_files = [
        f
        for f in root_path.rglob("*.md")
        if not any(marker in str(f.relative_to(root_path)) for marker in excluded_markers)
    ]

    # Get all translated markdown files for the target language
    lang_dir = root_path / lang
    lang_files = list(lang_dir.rglob("*.md")) if lang_dir.exists() else []

    # Build modification time mapping
    en_mtime = {f: f.stat().st_mtime for f in en_files}
    lang_mtime = {f: f.stat().st_mtime for f in lang_files}

    outdated = []
    not_translated = []

    for en_file, en_time in sorted(en_mtime.items()):
        try:
            rel_path = en_file.relative_to(root_path)
        except ValueError:
            if verbose:
                print(f"Skipping non-relative file: {en_file}")
            continue

        translated_file = root_path / lang / rel_path

        if translated_file in lang_mtime:
            translated_time = lang_mtime[translated_file]
            if en_time > translated_time:
                outdated.append(
                    {
                        "file": rel_path,
                        "en_mtime": datetime.fromtimestamp(en_time),
                        "translated_mtime": datetime.fromtimestamp(translated_time),
                        "days_diff": (en_time - translated_time) / 86400,
                    }
                )
        else:
            not_translated.append(
                {
                    "file": rel_path,
                    "status": "NOT_TRANSLATED",
                }
            )

    outdated.sort(key=lambda x: x["days_diff"], reverse=True)

    return outdated, not_translated


def format_outdated_table(outdated: list[dict], lang: str) -> str:
    """Format outdated files as a Markdown table."""
    if not outdated:
        return "**No outdated translations found!** All files are up to date.\n"

    table = f"### Outdated Translations ({lang}) - Need Update\n\n"
    table += f"| File | Last EN Update | Last {lang.upper()} Update | Days Behind |\n"
    table += "|------|----------------|-----------------|-------------|\n"

    for item in outdated:
        file_path = str(item["file"])
        en_date = item["en_mtime"].strftime("%Y-%m-%d")
        translated_date = item["translated_mtime"].strftime("%Y-%m-%d")
        days = int(item["days_diff"])

        if len(file_path) > 50:
            file_path = "..." + file_path[-47:]

        table += f"| `{file_path}` | {en_date} | {translated_date} | **{days} days** |\n"

    return table


def format_not_translated_table(not_translated: list[dict], lang: str) -> str:
    """Format not translated files as a Markdown table."""
    if not not_translated:
        return f"\n**All files have been translated into {lang}!**\n"

    table = f"\n### Not Translated Yet ({lang})\n\n"
    table += "| File | Status |\n"
    table += "|------|--------|\n"

    for item in not_translated:
        file_path = str(item["file"])

        if len(file_path) > 60:
            file_path = "..." + file_path[-57:]

        table += f"| `{file_path}` | **Not translated** |\n"

    return table


def format_summary(outdated: list[dict], not_translated: list[dict], lang: str) -> str:
    """Format summary statistics."""
    total_outdated = len(outdated)
    total_not_translated = len(not_translated)
    total_files = total_outdated + total_not_translated

    summary = f"## Summary ({lang})\n\n"
    summary += f"- **Total files needing attention:** {total_files}\n"
    summary += f"- **Outdated translations:** {total_outdated}\n"
    summary += f"- **Not translated yet:** {total_not_translated}\n"

    if total_outdated > 0:
        most_outdated = max(outdated, key=lambda x: x["days_diff"])
        summary += f"- **Most outdated file:** {most_outdated['file']} ({int(most_outdated['days_diff'])} days behind)\n"

    summary += "\n---\n\n"

    return summary


def run_for_lang(lang: str, root_path: Path, verbose: bool) -> tuple[list[dict], list[dict]]:
    """Run the check for a single language and print its report."""
    if verbose:
        print(f"Checking '{lang}' translations in: {root_path}")
        print()

    outdated, not_translated = check_translation_status(lang, root_path, verbose)

    print("=" * 60)
    print(f"Translation Status Report: {lang}")
    print("=" * 60)
    print()

    total_outdated = len(outdated)
    total_not_translated = len(not_translated)

    if total_outdated == 0 and total_not_translated == 0:
        print(f"All '{lang}' files are up to date.")
        print()
        return outdated, not_translated

    print(f"Found {total_outdated} outdated + {total_not_translated} not translated files")
    print()

    if verbose and outdated:
        print("OUTDATED FILES (need update):")
        print("-" * 60)
        for i, item in enumerate(outdated, 1):
            print(f"{i}. {item['file']}")
            print(f"   EN: {item['en_mtime'].strftime('%Y-%m-%d %H:%M')}")
            print(f"   {lang.upper()}: {item['translated_mtime'].strftime('%Y-%m-%d %H:%M')}")
            print(f"   Behind by: {int(item['days_diff'])} days")
            print()

    if verbose and not_translated:
        print("NOT TRANSLATED FILES:")
        print("-" * 60)
        for i, item in enumerate(not_translated[:20], 1):
            print(f"{i}. {item['file']}")

        if len(not_translated) > 20:
            print(f"... and {len(not_translated) - 20} more files")
        print()

    print("=" * 60)
    print(f"Markdown Report ({lang})")
    print("=" * 60)
    print()

    report = format_summary(outdated, not_translated, lang)
    report += format_outdated_table(outdated, lang)
    report += format_not_translated_table(not_translated, lang)

    print(report)

    return outdated, not_translated


def main():
    parser = argparse.ArgumentParser(
        description="Check translation status against the English version"
    )
    parser.add_argument(
        "--lang",
        "-l",
        default="vi",
        help="Language directory to check (default: vi). Ignored if --all-langs is set.",
    )
    parser.add_argument(
        "--all-langs",
        action="store_true",
        help="Check every known language directory that exists in the repo (vi, zh, ja, uk).",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Print detailed information"
    )
    parser.add_argument(
        "--root",
        "-r",
        type=Path,
        default=None,
        help="Root directory of repository (default: auto-detect)",
    )

    args = parser.parse_args()

    root_path = args.root or Path(__file__).parent.parent

    if args.all_langs:
        langs = [lang for lang in KNOWN_LANGS if (root_path / lang).exists()]
    else:
        langs = [args.lang]

    for lang in langs:
        run_for_lang(lang, root_path, args.verbose)


if __name__ == "__main__":
    main()
