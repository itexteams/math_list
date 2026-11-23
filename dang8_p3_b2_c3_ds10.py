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


def bt_dang8_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = random.choice([6, 8, 10])
        while True:
            arr = [randint(10, 25) for _ in range(n - 1)]
            tb = randint(13, 22)
            tong_can = tb * n
            x_val = tong_can - sum(arr)
            if 8 <= x_val <= 30:
                break
                
        mau_str = '; '.join(str(v) for v in arr) + '; x'
        
        full_arr = sorted(arr + [x_val])
        mau_sx_str = '; '.join(str(v) for v in full_arr)
        
        mid1 = n // 2 - 1
        mid2 = n // 2
        v1 = full_arr[mid1]
        v2 = full_arr[mid2]
        
        med_rat = Rational(v1 + v2, 2)
        if med_rat.q == 1:
            kq_str = str(med_rat.p)
        else:
            number = Decimal(float(med_rat))
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq_str = str(kq).replace('.', ',')
            
        tong_7_str = ' + '.join(str(v) for v in arr)
        tong_7_val = sum(arr)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một nông trại thu hoạch thanh long trong $%s$ ngày với sản lượng (đơn vị: tạ) được ghi lại là: $%s$. Biết rằng sản lượng trung bình mỗi ngày là $%s$ tạ. Trung vị của mẫu số liệu trên bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                         %(str(n), mau_str, str(tb)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì sản lượng trung bình mỗi ngày trong $%s$ ngày là $%s$ tạ nên tổng sản lượng thu hoạch được là: \\\\
                   $%s \\cdot %s = %s$ (tạ). \\\\
                   Theo đề bài, ta có phương trình: \\\\
                   $%s + x = %s \\Leftrightarrow %s + x = %s \\Leftrightarrow x = %s$. \\\\
                   Sắp xếp mẫu số liệu gồm $%s$ giá trị theo thứ tự không giảm, ta được: \\\\
                   $%s$. \\\\
                   Vì mẫu số liệu có $n = %s$ là số chẵn nên trung vị $M_e$ là trung bình cộng của hai giá trị chính giữa (ở vị trí thứ $%s$ và thứ $%s$): \\\\
                   $M_e = \\dfrac{%s + %s}{2} = %s$.'''
                   %(str(n), str(tb),
                     str(tb), str(n), str(tong_can),
                     tong_7_str, str(tong_can), str(tong_7_val), str(tong_can), str(x_val),
                     str(n),
                     mau_sx_str,
                     str(n), str(mid1 + 1), str(mid2 + 1),
                     str(v1), str(v2), kq_str
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

