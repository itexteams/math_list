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


def bt_dang16_p4_b2_c3_ds10(self):
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
        # Sinh ngẫu nhiên dãy 15 số liệu quanh mức chuẩn m_chuan (500g hoặc 250g)
        # Đảm bảo có duy nhất 1 mốt (xuất hiện 5 lần) và tổng chia hết cho 15 để số trung bình đẹp
        while True:
            m_chuan = random.choice([250, 500])
            mot_val = random.choice([m_chuan, m_chuan + 1])
            pool = [v for v in range(m_chuan - 3, m_chuan + 4) if v != mot_val]
            others = []
            counts = {mot_val: 5}
            while len(others) < 10:
                c = random.choice(pool)
                if counts.get(c, 0) < 4:
                    others.append(c)
                    counts[c] = counts.get(c, 0) + 1
            data = [mot_val]*5 + others
            random.shuffle(data)
            
            tong = sum(data)
            # Kiểm tra để số trung bình là số thập phân hữu hạn (tối đa 1 chữ số thập phân)
            if (tong * 10) % 15 == 0:
                break
    
        data_str = "; ".join(str(v) for v in data)
        sorted_data = sorted(data)
        sorted_str = "; ".join(str(v) for v in sorted_data)
        
        # Tính các đặc trưng mẫu (n = 15)
        tb_dec = Decimal(tong) / Decimal(15)
        tb_str = format_num(tb_dec)
        
        # Trung vị Q2: vị trí thứ 8 (index 7)
        me_val = sorted_data[7]
        
        # Nửa số liệu bên trái gồm 7 số (index 0..6) -> Q1 là vị trí thứ 4 (index 3)
        left_str = "; ".join(str(v) for v in sorted_data[:7])
        q1_val = sorted_data[3]
        
        # Nửa số liệu bên phải gồm 7 số (index 8..14) -> Q3 là vị trí thứ 12 (index 11)
        right_str = "; ".join(str(v) for v in sorted_data[8:])
        q3_val = sorted_data[11]
        
        # Điều kiện câu b
        sai_lech_max = Decimal('0.5')
        sai_lech_max_str = format_num(sai_lech_max)
        nguong_min = m_chuan - 1
        
        sai_lech_thuc = abs(tb_dec - Decimal(m_chuan))
        sai_lech_thuc_str = format_num(sai_lech_thuc)
        
        so_goi_dat = sum(1 for v in data if v >= nguong_min)
        ty_le_dat = (Decimal(so_goi_dat) * Decimal(100) / Decimal(15)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        ty_le_dat_str = format_num(ty_le_dat)
        
        dk1 = (sai_lech_thuc <= sai_lech_max)
        dk2 = (Decimal(so_goi_dat) / Decimal(15) >= Decimal('0.75'))
        
        if dk1:
            kl_dk1 = "$|\\overline{x} - %s| = |%s - %s| = %s \\le %s\\text{g}$ (thỏa mãn điều kiện thứ nhất)." % (m_chuan, tb_str, m_chuan, sai_lech_thuc_str, sai_lech_max_str)
        else:
            kl_dk1 = "$|\\overline{x} - %s| = |%s - %s| = %s > %s\\text{g}$ (không thỏa mãn điều kiện thứ nhất)." % (m_chuan, tb_str, m_chuan, sai_lech_thuc_str, sai_lech_max_str)
            
        if dk2:
            kl_dk2 = "Số gói có khối lượng từ $%s\\text{g}$ trở lên là $%s$ gói, chiếm tỉ lệ $\\dfrac{%s}{15} \\approx %s\\%% \\ge 75\\%%$ (thỏa mãn điều kiện thứ hai)." % (nguong_min, so_goi_dat, so_goi_dat, ty_le_dat_str)
        else:
            kl_dk2 = "Số gói có khối lượng từ $%s\\text{g}$ trở lên là $%s$ gói, chiếm tỉ lệ $\\dfrac{%s}{15} \\approx %s\\%% < 75\\%%$ (không thỏa mãn điều kiện thứ hai)." % (nguong_min, so_goi_dat, so_goi_dat, ty_le_dat_str)
            
        if dk1 and dk2:
            ket_luan_b = "Vậy lô hàng trên \\textbf{đạt chuẩn}."
        else:
            ket_luan_b = "Vậy lô hàng trên \\textbf{không đạt chuẩn}."
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một dây chuyền đóng gói hạt điều xuất khẩu yêu cầu khối lượng tịnh mỗi gói là $%s\\text{g}$. Kiểm tra ngẫu nhiên $15$ gói thu được kết quả (đơn vị: gam):
    $$%s.$$
    a) Tìm số trung bình, trung vị, tứ phân vị và mốt của mẫu số liệu. \\\\
    b) Một lô hàng được coi là đạt chuẩn nếu số trung bình sai lệch không quá $%s\\text{g}$ so với $%s\\text{g}$ và ít nhất $75\\%%$ số gói kiểm tra có khối lượng từ $%s\\text{g}$ trở lên. Hỏi lô hàng trên có đạt chuẩn không?'''
                         %(m_chuan, data_str, sai_lech_max_str, m_chuan, nguong_min
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Sắp xếp mẫu số liệu theo thứ tự không giảm ta được:
    $$%s.$$
    Mẫu số liệu gồm $n = 15$ giá trị.
    \\begin{itemize}
    \\item Số trung bình cộng của mẫu số liệu là:
    $$\\overline{x} = \\dfrac{%s}{15} = \\dfrac{%s}{15} = %s \\text{ (gam)}.$$
    \\item Vì cỡ mẫu $n = 15$ là số lẻ nên trung vị là giá trị đứng ở vị trí chính giữa (vị trí thứ $8$):
    $$M_e = %s \\text{ (gam)}.$$
    \\item Nửa số liệu bên trái gồm $7$ giá trị: $%s$. Tứ phân vị thứ nhất là trung vị của nửa số liệu bên trái (giá trị ở vị trí thứ $4$):
    $$Q_1 = %s \\text{ (gam)}.$$
    \\item Tứ phân vị thứ hai chính là trung vị: $Q_2 = M_e = %s \\text{ (gam)}$.
    \\item Nửa số liệu bên phải gồm $7$ giá trị: $%s$. Tứ phân vị thứ ba là trung vị của nửa số liệu bên phải (giá trị ở vị trí thứ $12$):
    $$Q_3 = %s \\text{ (gam)}.$$
    \\item Trong mẫu số liệu trên, giá trị $%s$ xuất hiện nhiều nhất ($5$ lần) nên mốt của mẫu số liệu là $M_o = %s \\text{ (gam)}$.
    \\end{itemize}
    \\item Ta kiểm tra hai điều kiện đạt chuẩn của lô hàng:
    \\begin{itemize}
    \\item Độ sai lệch của số trung bình so với $%s\\text{g}$ là: %s
    \\item %s
    \\end{itemize}
    %s
    \\end{enumEX}'''
                   %(sorted_str,
                     " + ".join(str(v) for v in data), tong, tb_str,
                     me_val,
                     left_str, q1_val,
                     me_val,
                     right_str, q3_val,
                     mot_val, mot_val,
                     m_chuan, kl_dk1,
                     kl_dk2,
                     ket_luan_b
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

