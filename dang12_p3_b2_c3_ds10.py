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


def bt_dang12_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = 10
        while True:
            arr_normal = [randint(35, 65) for _ in range(n - 1)]
            outlier = randint(85, 115)
            arr = arr_normal + [outlier]
            
            tong = sum(arr)
            tb_rat = Rational(tong, n)
            
            arr_sx = sorted(arr)
            mid1 = n // 2 - 1
            mid2 = n // 2
            v1 = arr_sx[mid1]
            v2 = arr_sx[mid2]
            med_rat = Rational(v1 + v2, 2)
            
            diff_rat = abs(tb_rat - med_rat)
            if tb_rat.q in [1, 2, 5, 10] and diff_rat > 0:
                break
                
        random.shuffle(arr)
        mau_str = '; '.join(str(v) for v in arr)
        mau_sx_str = '; '.join(str(v) for v in arr_sx)
        tong_str = ' + '.join(str(v) for v in arr)
        
        def fmt_num(rat_val):
            if rat_val.q == 1:
                return str(rat_val.p)
            else:
                num = Decimal(float(rat_val))
                kq = num.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                return str(kq).replace('.', ',')
                
        tb_str = fmt_num(tb_rat)
        med_str = fmt_num(med_rat)
        kq_str = fmt_num(diff_rat)
        
        if tb_rat >= med_rat:
            tru_str = '%s - %s' %(tb_str, med_str)
        else:
            tru_str = '%s - %s' %(med_str, tb_str)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Kết quả đo nồng độ bụi mịn PM$2,5$ ($\\mu\\text{g}/\\text{m}^3$) tại một ngã tư trong $%s$ khung giờ cao điểm lần lượt là: $%s$. Để đánh giá đúng mức độ ô nhiễm phổ biến mà không bị sai lệch bởi giờ tắc đường cục bộ ($%s$), người ta dùng trung vị thay cho số trung bình. Độ chênh lệch giữa số trung bình và trung vị của mẫu số liệu trên bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục).'''
                         %(str(n), mau_str, str(outlier)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Số trung bình của mẫu số liệu trên là: \\\\
                   $\\overline{x} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s} = %s$ ($\\mu\\text{g}/\\text{m}^3$). \\\\
                   Sắp xếp mẫu số liệu gồm $%s$ giá trị theo thứ tự không giảm, ta được: \\\\
                   $%s$. \\\\
                   Vì mẫu số liệu có $n = %s$ là số chẵn nên trung vị $M_e$ là trung bình cộng của hai giá trị chính giữa (ở vị trí thứ $%s$ và thứ $%s$): \\\\
                   $M_e = \\dfrac{%s + %s}{2} = %s$ ($\\mu\\text{g}/\\text{m}^3$). \\\\
                   Vậy độ chênh lệch giữa số trung bình và trung vị của mẫu số liệu trên là: \\\\
                   $|\\overline{x} - M_e| = %s = %s$ ($\\mu\\text{g}/\\text{m}^3$).'''
                   %(tong_str, str(n), str(tong), str(n), tb_str,
                     str(n),
                     mau_sx_str,
                     str(n), str(mid1 + 1), str(mid2 + 1),
                     str(v1), str(v2), med_str,
                     tru_str, kq_str
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

