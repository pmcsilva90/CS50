def main():
    string = input()

    string = convert(string)

    print(string)

def convert(emoticon):
    emoticon.replace(":)","🙂")
    emoticon.replace(":(","🙁")
    emoticon.replace(":|","😐")

main()
