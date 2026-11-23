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


def bt_dang19_p3_b2_c3_ds10(self):
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
    
        n = 15
        while True:
            arr_14 = sorted([randint(15, 38) for _ in range(n - 1)])
            # Đảm bảo q1, q2, q3 rõ ràng và mẫu không giảm
            q2_val = arr_14[7]
            q1_val = arr_14[3]
            q3_val = arr_14[11]
            
            if q1_val < q2_val < q3_val and arr_14[13] >= arr_14[12]:
                delta_q = q3_val - q1_val
                nguong_rat = Rational(q3_val, 1) + Rational(3, 2) * Rational(delta_q, 1)
                m_min = math.floor(float(nguong_rat)) + 1
                if m_min > arr_14[13]:
                    break
    
        mau_str = '; '.join(str(v) for v in arr_14) + '; m'
        nua_trai_str = '; '.join(str(v) for v in arr_14[:7])
        nua_phai_str = '; '.join(str(v) for v in arr_14[8:]) + '; m'
        
        tich_15_rat = Rational(3, 2) * Rational(delta_q, 1)
        tich_15_str = fmt_dec(tich_15_rat)
        nguong_str = fmt_dec(nguong_rat)
        kq_str = str(m_min)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Khảo sát thời gian hoàn thành một bài kiểm tra trực tuyến (đơn vị: phút) của $%s$ thí sinh cho kết quả đã sắp xếp:
    $%s$.
    Theo quy tắc phát hiện giá trị bất thường (ngoại lai), một giá trị được gọi là bất thường nếu nó lớn hơn $Q_3 + 1,5\\Delta_Q$. Giá trị nguyên nhỏ nhất của $m$ để thời gian của thí sinh cuối cùng bị hệ thống đánh dấu là bất thường bằng bao nhiêu?'''
                         %(str(n), mau_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì mẫu số liệu gồm $n = %s$ giá trị đã được sắp xếp theo thứ tự không giảm nên: \\\\
                   - Trung vị của mẫu là giá trị chính giữa (ở vị trí thứ $8$), tức là $Q_2 = %s$. \\\\
                   - Nửa số liệu bên trái $Q_2$ gồm $7$ giá trị là: $%s$ nên tứ phân vị thứ nhất là giá trị chính giữa (ở vị trí thứ $4$ của nửa bên trái): $Q_1 = %s$. \\\\
                   - Nửa số liệu bên phải $Q_2$ gồm $7$ giá trị là: $%s$ nên tứ phân vị thứ ba là giá trị chính giữa (ở vị trí thứ $4$ của nửa bên phải, tức vị trí thứ $12$ của mẫu): $Q_3 = %s$. \\\\
                   Khoảng tứ phân vị của mẫu số liệu là: \\\\
                   $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$. \\\\
                   Ngưỡng trên để xác định giá trị bất thường là: \\\\
                   $Q_3 + 1,5\\Delta_Q = %s + 1,5 \\cdot %s = %s + %s = %s$. \\\\
                   Để thời gian $m$ của thí sinh cuối cùng bị đánh dấu là bất thường (và thỏa mãn thứ tự không giảm $m \\ge %s$) thì: \\\\
                   $m > %s$. \\\\
                   Vì $m$ là số nguyên nên giá trị nguyên nhỏ nhất của $m$ là $%s$.'''
                   %(str(n),
                     str(q2_val),
                     nua_trai_str, str(q1_val),
                     nua_phai_str, str(q3_val),
                     str(q3_val), str(q1_val), str(delta_q),
                     str(q3_val), str(delta_q), str(q3_val), tich_15_str, nguong_str,
                     str(arr_14[13]),
                     nguong_str,
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

