import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
#HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    # 得到字母对应的次数的字典
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq





def get_word_score(word,n):

    word=word.lower()
    the_first_part=0
    the_second_part=0
    for i in word:
        the_first_part+=SCRABBLE_LETTER_VALUES[i]
    word_length=len(word)
    the_second_part=7*word_length - 3*(n-word_length)
    if the_second_part<1:
        the_second_part=1
    total_scores=the_first_part*the_second_part
    return total_scores


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
#生成hand
def deal_hand(n):

    hand={}
    num_vowels = int(math.ceil(n / 3))  #取不超过这个数的最大值
    # q=random.randint(0,num_vowels)
    for i in range(num_vowels):
        # if i==q:
        #     hand['*']=
        #
        x = random.choice(VOWELS)    #VOWELS是元音aeiou
        hand[x] = hand.get(x, 0) + 1    #统计次数
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand




#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):

    hand_copy=hand.copy()
    hand_keys=[]#找到在字典里的字符
    error=0
    for i in word:
        if i in hand_copy.keys():
            for t in range(hand_copy[i]):
                hand_keys.append(i)
    for key in word:
        if key in hand_copy.keys():
            hand_copy[key]-=1
            找到字母出现的位置并删除该字母
            for x in range(len(hand_keys)):
                if hand_keys==key:
                    del hand_keys[x]
                    break
        else:
            error_key+=1
        #次数永远不小于零,好像不用写
        # if hand_score[key]<0:
        #     hand_score[key]=[0]

    #输入了错误单词，作为惩罚将减去hand的单词,如果为0则删除掉hand的元素
    if error>0:
        for i in hand_keys:
            hand_copy[i]-=1
            if hand_copy[i]==0:
                del hand_copy[i]
    return hand_copy




#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    word_lists=[]
    yuanyin=['a','e','i','o','u']
    _replace=word.find('*')
    #构造有*的替换单词
    if _replace!=-1:
        for i in yuanyin:
            strs=word[0:_replace+1]+i+word[_replace+1::]
            world_lists.append(strs)
    else:
        word_lists.append(word)
    for word in word_lists:
        if word in word_list:
            for i in word:
                if i not in hand.keys():
                    return False
            else:
                return True
    else:
        return False



def play_hand(hand,word_list):


    display_hand(hand)
    word=input('Enter word, or "!!" to indicate that you are finished:')
    flag=is_valid_word(word,hand,word_list)
    while not flag:
        word = input('The word is invalid,please choose anther word:')
        flag = is_valid_word(word, hand, word_list)
    score=0
    while 1:
        if word=='!!':
            print('Total score:',score)
            break
        else:
            hand=get_frequency_dict(update_hand(hand,word))
            if len(hand)==0:
                print('Total score:',score)
                break
            display_hand(hand)
        score+=get_word_score(word,len(word))
        print('"%s" earned %d points. Total: %d points'%(word,get_word_score(word,len(word)),score))
        word = input('Enter word, or "!!" to indicate that you are finished:')
    return score


def substitute_hand(hand, letter):
    value=hand[letter]
    del hand[letter]
    while 1:
        x = random.choice(VOWELS+CONSONANTS)
        if x not in hand.keys():
            hand[x]=value
            break
    return hand


def play_game(word_list):
    #提示用户怎么玩
    print('根据显示的letters输入猜的单词，其中*可以代替元音字母之一，按下回车，游戏将会执行！')
    print('当你输入“！！”时，游戏会提前结束！')
    print('当你输入的单词的字母不在hand中时，将会扣除hand的letter数量')
    print('当letter用完时，游戏会自动结束！')
    HAND_SIZE=int(input('Enter total number of hands:'))
    hand=deal_hand(HAND_SIZE)
    show = input('Would you like to substitute a letter?')
    if show == 'yes':
        show2=input('Which letter would you like to replace:')
        hand=substitute_hand(hand,show2)
    else:
        play_hand(hand,word_list)



if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
