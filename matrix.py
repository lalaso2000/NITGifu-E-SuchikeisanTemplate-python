# -*- coding: utf-8 -*-

import csv


class Matrix:
    '''行列を使いやすくするクラス'''

    @staticmethod
    def input():
        '''キーボードから行列を取得 -> ２次元配列を返します'''
        print '行列を入力します。'
        row = input('行数を入力 >>> ')
        col = input('列数を入力 >>> ')
        mat = []
        for i in range(0, row):
            n = []
            for j in range(0, col):
                s = '[' + str(i) + '][' + str(j) + ']成分を入力 >>> '
                t = input(s)
                n.append(t)
            mat.append(n)
        return mat

    @staticmethod
    def readCsv(fileName):
        '''csvファイルから行列を取得 -> ２次元配列を返します'''
        with open(fileName, 'r') as f:
            reader = csv.reader(f)
            data = [v for v in reader]
            return [[int(elm) for elm in v] for v in data]

    @staticmethod
    def printMatrix(mat):
        '''行列っぽく画面に出力'''
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                print '{0:.3f}'.format(mat[i][j]) + '\t',
            print ''

    @staticmethod
    def writeCsv(fileName, mat):
        '''csvファイルへ行列を出力'''
        with open(fileName, 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(mat)
