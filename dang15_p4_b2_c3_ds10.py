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


def bt_dang15_p4_b2_c3_ds10(self):
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
        # Mẫu 9 số không giảm: x1; x2; a; x4; x5; x6; b; x8; x9
        # Nửa trái: x1; x2; a; x4 -> Q1 = (x2 + a)/2
        # Nửa phải: x6; b; x8; x9 -> Q3 = (b + x8)/2
        # Khoảng tứ phân vị: Delta_Q = Q3 - Q1 = (b + x8 - x2 - a)/2
        while True:
            x1 = randint(1, 3)
            x2 = randint(x1 + 1, x1 + 3)
            # Khoảng của a: x2 <= a <= x4
            x4 = randint(x2 + 2, x2 + 4)
            x5 = randint(x4 + 1, x4 + 3)
            x6 = randint(x5 + 1, x5 + 3)
            # Khoảng của b: x6 <= b <= x8
            x8 = randint(x6 + 2, x6 + 4)
            x9 = randint(x8 + 1, x8 + 3)
            
            tong_biet = x1 + x2 + x4 + x5 + x6 + x8 + x9
            # Chọn trước một cặp nghiệm (a0, b0) hợp lệ để tính tổng và Delta_Q
            a0 = randint(x2, x4)
            b0 = randint(x6, x8)
            
            if (b0 + x8 - x2 - a0) % 2 == 0 and (b0 + x8 - x2 - a0) > 0:
                delta_q = (b0 + x8 - x2 - a0) // 2
                tong_9 = tong_biet + a0 + b0
                tong_ab = a0 + b0
                hieu_ba = 2 * delta_q - (x8 - x2)
                
                # Tìm tất cả các cặp (a, b) thỏa mãn điều kiện bài toán
                nghiem = []
                for a_cand in range(x2, x4 + 1):
                    b_cand = tong_ab - a_cand
                    if x6 <= b_cand <= x8 and (b_cand - a_cand == hieu_ba):
                        nghiem.append((a_cand, b_cand))
                
                if len(nghiem) >= 1:
                    break
    
        # Làm tròn số trung bình đến hàng phần chục bằng Decimal, ROUND_HALF_UP
        tb_round = (Decimal(tong_9) / Decimal(9)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        tb_round_str = format_num(tb_round)
        
        # Diễn giải giải hệ phương trình tìm a, b
        # a + b = tong_ab
        # b - a = hieu_ba
        # => 2b = tong_ab + hieu_ba => b = (tong_ab + hieu_ba) // 2, a = tong_ab - b
        hai_b = tong_ab + hieu_ba
        b_sol = hai_b // 2
        a_sol = tong_ab - b_sol
        
        # Kiểm tra điều kiện
        ket_luan_str = "Vậy cặp số nguyên duy nhất thỏa mãn điều kiện bài toán là $(a; b) = (%s; %s)$." % (a_sol, b_sol)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho mẫu số liệu gồm $9$ số nguyên dương đã sắp xếp không giảm:
    $$%s; %s; a; %s; %s; %s; b; %s; %s.$$
    Biết rằng số trung bình của mẫu số liệu là $%s$ (làm tròn đến hàng phần chục từ tổng nguyên) — cụ thể tổng $9$ số bằng $%s$, và khoảng tứ phân vị $\\Delta_Q = %s$. Tìm tất cả các cặp số nguyên $(a; b)$ thỏa mãn điều kiện bài toán.'''
                         %(x1, x2, x4, x5, x6, x8, x9,
                           tb_round_str, tong_9, delta_q
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì mẫu số liệu gồm $9$ số nguyên dương đã sắp xếp theo thứ tự không giảm nên ta có điều kiện:
    $$%s \\le a \\le %s \\quad \\text{và} \\quad %s \\le b \\le %s \\quad (a, b \\in \\mathbb{Z}).$$
    Theo đề bài, tổng của $9$ số trong mẫu số liệu bằng $%s$ nên ta có phương trình:
    $$%s + %s + a + %s + %s + %s + b + %s + %s = %s$$
    $$\\Leftrightarrow %s + a + b = %s \\Leftrightarrow a + b = %s \\quad (1).$$
    Mặt khác, mẫu số liệu có $n = 9$ giá trị nên trung vị là giá trị đứng ở vị trí thứ $5$, tức là $M_e = %s$.
    \\begin{itemize}
    \\item Nửa số liệu bên trái gồm $4$ giá trị: $%s; %s; a; %s$. Tứ phân vị thứ nhất là trung vị của nửa số liệu bên trái:
    $$Q_1 = \\dfrac{%s + a}{2}.$$
    \\item Nửa số liệu bên phải gồm $4$ giá trị: $%s; b; %s; %s$. Tứ phân vị thứ ba là trung vị của nửa số liệu bên phải:
    $$Q_3 = \\dfrac{b + %s}{2}.$$
    \\end{itemize}
    Theo giả thiết, khoảng tứ phân vị $\\Delta_Q = %s$ nên ta có phương trình:
    $$\\Delta_Q = Q_3 - Q_1 = %s \\Leftrightarrow \\dfrac{b + %s}{2} - \\dfrac{%s + a}{2} = %s$$
    $$\\Leftrightarrow b - a + %s = %s \\Leftrightarrow b - a = %s \\quad (2).$$
    Từ $(1)$ và $(2)$ ta có hệ phương trình:
    $$\\begin{cases} a + b = %s \\\\ -a + b = %s \\end{cases} \\Leftrightarrow \\begin{cases} 2b = %s \\\\ a = %s - b \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}.$$
    Kiểm tra điều kiện: ta thấy $%s \\le %s \\le %s$ và $%s \\le %s \\le %s$ (thỏa mãn). \\\\
    %s'''
                   %(x2, x4, x6, x8,
                     tong_9,
                     x1, x2, x4, x5, x6, x8, x9, tong_9,
                     tong_biet, tong_9, tong_ab,
                     x5,
                     x1, x2, x4,
                     x2,
                     x6, x8, x9,
                     x8,
                     delta_q,
                     delta_q, x8, x2, delta_q,
                     x8 - x2, 2 * delta_q, hieu_ba,
                     tong_ab, hieu_ba, hai_b, tong_ab, a_sol, b_sol,
                     x2, a_sol, x4, x6, b_sol, x8,
                     ket_luan_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

