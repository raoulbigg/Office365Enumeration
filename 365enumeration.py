
import argparse
import sys
import requests

emails = []
valid_emails = []



def parse_args():
    parser = argparse.ArgumentParser(description="This script uses the autodiscover json API of office365 to enumerate "
                                                 "valid o365 email accounts. This does not require any login attempts "
                                                 "unlike other enumeration methods and therefore is very stealthy.")
    parser.add_argument("file", type=argparse.FileType('r'), help="Input file containing one email per line")

    return parser.parse_args()


def check_api():
    user_agent = 'Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.12026; Pro)'
    headers = {'User-Agent': user_agent, 'Accept': 'application/json'}
    for email in emails:
        r = requests.get("https://outlook.office365.com/autodiscover/autodiscover.json/v1.0/{}?Protocol=rest".format(email.strip()), headers=headers, verify=False, allow_redirects=False, proxies=False)
        if r.status_code == 200:
            valid_emails.append(email.strip())
        else:
            pass

if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings()
    args = parse_args()
    with args.file as emailFile:
        for line in emailFile:
            emails.append(line)
    check_api()
    print("Existing Office365 emails: \n")
    print(*valid_emails, sep="\n")

            
