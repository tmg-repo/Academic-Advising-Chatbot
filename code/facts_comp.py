def run():
    import wikipediaapi

    wiki = wikipediaapi.Wikipedia('en')

    page = wiki.page('Computer_science')

    print("Title: %s" % page.title)

    print("Summary: %s" % page.summary[0:596])



