#!/usr/bin/python
# coding=utf-8
import sys
import re
from numpy import matrix
from numpy import linalg
import pickle

def pickler():
  aux = 0
  user = dict() #lista de dados de usuário
  beer = dict() #lista de dados de cerveja
  f = open("../datasets/beeradvocate.txt", 'r')
  puser = open('users.pkl', 'wb')
  pbeer = open('beers.pkl', 'wb')
  
  count = 0
  numbeer = 0
  numusers = 0
  """
    0->Nome da cerveja
    1-> ID da cerveja
    2-> ID da cervejaria
    3-> ABV da cerveja
    4-> Estilo
    5-> Aparência *
    6-> Aroma *
    7-> Paladar *
    8-> OVERALL *
  """
  """DICT da cerveja:
    Nome
    beerId
    brewerId
    ABV
    Estilo
    Média da Aparência
    Média do Aroma
    Média do Paladar
    Média do OVERALL
    text
    Número de reviews dessa cerveja
    users -> lista de usuarios que já deram reviews
  """
  """DICT do user:
    número de ratings dados
    rating médio

  """
  #primeira coisa a se calcular: sparcity (quantos % dos usuários não deram rating em uma cerveja)
  # Insercão das linhas
  used = 0
  for line in f:
    print line
    if len(line) <= 2: #entre dois ratings existe uma linha vazia
      count = 0
      continue
    if count == 0: #primeira linha. Nome da cerveja. Deve ser salva na próxima linha
      name = line.split(': ')[1]
      name = name.rstrip()
      count +=1
      numbeer +=1
      continue
    if  count ==1: #ID
      beerId = line.split(': ')[1].rstrip()
      if beerId in beer:
        used = 1
        beer[beerId]['numReviews']+=1
      else:
        beer[beerId] = dict()
        beer[beerId]['name'] = name 
        beer[beerId]['numReviews'] = beer[beerId].get('numReviews', 0)+1
        beer[beerId]['users'] = []
      count+=1
      continue
    if count ==2 and not used: #cervejaria
      brewerId = line.split(': ')[1].rstrip()
      beer[beerId]['brewerId'] = brewerId
      count+=1
      continue
    if count == 3 and not used: #álcool
      abv = line.split(': ')[1].rstrip()
      beer[beerId]['ABV'] = abv
      count+=1
      continue
    if count == 4 and not used: #Estilo
      style = line.split(': ')[1].rstrip()
      beer[beerId]['style'] = style
      count+=1
      continue
    
    if count == 5: #nota de aparência
      aparencia = float(line.split(': ')[1].rstrip())
      beer[beerId]['appearence'] = (float(beer[beerId].get('appearence', 0)) + aparencia)/beer[beerId]['numReviews'] #media de rating da aparencia
    
    if count == 6: #aroma
      aroma = float(line.split(': ')[1].rstrip())
      beer[beerId]['aroma'] = (float(beer[beerId].get('aroma', 0)) + aroma)/beer[beerId]['numReviews'] #media de rating da aparencia

    if count == 7:#paladar
      palate = float(line.split(': ')[1].rstrip())
      beer[beerId]['palate'] = (float(beer[beerId].get('palate', 0)) + palate)/beer[beerId]['numReviews'] #media de rating da aparencia

    if count == 8:#gosto
      taste = float(line.split(': ')[1].rstrip())
      beer[beerId]['taste'] = (float(beer[beerId].get('taste', 0)) + taste)/beer[beerId]['numReviews'] #media de rating da aparencia
    
    if count == 9:#média final
      overall = float(line.split(': ')[1].rstrip())
      beer[beerId]['overall'] = (float(beer[beerId].get('overall', 0)) + overall)/beer[beerId]['numReviews'] #media de rating da aparencia
    
    if count == 11:#
      name = line.split(": ")[1].rstrip()
      numusers+=1
      if not name in user: # se for um novo usuário
        user[name] = dict()
        numusers +=1
      user[name]['numRatings'] = user[name].get('numRatings',0) + 1
      user[name]['overall'] = (float(user[name].get('overall',0)) + overall)/user[name]['numRatings'] # atualizar a nota média do usuário
      beer[beerId]['users'].append(name)
    

    if count == 12 :
      text = line.split(': ')[1]
      beer[beerId]['text'] = (beer[beerId].get('text', '') + " " + text) #Todas as strings juntas

    count+=1   

  pickle.dump(user, puser)
  pickle.dump(beer, pbeer)
  return user, beer
pickler()