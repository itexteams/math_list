import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from decimal import Decimal, ROUND_HALF_UP


def bt_dang12_p4_b2_c3_ds10(self):
    def format_num(val):
        if isinstance(val, Decimal):
            val = val.normalize()
            s = format(val, 'f')
            if '.' in s:
                s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        if isinstance(val, float):
            if val.is_integer():
                return str(int(val))
            return str(val).replace('.', ',')
        return str(val)
    
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Sinh ngẫu nhiên dữ liệu Nhóm I (9 học sinh, điểm tập trung cao và đồng đều, có 1 mốt duy nhất)
        # và Nhóm II (10 học sinh, điểm phân tán hơn nhưng cùng số trung bình với Nhóm I)
        while True:
            # Nhóm I: 9 học sinh, điểm từ 6 đến 10, mốt xuất hiện 3 lần, tổng chia hết cho 9
            mot1 = random.choice([7, 8, 9])
            pool1 = [v for v in [6, 7, 8, 9, 10] if v != mot1]
            others1 = []
            counts1 = {mot1: 3}
            while len(others1) < 6:
                c = random.choice(pool1)
                if counts1.get(c, 0) < 2:
                    others1.append(c)
                    counts1[c] = counts1.get(c, 0) + 1
            data1 = sorted([mot1]*3 + others1)
            tong1 = sum(data1)
            if tong1 % 9 != 0:
                continue
            tb1 = tong1 // 9
            if tb1 < 7 or tb1 > 9:
                continue
                
            # Nhóm II: 10 học sinh, tổng = 10 * tb1, có các điểm thấp (4, 5) và điểm cao (9, 10), mốt xuất hiện 3 lần
            tong2_target = 10 * tb1
            mot2 = random.choice([9, 10])
            low_vals = [randint(4, 5), randint(5, 7)]
            pool2 = [v for v in range(6, 11) if v != mot2]
            others2 = []
            counts2 = {mot2: 3}
            for v in low_vals:
                counts2[v] = counts2.get(v, 0) + 1
            while len(others2) < 5:
                c = random.choice(pool2)
                if counts2.get(c, 0) < 2:
                    others2.append(c)
                    counts2[c] = counts2.get(c, 0) + 1
            data2 = sorted([mot2]*3 + low_vals + others2)
            if sum(data2) == tong2_target and max(counts2.values()) == 3:
                # Đảm bảo chỉ có duy nhất 1 giá trị đạt tần số 3
                if list(counts2.values()).count(3) == 1:
                    break
    
        data1_str = "; ".join(str(v) for v in data1)
        data2_str = "; ".join(str(v) for v in data2)
        
        # Tính đặc trưng Nhóm I (n = 9, đã sắp xếp không giảm)
        me1 = data1[4]
        
        # Tính đặc trưng Nhóm II (n = 10, đã sắp xếp không giảm)
        tb2 = tong2_target // 10
        x5_2, x6_2 = data2[4], data2[5]
        me2_dec = (Decimal(x5_2) + Decimal(x6_2)) / Decimal(2)
        me2_str = format_num(me2_dec)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giáo viên chia lớp thành hai nhóm tự học theo hai phương pháp khác nhau. Điểm kiểm tra sau một tháng của hai nhóm được ghi lại:
    \\begin{itemize}
    \\item Nhóm I ($9$ học sinh): $%s$.
    \\item Nhóm II ($10$ học sinh): $%s$.
    \\end{itemize}
    Hãy tính số trung bình, trung vị và mốt của mỗi nhóm. Dựa vào các số đặc trưng đo xu thế trung tâm, hãy nhận xét nhóm nào có thành tích học tập đồng đều và ổn định hơn.'''
                         %(data1_str, data2_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\textbf{1. Tính các số đặc trưng đo xu thế trung tâm của mỗi nhóm:}
    \\begin{itemize}
    \\item \\textbf{Đối với Nhóm I ($n_1 = 9$):} \\\\
    Mẫu số liệu đã được sắp xếp theo thứ tự không giảm: $%s$.
    \\begin{itemize}
    \\item Số trung bình cộng của Nhóm I là:
    $$\\overline{x}_1 = \\dfrac{%s}{9} = \\dfrac{%s}{9} = %s.$$
    \\item Vì cỡ mẫu $n_1 = 9$ là số lẻ nên trung vị của Nhóm I là số liệu đứng ở vị trí chính giữa (vị trí thứ $5$):
    $$M_{e1} = %s.$$
    \\item Trong mẫu số liệu của Nhóm I, điểm $%s$ xuất hiện nhiều nhất ($3$ lần) nên mốt của Nhóm I là:
    $$M_{o1} = %s.$$
    \\end{itemize}
    \\item \\textbf{Đối với Nhóm II ($n_2 = 10$):} \\\\
    Mẫu số liệu đã được sắp xếp theo thứ tự không giảm: $%s$.
    \\begin{itemize}
    \\item Số trung bình cộng của Nhóm II là:
    $$\\overline{x}_2 = \\dfrac{%s}{10} = \\dfrac{%s}{10} = %s.$$
    \\item Vì cỡ mẫu $n_2 = 10$ là số chẵn nên trung vị của Nhóm II là trung bình cộng của hai số liệu đứng ở vị trí thứ $5$ và thứ $6$:
    $$M_{e2} = \\dfrac{%s + %s}{2} = %s.$$
    \\item Trong mẫu số liệu của Nhóm II, điểm $%s$ xuất hiện nhiều nhất ($3$ lần) nên mốt của Nhóm II là:
    $$M_{o2} = %s.$$
    \\end{itemize}
    \\end{itemize}
    \\textbf{2. Nhận xét:} \\\\
    Hai nhóm có cùng mức điểm trung bình là $\\overline{x}_1 = \\overline{x}_2 = %s$. Tuy nhiên, nếu xét các đặc trưng khác cùng với sự phân bố điểm số:
    \\begin{itemize}
    \\item Ở Nhóm I, các giá trị trung bình, trung vị và mốt rất gần nhau ($\\overline{x}_1 = %s$, $M_{e1} = %s$, $M_{o1} = %s$) và tất cả học sinh đều đạt điểm khá giỏi (từ $6$ đến $10$ điểm), không có điểm yếu kém.
    \\item Ở Nhóm II, tuy có nhiều điểm $%s$ ($M_{o2} = %s$) và trung vị đạt $M_{e2} = %s$ nhưng có sự chênh lệch lớn giữa các học sinh (vẫn có các điểm thấp là $%s$ và $%s$), làm cho các số đặc trưng phân tán hơn.
    \\end{itemize}
    Vậy \\textbf{Nhóm I} có thành tích học tập đồng đều và ổn định hơn.'''
                   %(data1_str,
                     " + ".join(str(v) for v in data1), tong1, tb1,
                     me1,
                     mot1, mot1,
                     data2_str,
                     " + ".join(str(v) for v in data2), tong2_target, tb2,
                     x5_2, x6_2, me2_str,
                     mot2, mot2,
                     tb1,
                     tb1, me1, mot1,
                     mot2, mot2, me2_str, data2[0], data2[1]
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

