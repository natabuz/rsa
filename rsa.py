#!/usr/bin/python
# -*- coding: utf-8 -*-

import lint
import sys

def xgcd(a, b):								#Расширенный алгоритм Евклида
	if a == lint.Lint("0"):
		return 0, 1, b

	if b == lint.Lint("0"):
		return 1, 0, a

	px = lint.Lint("0")
	ppx = lint.Lint("1")
	py = lint.Lint("1")
	ppy = lint.Lint("0")

	while b > lint.Lint("0"):
		q = a / b
		a, b = b, a % b
		x = ppx - q * px
		y = ppy - q * py
		ppx, px = px, x
		ppy, py = py, y

	return ppx, ppy, a

def gend(a, b):								#Генерироваие числа d
	while True:
		x, y, g = xgcd(a, b)
		z = x % b
		break
	return z

if __name__ == "__main__":
	f = open(sys.argv[1])
	
	mes = int(f.read())						#Сообщение из файла

	f.close()

	p = lint.Lint(mes.read("p.txt"))
	q = lint.Lint(mes.read("q.txt"))
	e = lint.Lint(mes.read("e.txt"))

	mes = lint.Lint(str(mes))				#Сообщение в виде большого числа
	
	mod = p * q

	phi = (p - lint.Lint("1")) * (q - lint.Lint("1"))
	
	d = gend(e, phi)
	
	encode = d.powmod(mes, e, mod)          #Шифровка             

	decode = d.powmod(encode, d, mod)		#Расшифровка
	
	f = open("decode.txt", "w")
	
	f.write(decode.trim().toString())		#Запись расшифрованного сообщения
	
	f.close()
