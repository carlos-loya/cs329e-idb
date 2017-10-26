import logging

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('splash.html')

@app.route('/<page>/')
def anypage(page):
    return render_template(page+'.html')

@app.route('/book/<int:id_b>')
def book(id_b):
    if id_b == 1:
        content = {
                "id_b":"1",
                "cover":"https://books.google.com/books/content/images/frontcover/wrOQLV6xB-wC?fife=w500",
                "title":"Harry Potter and the Sorcerer's Stone",
                "description":"Turning the envelope over, his hand trembling, Harry saw a purple wax seal bearing a coat of arms; a lion, an eagle, a badger and a snake surrounding a large letter 'H'. Harry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are swiftly confiscated by his grisly aunt and uncle. Then, on Harry's eleventh birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. An incredible adventure is about to begin!",
                "googleid":"wrOQLV6xB-wC",
                "isbn":"9781781100486",
                "pubdate":"2015-12-08"
        }
        return render_template('book.html',**content)
    elif id_b == 2:
        content = {
                "id_b":"2",
                "cover":"https://books.google.com/books/content/images/frontcover/Y-41Q9zk32kC?fife=w500",
                "title":"The Well of Ascension",
                "description":"From #1 New York Times bestselling author Brandon Sanderson, the Mistborn series is a heist story of political intrigue and magical, martial-arts action. The impossible has been accomplished. The Lord Ruler -- the man who claimed to be god incarnate and brutally ruled the world for a thousand years -- has been vanquished. But Kelsier, the hero who masterminded that triumph, is dead too, and now the awesome task of building a new world has been left to his young protege, Vin, the former street urchin who is now the most powerful Mistborn in the land, and to the idealistic young nobleman she loves. As Kelsier's protege and slayer of the Lord Ruler she is now venerated by a budding new religion, a distinction that makes her intensely uncomfortable. Even more worrying, the mists have begun behaving strangely since the Lord Ruler died, and seem to harbor a strange vaporous entity that haunts her. Stopping assassins may keep Vin's Mistborn skills sharp, but it's the least of her problems. Luthadel, the largest city of the former empire, doesn't run itself, and Vin and the other members of Kelsier's crew, who lead the revolution, must learn a whole new set of practical and political skills to help. It certainly won't get easier with three armies, one of them composed of ferocious giants now vying to conquer the city, and no sign of the Lord Ruler's hidden cache of atium, the rarest and most powerful allomantic metal. As the siege of Luthadel tightens, an ancient legend seems to offer a glimmer of hope. But even if it really exists, no one knows where to find the Well of Ascension or what manner of power it bestows. The Cosmere The Mistborn series Mistborn: The Final Empire The Well of Ascension The Hero of Ages Alloy of Law Shadows of Self Bands of Mourning The Stormlight Archive The Way of Kings Words of Radiance Edgedancer (Novella) Oathbringer (forthcoming) Collection Arcanum Unbounded Other Cosmere Titles Elantris Warbreaker Rithmatist The Alcatraz vs. the Evil Librarians series Alcatraz vs. the Evil Librarians The Scrivener's Bones The Knights of Crystallia The Shattered Lens The Dark Talent The Reckoners Steelheart Firefight Calamity At the Publisher's request, this title is being sold without Digital Rights Management Software (DRM) applied.",
                "googleid":"Y-41Q9zk32kC",
                "isbn":"1429961813",
                "pubdate":"2010-04-01"
        }
        return render_template('book.html',**content)
    else:
        content = {
                "id_b":"3",
                "cover":"https://books.google.com/books/content/images/frontcover/dLo_GyEykjQC?fife=w500",
                "title":"The Wise Man's Fear",
                "description":"There are three things all wise men fear: the sea in storm, a night with no moon, and the anger of a gentle man.My name is Kvothe. You may have heard of me. So begins the tale of a hero told from his own point of view a story unequaled in fantasy literature. Now in The Wise Man's Fear, Day Two of The Kingkiller Chronicle, Kvothe takes his first steps on the path of the hero and learns how difficult life can be when a man becomes a legend in his own time.",
                "googleid":"dLo_GyEykjQC",
                "isbn":"1101486406",
                "pubdate":"2011-03-01"
        }
        return render_template('book.html',**content)

@app.route('/author/<int:id_a>')
def author(id_a):
    if id_a == 1:
        content = {
                "id_a":"1",
                "cover":"http://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/J._K._Rowling_2010.jpg/220px-J._K._Rowling_2010.jpg",
                "name":"J.K. Rowling",
                "description":"Joanne 'Jo' Rowling, OBE, FRSL, pen names J. K. Rowling and Robert Galbraith, is a British novelist, screenwriter and film producer best known as the author of the Harry Potter fantasy series.",
                "dob":"1956-07-31",
                "nationality":"British",
                "alma_mater":"University of Exeter",
                "wiki":"https://en.wikipedia.org/wiki/J._K._Rowling"
        }
        return render_template('author.html',**content)
    elif id_a == 2:
        content = {
                "id_a":"2",
                "cover":"http://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Brandon_Sanderson_sign.jpg/250px-Brandon_Sanderson_sign.jpg",
                "name":"Brandon Sanderson",
                "description":"Brandon Sanderson is an American fantasy and science fiction writer. He is best known for his Mistborn series and his work in finishing Robert Jordan's epic fantasy series The Wheel of Time.",
                "dob":"1975-12-19",
                "nationality":"American",
                "alma_mater":"Brigham Young University",
                "wiki":"https://en.wikipedia.org/wiki/Brandon_Sanderson"
        }
        return render_template('author.html',**content)
    else:
        content = {
                "id_a":"3",
                "cover":"http://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Patrick-rothfuss-2014-kyle-cassidy.jpg/250px-Patrick-rothfuss-2014-kyle-cassidy.jpg",
                "name":"Patrick Rothfuss",
                "description":"Patrick James Rothfuss is an American writer of epic fantasy. He is best known for his projected three-volume series The Kingkiller Chronicle.",
                "dob":"1973-06-06",
                "nationality":"American",
                "alma_mater":"Washington State University",
                "wiki":"https://en.wikipedia.org/wiki/Patrick_Rothfuss"
        }
        return render_template('author.html',**content)

@app.route('/publisher/<int:id_p>')
def publisher(id_p):
    if id_p == 1:
        content = {
                "id_p":"1",
                "logo":"http://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Pottermore.png/225px-Pottermore.png",
                "name":"Pottermore",
                "description":"Pottermore is the digital publishing, e-commerce, entertainment, and news company from J.K. Rowling and is the global digital publisher of Harry Potter and J.K. Rowling's Wizarding World.",
                "owner":"J.K. Rowling",
                "website":"http://www.pottermore.com",
                "wiki":"https://en.wikipedia.org/wiki/Pottermore"
        }
        return render_template('publisher.html',**content)
    elif id_p == 2:
        content = {
                "id_p":"2",
                "logo":"https://www.nature.com/openresearch/wp-content/blogs.dir/31/files/2015/05/PalMac_logo_CoolGrey11.jpg",
                "name":"Palgrave Macmillian",
                "description":"Palgrave Macmillan is an international academic and trade publishing company. Its programme includes textbooks, journals, monographs, professional and reference works in print and online. Palgrave Macmillan was created in 2000 when St.",
                "owner":"Springer Nature",
                "website":"http://www.palgrave.com",
                "wiki":"https://en.wikipedia.org/wiki/Palgrave_Macmillan"
        }
        return render_template('publisher.html',**content)
    else:
        content = {
                "id_p":"3",
                "logo":"http://upload.wikimedia.org/wikipedia/en/thumb/1/1c/Penguin_logo.svg/150px-Penguin_logo.svg.png",
                "name":"Penguin Group",
                "description":"The Penguin Group is a trade book publisher, part of Penguin Random House. It is owned by Pearson PLC, the global education and publishing company, and Bertelsmann, the German media conglomerate.",
                "owner":"Penguin Random House",
                "website":"http://Penguin.com",
                "wiki":"https://en.wikipedia.org/wiki/Penguin_Group"
        }
        return render_template('publisher.html',**content)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__== "__main__":
    app.run()