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


def bt_dang27_p4_b2_c3_ds10(self):
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
    
    def format_2dec(val):
        s = format(val, '.2f')
        return s.replace('.', ',')
    
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            ten1 = "Nam"
            ten2 = "Hùng"
            
            pool_nam = [Decimal(k) / Decimal(100) for k in range(685, 736, 5)]
            nam_valid = random.sample(pool_nam, 5)
            tong_nam = sum(nam_valid)
            
            if (tong_nam * 100) % 6 != 0:
                continue
                
            pool_hung = [Decimal(k) / Decimal(100) for k in range(702, 718)]
            hung_vals = random.sample(pool_hung, 6)
            tong_hung = sum(hung_vals)
            
            if (tong_hung * 100) % 6 != 0:
                continue
                
            tb_nam_6 = tong_nam / Decimal(6)
            tb_hung_6 = tong_hung / Decimal(6)
            tb_nam_5 = tong_nam / Decimal(5)
            
            nam_all = nam_valid + [Decimal('0')]
            random.shuffle(nam_all)
            
            nam_sorted = sorted(nam_all)
            hung_sorted = sorted(hung_vals)
            
            me_nam = (nam_sorted[2] + nam_sorted[3]) / Decimal(2)
            me_hung = (hung_sorted[2] + hung_sorted[3]) / Decimal(2)
            
            # Kiểm tra điều kiện: tb_hung_6 > tb_nam_6, me_nam > me_hung, tb_nam_5 > tb_hung_6
            # và với n = 6: Q1 = nam_sorted[1], Q3 = nam_sorted[4], nguong_duoi = Q1 - 1.5*(Q3 - Q1) > 0
            q1_nam = nam_sorted[1]
            q3_nam = nam_sorted[4]
            dq_nam = q3_nam - q1_nam
            nguong_duoi = q1_nam - Decimal('1.5') * dq_nam
            nguong_tren = q3_nam + Decimal('1.5') * dq_nam
            
            if (tb_hung_6 > tb_nam_6 and me_nam > me_hung and tb_nam_5 > tb_hung_6
                    and nguong_duoi > Decimal('0') and nam_sorted[1] >= nguong_duoi and nam_sorted[5] <= nguong_tren):
                break
    
        # Tạo chuỗi đề bài cho Nam (ghi rõ 0 (phạm quy))
        nam_de_parts = []
        for v in nam_all:
            if v == Decimal('0'):
                nam_de_parts.append("0 \\text{ (phạm quy)}")
            else:
                nam_de_parts.append(format_2dec(v))
        nam_de_str = "; ".join(nam_de_parts)
        
        hung_de_str = "; ".join(format_2dec(v) for v in hung_vals)
        
        # Chuỗi tính toán câu a
        nam_sum_expr = " + ".join("0" if v == Decimal('0') else format_2dec(v) for v in nam_all)
        hung_sum_expr = " + ".join(format_2dec(v) for v in hung_vals)
        
        tong_nam_str = format_num(tong_nam)
        tong_hung_str = format_num(tong_hung)
        tb_nam_6_str = format_num(tb_nam_6)
        tb_hung_6_str = format_num(tb_hung_6)
        
        # Chuỗi tính toán câu b
        nam_sorted_str = "; ".join("0" if v == Decimal('0') else format_2dec(v) for v in nam_sorted)
        hung_sorted_str = "; ".join(format_2dec(v) for v in hung_sorted)
        
        me_nam_str = format_num(me_nam)
        me_hung_str = format_num(me_hung)
        
        # Chuỗi tính toán câu c
        q1_nam_str = format_2dec(q1_nam)
        q3_nam_str = format_2dec(q3_nam)
        dq_nam_str = format_num(dq_nam)
        nguong_duoi_str = format_num(nguong_duoi)
        nguong_tren_str = format_num(nguong_tren)
        
        nam_valid_sorted = sorted(nam_valid)
        nam_valid_str = "; ".join(format_2dec(v) for v in nam_valid_sorted)
        nam_valid_sum_expr = " + ".join(format_2dec(v) for v in nam_valid_sorted)
        tb_nam_5_str = format_num(tb_nam_5)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong môn nhảy xa, mỗi vận động viên thực hiện $6$ lần nhảy. Thành tích của vận động viên %s (đơn vị: mét) qua $6$ lần nhảy là:
    $$%s.$$
    Thành tích của vận động viên %s là:
    $$%s.$$
    a) Nếu tính số trung bình của cả $6$ lần nhảy (lần phạm quy tính $0\\text{m}$) thì vận động viên nào xếp trên? \\\\
    b) Nếu dùng \\textbf{trung vị} của $6$ lần nhảy để xếp hạng nhằm giảm thiểu rủi ro của một lần phạm quy, thì ai xếp trên? \\\\
    c) Hãy đề xuất một quy tắc loại bỏ giá trị bất thường dựa trên $\\Delta_Q$ cho thành tích của %s và tính lại thành tích trung bình của %s sau khi loại bỏ giá trị bất thường đó.'''
                         %(ten1, nam_de_str,
                           ten2, hung_de_str,
                           ten1, ten1
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Thành tích trung bình của cả $6$ lần nhảy của mỗi vận động viên là:
    \\begin{itemize}
    \\item Đối với vận động viên %s:
    $$\\overline{x}_{\\text{%s}} = \\dfrac{%s}{6} = \\dfrac{%s}{6} = %s \\text{ (m)}.$$
    \\item Đối với vận động viên %s:
    $$\\overline{x}_{\\text{%s}} = \\dfrac{%s}{6} = \\dfrac{%s}{6} = %s \\text{ (m)}.$$
    \\end{itemize}
    Vì $%s > %s$ nên nếu tính số trung bình của cả $6$ lần nhảy thì vận động viên \\textbf{%s} xếp trên.
    \\item Sắp xếp thành tích $6$ lần nhảy của hai vận động viên theo thứ tự không giảm:
    \\begin{itemize}
    \\item Thành tích của %s: $%s$. \\\\
    Vì cỡ mẫu $n = 6$ là số chẵn nên trung vị là trung bình cộng của hai giá trị ở vị trí thứ $3$ và thứ $4$:
    $$M_e(\\text{%s}) = \\dfrac{%s + %s}{2} = %s \\text{ (m)}.$$
    \\item Thành tích của %s: $%s$. \\\\
    Trung vị thành tích của %s là:
    $$M_e(\\text{%s}) = \\dfrac{%s + %s}{2} = %s \\text{ (m)}.$$
    \\end{itemize}
    Vì $%s > %s$ nên nếu dùng trung vị để xếp hạng thì vận động viên \\textbf{%s} xếp trên.
    \\item \\textbf{Đề xuất quy tắc:} Sử dụng quy tắc khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$: mọi giá trị nhỏ hơn $Q_1 - 1,5\\Delta_Q$ hoặc lớn hơn $Q_3 + 1,5\\Delta_Q$ được coi là giá trị bất thường (ngoại lệ) và bị loại bỏ khỏi mẫu số liệu. \\\\
    \\textbf{Áp dụng cho thành tích của %s:} \\\\
    Từ dãy số liệu đã sắp xếp của %s là $%s$ ($n = 6$):
    \\begin{itemize}
    \\item Nửa số liệu bên trái gồm $3$ giá trị: $0; %s; %s \\Rightarrow Q_1 = %s \\text{ (m)}$.
    \\item Nửa số liệu bên phải gồm $3$ giá trị: $%s; %s; %s \\Rightarrow Q_3 = %s \\text{ (m)}$.
    \\item Khoảng tứ phân vị là: $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s \\text{ (m)}$.
    \\end{itemize}
    Các ngưỡng xác định giá trị bất thường là:
    $$Q_1 - 1,5\\Delta_Q = %s - 1,5 \\cdot %s = %s \\text{ (m)};$$
    $$Q_3 + 1,5\\Delta_Q = %s + 1,5 \\cdot %s = %s \\text{ (m)}.$$
    Ta thấy lần nhảy phạm quy $0\\text{m} < %s\\text{m}$ là giá trị bất thường duy nhất (các lần nhảy còn lại đều nằm trong đoạn $[%s; %s]$). \\\\
    Loại bỏ giá trị bất thường $0\\text{m}$, thành tích $5$ lần nhảy hợp lệ của %s là:
    $$%s.$$
    Thành tích trung bình mới của %s sau khi loại bỏ giá trị bất thường là:
    $$\\overline{x}_{\\text{mới}} = \\dfrac{%s}{5} = \\dfrac{%s}{5} = %s \\text{ (m)}.$$
    \\end{enumEX}'''
                   %(ten1, ten1, nam_sum_expr, tong_nam_str, tb_nam_6_str,
                     ten2, ten2, hung_sum_expr, tong_hung_str, tb_hung_6_str,
                     tb_hung_6_str, tb_nam_6_str, ten2,
                     ten1, nam_sorted_str,
                     ten1, format_2dec(nam_sorted[2]), format_2dec(nam_sorted[3]), me_nam_str,
                     ten2, hung_sorted_str,
                     ten2, ten2, format_2dec(hung_sorted[2]), format_2dec(hung_sorted[3]), me_hung_str,
                     me_nam_str, me_hung_str, ten1,
                     ten1, ten1, nam_sorted_str,
                     q1_nam_str, format_2dec(nam_sorted[2]), q1_nam_str,
                     format_2dec(nam_sorted[3]), q3_nam_str, format_2dec(nam_sorted[5]), q3_nam_str,
                     q3_nam_str, q1_nam_str, dq_nam_str,
                     q1_nam_str, dq_nam_str, nguong_duoi_str,
                     q3_nam_str, dq_nam_str, nguong_tren_str,
                     nguong_duoi_str, nguong_duoi_str, nguong_tren_str,
                     ten1, nam_valid_str,
                     ten1, nam_valid_sum_expr, tong_nam_str, tb_nam_5_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

