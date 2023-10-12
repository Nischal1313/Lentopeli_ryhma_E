def game_instructions():
    print("Hetacoins: \nPelin alussa pelaajalla on 4 kolikkoa. Lentäminen maksaa 1 kolikon, ja lisävihje maksaa 1 kolikon. \nJos lennät oikeaan kohteeseen ilman lisävihjettä, saat 2 kolikkoa lisää. Jos lennät oikeaan kohteeseen \nlisävihjeen kanssa, saat 1 kolikon. Jos kolikot loppuu, häviät pelin.\n")
    print("Kilometrit: \nLennetyt kilometrit + mahdolliset kilometri rangaistukset. Kilometri rangaistuksen saa, \njos lentää väärään kohteeseen. Rangaistus on matkan pituudesta riippuen (lennetty matka - oikea matka) * 2 \ntai (oikeamatka - lennetty matka) * 2, ja tämä lisätään kilometrimäärään.\n")
    print("Lentäminen: \nLennät kohteeseen valitsemalla valtion, johon saatu vihje viittaa. \nSaat ilmoituksen mille lentokentälle lensit, ja pysäytettyjen rikosten määrä kasvaa \njos olit ajoissa pysäyttämäsää rikoksen, eli lensit oikein.\n")
    print("Voittaminen: \nVoitat pelin jos pysäytit vähintään 3 rikosta, eli lensit oikein kolmesti, \nsekä päädyit oikealle lentokentälle. Jos kilometrisi ylittävät oikein lennetyt kilometrit 30%, \ntuhlasit kilometrejä ja et lentänyt ympäristöystävällisesti, eli häviät pelin. \nJos kolikkosi ovat 10 tai yli, lensit taloudellisesti vastuullisesti, ja saat tästä ekstra maininnan!")
    return


game_instructions()