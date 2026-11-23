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


def bt_dang17_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = 7
        while True:
            # Mẫu gồm 7 số nguyên dương sắp xếp không giảm: x1; x2; a; x4; b; x6; x7
            # Q2 = x4, Q1 = x2, Q3 = x6
            # Điều kiện để xác định duy nhất cặp số nguyên (a, b):
            # x2 <= a <= x4 và x4 <= b <= x6
            # Để a + b = S có duy nhất 1 nghiệm nguyên (a, b), ta chọn a = x4 và b = x6 (tức S = x4 + x6)
            # hoặc chọn a = x2 và b = x4 (tức S = x2 + x4)
            x1 = randint(1, 4)
            x2 = randint(x1 + 1, x1 + 4) # Q1
            x4 = randint(x2 + 2, x2 + 5) # Q2
            x6 = randint(x4 + 2, x4 + 5) # Q3
            x7 = randint(x6 + 1, x6 + 5)
            
            case = random.choice([1, 2])
            if case == 1:
                a_val = x4
                b_val = x6
                giai_thich_ab = ('''Vì $%s \\le a \\le %s$ và $%s \\le b \\le %s$ nên ta có $a + b \\le %s + %s = %s$. \\\\
                   Dấu bằng xảy ra khi và chỉ khi $a = %s$ và $b = %s$.'''
                   %(str(x2), str(x4), str(x4), str(x6), str(x4), str(x6), str(x4 + x6),
                     str(a_val), str(b_val)))
            else:
                a_val = x2
                b_val = x4
                giai_thich_ab = ('''Vì $%s \\le a \\le %s$ và $%s \\le b \\le %s$ nên ta có $a + b \\ge %s + %s = %s$. \\\\
                   Dấu bằng xảy ra khi và chỉ khi $a = %s$ và $b = %s$.'''
                   %(str(x2), str(x4), str(x4), str(x6), str(x2), str(x4), str(x2 + x4),
                     str(a_val), str(b_val)))
                     
            tong = x1 + x2 + a_val + x4 + b_val + x6 + x7
            tb_rat = Rational(tong, n)
            if tb_rat.q == 1:
                tb_val = tb_rat.p
                break
                
        mau_str = '%s; %s; a; %s; b; %s; %s' %(str(x1), str(x2), str(x4), str(x6), str(x7))
        tong_5_so = x1 + x2 + x4 + x6 + x7
        tong_ab = a_val + b_val
        kq_val = a_val * b_val
        kq_str = str(kq_val)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho mẫu số liệu gồm $%s$ số nguyên dương đã sắp xếp không giảm: $%s$. Biết rằng tứ phân vị thứ nhất $Q_1 = %s$ và tứ phân vị thứ ba $Q_3 = %s$, đồng thời số trung bình của mẫu bằng $%s$. Tích $a \\cdot b$ bằng bao nhiêu?'''
                         %(str(n), mau_str, str(x2), str(x6), str(tb_val)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì mẫu số liệu gồm $n = %s$ giá trị đã sắp xếp theo thứ tự không giảm nên: \\\\
                   - Trung vị của mẫu là giá trị ở vị trí thứ $4$, tức là $Q_2 = %s$. \\\\
                   - Nửa số liệu bên trái $Q_2$ gồm $3$ giá trị là: $%s; %s; a$ nên tứ phân vị thứ nhất là $Q_1 = %s$ (thỏa mãn giả thiết). \\\\
                   - Nửa số liệu bên phải $Q_2$ gồm $3$ giá trị là: $b; %s; %s$ nên tứ phân vị thứ ba là $Q_3 = %s$ (thỏa mãn giả thiết). \\\\
                   Vì mẫu số liệu đã được sắp xếp theo thứ tự không giảm nên ta có điều kiện: $%s \\le a \\le %s$ và $%s \\le b \\le %s$. \\\\
                   Mặt khác, số trung bình của mẫu số liệu bằng $%s$ nên tổng của $%s$ số là: \\\\
                   $%s + %s + a + %s + b + %s + %s = %s \\cdot %s \\Leftrightarrow %s + a + b = %s \\Leftrightarrow a + b = %s$. \\\\
                   %s \\\\
                   Vậy tích cần tìm là: $a \\cdot b = %s \\cdot %s = %s$.'''
                   %(str(n),
                     str(x4),
                     str(x1), str(x2), str(x2),
                     str(x6), str(x7), str(x6),
                     str(x2), str(x4), str(x4), str(x6),
                     str(tb_val), str(n),
                     str(x1), str(x2), str(x4), str(x6), str(x7), str(n), str(tb_val), str(tong_5_so), str(tong), str(tong_ab),
                     giai_thich_ab,
                     str(a_val), str(b_val), kq_str
                   ))
        
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+
    str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n')
    return content

