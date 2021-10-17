from contracts.documents import AddressParser
from os import listdir
import json
import sys



archive_dir = sys.argv[1]
ai_creds_path = sys.argv[2]
try:
    save_to = sys.argv[3]
except IndexError:
    save_to = None
output_json = {}
for folder in listdir(archive_dir):
    parser = AddressParser(f'{archive_dir}/{folder}/', format_='docx', ai_project_path=ai_creds_path)
    contracts = parser.get_contract_docs()


    for contract in contracts:
        print(contract)
        parser = AddressParser(format_='docx', ai_project_path=ai_creds_path)
        service_place = parser.extract_place_of_service(contract)
        if service_place and service_place.get('city'):
            output_json.update({
                folder: service_place.get('city').string_value
            })

if save_to:
    with open(save_to, 'w', encoding='utf-8') as f:
        f.write(json.dumps(output_json, indent=3, ensure_ascii=False))
print(
    json.dumps(output_json, indent=3, ensure_ascii=False)
)

print('Done')
