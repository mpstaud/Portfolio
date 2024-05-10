import math
import random

helmets = ['Commando', 'Recon', 'Mark VI', 'Mark VII', 'CQB', 'ODST', 'Scout', 'Grenadier', 'Air Assault',
           'Firefall', 'CQC', 'Rakshasa', 'SPI',
           'Mark V[B]', 'Yokai', 'EVA[C]', 'EVA']

armor_cores = ['Mjolnir Mark VII', 'Mjolnir Mark V[B]', 'Mjolnir Mark IV', 'Rakshasha', 'SPI']

shoulders = ['Mark V', 'Mark IV', 'Mark VII', 'ODST', 'Security', 'Sniper', 'FJ', 'CQC', 'Grenadier', 'EVA']
colors = ['Red', 'Blue', 'Green', 'Black', 'Purple', 'Yellow', 'White', 'Orange', 'Grey', 'Brown', 'Olive', 'Tan']


def selectPiece(items):
    piece = random.choice(items)
    return piece


helmet = selectPiece(helmets)
core = selectPiece(armor_cores)
right_shoulder = selectPiece(shoulders)
left_shoulder = selectPiece(shoulders)
color = selectPiece(colors)
print('Helmet: ' + helmet)
print('Core: ' + core)
print('Right Shoulder: ' + right_shoulder)
print('Left Shoulder: ' + left_shoulder)
print('Color: ' + color) 
