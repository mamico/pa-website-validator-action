
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
            if "categories" in audit:
                # old validator
                item = {
                    'report': {
                        'date': audit['fetchTime'],
                        'url': f"./{file.replace('.json', '.html')}"
                    },
                    'site': audit.get('finalUrl'),
                    'performance': int((audit['categories']['performance']['score'] or 0) * 100),
                    'modelComplianceInformation': int((audit['categories']['modelComplianceInformation']['score'] or 0) * 100),
                    'reccomandationsAndAdditionalTests': int((audit['categories']['reccomandationsAndAdditionalTests']['score'] or 0) * 100),
                    'additionalTests': int((audit['categories']['additionalTests']['score'] or 0) * 100)
                }
            else:
                modelComplianceInformation = 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-ux-ui-consistency-bootstrap-italia-double-check"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-legislation-cookie-domain-check"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-domain"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-legislation-accessibility-declaration-is-present"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-feedback-element"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-ux-ui-consistency-fonts-check"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-faq-is-present"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-controlled-vocabularies"]["score"]>= 0.5 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-performance-improvement-plan"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-inefficiency-report"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-booking-appointment-check"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-license-and-attribution"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-legislation-privacy-is-present"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-security"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-contacts-assistency"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-servizi-structure-match-model"]["score"]>= 0.5 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-ux-ui-consistency-theme-version-check"]["score"]>= 0.5 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-menu-structure-match-model"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-user-experience-evaluation"]["score"]>= 0.5 else 0
                modelComplianceInformation += 1 if audit["audits"]["common-security-ip-location"]["score"]== 1 else 0
                modelComplianceInformation += 1 if audit["audits"]["municipality-second-level-pages"]["score"]>= 0.5 else 0

                modelComplianceInformation = int(modelComplianceInformation * 100.0 / 21.0)

                reccomandationsAndAdditionalTests = 0
                reccomandationsAndAdditionalTests += 1 if audit["audits"]["municipality-metatag"]["score"]== 1 else 0
                reccomandationsAndAdditionalTests += 1 if audit["audits"]["municipality-informative-cloud-infrastructure"]["score"]== 1 else 0
                reccomandationsAndAdditionalTests += 1 if audit["audits"]["municipality-informative-reuse"]["score"]== 1 else 0

                reccomandationsAndAdditionalTests = int(reccomandationsAndAdditionalTests * 100.0 / 3.0)

                #  ('municipality-ux-ui-consistency-bootstrap-italia-double-check', 'C.SI.1.2'),
                #  ('municipality-legislation-cookie-domain-check', 'C.SI.3.1'),
                #  ('municipality-domain', 'C.SI.5.2'),
                #  ('municipality-legislation-accessibility-declaration-is-present', 'C.SI.3.2'),
                #  ('municipality-feedback-element', 'C.SI.2.5'),
                #  ('municipality-ux-ui-consistency-fonts-check', 'C.SI.1.1'),
                #  ('municipality-faq-is-present', 'C.SI.2.3'),
                #  ('municipality-controlled-vocabularies', 'C.SI.1.5'),
                #  ('municipality-performance-improvement-plan', ''),
                #  ('municipality-inefficiency-report', 'C.SI.2.4'),
                #  ('municipality-booking-appointment-check', 'C.SI.2.1'),
                #  ('municipality-license-and-attribution', 'C.SI.3.4'),
                #  ('municipality-legislation-privacy-is-present', 'C.SI.3.3'),
                #  ('municipality-security', 'C.SI.5.1'),
                #  ('municipality-contacts-assistency', 'C.SI.2.2'),
                #  ('municipality-metatag', 'R.SI.1.1'),
                #  ('municipality-servizi-structure-match-model', 'C.SI.1.3'),
                #  ('municipality-ux-ui-consistency-theme-version-check', 'C.SI.1.4'),
                #  ('municipality-informative-cloud-infrastructure', 'R.SI.2.1'),
                #  ('municipality-informative-reuse', 'R.SI.2.2'),
                #  ('municipality-menu-structure-match-model', 'C.SI.1.6'),
                #  ('municipality-user-experience-evaluation', 'C.SI.2.6'),
                #  ('common-security-ip-location', 'Localizzazione IP'),
                #  ('municipality-second-level-pages', 'C.SI.1.7')]

                item = {
                    'report': {
                        'date': audit['fetchTime'],
                        'url': f"./{file.replace('.json', '.html')}"
                    },
                    'site': audit.get('finalUrl'),
                    'performance': int((audit["audits"]["lighthouse"]["score"] or 0) * 100),
                    'modelComplianceInformation': modelComplianceInformation,
                    'reccomandationsAndAdditionalTests': reccomandationsAndAdditionalTests,
                    'additionalTests': 0,
                }
            data.append(item)
        except:
            # print(f"Error parsing {file}")
            # print(traceback.format_exc())
            pass
    return data

data = parse_files()
print(json.dumps(data, indent=2))
