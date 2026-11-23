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
from collections import Counter


def bt_dang9_p4_b2_c3_ds10(self):
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
        # Sinh ngẫu nhiên dãy 12 số liệu (11 số bình thường từ 14 đến 20 và 1 giá trị bất thường lớn từ 26 đến 32)
        # Đảm bảo có duy nhất một mốt và tổng chia hết cho 12 hoặc chia hết cho 4 để số trung bình đẹp (hoặc làm tròn 2 chữ số thập phân)
        while True:
            # Tạo 11 số trong khoảng [14, 20], chọn 1 số xuất hiện 3 lần (làm mốt duy nhất), các số khác tối đa 2 lần
            mot_val = randint(15, 18)
            pool = [v for v in range(14, 21) if v != mot_val]
            others = []
            counts = {mot_val: 3}
            while len(others) < 8:
                c = random.choice(pool)
                if counts.get(c, 0) < 2:
                    others.append(c)
                    counts[c] = counts.get(c, 0) + 1
            outlier = randint(26, 32)
            data = [mot_val]*3 + others + [outlier]
            random.shuffle(data)
            
            tong = sum(data)
            # Kiểm tra để số trung bình là số thập phân hữu hạn đẹp (chia hết cho 12 hoặc mẫu số ước của 4)
            if (tong * 4) % 12 == 0:
                break
    
        data_str = "; ".join(str(v) for v in data)
        sorted_data = sorted(data)
        sorted_str = "; ".join(str(v) for v in sorted_data)
        
        # Tính toán các đặc trưng mẫu (n = 12)
        tb_dec = Decimal(tong) / Decimal(12)
        tb_str = format_num(tb_dec)
        
        # Trung vị Q2: trung bình cộng số thứ 6 (index 5) và số thứ 7 (index 6)
        x6, x7 = sorted_data[5], sorted_data[6]
        q2_dec = (Decimal(x6) + Decimal(x7)) / Decimal(2)
        q2_str = format_num(q2_dec)
        
        # Tứ phân vị thứ nhất Q1: trung vị của 6 số đầu (index 2 và index 3)
        x3, x4 = sorted_data[2], sorted_data[3]
        q1_dec = (Decimal(x3) + Decimal(x4)) / Decimal(2)
        q1_str = format_num(q1_dec)
        
        # Tứ phân vị thứ ba Q3: trung vị của 6 số cuối (index 8 và index 9)
        x9, x10 = sorted_data[8], sorted_data[9]
        q3_dec = (Decimal(x9) + Decimal(x10)) / Decimal(2)
        q3_str = format_num(q3_dec)
        
        # Khoảng lý tưởng
        low_ideal = 15
        high_ideal = 18
        
        # Nhận xét câu b
        if Decimal(low_ideal) <= q2_dec <= Decimal(high_ideal):
            nhan_xet_q2 = "nằm trong khoảng lý tưởng từ $%s\\text{‰}$ đến $%s\\text{‰}$" % (low_ideal, high_ideal)
        else:
            nhan_xet_q2 = "phản ánh sát thực tế phần lớn các ngày đo của vuông tôm"
            
        if tb_dec > Decimal(high_ideal):
            nhan_xet_tb = "bị kéo lệch lên cao (vượt ngưỡng lý tưởng $%s\\text{‰}$)" % high_ideal
        else:
            nhan_xet_tb = "bị kéo lệch lên cao"
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Độ mặn (đơn vị: $\\text{‰}$) của nước tại một vuông tôm được đo vào buổi sáng trong $12$ ngày liên tiếp cho kết quả:
    $$%s.$$
    a) Tìm số trung bình, trung vị, tứ phân vị và mốt của mẫu số liệu trên. \\\\
    b) Biết độ mặn lý tưởng cho tôm sinh trưởng là từ $%s\\text{‰}$ đến $%s\\text{‰}$. Kỹ sư thủy sản muốn dùng một số đặc trưng để báo cáo mức độ mặn phổ biến của vuông tôm trong $12$ ngày qua. Nên chọn số trung bình hay trung vị? Giải thích.'''
                         %(data_str, low_ideal, high_ideal
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Sắp xếp mẫu số liệu theo thứ tự không giảm ta được:
    $$%s.$$
    Mẫu số liệu gồm $n = 12$ giá trị.
    \\begin{itemize}
    \\item Số trung bình cộng của mẫu số liệu là:
    $$\\overline{x} = \\dfrac{%s}{12} = \\dfrac{%s}{12} = %s \\text{ (‰)}.$$
    \\item Vì cỡ mẫu $n = 12$ là số chẵn nên trung vị là trung bình cộng của hai giá trị chính giữa (ở vị trí thứ $6$ và thứ $7$):
    $$M_e = \\dfrac{%s + %s}{2} = %s \\text{ (‰)}.$$
    \\item Nửa số liệu bên trái gồm $6$ giá trị: $%s; %s; %s; %s; %s; %s$. Tứ phân vị thứ nhất là trung vị của nửa số liệu bên trái:
    $$Q_1 = \\dfrac{%s + %s}{2} = %s \\text{ (‰)}.$$
    \\item Tứ phân vị thứ hai chính là trung vị: $Q_2 = M_e = %s \\text{ (‰)}$.
    \\item Nửa số liệu bên phải gồm $6$ giá trị: $%s; %s; %s; %s; %s; %s$. Tứ phân vị thứ ba là trung vị của nửa số liệu bên phải:
    $$Q_3 = \\dfrac{%s + %s}{2} = %s \\text{ (‰)}.$$
    \\item Trong mẫu số liệu trên, giá trị $%s$ xuất hiện nhiều nhất ($3$ lần) nên mốt của mẫu số liệu là $M_o = %s \\text{ (‰)}$.
    \\end{itemize}
    \\item Kỹ sư thủy sản nên chọn \\textbf{trung vị} ($M_e = %s\\text{‰}$) để báo cáo mức độ mặn phổ biến của vuông tôm trong $12$ ngày qua. \\\\
    \\textbf{Giải thích:} Trong mẫu số liệu có xuất hiện giá trị bất thường rất lớn là $%s\\text{‰}$ (cao hơn hẳn so với các ngày còn lại). Giá trị ngoại lệ này làm cho số trung bình cộng %s ($\overline{x} = %s\\text{‰}$), không đại diện chính xác cho xu thế chung. Trong khi đó, trung vị không bị ảnh hưởng bởi giá trị bất thường này và %s, phản ánh đúng mức độ mặn phổ biến của vuông tôm.
    \\end{enumEX}'''
                   %(sorted_str,
                     " + ".join(str(v) for v in data), tong, tb_str,
                     x6, x7, q2_str,
                     sorted_data[0], sorted_data[1], sorted_data[2], sorted_data[3], sorted_data[4], sorted_data[5],
                     x3, x4, q1_str,
                     q2_str,
                     sorted_data[6], sorted_data[7], sorted_data[8], sorted_data[9], sorted_data[10], sorted_data[11],
                     x9, x10, q3_str,
                     mot_val, mot_val,
                     q2_str,
                     outlier, nhan_xet_tb, tb_str, nhan_xet_q2
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

