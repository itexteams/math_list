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


def bt_dang27_p3_b2_c3_ds10(self):
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
    
        n = 10
        while True:
            arr = sorted(random.sample(range(100, 165), n))
            # arr[4] < arr[5], trung vị là (arr[4] + arr[5])/2
            # Nửa trái gồm 5 số đầu đều nhỏ hơn trung vị -> cộng thêm hut
            # Nửa phải gồm 5 số cuối đều lớn hơn trung vị -> trừ đi vuot
            hut = randint(2, 5)
            vuot = randint(2, 6)
            
            arr_thuc = [v + hut for v in arr[:5]] + [v - vuot for v in arr[5:]]
            # Đảm bảo sau khi hiệu chỉnh mẫu vẫn giữ nguyên thứ tự không giảm
            if arr_thuc[4] <= arr_thuc[5]:
                break
    
        mau_str = '; '.join(str(v) for v in arr)
        mau_thuc_str = '; '.join(str(v) for v in arr_thuc)
        
        med_cu_rat = Rational(arr[4] + arr[5], 2)
        med_cu_str = fmt_dec(med_cu_rat)
        
        nua_trai_thuc_str = '; '.join(str(v) for v in arr_thuc[:5])
        nua_phai_thuc_str = '; '.join(str(v) for v in arr_thuc[5:])
        
        q1_thuc = arr_thuc[2]
        q3_thuc = arr_thuc[7]
        delta_q = q3_thuc - q1_thuc
        kq_str = str(delta_q)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một trạm thủy văn đo mực nước sông (đơn vị: cm) lúc $7$h sáng trong $%s$ ngày đầu mùa lũ, thu được mẫu số liệu đã sắp xếp không giảm:
    $%s$.
    Do sai số thiết bị cảm biến, tất cả các số đo nhỏ hơn trung vị đều bị hụt đi $%s$ cm so với thực tế, còn các số đo lớn hơn trung vị đều bị vượt quá $%s$ cm so với thực tế. Khoảng tứ phân vị $\\Delta_Q$ của mẫu số liệu thực tế sau khi đã hiệu chỉnh sai số bằng bao nhiêu?'''
                         %(str(n), mau_str, str(hut), str(vuot)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Mẫu số liệu ban đầu gồm $n = %s$ giá trị đã sắp xếp không giảm nên trung vị ban đầu là trung bình cộng của hai giá trị chính giữa (ở vị trí thứ $5$ và thứ $6$): \\\\
                   $M_e = \\dfrac{%s + %s}{2} = %s$ (cm). \\\\
                   Nhận thấy $5$ số liệu đầu tiên đều nhỏ hơn $%s$ (nên phải cộng thêm $%s$ cm) và $5$ số liệu cuối cùng đều lớn hơn $%s$ (nên phải trừ đi $%s$ cm). \\\\
                   Sau khi hiệu chỉnh sai số, ta thu được mẫu số liệu thực tế (vẫn giữ nguyên thứ tự không giảm) là: \\\\
                   $%s$. \\\\
                   Khi đó: \\\\
                   - Nửa số liệu bên trái trung vị mới gồm $5$ giá trị là: $%s$ nên tứ phân vị thứ nhất là giá trị chính giữa: $Q_1 = %s$ (cm). \\\\
                   - Nửa số liệu bên phải trung vị mới gồm $5$ giá trị là: $%s$ nên tứ phân vị thứ ba là giá trị chính giữa: $Q_3 = %s$ (cm). \\\\
                   Vậy khoảng tứ phân vị của mẫu số liệu thực tế là: \\\\
                   $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$ (cm).'''
                   %(str(n),
                     str(arr[4]), str(arr[5]), med_cu_str,
                     med_cu_str, str(hut), med_cu_str, str(vuot),
                     mau_thuc_str,
                     nua_trai_thuc_str, str(q1_thuc),
                     nua_phai_thuc_str, str(q3_thuc),
                     str(q3_thuc), str(q1_thuc), kq_str
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

