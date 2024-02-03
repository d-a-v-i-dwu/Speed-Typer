def punctuation_retriever():
    text = input("Text: ")
    punctuation_list = [",", ".", ";", ":", "/", "?", "(", ")", "'", "-", '"', "@", "$", "*", "&", "^", "#", "!", "<", ">", "+", "=", "_", "{", "[", "]", "}" ]
    punctuation = []
    for ele in text:
        if ele in punctuation_list:
            punctuation.append(ele)
        else:
            continue
    if len(punctuation) == 0:
        print("There is no punctuation in your text")
    else:
        print("Punctuation in your text: ", end = "")
        for ele in punctuation:
            print(ele, end = "")
punctuation_retriever()