bout_bois = {
  'name': 'Bout de bois tordu',
  'resistance': 1,
  'degat': 1,
  'poids': 1
}
saucisson = {
  'name': "Saucisson a l'ail bien sec",
  'resistance': 15,
  'degat': 3,
  'poids': 2
}
cornichons = {
  'name': "Cornichons marines",
  'resistance': 0,
  'degat': 1,
  'poids': 1
}

mon_inventaire = [bout_bois, saucisson, cornichons]
ton_inventaire = [bout_bois]

def calcul_statut(inventaire):
  statut = {
    'resistance': 0,
    'degat': 0,
    'poids': 0
  }
  
  for item in inventaire:
    statut['resistance'] += item['resistance']
    statut['degat'] += item['degat']
    statut['poids'] += item['poids']
  
  return statut

mon_statut = calcul_statut(inventaire=mon_inventaire)
ton_statut = calcul_statut(inventaire=ton_inventaire)

print mon_statut
print ton_statut
