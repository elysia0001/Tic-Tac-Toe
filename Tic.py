print("井字棋")
lis = [" ", " ", "O", " ", " ", "O", " ", " ", "O"]
def draw(lst):
    for i in range(3):
        print(lis[i*3], "|", lis[i * 3 + 1],"|" , lis[i * 3 + 2])
        print("- - - - - ")
      
print (draw(lis))

def check_winner(lis):
    winner_status = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [2,5,8],
        [0,3,6],
        [1,4,7],
        [0,4,8],
        [2,4,6],
    ]
    for m in range(len(winner_status)):
        if lis[winner_status[m][0]] != " " and lis[winner_status[m][0]] == lis[winner_status[m][1]] and lis[winner_status[m][1]] == lis[winner_status[m][1]]:
            return lis[winner_status[m][0]]
    return 0 
        
print(check_winner(lis))
# def main():
#     count = 0 
#     while True:
