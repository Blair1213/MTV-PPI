from numpy import *
import numpy as np
import random
import math
import os
import time
import pandas as pd
import csv
import math
import random
import Tool
# 定义函数
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  # 把每个rna疾病对加入OriginalData，注意表头
        SaveList.append(row)
    return

def ReadMyCsv2(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        counter = 0
        while counter < len(row):
            row[counter] = int(row[counter])      # 转换数据类型
            counter = counter + 1
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return



lncAndDisease = []
ReadMyCsv(lncAndDisease, "LncAndProtein.csv")
print('lncDisease[0]', lncAndDisease[0])
print('len(lncDisease)', len(lncAndDisease))

AllDiseaseNum = []
ReadMyCsv(AllDiseaseNum, "AllProteinNum.csv")         # 不使用下三角矩阵，无所为第一个数字大于第二个

AllLncNum = []
ReadMyCsv(AllLncNum, "AllLncNum.csv")         # 不使用下三角矩阵，无所为第一个数字大于第二个

print(AllLncNum[0])

import Tool
NegativeSample = Tool.NegativeGenerate(lncAndDisease, AllLncNum, AllDiseaseNum)
Tool.StorFile(NegativeSample, 'NegativeSample.csv')
