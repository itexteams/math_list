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


def bt_dang25_p4_b2_c3_ds10(self):
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
        # Sinh ngẫu nhiên sĩ số và điểm hai lớp:
        # Lớp A có sĩ số lẻ nA (31, 33, 35, 37, 39), trung vị MeA = x_{(nA+1)/2}
        # Lớp B có sĩ số chẵn nB (36, 38, 40, 42, 44), trung vị MeB = (y_{nB/2} + y_{nB/2 + 1}) / 2
        # Tổng sĩ số N = nA + nB là số lẻ -> trung vị chung Me là phần tử đứng ở vị trí thứ (N + 1)/2
        # Đảm bảo điểm trung bình chung chia hết cho N (số thập phân hữu hạn đẹp) và MeA < MeB
        while True:
            lopA = random.choice(["10A", "10C", "11A", "11C"])
            lopB = random.choice(["10B", "10D", "11B", "11D"])
            nA = random.choice([31, 33, 35, 37, 39])
            nB = random.choice([36, 38, 40, 42, 44])
            N = nA + nB
            
            tbA = Decimal(randint(68, 76)) / Decimal(10)
            tbB = Decimal(randint(76, 84)) / Decimal(10)
            if tbA >= tbB:
                continue
                
            tongA = Decimal(nA) * tbA
            tongB = Decimal(nB) * tbB
            tong_chung = tongA + tongB
            
            # Kiểm tra để điểm trung bình chung là số thập phân hữu hạn (tối đa 2 chữ số thập phân)
            if (tong_chung * 100) % N != 0:
                continue
                
            meA = Decimal(random.choice([70, 75, 80])) / Decimal(10)
            meB = meA + Decimal(random.choice([5, 10])) / Decimal(10)
            if meB > Decimal('9.0'):
                continue
            break
    
        tbA_str = format_1dec(tbA)
        tbB_str = format_1dec(tbB)
        meA_str = format_1dec(meA)
        meB_str = format_1dec(meB)
        
        tongA_str = format_num(tongA)
        tongB_str = format_num(tongB)
        tong_chung_str = format_num(tong_chung)
        
        tb_chung = tong_chung / Decimal(N)
        tb_chung_str = format_num(tb_chung)
        
        pos_meA = (nA + 1) // 2
        pos_meB_1 = nB // 2
        pos_meB_2 = nB // 2 + 1
        pos_me_chung = (N + 1) // 2
        
        so_nho_hon_meA = pos_meA
        so_nho_hon_meB = pos_meB_1
        tong_nho_hon_meB = so_nho_hon_meA + so_nho_hon_meB
        
        so_lon_hon_meA = nA - pos_meA + 1
        so_lon_hon_meB = nB - pos_meB_1
        tong_lon_hon_meA = so_lon_hon_meA + so_lon_hon_meB
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Lớp %s có $%s$ học sinh, điểm kiểm tra Toán có số trung bình là $%s$ và trung vị là $%s$. Lớp %s có $%s$ học sinh, điểm kiểm tra Toán có số trung bình là $%s$ và trung vị là $%s$. \\\\
    a) Tính điểm trung bình chung của toàn bộ $%s$ học sinh hai lớp. \\\\
    b) Khi gộp chung bảng điểm của cả $%s$ học sinh thành một mẫu số liệu duy nhất, trung vị chung $M_e$ của $%s$ học sinh chắc chắn nằm trong khoảng nào? Chứng minh nhận định đó.'''
                         %(lopA, nA, tbA_str, meA_str, lopB, nB, tbB_str, meB_str,
                           N,
                           N, N
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Tổng điểm kiểm tra Toán của $%s$ học sinh lớp %s là:
    $$S_A = %s \\cdot %s = %s.$$
    Tổng điểm kiểm tra Toán của $%s$ học sinh lớp %s là:
    $$S_B = %s \\cdot %s = %s.$$
    Điểm trung bình chung của toàn bộ $%s + %s = %s$ học sinh hai lớp là:
    $$\\overline{x} = \\dfrac{S_A + S_B}{%s + %s} = \\dfrac{%s + %s}{%s} = \\dfrac{%s}{%s} = %s.$$
    \\item \\textbf{Nhận định:} Trung vị chung $M_e$ của $%s$ học sinh chắc chắn nằm trong đoạn $[%s; %s]$. \\\\
    \\textbf{Chứng minh:} \\\\
    Gọi dãy điểm của lớp %s đã sắp xếp theo thứ tự không giảm là $x_1 \\le x_2 \\le \\dots \\le x_{%s}$ và dãy điểm của lớp %s đã sắp xếp theo thứ tự không giảm là $y_1 \\le y_2 \\le \\dots \\le y_{%s}$. \\\\
    Khi gộp chung bảng điểm của cả $N = %s$ học sinh (là số lẻ) và sắp xếp theo thứ tự không giảm thành $z_1 \\le z_2 \\le \\dots \\le z_{%s}$, trung vị chung là phần tử đứng ở vị trí chính giữa:
    $$M_e = z_{%s}.$$
    Ta chứng minh $%s \\le z_{%s} \\le %s$:
    \\begin{itemize}
    \\item \\textbf{Chứng minh $z_{%s} \\ge %s$:} \\\\
    Ở lớp %s (có $%s$ học sinh), trung vị là $x_{%s} = %s$, nên có ít nhất $%s - %s + 1 = %s$ học sinh có điểm lớn hơn hoặc bằng $%s$ (từ $x_{%s}$ đến $x_{%s}$). \\\\
    Ở lớp %s (có $%s$ học sinh), trung vị là $\\dfrac{y_{%s} + y_{%s}}{2} = %s$. Vì $y_{%s} \\le y_{%s}$ nên $y_{%s} \\ge %s > %s$, do đó có ít nhất $%s - %s + 1 = %s$ học sinh có điểm lớn hơn $%s$ (từ $y_{%s}$ đến $y_{%s}$). \\\\
    Suy ra trong cả hai lớp có ít nhất $%s + %s = %s$ học sinh có điểm lớn hơn hoặc bằng $%s$. Khi sắp xếp $%s$ điểm số tăng dần từ trái sang phải, $%s$ học sinh này nằm ở $%s$ vị trí cuối cùng (từ vị trí thứ $%s - %s + 1 = %s$ đến vị trí thứ $%s$). Vì vị trí thứ $%s > %s$ nên phần tử $z_{%s}$ chắc chắn thuộc nhóm này, tức là $z_{%s} \\ge %s$.
    \\item \\textbf{Chứng minh $z_{%s} \\le %s$:} \\\\
    Ở lớp %s, có ít nhất $%s$ học sinh có điểm nhỏ hơn hoặc bằng $x_{%s} = %s < %s$ (từ $x_1$ đến $x_{%s}$). \\\\
    Ở lớp %s, vì $\\dfrac{y_{%s} + y_{%s}}{2} = %s$ và $y_{%s} \\le y_{%s}$ nên $y_{%s} \\le %s$, do đó có ít nhất $%s$ học sinh có điểm nhỏ hơn hoặc bằng $%s$ (từ $y_1$ đến $y_{%s}$). \\\\
    Suy ra trong cả hai lớp có ít nhất $%s + %s = %s$ học sinh có điểm nhỏ hơn hoặc bằng $%s$. Khi sắp xếp $%s$ điểm số không giảm, $%s$ học sinh này chiếm $%s$ vị trí đầu tiên (từ $z_1$ đến $z_{%s}$). Vì $%s < %s$ nên phần tử $z_{%s}$ chắc chắn nằm trong nhóm này, tức là $z_{%s} \\le %s$.
    \\end{itemize}
    Từ hai điều trên suy ra $%s \\le M_e \\le %s$ (tức trung vị chung $M_e$ chắc chắn nằm trong đoạn $[%s; %s]$).
    \\end{enumEX}'''
                   %(nA, lopA, nA, tbA_str, tongA_str,
                     nB, lopB, nB, tbB_str, tongB_str,
                     nA, nB, N, nA, nB, tongA_str, tongB_str, N, tong_chung_str, N, tb_chung_str,
                     N, meA_str, meB_str,
                     lopA, nA, lopB, nB,
                     N, N, pos_me_chung,
                     meA_str, pos_me_chung, meB_str,
                     pos_me_chung, meA_str,
                     lopA, nA, pos_meA, meA_str, nA, pos_meA, so_lon_hon_meA, meA_str, pos_meA, nA,
                     lopB, nB, pos_meB_1, pos_meB_2, meB_str, pos_meB_1, pos_meB_2, pos_meB_2, meB_str, meA_str, nB, pos_meB_2, so_lon_hon_meB, meA_str, pos_meB_2, nB,
                     so_lon_hon_meA, so_lon_hon_meB, tong_lon_hon_meA, meA_str, N, tong_lon_hon_meA, tong_lon_hon_meA, N, tong_lon_hon_meA, N - tong_lon_hon_meA + 1, N, pos_me_chung, N - tong_lon_hon_meA + 1, pos_me_chung, pos_me_chung, meA_str,
                     pos_me_chung, meB_str,
                     lopA, so_nho_hon_meA, pos_meA, meA_str, meB_str, pos_meA,
                     lopB, pos_meB_1, pos_meB_2, meB_str, pos_meB_1, pos_meB_2, pos_meB_1, meB_str, so_nho_hon_meB, meB_str, pos_meB_1,
                     so_nho_hon_meA, so_nho_hon_meB, tong_nho_hon_meB, meB_str, N, tong_nho_hon_meB, tong_nho_hon_meB, tong_nho_hon_meB, pos_me_chung, tong_nho_hon_meB, pos_me_chung, pos_me_chung, meB_str,
                     meA_str, meB_str, meA_str, meB_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

