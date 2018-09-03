
chat_ids = []


def add_chat_id(chat_id):
    global chat_ids
    chat_ids.append({"chat_id": chat_id, "i": 0})


def set_i(chat_id, val):
    global chat_ids
    elem = next((item for item in chat_ids if item["chat_id"] == chat_id), False)
    chat_ids[chat_ids.index(elem)]["i"] = val


def get_i(chat_id):
    global chat_ids
    elem = next((item for item in chat_ids if item["chat_id"] == chat_id), False)
    return chat_ids[chat_ids.index(elem)]["i"]




