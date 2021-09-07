#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot_chr = list(mot)
    for i in range(len(mot_chr)):
        curr_char = ord(mot_chr[i])
        mot_chr[i] = chr(curr_char-32)
    mot = ''.join(mot_chr)
    # TODO completer la fonction ici
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
