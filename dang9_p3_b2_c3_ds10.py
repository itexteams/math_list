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


def bt_dang9_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = random.choice([7, 9, 11])
        arr = [randint(20, 45) for _ in range(n)]
        mau_str = '; '.join(str(v) for v in arr)
        
        arr_sx = sorted(arr)
        mau_sx_str = '; '.join(str(v) for v in arr_sx)
        
        mid_idx = n // 2
        q2_val = arr_sx[mid_idx]
        
        nua_trai = arr_sx[:mid_idx]
        nua_phai = arr_sx[mid_idx + 1:]
        
        nua_trai_str = '; '.join(str(v) for v in nua_trai)
        nua_phai_str = '; '.join(str(v) for v in nua_phai)
        
        m = len(nua_trai)
        if m % 2 == 1:
            q1_rat = Rational(nua_trai[m // 2], 1)
            q3_rat = Rational(nua_phai[m // 2], 1)
            q1_str = str(q1_rat.p)
            q3_str = str(q3_rat.p)
            buoc_q1_q3 = ('''Nửa số liệu bên trái $Q_2$ gồm $%s$ giá trị là: $%s$ nên tứ phân vị thứ nhất là $Q_1 = %s$. \\\\
                   Nửa số liệu bên phải $Q_2$ gồm $%s$ giá trị là: $%s$ nên tứ phân vị thứ ba là $Q_3 = %s$.'''
                   %(str(m), nua_trai_str, q1_str, str(m), nua_phai_str, q3_str))
        else:
            q1_rat = Rational(nua_trai[m // 2 - 1] + nua_trai[m // 2], 2)
            q3_rat = Rational(nua_phai[m // 2 - 1] + nua_phai[m // 2], 2)
            q1_str = str(q1_rat.p) if q1_rat.q == 1 else str(Decimal(float(q1_rat)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
            q3_str = str(q3_rat.p) if q3_rat.q == 1 else str(Decimal(float(q3_rat)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
            buoc_q1_q3 = ('''Nửa số liệu bên trái $Q_2$ gồm $%s$ giá trị là: $%s$ nên tứ phân vị thứ nhất là $Q_1 = \\dfrac{%s + %s}{2} = %s$. \\\\
                   Nửa số liệu bên phải $Q_2$ gồm $%s$ giá trị là: $%s$ nên tứ phân vị thứ ba là $Q_3 = \\dfrac{%s + %s}{2} = %s$.'''
                   %(str(m), nua_trai_str, str(nua_trai[m // 2 - 1]), str(nua_trai[m // 2]), q1_str,
                     str(m), nua_phai_str, str(nua_phai[m // 2 - 1]), str(nua_phai[m // 2]), q3_str))
                     
        delta_q = q3_rat - q1_rat
        if delta_q.q == 1:
            kq_str = str(delta_q.p)
        else:
            number = Decimal(float(delta_q))
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq_str = str(kq).replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Thống kê số lượng đơn hàng giao thành công mỗi ngày của một shipper trong $%s$ ngày liên tiếp cho kết quả: $%s$. Khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$ của mẫu số liệu bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                         %(str(n), mau_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Sắp xếp mẫu số liệu gồm $%s$ giá trị theo thứ tự không giảm, ta được: \\\\
                   $%s$. \\\\
                   Vì mẫu số liệu có $n = %s$ là số lẻ nên trung vị của mẫu là giá trị chính giữa (ở vị trí thứ $%s$), tức là $Q_2 = %s$. \\\\
                   %s \\\\
                   Vậy khoảng tứ phân vị của mẫu số liệu đã cho là: \\\\
                   $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$.'''
                   %(str(n),
                     mau_sx_str,
                     str(n), str(mid_idx + 1), str(q2_val),
                     buoc_q1_q3,
                     q3_str, q1_str, kq_str
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

