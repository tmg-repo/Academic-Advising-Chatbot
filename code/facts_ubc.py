def run():    
    import wikipediaapi

    wiki = wikipediaapi.Wikipedia('en')

    page = wiki.page('University_of_British_Columbia_(Okanagan_Campus)')

    print("Title: %s" % page.title)

    print("Summary: %s" % page.summary[0:600])
