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


def bt_dang11_p4_b2_c3_ds10(self):
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
        # Sinh ngẫu nhiên dữ liệu bài toán đảm bảo x, y nguyên dương, số trung bình thập phân đẹp
        while True:
            N = random.choice([36, 40, 44, 48])
            n0 = randint(8, 15)
            n1 = randint(7, 13)
            x_val = randint(4, 10)
            n3 = randint(3, 8)
            y_val = randint(2, 6)
            n5 = randint(1, 4)
            
            if n0 + n1 + x_val + n3 + y_val + n5 == N:
                tong_lan = 0*n0 + 1*n1 + 2*x_val + 3*n3 + 4*y_val + 5*n5
                # Kiểm tra trung bình là số thập phân hữu hạn tối đa 2 chữ số
                if (tong_lan * 100) % N == 0:
                    break
    
        tb_dec = Decimal(tong_lan) / Decimal(N)
        tb_str = format_num(tb_dec)
        
        tong_biet = n0 + n1 + n3 + n5
        tong_xy = N - tong_biet
        
        tong_lan_biet = 1*n1 + 3*n3 + 5*n5
        tong_2x_4y = tong_lan - tong_lan_biet
        tong_x_2y = tong_2x_4y // 2
        
        # Khôi phục danh sách đầy đủ để tìm Q1, Q3 chính xác
        full_data = [0]*n0 + [1]*n1 + [2]*x_val + [3]*n3 + [4]*y_val + [5]*n5
        half = N // 2
        left_half = full_data[:half]
        right_half = full_data[half:]
        
        # Vì N chọn là bội của 4 (36, 40, 44, 48) nên half (18, 20, 22, 24) là số chẵn
        idx_q1_1 = half // 2 - 1
        idx_q1_2 = half // 2
        v_q1_1 = left_half[idx_q1_1]
        v_q1_2 = left_half[idx_q1_2]
        q1_dec = (Decimal(v_q1_1) + Decimal(v_q1_2)) / Decimal(2)
        q1_str = format_num(q1_dec)
        
        idx_q3_1 = half + half // 2 - 1
        idx_q3_2 = half + half // 2
        v_q3_1 = full_data[idx_q3_1]
        v_q3_2 = full_data[idx_q3_2]
        q3_dec = (Decimal(v_q3_1) + Decimal(v_q3_2)) / Decimal(2)
        q3_str = format_num(q3_dec)
        
        delta_q_dec = q3_dec - q1_dec
        delta_q_str = format_num(delta_q_dec)
        
        lop = random.choice(["10A", "10B", "10C", "10D", "11A", "11B"])
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Bảng thống kê số lần đi muộn trong học kỳ I của $%s$ học sinh lớp %s bị nhòe mất hai vị trí $x$ và $y$ như sau:
    \\begin{center}
    \\begin{tabular}{|l|c|c|c|c|c|c|}
    \\hline
    \\textbf{Số lần đi muộn} & $0$ & $1$ & $2$ & $3$ & $4$ & $5$ \\\\
    \\hline
    \\textbf{Số học sinh} & $%s$ & $%s$ & $x$ & $%s$ & $y$ & $%s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Biết rằng số lần đi muộn trung bình của mỗi học sinh trong lớp là $%s$ lần. Hãy tìm $x, y$ và xác định khoảng tứ phân vị $\\Delta_Q$ của mẫu số liệu.'''
                         %(N, lop, n0, n1, n3, n5, tb_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì lớp %s có tất cả $%s$ học sinh nên ta có phương trình:
    $$%s + %s + x + %s + y + %s = %s \\Leftrightarrow x + y = %s \\quad (1).$$
    Mặt khác, số lần đi muộn trung bình của mỗi học sinh trong lớp là $%s$ lần nên ta có phương trình:
    $$\\dfrac{0 \\cdot %s + 1 \\cdot %s + 2x + 3 \\cdot %s + 4y + 5 \\cdot %s}{%s} = %s$$
    $$\\Leftrightarrow %s + 2x + 4y = %s \\Leftrightarrow 2x + 4y = %s \\Leftrightarrow x + 2y = %s \\quad (2).$$
    Từ $(1)$ và $(2)$ ta có hệ phương trình:
    $$\\begin{cases} x + y = %s \\\\ x + 2y = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases} \\text{ (thỏa mãn } x, y \\in \\mathbb{N}^*\\text{)}.$$
    Sau khi khôi phục bảng tần số, sắp xếp mẫu số liệu gồm $n = %s$ giá trị theo thứ tự không giảm:
    \\begin{itemize}
    \\item Nửa số liệu bên trái gồm $%s$ giá trị đầu tiên (từ $x_1$ đến $x_{%s}$). Tứ phân vị thứ nhất $Q_1$ là trung bình cộng của giá trị thứ $%s$ và giá trị thứ $%s$:
    $$Q_1 = \\dfrac{x_{%s} + x_{%s}}{2} = \\dfrac{%s + %s}{2} = %s.$$
    \\item Nửa số liệu bên phải gồm $%s$ giá trị cuối cùng (từ $x_{%s}$ đến $x_{%s}$). Tứ phân vị thứ ba $Q_3$ là trung bình cộng của giá trị thứ $%s$ và giá trị thứ $%s$:
    $$Q_3 = \\dfrac{x_{%s} + x_{%s}}{2} = \\dfrac{%s + %s}{2} = %s.$$
    \\end{itemize}
    Vậy khoảng tứ phân vị của mẫu số liệu là:
    $$\\Delta_Q = Q_3 - Q_1 = %s - %s = %s.$$'''
                   %(lop, N,
                     n0, n1, n3, n5, N, tong_xy,
                     tb_str,
                     n0, n1, n3, n5, N, tb_str,
                     tong_lan_biet, tong_lan, tong_2x_4y, tong_x_2y,
                     tong_xy, tong_x_2y, x_val, y_val,
                     N,
                     half, half, idx_q1_1 + 1, idx_q1_2 + 1,
                     idx_q1_1 + 1, idx_q1_2 + 1, v_q1_1, v_q1_2, q1_str,
                     half, half + 1, N, idx_q3_1 + 1, idx_q3_2 + 1,
                     idx_q3_1 + 1, idx_q3_2 + 1, v_q3_1, v_q3_2, q3_str,
                     q3_str, q1_str, delta_q_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

