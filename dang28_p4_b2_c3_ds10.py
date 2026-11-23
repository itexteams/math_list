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


def bt_dang28_p4_b2_c3_ds10(self):
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
        mode_type = random.choice(['const_all', 'k_ge_2'])
        d = random.choice([1, 2])
        x1 = randint(1, 5)
        x2 = x1 + d
        x3 = x1 + 2 * d
        x4 = x1 + 3 * d
        x5 = x1 + 4 * d
        
        if mode_type == 'const_all':
            c1, c2, c3 = 1, 2, 3
            M = 9
            dq_min = x4 - x2
            
            noidungcauhoi = ('''Cho bảng tần số của một mẫu số liệu định lượng gồm $N$ phần tử:
    \\begin{center}
    \\begin{tabular}{|l|c|c|c|c|c|}
    \\hline
    \\textbf{Giá trị ($x_i$)} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\textbf{Tần số ($n_i$)} & $k$ & $2k$ & $3k$ & $2k$ & $k$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    với $k$ là số nguyên dương. \\\\
    a) Chứng minh rằng số trung bình, trung vị và mốt của mẫu số liệu luôn bằng nhau và không phụ thuộc vào giá trị của $k$. \\\\
    b) Tìm tất cả các giá trị nguyên dương của $k$ sao cho khoảng tứ phân vị $\\Delta_Q$ của mẫu số liệu đạt giá trị nhỏ nhất.'''
                             %(x1, x2, x3, x4, x5
                             ))
            
            loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Tổng số phần tử của mẫu số liệu là:
    $$N = k + 2k + 3k + 2k + k = 9k.$$
    \\begin{itemize}
    \\item \\textbf{Số trung bình:}
    $$\\overline{x} = \\dfrac{%s \\cdot k + %s \\cdot 2k + %s \\cdot 3k + %s \\cdot 2k + %s \\cdot k}{9k} = \\dfrac{(%s + %s + %s + %s + %s)k}{9k} = \\dfrac{%s k}{9k} = %s.$$
    \\item \\textbf{Trung vị:} Vì $N = 9k$ nên ta xét hai trường hợp của số nguyên dương $k$:
    \\begin{itemize}
    \\item Nếu $k$ lẻ ($k = 2m + 1$, $m \\in \\mathbb{N}$) thì $N = 9(2m + 1) = 18m + 9$ là số lẻ, do đó trung vị là phần tử đứng ở vị trí thứ $\\dfrac{N + 1}{2} = 9m + 5$. \\\\
    Ta có tổng tần số của hai giá trị đầu tiên ($%s$ và $%s$) là $k + 2k = 3k = 6m + 3$, và tổng tần số của ba giá trị đầu tiên ($%s, %s, %s$) là $6k = 12m + 6$. \\\\
    Vì $6m + 3 < 9m + 5 \\le 12m + 6$ với mọi $m \\in \\mathbb{N}$ nên phần tử đứng ở vị trí thứ $9m + 5$ luôn nhận giá trị bằng $%s$, suy ra $M_e = %s$.
    \\item Nếu $k$ chẵn ($k = 2m$, $m \\in \\mathbb{N}^*$) thì $N = 18m$ là số chẵn, do đó trung vị là trung bình cộng của hai phần tử đứng ở vị trí thứ $9m$ và thứ $9m + 1$. \\\\
    Vì $3k = 6m < 9m < 9m + 1 \\le 12m = 6k$ với mọi $m \\in \\mathbb{N}^*$ nên cả hai phần tử ở vị trí thứ $9m$ và thứ $9m + 1$ đều bằng $%s$, suy ra $M_e = \\dfrac{%s + %s}{2} = %s$.
    \\end{itemize}
    Vậy trong mọi trường hợp, trung vị luôn bằng $M_e = %s$.
    \\item \\textbf{Mốt:} Vì $k \\in \\mathbb{N}^*$ nên tần số lớn nhất trong bảng là $3k$ (do $3k > 2k > k > 0$), tương ứng với giá trị $%s$. Do đó mốt của mẫu số liệu là $M_o = %s$.
    \\end{itemize}
    Vậy $\\overline{x} = M_e = M_o = %s$, tức là số trung bình, trung vị và mốt luôn bằng nhau và không phụ thuộc vào giá trị của $k$.
    \\item Ta xác định tứ phân vị thứ nhất $Q_1$ và tứ phân vị thứ ba $Q_3$ theo $k \\in \\mathbb{N}^*$:
    \\begin{itemize}
    \\item \\textbf{Trường hợp 1: $k = 4m + 1$ ($m \\in \\mathbb{N}$).} Khi đó $N = 36m + 9$ (lẻ), nửa số liệu bên trái gồm $18m + 4$ phần tử (chẵn) nên $Q_1$ là trung bình cộng của hai phần tử đứng ở vị trí thứ $9m + 2$ và thứ $9m + 3$. \\\\
    Ta có số phần tử bằng $%s$ là $k = 4m + 1$, số phần tử nhỏ hơn hoặc bằng $%s$ là $3k = 12m + 3$. \\\\
    Vì $4m + 1 < 9m + 2 < 9m + 3 \\le 12m + 3$ với mọi $m \\in \\mathbb{N}$ nên cả hai phần tử này đều bằng $%s$, suy ra $Q_1 = %s$. \\\\
    Tương tự, do tính đối xứng của bảng tần số, hai phần tử xác định $Q_3$ ở nửa số liệu bên phải đều bằng $%s$, suy ra $Q_3 = %s$. \\\\
    Do đó $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$.
    \\item \\textbf{Trường hợp 2: $k = 4m + 2$ ($m \\in \\mathbb{N}$).} Khi đó $N = 36m + 18$ (chẵn), nửa số liệu bên trái gồm $18m + 9$ phần tử (lẻ) nên $Q_1$ là phần tử đứng ở vị trí thứ $9m + 5$. \\\\
    Vì $k = 4m + 2 < 9m + 5 \\le 12m + 6 = 3k$ với mọi $m \\in \\mathbb{N}$ nên $Q_1 = %s$. Tương tự $Q_3 = %s$, suy ra $\\Delta_Q = %s - %s = %s$.
    \\item \\textbf{Trường hợp 3: $k = 4m + 3$ ($m \\in \\mathbb{N}$).} Khi đó $N = 36m + 27$ (lẻ), nửa số liệu bên trái gồm $18m + 13$ phần tử (lẻ) nên $Q_1$ là phần tử đứng ở vị trí thứ $9m + 7$. \\\\
    Vì $k = 4m + 3 < 9m + 7 \\le 12m + 9 = 3k$ với mọi $m \\in \\mathbb{N}$ nên $Q_1 = %s$. Tương tự $Q_3 = %s$, suy ra $\\Delta_Q = %s - %s = %s$.
    \\item \\textbf{Trường hợp 4: $k = 4m$ ($m \\in \\mathbb{N}^*$).} Khi đó $N = 36m$ (chẵn), nửa số liệu bên trái gồm $18m$ phần tử (chẵn) nên $Q_1$ là trung bình cộng của hai phần tử đứng ở vị trí thứ $9m$ và thứ $9m + 1$. \\\\
    Vì $k = 4m < 9m < 9m + 1 \\le 12m = 3k$ với mọi $m \\in \\mathbb{N}^*$ nên $Q_1 = %s$. Tương tự $Q_3 = %s$, suy ra $\\Delta_Q = %s - %s = %s$.
    \\end{itemize}
    Như vậy, với mọi số nguyên dương $k$, khoảng tứ phân vị luôn không đổi và bằng $\\Delta_Q = %s$. \\\\
    Vậy \\textbf{mọi số nguyên dương $k$} ($k \\in \\mathbb{N}^*$) đều làm cho khoảng tứ phân vị $\\Delta_Q$ đạt giá trị nhỏ nhất (bằng $%s$).
    \\end{enumEX}'''
                       %(x1, x2, x3, x4, x5,
                         x1, 2 * x2, 3 * x3, 2 * x4, x5, 9 * x3, x3,
                         x1, x2, x1, x2, x3, x3, x3,
                         x3, x3, x3, x3,
                         x3,
                         x3, x3,
                         x3,
                         x1, x2, x2, x2, x4, x4, x4, x2, dq_min,
                         x2, x4, x4, x2, dq_min,
                         x2, x4, x4, x2, dq_min,
                         x2, x4, x4, x2, dq_min,
                         dq_min, dq_min
                       ))
        else:
            # Cấu hình tần số: 3k, k, 5k, k, 3k -> N = 13k
            # Khi k = 1: N = 13 -> nửa trái 6 số (x1, x1, x1, x2, x3, x3) -> Q1 = (x1 + x2)/2, Q3 = (x4 + x5)/2 -> Delta_Q = x4 + x5 - x1 - x2 = 3d
            # Khi k >= 2: 3k < nửa trái -> Q1 = x2, Q3 = x4 -> Delta_Q = x4 - x2 = 2d (nhỏ nhất!)
            dq_k1 = format_num((Decimal(x4 + x5) - Decimal(x1 + x2)) / Decimal(2))
            q1_k1 = format_num((Decimal(x1 + x2)) / Decimal(2))
            q3_k1 = format_num((Decimal(x4 + x5)) / Decimal(2))
            dq_min = x4 - x2
            
            noidungcauhoi = ('''Cho bảng tần số của một mẫu số liệu định lượng gồm $N$ phần tử:
    \\begin{center}
    \\begin{tabular}{|l|c|c|c|c|c|}
    \\hline
    \\textbf{Giá trị ($x_i$)} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\textbf{Tần số ($n_i$)} & $3k$ & $k$ & $5k$ & $k$ & $3k$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    với $k$ là số nguyên dương. \\\\
    a) Chứng minh rằng số trung bình, trung vị và mốt của mẫu số liệu luôn bằng nhau và không phụ thuộc vào giá trị của $k$. \\\\
    b) Tìm tất cả các giá trị nguyên dương của $k$ sao cho khoảng tứ phân vị $\\Delta_Q$ của mẫu số liệu đạt giá trị nhỏ nhất.'''
                             %(x1, x2, x3, x4, x5
                             ))
            
            loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Tổng số phần tử của mẫu số liệu là:
    $$N = 3k + k + 5k + k + 3k = 13k.$$
    \\begin{itemize}
    \\item \\textbf{Số trung bình:}
    $$\\overline{x} = \\dfrac{%s \\cdot 3k + %s \\cdot k + %s \\cdot 5k + %s \\cdot k + %s \\cdot 3k}{13k} = \\dfrac{(%s + %s + %s + %s + %s)k}{13k} = \\dfrac{%s k}{13k} = %s.$$
    \\item \\textbf{Trung vị:} Vì $N = 13k$ nên ta xét hai trường hợp của số nguyên dương $k$:
    \\begin{itemize}
    \\item Nếu $k$ lẻ ($k = 2m + 1$, $m \\in \\mathbb{N}$) thì $N = 13(2m + 1) = 26m + 13$ là số lẻ, do đó trung vị là phần tử đứng ở vị trí thứ $\\dfrac{N + 1}{2} = 13m + 7$. \\\\
    Tổng tần số của hai giá trị đầu tiên ($%s$ và $%s$) là $4k = 8m + 4$, và tổng tần số của ba giá trị đầu tiên ($%s, %s, %s$) là $9k = 18m + 9$. \\\\
    Vì $8m + 4 < 13m + 7 \\le 18m + 9$ với mọi $m \\in \\mathbb{N}$ nên phần tử đứng ở vị trí thứ $13m + 7$ luôn bằng $%s$, suy ra $M_e = %s$.
    \\item Nếu $k$ chẵn ($k = 2m$, $m \\in \\mathbb{N}^*$) thì $N = 26m$ là số chẵn, do đó trung vị là trung bình cộng của hai phần tử đứng ở vị trí thứ $13m$ và thứ $13m + 1$. \\\\
    Vì $4k = 8m < 13m < 13m + 1 \\le 18m = 9k$ với mọi $m \\in \\mathbb{N}^*$ nên cả hai phần tử ở vị trí thứ $13m$ và thứ $13m + 1$ đều bằng $%s$, suy ra $M_e = \\dfrac{%s + %s}{2} = %s$.
    \\end{itemize}
    Vậy trong mọi trường hợp, trung vị luôn bằng $M_e = %s$.
    \\item \\textbf{Mốt:} Vì $k \\in \\mathbb{N}^*$ nên tần số lớn nhất trong bảng là $5k$ (do $5k > 3k > k > 0$), tương ứng với giá trị $%s$. Do đó mốt của mẫu số liệu là $M_o = %s$.
    \\end{itemize}
    Vậy $\\overline{x} = M_e = M_o = %s$, tức là số trung bình, trung vị và mốt luôn bằng nhau và không phụ thuộc vào giá trị của $k$.
    \\item Ta xác định khoảng tứ phân vị $\\Delta_Q$ theo $k \\in \\mathbb{N}^*$:
    \\begin{itemize}
    \\item \\textbf{Với $k = 1$:} Cỡ mẫu $N = 13$, dãy số liệu là:
    $$%s; %s; %s; %s; %s; %s; %s; %s; %s; %s; %s; %s; %s.$$
    Nửa số liệu bên trái gồm $6$ giá trị đầu ($%s; %s; %s; %s; %s; %s$) nên $Q_1 = \\dfrac{%s + %s}{2} = %s$. \\\\
    Nửa số liệu bên phải gồm $6$ giá trị cuối ($%s; %s; %s; %s; %s; %s$) nên $Q_3 = \\dfrac{%s + %s}{2} = %s$. \\\\
    Khi đó $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$.
    \\item \\textbf{Với $k \\ge 2$:} Số phần tử nhận giá trị $%s$ là $3k$, số phần tử nhỏ hơn hoặc bằng $%s$ là $4k$.
    \\begin{itemize}
    \\item Nếu $k$ lẻ ($k = 2m + 1$, $m \\ge 1$): nửa số liệu bên trái gồm $\\dfrac{13k - 1}{2} = 13m + 6$ phần tử (lẻ), nên $Q_1$ là phần tử đứng ở vị trí thứ $\\dfrac{13m + 7}{2}$ (nếu $m$ lẻ) hoặc trung bình cộng hai vị trí quanh $\\dfrac{13m + 6}{2}$ (nếu $m$ chẵn). Trong cả hai trường hợp, vị trí xác định $Q_1$ luôn lớn hơn $3k = 6m + 3$ (vì $6m + 3 < 6,5m + 3$) và nhỏ hơn hoặc bằng $4k = 8m + 4$, nên $Q_1 = %s$. Tương tự $Q_3 = %s$.
    \\item Nếu $k$ chẵn ($k = 2m$, $m \\ge 1$): nửa số liệu bên trái gồm $13m$ phần tử, vị trí xác định $Q_1$ xấp xỉ $6,5m$, luôn lớn hơn $3k = 6m$ và nhỏ hơn hoặc bằng $4k = 8m$, nên $Q_1 = %s$. Tương tự $Q_3 = %s$.
    \\end{itemize}
    Do đó với mọi $k \\ge 2$, ta luôn có $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$.
    \\end{itemize}
    So sánh hai trường hợp, ta thấy $%s < %s$. \\\\
    Vậy khoảng tứ phân vị $\\Delta_Q$ đạt giá trị nhỏ nhất (bằng $%s$) khi và chỉ khi \\textbf{$k \\ge 2$ ($k \\in \\mathbb{N}$)}.
    \\end{enumEX}'''
                       %(x1, x2, x3, x4, x5,
                         3 * x1, x2, 5 * x3, x4, 3 * x5, 13 * x3, x3,
                         x1, x2, x1, x2, x3, x3, x3,
                         x3, x3, x3, x3,
                         x3,
                         x3, x3,
                         x3,
                         x1, x1, x1, x2, x3, x3, x3, x3, x3, x4, x5, x5, x5,
                         x1, x1, x1, x2, x3, x3, x1, x2, q1_k1,
                         x3, x3, x4, x5, x5, x5, x4, x5, q3_k1,
                         q3_k1, q1_k1, dq_k1,
                         x1, x2,
                         x2, x4,
                         x2, x4,
                         x4, x2, dq_min,
                         dq_min, dq_k1,
                         dq_min
                       ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

