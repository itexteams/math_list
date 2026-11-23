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


def bt_dang23_p4_b2_c3_ds10(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':        
        while True:
            luong1 = random.choice([8, 9, 10, 11, 12])
            m_val = luong1 + random.choice([2, 3, 4])
            # Chọn một bộ (a, b, c) và một giá trị n_val > m_val sao cho tổng lương chia hết cho 15
            abc_pool = [(7, 6, 2), (7, 5, 3), (6, 5, 4)]
            a_true, b_true, c_true = random.choice(abc_pool)
            n_val = randint(m_val + 4, m_val + 14)
            
            tong_luong = a_true * luong1 + b_true * m_val + c_true * n_val
            if tong_luong % 15 == 0:
                tb_val = tong_luong // 15
                break
    
        # Giải phương trình c * n = tong_luong - a * luong1 - b * m cho từng trường hợp (a, b, c) để trình bày chi tiết
        cases_info = []
        valid_solutions = []
        for (a_c, b_c, c_c) in [(7, 6, 2), (7, 5, 3), (6, 5, 4)]:
            vp = tong_luong - a_c * luong1 - b_c * m_val
            if vp > 0 and vp % c_c == 0:
                n_cand = vp // c_c
                if n_cand > m_val:
                    valid_solutions.append((a_c, b_c, c_c, n_cand))
                    cases_info.append("\\item \\textbf{Trường hợp $(a; b; c) = (%s; %s; %s)$:} \\\\\nThay vào phương trình tổng lương ta được:\n$$%s \\cdot %s + %s \\cdot %s + %s n = %s \\Leftrightarrow %s + %s n = %s \\Leftrightarrow %s n = %s \\Leftrightarrow n = %s.$$"
                                      "\nVì $n = %s \\in \\mathbb{N}$ và $n > %s$ nên trường hợp này \\textbf{thỏa mãn}." % (
                                          a_c, b_c, c_c,
                                          a_c, luong1, b_c, m_val, c_c, tong_luong,
                                          a_c * luong1 + b_c * m_val, c_c, tong_luong,
                                          c_c, vp, n_cand,
                                          n_cand, m_val
                                      ))
                else:
                    cases_info.append("\\item \\textbf{Trường hợp $(a; b; c) = (%s; %s; %s)$:} \\\\\nThay vào phương trình tổng lương ta được:\n$$%s \\cdot %s + %s \\cdot %s + %s n = %s \\Leftrightarrow %s + %s n = %s \\Leftrightarrow %s n = %s \\Leftrightarrow n = %s.$$"
                                      "\nVì $n = %s \\le %s$ (không thỏa mãn $n > m$) nên trường hợp này \\textbf{loại}." % (
                                          a_c, b_c, c_c,
                                          a_c, luong1, b_c, m_val, c_c, tong_luong,
                                          a_c * luong1 + b_c * m_val, c_c, tong_luong,
                                          c_c, vp, n_cand,
                                          n_cand, m_val
                                      ))
            else:
                # Không chia hết
                tu_so = vp // math.gcd(vp, c_c)
                mau_so = c_c // math.gcd(vp, c_c)
                cases_info.append("\\item \\textbf{Trường hợp $(a; b; c) = (%s; %s; %s)$:} \\\\\nThay vào phương trình tổng lương ta được:\n$$%s \\cdot %s + %s \\cdot %s + %s n = %s \\Leftrightarrow %s + %s n = %s \\Leftrightarrow %s n = %s \\Leftrightarrow n = \\dfrac{%s}{%s} \\notin \\mathbb{N}.$$"
                                  "\nDo đó trường hợp này \\textbf{loại}." % (
                                      a_c, b_c, c_c,
                                      a_c, luong1, b_c, m_val, c_c, tong_luong,
                                      a_c * luong1 + b_c * m_val, c_c, tong_luong,
                                      c_c, vp, tu_so, mau_so
                                  ))
    
        cases_str = "\n".join(cases_info)
        
        if len(valid_solutions) == 1:
            sol = valid_solutions[0]
            ket_luan_str = "Vậy công ty có $%s$ nhân viên Bậc 1, $%s$ nhân viên Bậc 2, $%s$ nhân viên Bậc 3 và các mức lương tương ứng là $m = %s$ triệu đồng, $n = %s$ triệu đồng." % (
                sol[0], sol[1], sol[2], m_val, sol[3]
            )
        else:
            parts = []
            for sol in valid_solutions:
                parts.append("Bậc 1 có $%s$ người, Bậc 2 có $%s$ người, Bậc 3 có $%s$ người với mức lương $m = %s$ triệu đồng, $n = %s$ triệu đồng" % (
                    sol[0], sol[1], sol[2], m_val, sol[3]
                ))
            ket_luan_str = "Vậy các phương án thỏa mãn bài toán là: " + "; ".join(parts) + "."
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một công ty có $15$ nhân viên chia làm $3$ bậc lương: Bậc 1 (nhân viên mới), Bậc 2 (chuyên viên) và Bậc 3 (trưởng nhóm). Hiện tại, bảng thống kê lương (triệu đồng/tháng) có số trung bình là $%s$ triệu, trung vị là $%s$ triệu và mốt duy nhất là $%s$ triệu. Biết số nhân viên Bậc 1 nhiều hơn Bậc 2, số nhân viên Bậc 2 nhiều hơn Bậc 3 và mỗi bậc có ít nhất $2$ người. Mức lương của Bậc 1, Bậc 2, Bậc 3 lần lượt là $%s$ triệu, $m$ triệu và $n$ triệu ($%s < m < n$, với $m, n \\in \\mathbb{N}$). Hãy xác định số nhân viên ở từng bậc và các mức lương $m, n$.'''
                         %(tb_val, m_val, luong1, luong1, luong1
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Gọi $a, b, c$ lần lượt là số nhân viên của Bậc 1, Bậc 2 và Bậc 3 ($a, b, c \\in \\mathbb{N}^*$). \\\\
    Theo giả thiết của bài toán, ta có:
    \\begin{itemize}
    \\item Tổng số nhân viên của công ty là $15$ người nên $a + b + c = 15$.
    \\item Số nhân viên Bậc 1 nhiều hơn Bậc 2, Bậc 2 nhiều hơn Bậc 3 và mỗi bậc có ít nhất $2$ người nên:
    $$a > b > c \\ge 2.$$
    \\item Bảng thống kê gồm $15$ mức lương được sắp xếp theo thứ tự không giảm gồm $a$ số $%s$, tiếp theo là $b$ số $m$ và cuối cùng là $c$ số $n$ (vì $%s < m < n$). \\\\
    Vì cỡ mẫu $N = 15$ là số lẻ nên trung vị của mẫu số liệu là giá trị đứng ở vị trí thứ $8$. Theo đề bài, trung vị bằng $%s$ triệu và mức lương Bậc 1 bằng $%s$ triệu ($%s \\ne %s$) nên phần tử đứng ở vị trí thứ $8$ phải thuộc nhóm Bậc 2. Suy ra:
    $$m = %s \\quad \\text{và} \\quad a \\le 7 < a + b.$$
    \\end{itemize}
    Từ $a > b > c \\ge 2$ và $a + b + c = 15$, ta tìm các bộ số nguyên dương $(a; b; c)$ thỏa mãn $a \\le 7$:
    \\begin{itemize}
    \\item Nếu $c = 2$ thì $a + b = 13$. Vì $7 \\ge a > b \\ge 3$ nên chỉ có bộ $(a; b; c) = (7; 6; 2)$ (thỏa mãn $a + b = 13 > 7$).
    \\item Nếu $c = 3$ thì $a + b = 12$. Vì $7 \\ge a > b \\ge 4$ nên chỉ có bộ $(a; b; c) = (7; 5; 3)$ (thỏa mãn $a + b = 12 > 7$).
    \\item Nếu $c = 4$ thì $a + b = 11$. Vì $7 \\ge a > b \\ge 5$ nên chỉ có bộ $(a; b; c) = (6; 5; 4)$ (thỏa mãn $a + b = 11 > 7$).
    \\item Nếu $c \\ge 5$ thì $b \\ge 6 \\Rightarrow a \\ge 7 \\Rightarrow a + b + c \\ge 18 > 15$ (vô lý).
    \\end{itemize}
    Mặt khác, mức lương trung bình của $15$ nhân viên là $%s$ triệu đồng/tháng nên tổng quỹ lương một tháng của công ty là:
    $$%s a + %s b + c n = 15 \\cdot %s = %s.$$
    Thử lần lượt $3$ bộ số $(a; b; c)$ vừa tìm được vào phương trình tổng lương:
    \\begin{itemize}
    %s
    \\end{itemize}
    %s'''
                   %(luong1, luong1,
                     m_val, luong1, luong1, m_val,
                     m_val,
                     tb_val,
                     luong1, m_val, tb_val, tong_luong,
                     cases_str,
                     ket_luan_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

