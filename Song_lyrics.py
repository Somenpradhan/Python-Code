# write a program to print repeated words in the song lyrics and the highest repeated word.
# dictionary will used but not the count.
# don't use the count function.

def repeated(lyrics):
    words = lyrics.split()
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    repeated_words = {word: count for word, count in word_dict.items() if count > 1}
    highest_repeated_word = max(repeated_words, key=repeated_words.get)

    print(repeated_words)
    print(highest_repeated_word)

lyrics = '''Dekh le tu aajizi ye meri
    Aaj bhi main thahra yahiin
    Aarzu jo teri yuun hone lagi
    Hoshon mein rahta nahiin
    Na jaane kyuun tu hi tu dil mein basa hai
    Tere bina kya jiyuun
    Bikhra ye man, kya sitam tune hain dhaaye
    Phir bhi main kuch na kahoon
    Ye to bata, kya hai mubtala meri nazar ke shikaar mein
    Ye to pata tujhe hai bhala sab hai tere ikhtiyaar mein
    Jaan le tu, badal bhi jaayein sabhi, main rahoonga iksaan yahiin
    Na jaane kyuun tu hi tu dil mein basa hai
    Tere bina kya jiyuun
    Bikhra ye man, kya sitam tune hain dhaaye
    Phir bhi main kuch na kahoon
    Na jaane kyuun tu hi tu dil mein basa hai
    Tere bina kya jiyun
    Bikhra ye man, kya sitam tune hain dhaaye
    Phir bhi main kuch na kahoon
    Na jaane kyuun, dil mein tu kyuun
    Na jaane kyuun ik tu hi tu
    Na jaane kyuun
    Phir bhi main kuch na kahoon'''
repeated(lyrics)