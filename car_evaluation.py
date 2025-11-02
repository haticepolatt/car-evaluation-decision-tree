#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 20:27:57 2025

@author: haticepolat
"""
'''
# car_load.py — kaydetmeden önce path'i kontrol et
import os
import pandas as pd

# --- 1) (Opsiyonel) çalışma dizinini zorla ayarla ---
# os.chdir("/Users/haticepolat/Desktop/car+evaluation")  # eğer GUI ile yapmadıysan burayı aktif et

# --- 2) Tam yolla kontrol et (başka bir klasördeysen bu yol işe yarar) ---
path = "/Users/haticepolat/Desktop/car+evaluation/car.data"  # kendi yolunla değiştir

print("Dosya var mı? ->", os.path.exists(path))
print("Bulunduğu klasör :", os.path.dirname(path))
print("Klasördeki dosyalar :", os.listdir(os.path.dirname(path)))

# --- 3) Dosyayı oku ---
df = pd.read_csv(path, header=None,
                 names=["buying","maint","doors","persons","lug_boot","safety","class"])

print("Yuklenen veri şekli:", df.shape)
print(df.head())

'''
# Data Preparation (Verinin Hazırlanması)
import pandas as pd

df = pd.read_csv('car.data', names=["buying","maint","doors","persons","lug_boot","safety","class"])

df.head()
inputs = pd.get_dummies(df.iloc[0:1728, 0:6])
target = df.iloc[:,-1:]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputs, target, test_size=0.25, random_state=100)

# Modeling (Modelleme)
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(min_samples_split=10)

dtc.fit(X_train, y_train)

train_tahminler = dtc.predict(X_train)
test_tahminler = dtc.predict(X_test)

from sklearn.tree import export_graphviz
export_graphviz(dtc, out_file="car_tree.dot", feature_names=X_train.columns)


from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

cm_train = confusion_matrix(y_train, train_tahminler)

acs_train = accuracy_score(y_train, train_tahminler)

cm_test = confusion_matrix(y_test, test_tahminler)
                           
acs_test = accuracy_score(y_test, test_tahminler)























