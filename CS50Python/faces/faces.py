def main():
    string = input()

    convert(string)

    print(string)

def convert(emoticon):
    emoticon.replace(":\)","🙂")
    emoticon.replace(":\()","🙁")
    emoticon.replace(":|)","😐")

main()
