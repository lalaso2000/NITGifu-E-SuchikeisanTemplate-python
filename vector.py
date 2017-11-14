# -*- coding: utf-8 -*-

import csv


class Vector:
    '''ベクトルを使いやすくするクラス'''

    @staticmethod
    def input():
        '''キーボードからベクトルを取得 -> １次元配列を返します'''
        print 'ベクトルを入力します。'
        dim = input('次数を入力 >>> ')
        vec = []
        for i in range(0, dim):
            s = '[' + str(i) + ']成分を入力 >>> '
            t = input(s)
            vec.append(t)
        return vec

    @staticmethod
    def readCsv(fileName):
        '''csvファイルからベクトルを取得 -> １次元配列を返します'''
        with open(fileName, 'r') as f:
            reader = csv.reader(f)
            data = [v for v in reader]
            return [int(elm) for elm in data[0]]

    @staticmethod
    def printVector(vec):
        '''ベクトルっぽく画面に出力'''
        for i in range(0, len(vec)):
            print '{0:.3f}'.format(vec[i])

    @staticmethod
    def writeCsv(fileName, vec):
        '''csvファイルへベクトルを出力'''
        with open(fileName, 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(vec)
