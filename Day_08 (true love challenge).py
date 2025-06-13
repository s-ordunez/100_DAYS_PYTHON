def calculate_love_score(name_1, name_2):
    
    true_score = 0
    love_score = 0
    
    true = ['t', 'r', 'u', 'e']
    love =  ['l', 'o', 'v', 'e']
    
    for x in true:
        true_score += name_1.count(x)
        true_score += name_2.count(x)
        
    for x in love:
        love_score += name_1.count(x)
        love_score += name_2.count(x)

    true_love_score = str(true_score) + str(love_score)
    
    print(true_love_score)

calculate_love_score("Kanye West", "Kim Kardashian")
