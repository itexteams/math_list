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


def bt_dang11_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            n_0 = randint(2, 5)
            n_1 = randint(4, 8)
            n_3 = randint(2, 6)
            a_val = randint(3, 8)
            b_val = randint(1, 5)
            
            N = n_0 + n_1 + a_val + n_3 + b_val
            tong_ngay = 0 * n_0 + 1 * n_1 + 2 * a_val + 3 * n_3 + 4 * b_val
            tb_rat = Rational(tong_ngay, N)
            
            if N in [20, 25, 30] and tb_rat.q in [1, 2, 5, 10]:
                break
                
        if tb_rat.q == 1:
            tb_str = str(tb_rat.p)
        else:
            number = Decimal(float(tb_rat))
            kq_tb = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            tb_str = str(kq_tb).replace('.', ',')
            
        tong_ab = N - (n_0 + n_1 + n_3)
        tong_2a4b = tong_ngay - (1 * n_1 + 3 * n_3)
        tong_a2b = tong_2a4b // 2
        
        c1 = randint(2, 4)
        c2 = randint(2, 5)
        while c1 == c2:
            c2 = randint(2, 5)
        kq_val = c1 * a_val + c2 * b_val
        kq_str = str(kq_val)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Bảng thống kê số ngày nghỉ phép trong năm của $%s$ nhân viên một phòng ban như sau:
    \\begin{center}
    \\begin{tabular}{|l|c|c|c|c|c|}
    \\hline
    \\textbf{Số ngày nghỉ} & $0$ & $1$ & $2$ & $3$ & $4$ \\\\
    \\hline
    \\textbf{Số nhân viên} & $%s$ & $%s$ & $a$ & $%s$ & $b$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Biết số ngày nghỉ trung bình của mỗi nhân viên là $%s$ ngày. Tổng $%sa+%sb$ bằng bao nhiêu?'''
                         %(str(N), str(n_0), str(n_1), str(n_3), tb_str, str(c1), str(c2)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì phòng ban có tất cả $%s$ nhân viên nên ta có phương trình: \\\\
                   $%s + %s + a + %s + b = %s \\Leftrightarrow a + b = %s \\quad (1)$. \\\\
                   Vì số ngày nghỉ trung bình của mỗi nhân viên là $%s$ ngày nên ta có phương trình: \\\\
                   $\\dfrac{0 \\cdot %s + 1 \\cdot %s + 2a + 3 \\cdot %s + 4b}{%s} = %s$ \\\\
                   $\\Leftrightarrow %s + 2a + 4b = %s \\Leftrightarrow 2a + 4b = %s \\Leftrightarrow a + 2b = %s \\quad (2)$. \\\\
                   Từ $(1)$ và $(2)$, ta có hệ phương trình: \\\\
                   $\\left\\{\\begin{aligned} a + b &= %s \\\\ a + 2b &= %s \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} a &= %s \\\\ b &= %s \\end{aligned}\\right.$ \\\\
                   Vậy giá trị của biểu thức cần tìm là: \\\\
                   $%sa + %sb = %s \\cdot %s + %s \\cdot %s = %s$.'''
                   %(str(N),
                     str(n_0), str(n_1), str(n_3), str(N), str(tong_ab),
                     tb_str,
                     str(n_0), str(n_1), str(n_3), str(N), tb_str,
                     str(1 * n_1 + 3 * n_3), str(tong_ngay), str(tong_2a4b), str(tong_a2b),
                     str(tong_ab), str(tong_a2b), str(a_val), str(b_val),
                     str(c1), str(c2), str(c1), str(a_val), str(c2), str(b_val), kq_str
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

