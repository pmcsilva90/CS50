def main():
    string = input()

    string = convert(string)

    print(string)

def convert(emoticon):
    emoticon = emoticon.replace(":)","🙂")
    emoticon = emoticon.replace(":(","🙁")
    emoticon = emoticon.replace(":|","😐")

main()
