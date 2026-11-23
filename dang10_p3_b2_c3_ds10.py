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


def bt_dang10_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            n1 = randint(10, 16)
            n2 = randint(3, 6)
            n_tong = n1 + n2
            tb1 = randint(175, 188)
            tb_tong = tb1 + random.choice([-2, -1, 1, 2, 3])
            
            tong1 = n1 * tb1
            tong_all = n_tong * tb_tong
            tong2 = tong_all - tong1
            
            tb2_rat = Rational(tong2, n2)
            if tb2_rat.q == 1 and 170 <= tb2_rat.p <= 205:
                kq_str = str(tb2_rat.p)
                break
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một đội bóng rổ gồm $%s$ cầu thủ có chiều cao trung bình là $%s$ cm. Sau khi huấn luyện viên bổ sung thêm $%s$ cầu thủ dự bị thì chiều cao trung bình của cả $%s$ người là $%s$ cm. Chiều cao trung bình (đơn vị: cm) của $%s$ cầu thủ mới được bổ sung bằng bao nhiêu?'''
                         %(str(n1), str(tb1), str(n2), str(n_tong), str(tb_tong), str(n2)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Tổng chiều cao của $%s$ cầu thủ ban đầu là: \\\\
                   $%s \\cdot %s = %s$ (cm). \\\\
                   Tổng chiều cao của cả $%s$ cầu thủ sau khi bổ sung là: \\\\
                   $%s \\cdot %s = %s$ (cm). \\\\
                   Tổng chiều cao của $%s$ cầu thủ dự bị mới được bổ sung là: \\\\
                   $%s - %s = %s$ (cm). \\\\
                   Chiều cao trung bình của $%s$ cầu thủ mới được bổ sung là: \\\\
                   $\\dfrac{%s}{%s} = %s$ (cm).'''
                   %(str(n1),
                     str(n1), str(tb1), str(tong1),
                     str(n_tong),
                     str(n_tong), str(tb_tong), str(tong_all),
                     str(n2),
                     str(tong_all), str(tong1), str(tong2),
                     str(n2),
                     str(tong2), str(n2), kq_str
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

