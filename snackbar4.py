#intro
print('Welkom naar snackbar frappu!')


patat = 0
frikadellen = 0
kroketten = 0
saus = 0
maat = 0
maatXXL = 0
brood = 0

while True:
    aantalpatat = int(input('hoeveel patat wilt u hebben? '))
    for i in range(aantalpatat):
        aantalsaus = input('patat met of zonder? ')
        if aantalsaus == 'met':
            saus = float(saus + 1)
    def thaSaus():
        saus = input('Welke sausen wil je?')
        return saus
    thaSaus()

    aantalfrikadellen = int(input('hoeveel frikadellen wilt u hebben? '))
    for i in range(aantalfrikadellen):
        aantalmaat = input('welke maat?: gewone, vega of XXL\nmet vega komt 0,30 cent erbij en met XXL komt 0,50 cent erbij:\n')
        if aantalmaat == 'vega':
            maat = float(maat + 1)
        elif aantalmaat == 'XXL':
            maatXXL = float(maat + 1)

    aantalkroketten = int(input('hoeveel kroketten wilt u hebben? '))
    for i in range(aantalkroketten):
        aantalbrood = input('met of zonder broodje?')
        if aantalbrood == 'met':
            brood = float(brood + 1)

    patat = float(aantalpatat * 1.10)
    frikadellen = float(aantalfrikadellen * 0.70)
    kroketten = float(aantalkroketten * 0.60)

    maat = float(maat * 0.30)
    maatXXL = float(maat * 0.50)
    saus = float(saus * 0.50)
    brood = float(brood * 0.80)

    float(totaal = patat + frikadellen + kroketten + saus + maat + brood)
    korting1 = int(totaal / 100 * 5)
    korting2 = int(totaal / 100 * 7.5)
    def calc():
        btw = totaal / 100 * 6
        return btw
    if totaal < 10:
        totaal = totaal + 0.35
    elif totaal > 40:
        totaal = totaal - korting1
    elif totaal > 100:
        totaal = totaal - korting2
    btw = totaal / 100 * 6

    print('----------bon----------')
    print('patat: '+ str(patat))
    print('sauses: '+ str(saus))
    print('frikadellen: ' + str(frikadellen))
    print('maat: '+ str(maat))
    print('maatXX: '+ str(maatXXL))
    print('kroketten: ' + str(kroketten))
    print('kroketten met een broodje: '+ str(brood))
    print('Totaal: ' + str(totaal))
    print('Btw' + str(btw))
    print('----------bon----------')

    bestellen = str(input('Wilt u nog meer bestellen?\n ja/nee\n'))
    if bestellen == 'ja':
        print('Welkom naar snackbar frappu!')
    else:
        break