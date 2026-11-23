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


def bt_dang20_p4_b2_c3_ds10(self):
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
        # Sinh ngẫu nhiên dữ liệu bài toán:
        # Cỡ mẫu n chẵn (6, 8, 10, 12) để trung vị là trung bình cộng hai số chính giữa có dạng k,5
        # Gọi S là tổng ban đầu, M_max là số lớn nhất, M_min là số nhỏ nhất
        # S - M_max = (n - 1) * tb1
        # S - M_max - M_min = (n - 2) * tb2
        # Suy ra: (n - 1) * tb1 - M_min = (n - 2) * tb2 => n * (tb2 - tb1) = 2 * tb2 - tb1 - M_min
        while True:
            n_val = random.choice([6, 8, 10, 12])
            tb1 = randint(16, 25)
            diff_tb = random.choice([1, 2])
            tb2 = tb1 + diff_tb
            
            # Tính M_min từ n_val * diff_tb = 2 * tb2 - tb1 - M_min => M_min = 2 * tb2 - tb1 - n_val * diff_tb
            m_min = 2 * tb2 - tb1 - n_val * diff_tb
            if m_min < 2 or m_min >= tb1 - 3:
                continue
                
            # Chọn M_max sao cho tổng S = (n - 1) * tb1 + M_max chia hết cho n_val (hoặc cho nửa n_val)
            tong_n_tru_1 = (n_val - 1) * tb1
            m_max = randint(tb2 + 8, tb2 + 18)
            tong_n = tong_n_tru_1 + m_max
            
            if (tong_n * 10) % n_val != 0:
                continue
                
            tb_ban_dau = Decimal(tong_n) / Decimal(n_val)
            
            # Chọn trung vị Me = mid_left + 0.5 (với mid_left nguyên quanh tb2)
            mid_left = tb2 - 1
            mid_right = mid_left + 1
            me_dec = Decimal(mid_left) + Decimal('0.5')
            
            # Tìm một mẫu gồm n_val số nguyên đôi một khác nhau: m_min < x_2 < ... < mid_left < mid_right < ... < m_max
            # Tổng n - 2 số ở giữa là tong_giua = (n - 2) * tb2
            tong_giua = (n_val - 2) * tb2
            so_ben_moi_phia = (n_val - 4) // 2
            
            # Thử tìm các số nguyên đôi một khác nhau thỏa mãn
            found_sample = None
            for _ in range(500):
                if so_ben_moi_phia > 0:
                    left_pool = list(range(m_min + 1, mid_left))
                    right_pool = list(range(mid_right + 1, m_max))
                    if len(left_pool) < so_ben_moi_phia or len(right_pool) < so_ben_moi_phia:
                        break
                    left_chosen = sorted(random.sample(left_pool, so_ben_moi_phia))
                    right_chosen = sorted(random.sample(right_pool, so_ben_moi_phia))
                else:
                    left_chosen = []
                    right_chosen = []
                    
                cand = [m_min] + left_chosen + [mid_left, mid_right] + right_chosen + [m_max]
                if sum(cand) == tong_n:
                    found_sample = cand
                    break
                    
            if found_sample is not None:
                break
    
        tb_ban_dau_str = format_num(tb_ban_dau)
        me_str = format_num(me_dec)
        sample_str = "; ".join(str(v) for v in found_sample)
        sample_sum_expr = " + ".join(str(v) for v in found_sample)
        
        # Các giá trị trung gian trong lời giải
        vp_pt = 2 * tb2 - tb1 - m_min
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho một mẫu số liệu gồm $n$ số thực ($n \\ge 5$) có số trung bình là $\\overline{x}$. Nếu loại bỏ số lớn nhất là $%s$ thì số trung bình của $n - 1$ số còn lại là $%s$. Nếu loại bỏ thêm số nhỏ nhất là $%s$ (tức loại bỏ cả $%s$ và $%s$) thì số trung bình của $n - 2$ số còn lại là $%s$. \\\\
    a) Tìm cỡ mẫu $n$ và số trung bình $\\overline{x}$ ban đầu. \\\\
    b) Biết thêm rằng mẫu ban đầu gồm các số nguyên đôi một khác nhau và có trung vị bằng $%s$. Hãy tìm một mẫu số liệu cụ thể thỏa mãn tất cả các dữ kiện trên.'''
                         %(m_max, tb1, m_min, m_max, m_min, tb2, me_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Gọi $S$ là tổng của tất cả $n$ số trong mẫu số liệu ban đầu ($S = n\\overline{x}$).
    \\begin{itemize}
    \\item Khi loại bỏ số lớn nhất là $%s$, tổng của $n - 1$ số còn lại là $S - %s$. Vì số trung bình của $n - 1$ số còn lại bằng $%s$ nên ta có:
    $$S - %s = %s(n - 1) \\Leftrightarrow S = %s n - %s + %s \\Leftrightarrow S = %s n + %s \\quad (1).$$
    \\item Khi loại bỏ cả số lớn nhất là $%s$ và số nhỏ nhất là $%s$, tổng của $n - 2$ số còn lại là $S - %s - %s = S - %s$. Vì số trung bình của $n - 2$ số còn lại bằng $%s$ nên ta có:
    $$S - %s = %s(n - 2) \\Leftrightarrow S = %s n - %s + %s \\Leftrightarrow S = %s n - %s \\quad (2).$$
    \\end{itemize}
    Từ $(1)$ và $(2)$ ta suy ra phương trình:
    $$%s n + %s = %s n - %s \\Leftrightarrow %s n = %s \\Leftrightarrow n = %s \\text{ (thỏa mãn } n \\ge 5\\text{)}.$$
    Thay $n = %s$ vào $(1)$ ta được tổng ban đầu:
    $$S = %s \\cdot %s + %s = %s.$$
    Suy ra số trung bình ban đầu của mẫu số liệu là:
    $$\\overline{x} = \\dfrac{S}{n} = \\dfrac{%s}{%s} = %s.$$
    \\item Mẫu ban đầu gồm $n = %s$ số nguyên đôi một khác nhau được sắp xếp tăng dần:
    $$%s = x_1 < x_2 < \\dots < x_{%s} < x_{%s} = %s.$$
    Vì cỡ mẫu $n = %s$ là số chẵn nên trung vị là trung bình cộng của hai số chính giữa $x_{%s}$ và $x_{%s}$:
    $$M_e = \\dfrac{x_{%s} + x_{%s}}{2} = %s \\Leftrightarrow x_{%s} + x_{%s} = %s.$$
    Vì $x_{%s} < x_{%s}$ là hai số nguyên nên ta có thể chọn $x_{%s} = %s$ và $x_{%s} = %s$. \\\\
    Các số nguyên còn lại được chọn đôi một khác nhau nằm giữa $%s$ và $%s$ sao cho tổng tất cả $%s$ số bằng $S = %s$. \\\\
    Chẳng hạn, ta chọn được một mẫu số liệu cụ thể thỏa mãn tất cả các dữ kiện của bài toán là:
    $$%s.$$
    (Kiểm tra: tổng của $%s$ số bằng $%s = %s$, trung vị $M_e = \\dfrac{%s + %s}{2} = %s$, loại bỏ $%s$ còn trung bình bằng $\\dfrac{%s}{%s} = %s$, loại bỏ thêm $%s$ còn trung bình bằng $\\dfrac{%s}{%s} = %s$).
    \\end{enumEX}'''
                   %(m_max, m_max, tb1,
                     m_max, tb1, tb1, tb1, m_max, tb1, m_max - tb1,
                     m_max, m_min, m_max, m_min, m_max + m_min, tb2,
                     m_max + m_min, tb2, tb2, 2 * tb2, m_max + m_min, tb2, 2 * tb2 - (m_max + m_min),
                     tb1, m_max - tb1, tb2, 2 * tb2 - (m_max + m_min), diff_tb, diff_tb * n_val, n_val,
                     n_val,
                     tb1, n_val, m_max - tb1, tong_n,
                     tong_n, n_val, tb_ban_dau_str,
                     n_val,
                     m_min, n_val - 1, n_val, m_max,
                     n_val, n_val // 2, n_val // 2 + 1,
                     n_val // 2, n_val // 2 + 1, me_str, n_val // 2, n_val // 2 + 1, mid_left + mid_right,
                     n_val // 2, n_val // 2 + 1, n_val // 2, mid_left, n_val // 2 + 1, mid_right,
                     m_min, m_max, n_val, tong_n,
                     sample_str,
                     n_val, sample_sum_expr, tong_n, mid_left, mid_right, me_str, m_max, tong_n_tru_1, n_val - 1, tb1, m_min, tong_giua, n_val - 2, tb2
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

