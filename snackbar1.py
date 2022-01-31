#intro
print('Welkom naar snackbar frappu!')

aantalpatat = int(input('hoeveel patat wilt u hebben? '))
aantalfrikadellen = int(input('hoeveel frikadellen wilt u hebben? '))
aantalkroketten = int(input('hoeveel kroketten wilt u hebben? '))

patat = float(aantalpatat * 1.10)
frikadellen = float(aantalfrikadellen * 0.70)
kroketten = float(aantalkroketten * 0.60)

totaal = patat + frikadellen + kroketten
korting1 = int(totaal / 100 * 5)
korting2 = int(totaal / 100 * 7.5)

if totaal < 10:
    totaal = totaal + 0.35
elif totaal > 40:
    totaal = totaal - korting1
elif totaal > 100:
    totaal = totaal -korting2
print(totaal)