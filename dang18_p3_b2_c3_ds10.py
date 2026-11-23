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


def bt_dang18_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = 8
        while True:
            # Mẫu số liệu gồm 8 số nguyên dương sắp xếp không giảm: a1; a2; x; y; a5; a6; a7; a8
            # Trong đó a1 < a2 < a5 < a6 < a7 < a8 đôi một khác nhau
            # Để mẫu có đúng hai mốt và trung vị bằng med = (y + a5)/2:
            # Ta chọn x = a2 và y = a5 - 2 (hoặc a5 - 4) sao cho y > x và y != a2, y != a5
            # Khi đó x = a2 xuất hiện 2 lần, y = a5 xuất hiện 2 lần -> đúng 2 mốt!
            # Hoặc chọn x = a2 và y = a5 -> x xuất hiện 2 lần, y xuất hiện 2 lần -> đúng 2 mốt!
            a1 = randint(2, 5)
            a2 = randint(a1 + 2, a1 + 4)
            a5 = randint(a2 + 3, a2 + 6)
            a6 = randint(a5 + 2, a5 + 4)
            a7 = randint(a6 + 2, a6 + 4)
            a8 = randint(a7 + 2, a7 + 5)
            
            x_val = a2
            y_val = a5
            
            med_val = a5 # Vì (y + a5)/2 = (a5 + a5)/2 = a5
            tong = a1 + a2 + x_val + y_val + a5 + a6 + a7 + a8
            tb_rat = Rational(tong, n)
            
            if tb_rat.q == 1:
                tb_val = tb_rat.p
                break
                
        mau_str = '%s; %s; x; y; %s; %s; %s; %s' %(str(a1), str(a2), str(a5), str(a6), str(a7), str(a8))
        tong_6_so = a1 + a2 + a5 + a6 + a7 + a8
        tong_xy = x_val + y_val
        
        c1 = randint(2, 4)
        c2 = randint(2, 5)
        while c1 == c2:
            c2 = randint(2, 5)
            
        kq_val = c1 * x_val + c2 * y_val
        kq_str = str(kq_val)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một mẫu số liệu gồm $%s$ số nguyên dương đã sắp xếp không giảm: $%s$. Biết rằng số trung bình của mẫu số liệu bằng $%s$, trung vị bằng $%s$ và mẫu số liệu có đúng hai mốt. Giá trị của biểu thức $P = %sx + %sy$ bằng bao nhiêu?'''
                         %(str(n), mau_str, str(tb_val), str(med_val), str(c1), str(c2)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì mẫu số liệu có $n = %s$ giá trị và đã được sắp xếp theo thứ tự không giảm nên trung vị của mẫu số liệu là trung bình cộng của hai giá trị chính giữa (ở vị trí thứ $4$ và thứ $5$): \\\\
                   $M_e = \\dfrac{y + %s}{2}$. \\\\
                   Theo đề bài, trung vị bằng $%s$ nên ta có: \\\\
                   $\\dfrac{y + %s}{2} = %s \\Leftrightarrow y + %s = %s \\Leftrightarrow y = %s$. \\\\
                   Mặt khác, số trung bình của mẫu số liệu bằng $%s$ nên tổng của $%s$ số là: \\\\
                   $%s + %s + x + y + %s + %s + %s + %s = %s \\cdot %s$ \\\\
                   $\\Leftrightarrow %s + x + y = %s \\Leftrightarrow x + y = %s$. \\\\
                   Thay $y = %s$ vào phương trình trên, ta được: $x = %s - %s = %s$. \\\\
                   Khi đó mẫu số liệu đầy đủ là: $%s; %s; %s; %s; %s; %s; %s; %s$ có đúng hai mốt là $%s$ và $%s$ (thỏa mãn điều kiện đề bài). \\\\
                   Vậy giá trị của biểu thức cần tìm là: \\\\
                   $P = %sx + %sy = %s \\cdot %s + %s \\cdot %s = %s$.'''
                   %(str(n),
                     str(a5),
                     str(med_val),
                     str(a5), str(med_val), str(a5), str(2 * med_val), str(y_val),
                     str(tb_val), str(n),
                     str(a1), str(a2), str(a5), str(a6), str(a7), str(a8), str(n), str(tb_val),
                     str(tong_6_so), str(tong), str(tong_xy),
                     str(y_val), str(tong_xy), str(y_val), str(x_val),
                     str(a1), str(a2), str(x_val), str(y_val), str(a5), str(a6), str(a7), str(a8), str(x_val), str(y_val),
                     str(c1), str(c2), str(c1), str(x_val), str(c2), str(y_val), kq_str
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

