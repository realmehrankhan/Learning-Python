def convert(emoticons):
    emoticons = emoticons.replace(":(", "🙁")
    emoticons = emoticons.replace(":)", "🙂")
    return emoticons
  
def main():
    emoticons = input("Enter emoticon: ")
    text = convert(emoticons)
    print(text)
  
main()
