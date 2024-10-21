def chercherlettre(message, lettre):
    reponse=[]
    index=0
    for lettre_message in message:
        if lettre_message == lettre:
            reponse.append(index)
        index = index + 1
    return reponse

print(chercherlettre("Marie", "i"))