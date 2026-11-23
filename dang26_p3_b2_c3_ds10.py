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


def bt_dang26_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = 11
        while True:

            q1_val = randint(3, 7)
            q2_val = randint(q1_val + 2, q1_val + 5)
            q3_val = randint(q2_val + 2, q2_val + 6)
            if q1_val >= 2 and q3_val > q2_val + 1:
                break
    
        
        
        s_min = 2 * q1_val + 4 * q2_val + 3 * q3_val
        kq_str = str(s_min)
        mau_min_str = '0; 0; %s; %s; %s; %s; %s; %s; %s; %s; %s' %(
            str(q1_val), str(q1_val),
            str(q2_val), str(q2_val), str(q2_val), str(q2_val),
            str(q3_val), str(q3_val), str(q3_val)
        )
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho mẫu số liệu gồm $%s$ số tự nhiên không giảm: $a_1 \\le a_2 \\le \\dots \\le a_{11}$. Biết rằng $Q_1 = %s$, $Q_2 = %s$, $Q_3 = %s$ và mẫu số liệu có duy nhất một mốt bằng $%s$. Giá trị nhỏ nhất có thể đạt được của tổng tất cả $%s$ số trong mẫu số liệu đó là bao nhiêu?'''
                         %(str(n), str(q1_val), str(q2_val), str(q3_val), str(q2_val), str(n)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì mẫu số liệu gồm $n = %s$ số tự nhiên đã được sắp xếp theo thứ tự không giảm $a_1 \\le a_2 \\le \\dots \\le a_{11}$ nên: \\\\
                   - Trung vị của mẫu số liệu là $Q_2 = a_6 = %s$. \\\\
                   - Nửa số liệu bên trái $Q_2$ gồm $5$ giá trị $a_1; a_2; a_3; a_4; a_5$ nên tứ phân vị thứ nhất là $Q_1 = a_3 = %s$. \\\\
                   - Nửa số liệu bên phải $Q_2$ gồm $5$ giá trị $a_7; a_8; a_9; a_{10}; a_{11}$ nên tứ phân vị thứ ba là $Q_3 = a_9 = %s$. \\\\
                   Do tính chất không giảm và các số đều là số tự nhiên nên ta luôn có: \\\\
                   $a_1 \\ge 0$, $a_2 \\ge 0$; $a_4 \\ge a_3 = %s$, $a_5 \\ge %s$; $a_7 \\ge a_6 = %s$, $a_8 \\ge %s$; $a_{10} \\ge a_9 = %s$, $a_{11} \\ge %s$. \\\\
                   Xét số lần xuất hiện (tần số) $k$ của giá trị mốt $%s$ trong mẫu số liệu ($k \\ge 2$): \\\\
                   - Nếu $k = 2$: mọi giá trị khác chỉ xuất hiện tối đa $1$ lần, suy ra $a_1 + a_2 \\ge 0 + 1 = 1$, $a_3 + a_4 \\ge %s + %s$, $a_5 + a_6 + a_7 + a_8 \\ge %s + %s + %s + %s$, $a_9 + a_{10} + a_{11} \\ge %s + %s + %s$, do đó tổng $11$ số lớn hơn hoặc bằng $%s$. \\\\
                   - Nếu $k = 3$: mọi giá trị khác xuất hiện tối đa $2$ lần, suy ra $a_8 \\ge %s$ và $a_{11} \\ge %s$, do đó tổng $11$ số lớn hơn hoặc bằng $2 \\cdot %s + 4 \\cdot %s + 3 \\cdot %s + 2 = %s$. \\\\
                   - Nếu $k = 4$: chọn $a_5 = a_6 = a_7 = a_8 = %s$, khi đó $%s$ xuất hiện $4$ lần, các giá trị còn lại có thể đạt giá trị nhỏ nhất là $a_1 = a_2 = 0$, $a_3 = a_4 = %s$ (xuất hiện $2$ lần) và $a_9 = a_{10} = a_{11} = %s$ (xuất hiện $3$ lần). Mẫu số liệu thu được là: $%s$, có duy nhất một mốt là $%s$ và có tổng bằng: \\\\
                   $S = 0 + 0 + 2 \\cdot %s + 4 \\cdot %s + 3 \\cdot %s = %s$. \\\\
                   - Nếu $k \\ge 5$: có ít nhất $5$ số bằng $%s$ (ví dụ $a_4 = a_5 = a_6 = a_7 = a_8 = %s$), khi đó tổng $11$ số lớn hơn hoặc bằng $%s + 5 \\cdot %s + 3 \\cdot %s = %s > %s$. \\\\
                   Vậy giá trị nhỏ nhất có thể đạt được của tổng tất cả $%s$ số trong mẫu số liệu là $%s$.'''
                   %(str(n),
                     str(q2_val),
                     str(q1_val),
                     str(q3_val),
                     str(q1_val), str(q1_val), str(q2_val), str(q2_val), str(q3_val), str(q3_val),
                     str(q2_val),
                     str(q1_val), str(q1_val + 1), str(q2_val), str(q2_val), str(q2_val + 1), str(q2_val + 2), str(q3_val), str(q3_val + 1), str(q3_val + 2), str(s_min + 8),
                     str(q2_val + 1), str(q3_val + 1), str(q1_val), str(q2_val), str(q3_val), str(s_min + 2),
                     str(q2_val), str(q2_val), str(q1_val), str(q3_val), mau_min_str, str(q2_val),
                     str(q1_val), str(q2_val), str(q3_val), kq_str,
                     str(q2_val), str(q2_val), str(q1_val), str(q2_val), str(q3_val), str(s_min + q2_val - q1_val), kq_str,
                     str(n), kq_str
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

