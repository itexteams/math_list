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


def bt_dang26_p4_b2_c3_ds10(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            q1 = randint(4, 7)
            q2 = q1 + randint(3, 5)
            q3 = q2 + randint(4, 6)
            xmax = q3 + randint(3, 7)
            
            xmax = q3 + random.choice([1, 2])
            if q1 >= 4 and q2 >= q1 + 3 and q3 >= q2 + 4:
                break
    
        s_min = 4 * q1 + 3 * q2 + 4 * q3 + 3
        s_max = 4 * q1 + 3 * q2 + 4 * q3 + xmax
        
        day_min_str = "0; %s; %s; %s; %s; %s; %s; %s; %s; %s; %s; %s" % (
            q1, q1, q1, q1 + 1, q2, q2, q2 + 1, q3, q3, q3, q3 + 1
        )
        day_max_str = "%s; %s; %s; %s; %s; %s; %s; %s; %s; %s; %s; %s" % (
            q1, q1, q1, q1, q2, q2, q2, q3, q3, q3, q3, xmax
        )
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho mẫu số liệu gồm $12$ số tự nhiên không giảm: $x_1 \\le x_2 \\le \\dots \\le x_{12}$. Biết rằng $Q_1 = %s$, $Q_2 = %s$, $Q_3 = %s$ và mẫu số liệu có đúng hai mốt là $%s$ và $%s$. \\\\
    a) Tìm giá trị nhỏ nhất có thể có của tổng $S = x_1 + x_2 + \\dots + x_{12}$. \\\\
    b) Nếu biết thêm giá trị lớn nhất $x_{12} = %s$, hãy tìm giá trị lớn nhất có thể có của tổng $S$.'''
                         %(q1, q2, q3, q1, q3,
                           xmax
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Mẫu số liệu gồm $n = 12$ số tự nhiên không giảm $0 \\le x_1 \\le x_2 \\le \\dots \\le x_{12}$. Từ giả thiết về các tứ phân vị ta có:
    \\begin{itemize}
    \\item $Q_1 = \\dfrac{x_3 + x_4}{2} = %s \\Rightarrow x_3 + x_4 = %s$, đồng thời $x_3 \\le %s \\le x_4$.
    \\item $Q_2 = \\dfrac{x_6 + x_7}{2} = %s \\Rightarrow x_6 + x_7 = %s$, đồng thời $x_6 \\le %s \\le x_7$.
    \\item $Q_3 = \\dfrac{x_9 + x_{10}}{2} = %s \\Rightarrow x_9 + x_{10} = %s$, đồng thời $x_9 \\le %s \\le x_{10}$.
    \\end{itemize}
    Vì mẫu số liệu có đúng hai mốt là $%s$ và $%s$ nên số lần xuất hiện của $%s$ và $%s$ phải bằng nhau (gọi số lần xuất hiện này là $k$, với $k \\ge 2$) và lớn hơn số lần xuất hiện của mọi giá trị khác trong mẫu. \\\\
    Ta viết lại tổng $S$ dưới dạng:
    $$S = (x_1 + x_2) + (x_3 + x_4) + x_5 + (x_6 + x_7) + x_8 + (x_9 + x_{10}) + (x_{11} + x_{12})$$
    $$= x_1 + x_2 + x_5 + x_8 + x_{11} + x_{12} + %s + %s + %s = x_1 + x_2 + x_5 + x_8 + x_{11} + x_{12} + %s.$$
    \\begin{enumEX}[a)]{1}
    \\item \\textbf{Tìm giá trị nhỏ nhất của $S$:} \\\\
    Từ tính chất không giảm của dãy số liệu, ta có các đánh giá chặn dưới:
    $$x_1 \\ge 0; \\quad x_2 \\ge 0; \\quad x_5 \\ge x_4 \\ge %s; \\quad x_8 \\ge x_7 \\ge %s; \\quad x_{12} \\ge x_{11} \\ge x_{10} \\ge %s.$$
    Ta xét các trường hợp của tần số $k$ của hai mốt $%s$ và $%s$:
    \\begin{itemize}
    \\item \\textbf{Nếu $k = 3$:} Khi đó số $%s$ xuất hiện $3$ lần và số $%s$ xuất hiện $3$ lần. Để tổng nhỏ nhất, ta chọn $x_1 = 0$, $x_2 = x_3 = x_4 = %s$ (đủ $3$ số $%s$), $x_5 = %s$ (vì $x_5$ không thể bằng $%s$), $x_6 = x_7 = %s$, $x_8 = %s$ (để số $%s$ chỉ xuất hiện $2$ lần), $x_9 = x_{10} = x_{11} = %s$ (đủ $3$ số $%s$) và $x_{12} = %s$. \\\\
    Ta thu được mẫu số liệu: $%s$ (thỏa mãn tất cả giả thiết với hai mốt là $%s$ và $%s$). \\\\
    Tổng của mẫu số liệu này là:
    $$S = 0 + 3 \\cdot %s + %s + 2 \\cdot %s + %s + 3 \\cdot %s + %s = %s.$$
    \\item \\textbf{Nếu $k \\ge 4$:} Khi đó số $%s$ xuất hiện ít nhất $4$ lần, buộc $x_1 = x_2 = x_3 = x_4 = %s$ (tức $x_1 + x_2 = %s$, tăng thêm $%s$ so với trường hợp trên), trong khi các số hạng $x_5, x_8, x_{11}, x_{12}$ không thể nhỏ hơn các giá trị ở trường hợp trên quá $1$ đơn vị, nên tổng $S$ chắc chắn lớn hơn $%s$.
    \\item \\textbf{Nếu $k = 2$:} Khi đó mọi giá trị khác chỉ xuất hiện tối đa $1$ lần, buộc $x_1 < x_2 < x_3 = x_4 = %s < x_5 < x_6 = x_7 = %s < x_8 < x_9 = x_{10} = %s < x_{11} < x_{12}$, làm cho $x_1 + x_2 \\ge 0 + 1 = 1$, $x_5 \\ge %s$, $x_8 \\ge %s$, $x_{11} + x_{12} \\ge %s + %s = %s$, dẫn đến tổng $S \\ge %s > %s$.
    \\end{itemize}
    Vậy giá trị nhỏ nhất có thể có của tổng $S$ là $%s$.
    \\item \\textbf{Tìm giá trị lớn nhất của $S$ khi $x_{12} = %s$:} \\\\
    Từ tính chất không giảm của dãy số liệu, ta có các đánh giá chặn trên:
    $$x_1 \\le x_2 \\le x_3 \\le %s; \\quad x_5 \\le x_6 \\le %s; \\quad x_8 \\le x_9 \\le %s; \\quad x_{11} \\le x_{12} = %s.$$
    Ta xét các trường hợp của tần số $k$ của hai mốt $%s$ và $%s$:
    \\begin{itemize}
    \\item \\textbf{Nếu $k = 4$:} Ta chọn $x_1 = x_2 = x_3 = x_4 = %s$ (số $%s$ xuất hiện $4$ lần), $x_5 = x_6 = x_7 = %s$ (số $%s$ xuất hiện $3$ lần $< 4$), $x_8 = x_9 = x_{10} = x_{11} = %s$ (số $%s$ xuất hiện $4$ lần) và $x_{12} = %s$ (xuất hiện $1$ lần). \\\\
    Ta thu được mẫu số liệu: $%s$ (thỏa mãn tất cả giả thiết với đúng hai mốt là $%s$ và $%s$). \\\\
    Tổng của mẫu số liệu này là:
    $$S = 4 \\cdot %s + 3 \\cdot %s + 4 \\cdot %s + %s = %s.$$
    \\item \\textbf{Nếu $k \\ge 5$:} Vì số $%s$ chỉ có thể nằm ở các vị trí từ $x_1$ đến $x_4$ (do $x_5$ không thể bằng $%s$ nếu $x_4 = %s$ mà $x_3 + x_4 = %s$, còn nếu $x_4 > %s$ thì $x_3 < %s$ nên số $%s$ xuất hiện tối đa $3$ lần) nên tần số của $%s$ không thể vượt quá $4$. Do đó $k \\ge 5$ không xảy ra.
    \\item \\textbf{Nếu $k \\le 3$:} Khi đó số $%s$ xuất hiện tối đa $3$ lần và số $%s$ xuất hiện tối đa $3$ lần. Khi đó trong $4$ vị trí $x_1, x_2, x_3, x_4$ có ít nhất một giá trị nhỏ hơn $%s$ (nên $x_1 \\le %s$), và trong $4$ vị trí $x_8, x_9, x_{10}, x_{11}$ có ít nhất một giá trị nhỏ hơn $%s$ (nên $x_8 \\le %s$), trong khi $x_{11}$ tăng tối đa từ $%s$ lên $%s$ (tăng $%s$). Khi đó:
    $$S \\le (%s + %s + %s + %s) + (%s + %s + %s) + (%s + %s + %s) + %s + %s = %s < %s.$$
    \\end{itemize}
    Vậy giá trị lớn nhất có thể có của tổng $S$ là $%s$.
    \\end{enumEX}'''
                   %(q1, 2 * q1, q1,
                     q2, 2 * q2, q2,
                     q3, 2 * q3, q3,
                     q1, q3, q1, q3,
                     2 * q1, 2 * q2, 2 * q3, 2 * (q1 + q2 + q3),
                     q1, q2, q3,
                     q1, q3,
                     q1, q3, q1, q1, q1 + 1, q1, q2, q2 + 1, q2, q3, q3, q3 + 1,
                     day_min_str, q1, q3,
                     q1, q1 + 1, q2, q2 + 1, q3, q3 + 1, s_min,
                     q1, q1, 2 * q1, 2 * q1, s_min,
                     q1, q2, q3, q1 + 1, q2 + 1, q3 + 1, q3 + 2, 2 * q3 + 3, s_min + 2, s_min,
                     s_min,
                     xmax,
                     q1, q2, q3, xmax,
                     q1, q3,
                     q1, q1, q2, q2, q3, q3, xmax,
                     day_max_str, q1, q3,
                     q1, q2, q3, xmax, s_max,
                     q1, q1, q1, 2 * q1, q1, q1, q1, q1,
                     q1, q3, q1, q1 - 1, q3, q3 - 1, q3, xmax, xmax - q3,
                     q1 - 1, q1, q1, q1, q2, q2, q2, q3 - 1, q3, q3, xmax, xmax, s_max - (2 - (xmax - q3)), s_max,
                     s_max
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

