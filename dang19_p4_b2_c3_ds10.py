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


def bt_dang19_p4_b2_c3_ds10(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Mẫu 7 số nguyên dương: x1 <= x2 <= x3 <= x4 <= x5 <= x6 <= x7
        # Trung vị x4 = me_val, mốt duy nhất = me_val (xuất hiện ít nhất 2 lần, các số khác nhiều nhất 1 lần)
        # Q1 = x2, Q3 = x6 => Delta_Q = x6 - x2
        # x7 = k * x1
        # Tìm các bộ tham số (tb_val, me_val, delta_q, k) sao cho bài toán có số nghiệm hữu hạn đẹp (1 đến 3 nghiệm)
        while True:
            tb_val = randint(9, 13)
            me_val = randint(tb_val - 2, tb_val)
            if me_val < 6:
                continue
            delta_q = randint(5, 9)
            k = random.choice([2, 3])
            tong_7 = 7 * tb_val
            
            solutions = []
            # Vét cạn tìm tất cả các bộ (x1, x2, x3, x4, x5, x6, x7) thỏa mãn
            x4 = me_val
            for x1 in range(1, me_val + 1):
                x7 = k * x1
                if x7 < me_val:
                    continue
                for x2 in range(x1, me_val + 1):
                    x6 = x2 + delta_q
                    if x6 < me_val or x6 > x7:
                        continue
                    for x3 in range(x2, me_val + 1):
                        for x5 in range(me_val, x6 + 1):
                            if x1 + x2 + x3 + x4 + x5 + x6 + x7 == tong_7:
                                arr = [x1, x2, x3, x4, x5, x6, x7]
                                cnt = Counter(arr)
                                max_freq = max(cnt.values())
                                if max_freq >= 2 and cnt[me_val] == max_freq and list(cnt.values()).count(max_freq) == 1:
                                    solutions.append(arr)
            
            if 1 <= len(solutions) <= 3:
                break
    
        # Chuyển đổi phần biện luận và liệt kê nghiệm chi tiết
        tong_con_lai = tong_7 - me_val
        
        # Liệt kê các trường hợp của x1 để trình bày lời giải chặt chẽ
        x1_max = me_val
        phan_tich_lines = []
        for x1_cand in range(1, x1_max + 1):
            x7_cand = k * x1_cand
            if x7_cand < me_val:
                phan_tich_lines.append("\\item Với $x_1 = %s \\Rightarrow x_7 = %s < %s$ (loại vì $x_7 \\ge x_4 = %s$)." % (x1_cand, x7_cand, me_val, me_val))
                continue
            
            sub_sols = []
            for x2_cand in range(x1_cand, me_val + 1):
                x6_cand = x2_cand + delta_q
                if x6_cand < me_val or x6_cand > x7_cand:
                    continue
                for x3_cand in range(x2_cand, me_val + 1):
                    for x5_cand in range(me_val, x6_cand + 1):
                        if x1_cand + x2_cand + x3_cand + me_val + x5_cand + x6_cand + x7_cand == tong_7:
                            arr = [x1_cand, x2_cand, x3_cand, me_val, x5_cand, x6_cand, x7_cand]
                            cnt = Counter(arr)
                            max_freq = max(cnt.values())
                            if max_freq >= 2 and cnt[me_val] == max_freq and list(cnt.values()).count(max_freq) == 1:
                                sub_sols.append(arr)
            
            if len(sub_sols) == 0:
                phan_tich_lines.append("\\item Với $x_1 = %s \\Rightarrow x_7 = %s$: thử các giá trị $x_2 \\in [%s; %s]$ và $x_6 = x_2 + %s \\le %s$, kết hợp điều kiện $x_3 + x_5 = %s - (x_1 + x_2 + x_6 + x_7)$ và mốt duy nhất bằng $%s$ không tìm được bộ số thỏa mãn (loại)." % (
                    x1_cand, x7_cand, x1_cand, me_val, delta_q, x7_cand, tong_con_lai, me_val
                ))
            else:
                sol_texts = []
                for s in sub_sols:
                    s_str = "; ".join(str(v) for v in s)
                    sol_texts.append("$(%s)$" % s_str)
                phan_tich_lines.append("\\item Với $x_1 = %s \\Rightarrow x_7 = %s$: chọn $x_2 \\in [%s; %s]$, $x_6 = x_2 + %s \\le %s$ và $x_3, x_5$ sao cho $x_2 \\le x_3 \\le %s \\le x_5 \\le x_6$, tổng các số bằng $%s$ và giá trị $%s$ xuất hiện nhiều lần nhất (duy nhất), ta thu được mẫu số liệu thỏa mãn là: %s." % (
                    x1_cand, x7_cand, x1_cand, me_val, delta_q, x7_cand, me_val, tong_7, me_val, ", ".join(sol_texts)
                ))
    
        phan_tich_str = "\n".join(phan_tich_lines)
        
        all_sol_texts = ["; ".join(str(v) for v in s) for s in solutions]
        if len(solutions) == 1:
            ket_luan_str = "Vậy mẫu số liệu duy nhất thỏa mãn bài toán là: $%s$." % all_sol_texts[0]
        else:
            ket_luan_str = "Vậy tất cả các mẫu số liệu thỏa mãn bài toán là: " + ", ".join("$(%s)$" % t for t in all_sol_texts) + "."
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một mẫu số liệu gồm $7$ số nguyên dương $x_1 \\le x_2 \\le x_3 \\le x_4 \\le x_5 \\le x_6 \\le x_7$ thỏa mãn đồng thời các điều kiện sau:
    \\begin{enumerate}
    \\item Số trung bình của mẫu số liệu bằng $%s$.
    \\item Trung vị bằng $%s$ và mốt duy nhất của mẫu bằng $%s$.
    \\item Khoảng tứ phân vị $\\Delta_Q = %s$, đồng thời giá trị lớn nhất gấp $%s$ lần giá trị nhỏ nhất ($x_7 = %s x_1$).
    \\end{enumerate}
    Hãy tìm tất cả các mẫu số liệu thỏa mãn bài toán.'''
                         %(tb_val, me_val, me_val, delta_q, k, k
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Ta phân tích các điều kiện của bài toán:
    \\begin{itemize}
    \\item Vì số trung bình của $7$ số bằng $%s$ nên tổng của $7$ số là:
    $$x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 = 7 \\cdot %s = %s.$$
    \\item Mẫu số liệu có $n = 7$ giá trị đã sắp xếp không giảm nên trung vị là số chính giữa $x_4 = %s$. \\\\
    Vì $%s$ là mốt duy nhất của mẫu số liệu nên giá trị $%s$ phải xuất hiện ít nhất $2$ lần (tức là $x_3 = %s$ hoặc $x_5 = %s$), đồng thời các giá trị khác $%s$ không được xuất hiện nhiều hơn hoặc bằng số lần xuất hiện của $%s$.
    \\item Nửa số liệu bên trái gồm $3$ giá trị $x_1; x_2; x_3$ nên tứ phân vị thứ nhất là $Q_1 = x_2$. \\\\
    Nửa số liệu bên phải gồm $3$ giá trị $x_5; x_6; x_7$ nên tứ phân vị thứ ba là $Q_3 = x_6$. \\\\
    Từ giả thiết khoảng tứ phân vị $\\Delta_Q = %s$ ta có:
    $$Q_3 - Q_1 = %s \\Leftrightarrow x_6 - x_2 = %s \\Leftrightarrow x_6 = x_2 + %s.$$
    \\item Mặt khác, $1 \\le x_1 \\le x_2 \\le x_3 \\le x_4 = %s$ nên $x_1 \\in \\{1; 2; \\dots; %s\\}$, và $x_7 = %s x_1$.
    \\end{itemize}
    Thay $x_4 = %s$, $x_6 = x_2 + %s$, $x_7 = %s x_1$ vào phương trình tổng ta được:
    $$x_1 + x_2 + x_3 + %s + x_5 + (x_2 + %s) + %s x_1 = %s \\Leftrightarrow %s x_1 + 2x_2 + x_3 + x_5 = %s.$$
    Xét các giá trị nguyên dương của $x_1$ từ $1$ đến $%s$:
    \\begin{itemize}
    %s
    \\end{itemize}
    %s'''
                   %(tb_val, tb_val, tong_7,
                     me_val, me_val, me_val, me_val, me_val, me_val, me_val,
                     delta_q, delta_q, delta_q, delta_q,
                     me_val, me_val, k,
                     me_val, delta_q, k,
                     me_val, delta_q, k, tong_7, k + 1, tong_7 - me_val - delta_q,
                     x1_max,
                     phan_tich_str,
                     ket_luan_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

