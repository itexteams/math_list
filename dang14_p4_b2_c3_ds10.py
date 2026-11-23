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


def bt_dang14_p4_b2_c3_ds10(self):
    def format_num(val):
        if isinstance(val, Decimal):
            val = val.normalize()
            s = format(val, 'f')
            if '.' in s:
                s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        if isinstance(val, float):
            if val.is_integer():
                return str(int(val))
            return str(val).replace('.', ',')
        return str(val)
    
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Sinh ngẫu nhiên dãy 10 số nguyên dương tăng dần (đơn vị: nghìn lượt)
        data = []
        cur = randint(10, 15)
        for _ in range(10):
            data.append(cur)
            cur += randint(2, 5)
            
        # Giá trị đột biến ở khung giờ thứ 11 (lớn hơn hẳn giá trị lớn nhất của 10 khung giờ đầu)
        x11 = data[-1] + randint(40, 60)
        
        data_str = "; ".join(str(v) for v in data)
        
        # Tính toán cho mẫu 10 giá trị
        # Trung vị Me10: trung bình cộng của số thứ 5 (index 4) và số thứ 6 (index 5)
        x5, x6 = data[4], data[5]
        me10_dec = (Decimal(x5) + Decimal(x6)) / Decimal(2)
        me10_str = format_num(me10_dec)
        
        # Nửa số liệu bên phải gồm 5 số cuối: index 5, 6, 7, 8, 9 -> Q3 là số chính giữa (index 7, tức vị trí thứ 8)
        right_10_str = "; ".join(str(v) for v in data[5:])
        q3_10 = data[7]
        
        # Mẫu mới gồm 11 giá trị
        data_11 = data + [x11]
        data_11_str = "; ".join(str(v) for v in data_11)
        
        # Với n = 11:
        # Trung vị Me11 là giá trị đứng ở vị trí thứ 6 (index 5)
        me11 = data_11[5]
        
        # Nửa số liệu bên phải của 11 giá trị gồm 5 giá trị cuối (từ vị trí thứ 7 đến 11: index 6, 7, 8, 9, 10)
        # Tứ phân vị thứ ba Q3' là trung vị của 5 giá trị này -> vị trí thứ 9 (index 8)
        right_11_str = "; ".join(str(v) for v in data_11[6:])
        q3_11 = data_11[8]
        
        # So sánh sự thay đổi của trung vị và Q3
        diff_me = Decimal(me11) - me10_dec
        diff_me_str = format_num(diff_me)
        
        diff_q3 = q3_11 - q3_10
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Lượng người truy cập một trang tin tức trong $10$ khung giờ sáng (đơn vị: nghìn lượt) lần lượt là:
    $$%s.$$
    Ban quản trị muốn nâng cấp máy chủ dựa trên ngưỡng lưu lượng cao (tức từ tứ phân vị thứ ba $Q_3$ trở lên). \\\\
    a) Xác định ngưỡng lưu lượng $Q_3$ để kích hoạt máy chủ dự phòng. \\\\
    b) Nếu trong khung giờ thứ $11$, lượng truy cập đột biến đạt $%s$ nghìn lượt thì trung vị và tứ phân vị thứ ba thay đổi như thế nào?'''
                         %(data_str, x11
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Mẫu số liệu gồm $n = 10$ giá trị đã được sắp xếp theo thứ tự tăng dần:
    $$%s.$$
    Nửa số liệu bên phải gồm $5$ giá trị cuối cùng: $%s$. \\\\
    Tứ phân vị thứ ba $Q_3$ là trung vị của nửa số liệu bên phải (giá trị đứng ở vị trí thứ $8$ của mẫu số liệu ban đầu):
    $$Q_3 = %s \\text{ (nghìn lượt)}.$$
    Vậy ngưỡng lưu lượng để kích hoạt máy chủ dự phòng là $%s$ nghìn lượt.
    \\item Trước khi có khung giờ thứ $11$, mẫu số liệu có $n = 10$ giá trị nên trung vị là trung bình cộng của hai giá trị ở vị trí thứ $5$ và thứ $6$:
    $$M_e = \\dfrac{%s + %s}{2} = %s \\text{ (nghìn lượt)}.$$
    Khi bổ sung thêm khung giờ thứ $11$ với lượng truy cập $%s$ nghìn lượt, ta được mẫu số liệu mới gồm $n' = 11$ giá trị sắp xếp theo thứ tự tăng dần:
    $$%s.$$
    \\begin{itemize}
    \\item Vì cỡ mẫu $n' = 11$ là số lẻ nên trung vị mới là giá trị đứng ở vị trí chính giữa (vị trí thứ $6$):
    $$M_e' = %s \\text{ (nghìn lượt)}.$$
    \\item Nửa số liệu bên phải của mẫu mới gồm $5$ giá trị cuối cùng: $%s$. Tứ phân vị thứ ba mới là trung vị của $5$ giá trị này (giá trị đứng ở vị trí thứ $9$ của mẫu mới):
    $$Q_3' = %s \\text{ (nghìn lượt)}.$$
    \\end{itemize}
    Vậy khi thêm khung giờ thứ $11$, trung vị tăng thêm $%s - %s = %s$ nghìn lượt (từ $%s$ lên $%s$ nghìn lượt) và tứ phân vị thứ ba tăng thêm $%s - %s = %s$ nghìn lượt (từ $%s$ lên $%s$ nghìn lượt).
    \\end{enumEX}'''
                   %(data_str,
                     right_10_str,
                     q3_10,
                     q3_10,
                     x5, x6, me10_str,
                     x11,
                     data_11_str,
                     me11,
                     right_11_str,
                     q3_11,
                     me11, me10_str, diff_me_str, me10_str, me11, q3_11, q3_10, diff_q3, q3_10, q3_11
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

