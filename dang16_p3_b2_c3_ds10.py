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


def bt_dang16_p3_b2_c3_ds10(self):
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
            n = random.choice([10, 12, 14])
            p_tang = random.choice([10, 15, 20, 25, 30])
            arr = [randint(40, 75) for _ in range(n)]
            
            arr_sx = sorted(arr)
            mid1 = n // 2 - 1
            mid2 = n // 2
            v1 = arr_sx[mid1]
            v2 = arr_sx[mid2]
            
            med_cu_rat = Rational(v1 + v2, 2)
            he_so_rat = Rational(100 + p_tang, 100)
            med_moi_rat = med_cu_rat * he_so_rat
            
            if (med_cu_rat * 10).q == 1 and (med_moi_rat * 100).q == 1:
                break
                
        mau_str = '; '.join(str(v) for v in arr)
        mau_sx_str = '; '.join(str(v) for v in arr_sx)
        med_cu_str = fmt_dec(med_cu_rat)
        he_so_str = fmt_dec(he_so_rat)
        kq_str = fmt_dec(med_moi_rat)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cửa hàng tiện lợi ghi nhận lượng khách hàng thanh toán qua ví điện tử trong $%s$ ngày: $%s$. Nếu tất cả các ngày này lượng khách đều tăng thêm $%s\\%%$ nhờ chương trình khuyến mãi mới, thì trung vị mới của mẫu số liệu bằng bao nhiêu?'''
                         %(str(n), mau_str, str(p_tang)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Sắp xếp mẫu số liệu ban đầu gồm $%s$ giá trị theo thứ tự không giảm, ta được: \\\\
                   $%s$. \\\\
                   Vì mẫu số liệu có $n = %s$ là số chẵn nên trung vị ban đầu của mẫu số liệu là trung bình cộng của hai giá trị chính giữa (ở vị trí thứ $%s$ và thứ $%s$): \\\\
                   $M_e = \\dfrac{%s + %s}{2} = %s$. \\\\
                   Khi tất cả các giá trị trong mẫu số liệu đều tăng thêm $%s\\%%$, tức là mỗi giá trị đều được nhân với cùng một hằng số $1 + %s\\%% = %s > 0$, thì thứ tự sắp xếp của các giá trị không đổi. \\\\
                   Do đó, trung vị mới của mẫu số liệu cũng tăng lên $%s\\%%$ và bằng: \\\\
                   $M_e' = %s \\cdot %s = %s$.'''
                   %(str(n),
                     mau_sx_str,
                     str(n), str(mid1 + 1), str(mid2 + 1),
                     str(v1), str(v2), med_cu_str,
                     str(p_tang), str(p_tang), he_so_str,
                     str(p_tang),
                     med_cu_str, he_so_str, kq_str
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

