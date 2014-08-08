
def title_except(s, exceptions=["a", "and", "or", "an", "the", "of"]):
    """Returns a title string with some exceptions"""
    word_list = s.split(' ')
    if(len(word_list[0].split('.'))==1):
        title = [word_list[0].strip().lower().capitalize()] #first word always capitalized
    else:
        title = [".".join(w.capitalize() for w in word_list[0].split('.'))]

    for word in word_list[1:]: #for all others, don't capitalize exceptions
        if(len(word.split('.'))==1):
            title.append(word.strip().lower() in exceptions and word.strip().lower() or word.capitalize())
        else:
            title.append(".".join(w.capitalize() for w in word.split('.')))
                      
    return " ".join(title)








