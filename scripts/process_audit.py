
import json
# import datetime
from glob import glob
import traceback


def parse_files():
    files = glob("*/report.json")
    data = []
    for file in files:
        try:
            audit = json.load(open(file))
            item = {
                'report': {
                    'date': audit.get('fetchTime'),
                    'url': f"./{file.replace('.json', '.html')}"
                },
                'site': audit.get('finalUrl'),
                'performance': int((audit['categories']['performance']['score'] or 0) * 100),
                'modelComplianceInformation': int((audit['categories']['modelComplianceInformation']['score'] or 0) * 100),
                'reccomandationsAndAdditionalTests': int((audit['categories']['reccomandationsAndAdditionalTests']['score'] or 0) * 100),
                'additionalTests': int((audit['categories']['additionalTests']['score'] or 0) * 100)
            }
            data.append(item)
        except:
            # print(f"Error parsing {file}")
            # print(traceback.format_exc())
            pass
    return data

data = parse_files()
print(json.dumps(data, indent=2))
