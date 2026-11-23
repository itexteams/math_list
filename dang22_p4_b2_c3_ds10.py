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


def bt_dang22_p4_b2_c3_ds10(self):
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
        # Sinh ngẫu nhiên cỡ mẫu chẵn n = 2k (6, 8, 10, 12) và hai giá trị chính giữa a_k < a_{k+1}
        n_val = random.choice([6, 8, 10, 12])
        k = n_val // 2
        k1 = k + 1
        
        # Chọn ngẫu nhiên cặp (a_k, a_{k+1}) nguyên dương đẹp với a_k < a_{k+1}
        pairs = [(2, 6), (3, 6), (4, 6), (4, 8), (4, 12), (5, 10), (6, 12), (2, 4), (3, 9), (6, 9)]
        ak, ak1 = random.choice(pairs)
        
        # Tính toán các giá trị chính xác bằng Rational (SymPy)
        me_a = Rational(ak + ak1, 2)
        inv_me_a = Rational(1, me_a)
        
        me_b = (Rational(1, ak) + Rational(1, ak1)) / 2
        diff_val = me_b - inv_me_a
        
        me_a_str = latex(me_a).replace('.', ',')
        inv_me_a_str = latex(inv_me_a).replace('.', ',')
        me_b_str = latex(me_b).replace('.', ',')
        diff_val_str = latex(diff_val).replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho mẫu số liệu gồm $%s$ số thực dương $0 < a_1 < a_2 < \\dots < a_{%s}$. Người ta tạo ra mẫu số liệu mới bằng cách lấy nghịch đảo từng phần tử: $b_i = \\dfrac{1}{a_i}$ với $i = 1, 2, \\dots, %s$. \\\\
    a) Chứng minh rằng trung vị $M_e(b)$ của mẫu mới không nhất thiết bằng $\\dfrac{1}{M_e(a)}$, nhưng luôn thỏa mãn bất đẳng thức $M_e(b) \\ge \\dfrac{1}{M_e(a)}$. Dấu bằng xảy ra khi nào? \\\\
    b) Cho $a_{%s} = %s$ và $a_{%s} = %s$. Tính độ chênh lệch giữa $M_e(b)$ và $\\dfrac{1}{M_e(a)}$.'''
                         %(n_val, n_val, n_val,
                           k, ak, k1, ak1
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Vì mẫu số liệu ban đầu gồm $n = %s$ số thực dương thỏa mãn:
    $$0 < a_1 < a_2 < \\dots < a_{%s} < a_{%s} < \\dots < a_{%s}$$
    nên trung vị của mẫu số liệu $(a_i)$ là trung bình cộng của hai số liệu đứng ở vị trí thứ $%s$ và thứ $%s$:
    $$M_e(a) = \\dfrac{a_{%s} + a_{%s}}{2} \\Rightarrow \\dfrac{1}{M_e(a)} = \\dfrac{2}{a_{%s} + a_{%s}}.$$
    Khi lấy nghịch đảo từng phần tử $b_i = \\dfrac{1}{a_i} > 0$, bất đẳng thức đổi chiều nên ta có dãy số liệu mới được sắp xếp theo thứ tự tăng dần là:
    $$0 < b_{%s} < \\dots < b_{%s} < b_{%s} < \\dots < b_2 < b_1.$$
    Hai số liệu đứng ở vị trí chính giữa (vị trí thứ $%s$ và thứ $%s$) của mẫu mới vẫn là $b_{%s}$ và $b_{%s}$, do đó trung vị của mẫu mới $(b_i)$ là:
    $$M_e(b) = \\dfrac{b_{%s} + b_{%s}}{2} = \\dfrac{1}{2}\\left(\\dfrac{1}{a_{%s}} + \\dfrac{1}{a_{%s}}\\right) = \\dfrac{a_{%s} + a_{%s}}{2a_{%s}a_{%s}}.$$
    Xét hiệu:
    $$M_e(b) - \\dfrac{1}{M_e(a)} = \\dfrac{a_{%s} + a_{%s}}{2a_{%s}a_{%s}} - \\dfrac{2}{a_{%s} + a_{%s}} = \\dfrac{(a_{%s} + a_{%s})^2 - 4a_{%s}a_{%s}}{2a_{%s}a_{%s}(a_{%s} + a_{%s})} = \\dfrac{(a_{%s} - a_{%s})^2}{2a_{%s}a_{%s}(a_{%s} + a_{%s})}.$$
    Vì $a_{%s} > 0$, $a_{%s} > 0$ và $(a_{%s} - a_{%s})^2 \\ge 0$ nên:
    $$\\dfrac{(a_{%s} - a_{%s})^2}{2a_{%s}a_{%s}(a_{%s} + a_{%s})} \\ge 0 \\Rightarrow M_e(b) \\ge \\dfrac{1}{M_e(a)}.$$
    Dấu bằng xảy ra khi và chỉ khi $a_{%s} = a_{%s}$. Tuy nhiên, theo giả thiết bài toán thì $a_{%s} < a_{%s}$ nên $a_{%s} \\ne a_{%s}$, suy ra $M_e(b) > \\dfrac{1}{M_e(a)}$ (tức là $M_e(b)$ không bằng $\\dfrac{1}{M_e(a)}$; tổng quát nếu cho phép dấu bằng trong dãy không giảm thì dấu bằng xảy ra khi $a_{%s} = a_{%s}$).
    \\item Thay $a_{%s} = %s$ và $a_{%s} = %s$ vào các công thức ở câu a), ta có:
    \\begin{itemize}
    \\item Trung vị của mẫu ban đầu:
    $$M_e(a) = \\dfrac{%s + %s}{2} = %s \\Rightarrow \\dfrac{1}{M_e(a)} = %s.$$
    \\item Trung vị của mẫu mới:
    $$M_e(b) = \\dfrac{1}{2}\\left(\\dfrac{1}{%s} + \\dfrac{1}{%s}\\right) = %s.$$
    \\end{itemize}
    Vậy độ chênh lệch giữa $M_e(b)$ và $\\dfrac{1}{M_e(a)}$ là:
    $$M_e(b) - \\dfrac{1}{M_e(a)} = %s - %s = %s.$$
    \\end{enumEX}'''
                   %(n_val,
                     k, k1, n_val,
                     k, k1,
                     k, k1, k, k1,
                     n_val, k1, k,
                     k, k1, k1, k,
                     k1, k, k, k1, k, k1, k, k1,
                     k, k1, k, k1, k, k1, k, k1, k, k1, k, k1, k, k1, k, k1, k, k1, k, k1,
                     k, k1, k, k1,
                     k, k1, k, k1, k, k1,
                     k, k1, k, k1, k, k1, k, k1,
                     k, ak, k1, ak1,
                     ak, ak1, me_a_str, inv_me_a_str,
                     ak, ak1, me_b_str,
                     me_b_str, inv_me_a_str, diff_val_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

