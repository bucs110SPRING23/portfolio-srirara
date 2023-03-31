import json

def main():
    #reading in the article and saving it
    file_pointer_news = open("ch06/exercises/news.txt", "r")
    article = file_pointer_news.read()
    file_pointer_news.close()

    #reading in the substitutions json file
    file_pointer_sub = open("ch06/exercises/subs.json", "r")
    substitutions = json.load(file_pointer_sub)
    file_pointer_sub.close()

    #replacing words
    better_article = article
    for k,v in substitutions.items():
        better_article = better_article.replace(k,v)

    #write new article
    file_pointer_write = open("ch06/exercises/betternews.txt", "w")
    file_pointer_write.write(better_article)
    file_pointer_write.close()

main()
