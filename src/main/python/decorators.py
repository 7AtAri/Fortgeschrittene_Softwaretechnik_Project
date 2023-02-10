def modus_operandi(element_search):
    def inner(mode, browser, text, by, *args, **kwargs):
        element = element_search(browser, text, by)
        if mode == "click":
            element.click()
        elif mode == "keys":
            element.send_keys(*args, **kwargs)
    return inner


