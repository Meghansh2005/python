
def find_mutual_friends(*friend_lists):
    if not friend_lists:
        return set()
    mutual_friends = set(friend_lists[0])
    for friends in friend_lists[1:]:
        mutual_friends &= set(friends)
    return mutual_friends

facebook_friends = ["Alice", "Bob", "Charlie"]
twitter_friends = ["Bob", "Charlie", "David"]
linkedin_friends = ["Bob", "Charlie", "Emma"]

mutual_friends = find_mutual_friends(facebook_friends, twitter_friends, linkedin_friends)
print("Mutual friends across all platforms:", mutual_friends)
