import os
import json
import base64
from glob import glob
import shelve

#asumsi, hanya ada player 1, 2
class PlayerServerInterface:
    def __init__(self):
        self.players = shelve.open('g.db',writeback=True)
        self.players['1']= "0,100"
        self.players['2']= "270,100"
        self.players['3']= "540,100"

    def set_location(self,params=[]):
        pnum = params[0]
        x = params[1]
        y = params[2]
        try:
            if (int(self.players['1'].split(',')[1]) >= 400 or int(self.players['2'].split(',')[1]) >= 400 or int(self.players['3'].split(',')[1]) >= 400) :
                return dict(status='FINISH')
            self.players[pnum]=f"{x},{y}"
            self.players.sync()
            return dict(status='OK', player=pnum)
        except Exception as e:
            return dict(status='ERROR')

    def get_location(self,params=[]):
        pnum = params[0]
        try:
            return dict(status='OK',location=self.players[pnum])
        except Exception as ee:
            return dict(status='ERROR')



if __name__=='__main__':
    p = PlayerServerInterface()
    p.set_location(['1',100,100])
    print(p.get_location('1'))
    p.set_location(['2',120,100])
    print(p.get_location('2'))
