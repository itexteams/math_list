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


def bt_dang20_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        def fmt_dec(rat_val):
            if rat_val.q == 1:
                return str(rat_val.p)
            else:
                d_val = Decimal(rat_val.p) / Decimal(rat_val.q)
                s = str(d_val.normalize())
                if 'E' in s or 'e' in s:
                    s = '{:f}'.format(d_val)
                return s.replace('.', ',')
    
        while True:
            n1 = random.choice([8, 10, 12, 15])
            n2 = random.choice([12, 15, 18, 20])
            n3 = random.choice([20, 25, 30])
            n_all = n1 + n2 + n3
            
            l1 = randint(15, 22)
            l2 = randint(20, 28)
            l3 = randint(24, 35)
            
            tong1 = n1 * l1
            tong2 = n2 * l2
            tong3 = n3 * l3
            tong_all = tong1 + tong2 + tong3
            
            tb_all_rat = Rational(tong_all, n_all)
            if (tb_all_rat * 10).q == 1 and l1 != l2 and l2 != l3:
                break
                
        tb_all_str = fmt_dec(tb_all_rat)
        tong12 = tong1 + tong2
        kq_str = str(l3)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một công ty công nghệ chia nhân viên làm $3$ nhóm dự án: nhóm Alpha ($%s$ người), nhóm Beta ($%s$ người) và nhóm Gamma ($%s$ người). Lương trung bình của nhóm Alpha là $%s$ triệu đồng, nhóm Beta là $%s$ triệu đồng. Biết lương trung bình của toàn bộ $%s$ nhân viên trong công ty là $%s$ triệu đồng. Mức lương trung bình (đơn vị: triệu đồng) của nhóm Gamma bằng bao nhiêu?'''
                         %(str(n1), str(n2), str(n3), str(l1), str(l2), str(n_all), tb_all_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Tổng tiền lương của toàn bộ $%s$ nhân viên trong công ty là: \\\\
                   $%s \\cdot %s = %s$ (triệu đồng). \\\\
                   Tổng tiền lương của nhóm Alpha là: \\\\
                   $%s \\cdot %s = %s$ (triệu đồng). \\\\
                   Tổng tiền lương của nhóm Beta là: \\\\
                   $%s \\cdot %s = %s$ (triệu đồng). \\\\
                   Tổng tiền lương của nhóm Gamma là: \\\\
                   $%s - (%s + %s) = %s - %s = %s$ (triệu đồng). \\\\
                   Vậy mức lương trung bình của nhóm Gamma là: \\\\
                   $\\dfrac{%s}{%s} = %s$ (triệu đồng).'''
                   %(str(n_all),
                     str(n_all), tb_all_str, str(tong_all),
                     str(n1), str(l1), str(tong1),
                     str(n2), str(l2), str(tong2),
                     str(tong_all), str(tong1), str(tong2), str(tong_all), str(tong12), str(tong3),
                     str(tong3), str(n3), kq_str
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

