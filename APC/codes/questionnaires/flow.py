def flow(answers):
    flow_msg = ["O programa funciona?"]

    if answers[0] == "SIM":
        flow_msg.append("Você entende o que fez?")

        if answers[1] == "NÃO":
            flow_msg.append("Já foi na tutoria?")
            pass

        if answers[1] == "SIM":
            flow_msg.append("Ótimo. Então não mexe!")
            return flow_msg

    if answers[0] == "NÃO":
        flow_msg.append("Você sabe onde está o erro?")

        if answers[1] == "SIM":
            flow_msg.append("Acha que pode solucionar sozinho?")

            if answers[2] == "SIM":
                flow_msg.append("Então mão na massa!")
                return flow_msg

            elif answers[2] == "NÃO":
                flow_msg.append("Já pesquisou no Google?")

                if answers[3] == "NÃO":
                    flow_msg.append("Corre lá então!")
                    return flow_msg

                elif answers[3] == "SIM":
                    flow_msg.append("Já foi na tutoria?")
                    pass
        elif answers[1] == "NÃO":
            flow_msg.append("Já foi na tutoria?")
            pass

    if answers[-1] == "NÃO":
        flow_msg.append("Temos um time a disposição!")
        return flow_msg

    elif answers[-1] == "SIM":
        flow_msg.append("Choremos!")
        return flow_msg
