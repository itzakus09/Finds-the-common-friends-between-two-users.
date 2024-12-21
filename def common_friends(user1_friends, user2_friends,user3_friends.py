def common_friends(user1_friends, user2_friends,user3_friends):
    set_user1 = set(user1_friends)
    set_user2 = set(user2_friends)
    set_user3 = set(user3_friends)
    common = set_user1.intersection(set_user2)
    common = common.intersection(set_user3)
    return common
if __name__ == "__main__":
    user1_friends = ['Abhishek', 'Aman', 'Rudra', 'Dhruv']
    user2_friends = ['Rudra', 'Abhishek', 'Virendra', 'Dhruv']
    user3_friends = ['Rudra', 'Abhishek', 'Virendra','Ram']
    
    common = common_friends(user1_friends, user2_friends, user3_friends)
    
    print("Common friends:", common)