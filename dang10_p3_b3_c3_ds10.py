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


def bt_dang10_p3_b3_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            # Tạo mẫu số liệu gồm 10 số nguyên tăng dần
            x1 = randint(100, 125)
            x2 = x1 + randint(2, 6)
            x3 = x2 + randint(2, 6) # Q1 là x3
            x4 = x3 + randint(2, 5)
            x5 = x4 + randint(2, 5)
            x6 = x5 + randint(2, 5)
            x7 = x6 + randint(2, 5)
            x8 = x7 + randint(2, 6) # Q3 là x8
            x9 = x8 + randint(3, 8)
            x10 = x9 + randint(25, 55) # Giá trị ngoại lai lớn
            
            data = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
            
            q1 = x3
            q3 = x8
            delta_q = q3 - q1
            
            # Ngưỡng trên = Q3 + 1.5 * Delta_Q
            nguong_tren = Rational(q3) + Rational(3, 2) * Rational(delta_q)
            
            # Kiểm tra điều kiện kết quả cuối cùng là số nguyên hoặc số thập phân có đúng 4 ký tự (ví dụ 172,5)
            if nguong_tren.q == 1:
                if -999 < int(nguong_tren) < 9999:
                    kq_str = str(int(nguong_tren))
                    break
            else:
                number = Decimal(float(nguong_tren))
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq).replace('.', ',')
                if len(kq_str) == 4 and -999 < float(kq) < 9999:
                    break
    
        # Tạo chuỗi hiển thị mẫu số liệu
        mau_so_lieu_str = "; \\quad ".join(str(val) for val in data)
        nua_dau_str = "; \\quad ".join(str(val) for val in data[:5])
        nua_sau_str = "; \\quad ".join(str(val) for val in data[5:])
        
        # Định dạng hiển thị 1.5 * Delta_Q
        tich_15_dq = Rational(3, 2) * Rational(delta_q)
        if tich_15_dq.q == 1:
            tich_15_dq_str = str(int(tich_15_dq))
        else:
            tich_15_dq_str = str(float(tich_15_dq)).replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Thời gian hoàn thành bài thi chạy bộ (đơn vị: phút) của $10$ thí sinh trong một cuộc thi phong trào được ghi lại như sau:\\\\
    $$%s$$
    Theo quy tắc $1,5 \\cdot \\Delta_Q$, giá trị ngưỡng trên để xác định thời gian chạy bất thường (quá chậm) của mẫu số liệu này là bao nhiêu phút?'''
                         %(mau_so_lieu_str))
        
        # Nội dung lời giải
        loigiai = ('''Mẫu số liệu đã được sắp xếp theo thứ tự không giảm gồm $10$ giá trị.\\\\
    Ta chia mẫu số liệu thành hai nửa bằng nhau:\\\\
    - Nửa số liệu bên trái gồm $5$ giá trị: $%s$. Trung vị của nửa số liệu bên trái là tứ phân vị thứ nhất, nên $Q_1 = %s$.\\\\
    - Nửa số liệu bên phải gồm $5$ giá trị: $%s$. Trung vị của nửa số liệu bên phải là tứ phân vị thứ ba, nên $Q_3 = %s$.\\\\
    Khoảng tứ phân vị của mẫu số liệu là:
    $$\\Delta_Q = Q_3 - Q_1 = %s - %s = %s.$$
    Theo quy tắc $1,5 \\cdot \\Delta_Q$, giá trị ngưỡng trên để xác định thời gian chạy bất thường (quá chậm) là:
    $$Q_3 + 1,5 \\cdot \\Delta_Q = %s + 1,5 \\cdot %s = %s + %s = %s \\text{ (phút)}.$$'''
                   %(nua_dau_str, str(q1),
                     nua_sau_str, str(q3),
                     str(q3), str(q1), str(delta_q),
                     str(q3), str(delta_q), str(q3), tich_15_dq_str, kq_str))
        
        # Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

