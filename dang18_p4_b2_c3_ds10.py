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


def bt_dang18_p4_b2_c3_ds10(self):
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
    
    def format_1dec(val):
        s = format(val, '.1f')
        return s.replace('.', ',')
    
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Sinh ngẫu nhiên dãy 13 chỉ số đường huyết sắp xếp không giảm:
        # 12 giá trị bình thường nằm trong [4.4, 6.4] và 1 giá trị bất thường lớn nằm trong [9.2, 11.5]
        # Đảm bảo tổng 12 giá trị bình thường chia hết cho 12 (tức tổng nhân 10 chia hết cho 12) để số trung bình đẹp
        while True:
            pool = [Decimal(k) / Decimal(10) for k in range(44, 65)]
            normal_vals = sorted(random.sample(pool, 12))
            tong_normal = sum(normal_vals)
            
            # Kiểm tra để trung bình 12 bệnh nhân bình thường có tối đa 2 chữ số thập phân đẹp
            if (tong_normal * 100) % 12 != 0:
                continue
                
            outlier = Decimal(randint(92, 115)) / Decimal(10)
            data = normal_vals + [outlier]
            
            # Tính Q1, Q3 cho n = 13:
            # Trung vị là phần tử thứ 7 (index 6)
            # Nửa trái gồm 6 phần tử đầu (index 0..5) -> Q1 = (data[2] + data[3]) / 2
            # Nửa phải gồm 6 phần tử cuối (index 7..12) -> Q3 = (data[9] + data[10]) / 2
            q1 = (data[2] + data[3]) / Decimal(2)
            q3 = (data[9] + data[10]) / Decimal(2)
            delta_q = q3 - q1
            
            nguong_duoi = q1 - Decimal('1.5') * delta_q
            nguong_tren = q3 + Decimal('1.5') * delta_q
            
            # Đảm bảo chỉ có duy nhất outlier vượt ngưỡng trên và không giá trị nào dưới ngưỡng dưới
            if data[0] >= nguong_duoi and data[11] <= nguong_tren and outlier > nguong_tren:
                break
    
        data_str = "; ".join(format_1dec(v) for v in data)
        
        left_str = "; ".join(format_1dec(v) for v in data[:6])
        right_str = "; ".join(format_1dec(v) for v in data[7:])
        
        x3_str = format_1dec(data[2])
        x4_str = format_1dec(data[3])
        q1_str = format_num(q1)
        
        x10_str = format_1dec(data[9])
        x11_str = format_1dec(data[10])
        q3_str = format_num(q3)
        
        delta_q_str = format_num(delta_q)
        nguong_duoi_str = format_num(nguong_duoi)
        nguong_tren_str = format_num(nguong_tren)
        outlier_str = format_1dec(outlier)
        
        normal_str = "; ".join(format_1dec(v) for v in normal_vals)
        normal_sum_expr = " + ".join(format_1dec(v) for v in normal_vals)
        tong_normal_str = format_num(tong_normal)
        
        tb_normal = tong_normal / Decimal(12)
        tb_normal_str = format_num(tb_normal)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Chỉ số đường huyết lúc đói (đơn vị: $\\text{mmol/L}$) của $13$ bệnh nhân tham gia tầm soát sức khỏe được ghi lại như sau:
    $$%s.$$
    Sử dụng quy tắc khoảng tứ phân vị (giá trị nhỏ hơn $Q_1 - 1,5\\Delta_Q$ hoặc lớn hơn $Q_3 + 1,5\\Delta_Q$ là giá trị bất thường), hãy xác định bệnh nhân nào có chỉ số bất thường và tính lại chỉ số đường huyết trung bình của nhóm bệnh nhân bình thường còn lại.'''
                         %(data_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Mẫu số liệu gồm $n = 13$ giá trị đã được sắp xếp theo thứ tự không giảm:
    $$%s.$$
    Vì cỡ mẫu $n = 13$ là số lẻ nên trung vị là giá trị đứng ở vị trí thứ $7$ ($M_e = %s$).
    \\begin{itemize}
    \\item Nửa số liệu bên trái gồm $6$ giá trị: $%s$. Tứ phân vị thứ nhất là trung bình cộng của hai giá trị ở vị trí thứ $3$ và thứ $4$:
    $$Q_1 = \\dfrac{%s + %s}{2} = %s.$$
    \\item Nửa số liệu bên phải gồm $6$ giá trị: $%s$. Tứ phân vị thứ ba là trung bình cộng của hai giá trị ở vị trí thứ $10$ và thứ $11$:
    $$Q_3 = \\dfrac{%s + %s}{2} = %s.$$
    \\item Khoảng tứ phân vị của mẫu số liệu là:
    $$\\Delta_Q = Q_3 - Q_1 = %s - %s = %s.$$
    \\end{itemize}
    Ta xác định các ngưỡng giá trị bất thường:
    $$Q_1 - 1,5\\Delta_Q = %s - 1,5 \\cdot %s = %s;$$
    $$Q_3 + 1,5\\Delta_Q = %s + 1,5 \\cdot %s = %s.$$
    So sánh với mẫu số liệu ban đầu, ta thấy chỉ có giá trị $%s > %s$ (các giá trị còn lại đều nằm trong đoạn $[%s; %s]$). \\\\
    Vậy bệnh nhân có chỉ số đường huyết bất thường là bệnh nhân có chỉ số $%s\\text{ mmol/L}$ (bệnh nhân cuối cùng trong dãy số liệu). \\\\
    Sau khi loại bỏ giá trị bất thường này, nhóm bệnh nhân bình thường còn lại gồm $12$ người với dãy chỉ số đường huyết là:
    $$%s.$$
    Chỉ số đường huyết trung bình của nhóm bệnh nhân bình thường còn lại là:
    $$\\overline{x} = \\dfrac{%s}{12} = \\dfrac{%s}{12} = %s \\text{ (mmol/L)}.$$'''
                   %(data_str,
                     format_1dec(data[6]),
                     left_str, x3_str, x4_str, q1_str,
                     right_str, x10_str, x11_str, q3_str,
                     q3_str, q1_str, delta_q_str,
                     q1_str, delta_q_str, nguong_duoi_str,
                     q3_str, delta_q_str, nguong_tren_str,
                     outlier_str, nguong_tren_str, nguong_duoi_str, nguong_tren_str,
                     outlier_str,
                     normal_str,
                     normal_sum_expr, tong_normal_str, tb_normal_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

