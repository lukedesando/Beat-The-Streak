from Players import Players
from pandas import DataFrame
import json

test = Players()

# test.matchups_to_csv(['W', 'L', 'earned_run_avg', 'whip', 'SO', 'opponent'])
print(test.get_pitcher_stats(39832))



# print("stats for Matt Harvey")
# print(test.matchups['Matt Harvey']['pitcher_stats']['W'],
# test.matchups['Matt Harvey']['pitcher_stats']['L'],
# test.matchups['Matt Harvey']['pitcher_stats']['earned_run_avg'],
# test.matchups['Matt Harvey']['pitcher_stats']['whip'],
# test.matchups['Matt Harvey']['pitcher_stats']['SO'],
# test.matchups['Matt Harvey']['opponent']
# )

# stats_we_want = ['W', 'L', 'earned_run_avg', 'whip', 'SO', 'opponent']
# out = []
# for key, value in test.matchups.items():
#     # print(key)
#     # print(value['pitcher_stats']['W'],
#     # value['pitcher_stats']['L'],
#     # value['pitcher_stats']['earned_run_avg'],
#     # value['pitcher_stats']['whip'],
#     # value['pitcher_stats']['SO'],
#     # value['opponent']
#     # )
#     item = {}
#     item['name'] = key
#     item['opponent'] = value['opponent']
#     item['date'] = value['date']
#     for p_key, p_stat in value['pitcher_stats'].items():
#         if (p_key in stats_we_want):
#             item[p_key] = p_stat
#     out.append(item)


# DataFrame(out).to_excel('pitcher_stats.xlsx')


