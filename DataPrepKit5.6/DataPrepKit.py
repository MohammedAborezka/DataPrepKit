# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 23:33:14 2024

@author: MOHAMMED
"""
import pandas as pd
import numpy as np 

class data():
    def __init__(self,file_name):
        if file_name.split(".")[1] == "json":
            self.file = pd.read_json(file_name)
            self.type = "json"
        elif file_name.split(".")[1] == "csv":
            self.file = pd.read_csv(file_name)
            self.type = "csv"
        elif file_name.split(".")[1] == "excel":
            self.file = pd.read_excel(file_name)
            self.type = "excel"
    def summary(self):
        print(self.file.info())
        print(self.file.describe())
        print("Most Frequent values\n",self.file.mode().iloc[0])
    def drop_col_wnan(self,column_name):
        try:    
            self.file.dropna(subset=[column_name],inplace=True)
        except KeyError :
            print("please enter vaild column name ")
    def col_mean_fill(self,column_name):
        mean_A = self.file[column_name].mean()
        self.file[column_name] = self.file[column_name].fillna(mean_A)
    def col_mode_fill(self,column_name):
        mean_A = self.file[column_name].mode()
        self.file[column_name] = self.file[column_name].fillna(mean_A)
    def col_median_fill(self,column_name):
        mean_A = self.file[column_name].median()
        self.file[column_name] = self.file[column_name].fillna(mean_A)
    