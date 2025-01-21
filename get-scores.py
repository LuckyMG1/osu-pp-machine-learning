import requests, csv
from bs4 import BeautifulSoup

def get_players(max_page):
    with open("users2.txt", 'w') as users_file:
        prefix = "https://osu.ppy.sh/rankings/osu/performance"
        for i in range(1,max_page):
            url = prefix + f"?page={i}#scores"
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)
                matching_links = [link['href'] for link in links if link['href'].startswith("https://osu.ppy.sh/users/")]
                users_file.writelines("\n".join(matching_links) + "\n")
            else:
                print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

# get_players(10)

json_keys = ['max_combo','total_combo','statistics.great','statistics.ok','statistics.meh','statistics.miss','accuracy','beatmap.bpm','beatmap.difficulty_rating','beatmap.total_length','pp']
pattern = "/best?mode=osu&limit=100&offset=0"

with (open("users2.txt", 'r') as file, open("plays_input2.csv", 'w') as plays_file):
    writer = csv.writer(plays_file)
    writer.writerow(json_keys)
    for line in file:
        url = line.split('\n')[0] + pattern
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for play_dict in data:  # iterate over top 100 plays
                extracted_play_data = []
                for key in json_keys:
                    split_key = key.split('.')
                    if len(split_key) > 1:
                        extracted_play_data += [play_dict[split_key[0]].get(split_key[1],0)]
                    elif key == "total_combo":
                        total_combo = play_dict["maximum_statistics"].get("great",0)
                        total_combo += play_dict["maximum_statistics"].get("legacy_combo_increase",0)
                        extracted_play_data += [total_combo]
                    else:
                        extracted_play_data += [play_dict[key]]
                writer.writerow(extracted_play_data)
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
