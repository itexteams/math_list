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


def bt_dang13_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = random.choice([10, 12, 14, 16])
        arr = [randint(0, 7) for _ in range(n)]
        mau_str = '; '.join(str(v) for v in arr)
        
        arr_sx = sorted(arr)
        mau_sx_str = '; '.join(str(v) for v in arr_sx)
        
        mid1 = n // 2 - 1
        mid2 = n // 2
        v1 = arr_sx[mid1]
        v2 = arr_sx[mid2]
        
        q2_rat = Rational(v1 + v2, 2)
        if q2_rat.q == 1:
            q2_str = str(q2_rat.p)
        else:
            q2_str = str(Decimal(float(q2_rat)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
            
        nua_phai = arr_sx[mid2:]
        nua_phai_str = '; '.join(str(v) for v in nua_phai)
        m = len(nua_phai)
        
        if m % 2 == 1:
            q3_idx = m // 2
            q3_val = nua_phai[q3_idx]
            kq_str = str(q3_val)
            buoc_q3 = ('''Vì $m = %s$ là số lẻ nên tứ phân vị thứ ba $Q_3$ là giá trị chính giữa của nửa số liệu bên phải (ở vị trí thứ $%s$ của nửa bên phải), tức là $Q_3 = %s$.'''
                       %(str(m), str(q3_idx + 1), kq_str))
        else:
            q3_idx1 = m // 2 - 1
            q3_idx2 = m // 2
            qv1 = nua_phai[q3_idx1]
            qv2 = nua_phai[q3_idx2]
            q3_rat = Rational(qv1 + qv2, 2)
            if q3_rat.q == 1:
                kq_str = str(q3_rat.p)
            else:
                kq_str = str(Decimal(float(q3_rat)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
            buoc_q3 = ('''Vì $m = %s$ là số chẵn nên tứ phân vị thứ ba $Q_3$ là trung bình cộng của hai giá trị chính giữa của nửa số liệu bên phải (ở vị trí thứ $%s$ và thứ $%s$ của nửa bên phải): \\\\
                   $Q_3 = \\dfrac{%s + %s}{2} = %s$.'''
                       %(str(m), str(q3_idx1 + 1), str(q3_idx2 + 1), str(qv1), str(qv2), kq_str))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một xưởng may thống kê số áo lỗi phát hiện được trên $%s$ lô hàng như sau: $%s$. Tứ phân vị thứ ba ($Q_3$) của mẫu số liệu trên bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                         %(str(n), mau_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Sắp xếp mẫu số liệu gồm $%s$ giá trị theo thứ tự không giảm, ta được: \\\\
                   $%s$. \\\\
                   Vì mẫu số liệu có $n = %s$ là số chẵn nên trung vị của mẫu là trung bình cộng của hai giá trị chính giữa (ở vị trí thứ $%s$ và thứ $%s$): \\\\
                   $Q_2 = \\dfrac{%s + %s}{2} = %s$. \\\\
                   Nửa số liệu bên phải $Q_2$ gồm $m = %s$ giá trị là: $%s$. \\\\
                   %s'''
                   %(str(n),
                     mau_sx_str,
                     str(n), str(mid1 + 1), str(mid2 + 1),
                     str(v1), str(v2), q2_str,
                     str(m), nua_phai_str,
                     buoc_q3
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

