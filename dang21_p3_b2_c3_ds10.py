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


def bt_dang21_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = 6
        while True:
            # Mẫu gồm 6 số thực x1 <= x2 <= x3 <= x4 <= x5 <= x6
            # Q1 = x2, Q3 = x5, Q2 = (x3 + x4)/2 => x3 + x4 = 2 * Q2
            # Tổng 6 số = 6 * tb = x1 + Q1 + 2*Q2 + Q3 + x6
            x1_val = randint(4, 9)
            q1_val = randint(x1_val + 2, x1_val + 5) # x2
            q2_val = randint(q1_val + 2, q1_val + 5)
            q3_val = randint(q2_val + 3, q2_val + 7) # x5
            x6_val = randint(q3_val + 2, q3_val + 8)
            
            tong = x1_val + q1_val + 2 * q2_val + q3_val + x6_val
            tb_rat = Rational(tong, n)
            if tb_rat.q == 1:
                tb_val = tb_rat.p
                break
                
        tong_x3x4 = 2 * q2_val
        tong_5_so = x1_val + q1_val + tong_x3x4 + q3_val
        kq_str = str(x6_val)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho mẫu số liệu gồm $%s$ số thực $x_1 \\le x_2 \\le x_3 \\le x_4 \\le x_5 \\le x_6$ thỏa mãn: tứ phân vị thứ nhất $Q_1 = %s$, trung vị $Q_2 = %s$, tứ phân vị thứ ba $Q_3 = %s$ và số trung bình của cả $%s$ số là $%s$. Biết giá trị nhỏ nhất $x_1 = %s$, giá trị lớn nhất $x_6$ bằng bao nhiêu?'''
                         %(str(n), str(q1_val), str(q2_val), str(q3_val), str(n), str(tb_val), str(x1_val)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì mẫu số liệu gồm $n = %s$ giá trị đã được sắp xếp theo thứ tự không giảm nên: \\\\
                   - Trung vị của mẫu số liệu là trung bình cộng của hai giá trị chính giữa (ở vị trí thứ $3$ và thứ $4$): \\\\
                   $Q_2 = \\dfrac{x_3 + x_4}{2} \\Leftrightarrow x_3 + x_4 = 2Q_2 = 2 \\cdot %s = %s$. \\\\
                   - Nửa số liệu bên trái $Q_2$ gồm $3$ giá trị là $x_1; x_2; x_3$ nên tứ phân vị thứ nhất là giá trị chính giữa: $Q_1 = x_2 = %s$. \\\\
                   - Nửa số liệu bên phải $Q_2$ gồm $3$ giá trị là $x_4; x_5; x_6$ nên tứ phân vị thứ ba là giá trị chính giữa: $Q_3 = x_5 = %s$. \\\\
                   Mặt khác, số trung bình của cả $%s$ số là $%s$ nên tổng của cả $%s$ số bằng: \\\\
                   $x_1 + x_2 + x_3 + x_4 + x_5 + x_6 = %s \\cdot %s = %s$. \\\\
                   Thay $x_1 = %s$, $x_2 = %s$, $x_3 + x_4 = %s$ và $x_5 = %s$ vào đẳng thức trên, ta được: \\\\
                   $%s + %s + %s + %s + x_6 = %s \\Leftrightarrow %s + x_6 = %s \\Leftrightarrow x_6 = %s$. \\\\
                   Vậy giá trị lớn nhất cần tìm là $x_6 = %s$.'''
                   %(str(n),
                     str(q2_val), str(tong_x3x4),
                     str(q1_val),
                     str(q3_val),
                     str(n), str(tb_val), str(n),
                     str(n), str(tb_val), str(tong),
                     str(x1_val), str(q1_val), str(tong_x3x4), str(q3_val),
                     str(x1_val), str(q1_val), str(tong_x3x4), str(q3_val), str(tong), str(tong_5_so), str(tong), kq_str,
                     kq_str
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

