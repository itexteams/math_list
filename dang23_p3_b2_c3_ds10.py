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


def bt_dang23_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = random.choice([8, 10, 12, 14])
        while True:
            x_tb = randint(15, 30)
            me_cu = x_tb + random.choice([-4, -3, -2, 2, 3, 4])
            a_val = randint(-5, -1)
            b_val = randint(30, 90)
            
            y_tb = a_val * x_tb + b_val
            me_moi = a_val * me_cu + b_val
            
            if y_tb > 0 and me_moi > 0:
                break
                
        c_val = randint(5, 15)
        t_val = c_val * a_val + b_val
        kq_str = str(t_val)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một mẫu số liệu gốc gồm $%s$ số thực có số trung bình $\\overline{x} = %s$ và trung vị $M_e = %s$. Người ta thực hiện phép biến đổi tuyến tính mỗi giá trị $x_i$ của mẫu gốc thành $y_i = ax_i + b$ (với $a < 0$) để thu được mẫu số liệu mới có số trung bình bằng $%s$ và trung vị bằng $%s$. Giá trị của biểu thức $T = %sa + b$ bằng bao nhiêu?'''
                         %(str(n), str(x_tb), str(me_cu), str(y_tb), str(me_moi), str(c_val)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Khi thực hiện phép biến đổi tuyến tính $y_i = ax_i + b$ với $a < 0$ cho từng giá trị của mẫu số liệu gốc: \\\\
                   - Số trung bình của mẫu số liệu mới là $\\overline{y} = a\\overline{x} + b$. \\\\
                   - Vì $a < 0$ nên thứ tự sắp xếp không giảm của mẫu số liệu gốc sẽ đảo ngược thành thứ tự không tăng ở mẫu số liệu mới; tuy nhiên, vị trí chính giữa (trung vị) vẫn được bảo toàn, tức là $M_e' = aM_e + b$. \\\\
                   Theo đề bài, ta có hệ phương trình: \\\\
                   $\\left\\{\\begin{aligned} %sa + b &= %s \\\\ %sa + b &= %s \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} a &= %s \\\\ b &= %s \\end{aligned}\\right.$ (thỏa mãn điều kiện $a < 0$). \\\\
                   Vậy giá trị của biểu thức cần tìm là: \\\\
                   $T = %sa + b = %s \\cdot (%s) + %s = %s$.'''
                   %(str(x_tb), str(y_tb),
                     str(me_cu), str(me_moi),
                     str(a_val), str(b_val),
                     str(c_val), str(c_val), str(a_val), str(b_val), kq_str
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

