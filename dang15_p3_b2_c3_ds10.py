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


def bt_dang15_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n = 9
        while True:
            # Tạo mẫu số liệu gồm 9 số đã sắp xếp không giảm với x ở vị trí chính giữa (vị trí thứ 5)
            # Để mẫu chỉ có duy nhất một mốt, cho một giá trị (khác x hoặc bằng x) lặp lại 2 lần, các giá trị còn lại xuất hiện 1 lần
            vals = sorted(random.sample(range(1, 20), 8))
            # Chọn vị trí lặp lại để tạo duy nhất một mốt
            rep_idx = randint(0, 7)
            arr_full = vals[:rep_idx] + [vals[rep_idx]] + vals[rep_idx:]
            
            med_val = arr_full[4]
            tong = sum(arr_full)
            tb_rat = Rational(tong, n)
            
            if tb_rat.q != 1:
                break
                
        mau_list = [str(arr_full[i]) if i != 4 else 'x' for i in range(n)]
        mau_str = '; '.join(mau_list)
        mau_full_str = '; '.join(str(v) for v in arr_full)
        tong_str = ' + '.join(str(v) for v in arr_full)
        
        number = Decimal(tong) / Decimal(n)
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Mẫu số liệu thống kê tuổi nghề (đơn vị: năm) của $%s$ kỹ sư tại một trạm biến áp đã sắp xếp không giảm là: $%s$. Biết rằng mẫu số liệu chỉ có duy nhất một mốt và trung vị bằng $%s$. Số trung bình của mẫu số liệu trên bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                         %(str(n), mau_str, str(med_val)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì mẫu số liệu có $n = %s$ giá trị và đã được sắp xếp theo thứ tự không giảm nên trung vị của mẫu là giá trị chính giữa (ở vị trí thứ $5$), tức là $M_e = x$. \\\\
                   Theo đề bài, trung vị bằng $%s$ nên ta suy ra $x = %s$. \\\\
                   Khi đó, mẫu số liệu đầy đủ là: $%s$ (thỏa mãn điều kiện mẫu số liệu chỉ có duy nhất một mốt). \\\\
                   Số trung bình của mẫu số liệu trên là: \\\\
                   $\\overline{x} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s} \\approx %s$ (năm).'''
                   %(str(n),
                     str(med_val), str(med_val),
                     mau_full_str,
                     tong_str, str(n), str(tong), str(n), kq_str
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

