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


def bt_dang22_p3_b2_c3_ds10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        def fmt_dec(rat_val):
            if rat_val.q == 1:
                return str(rat_val.p)
            else:
                d_val = Decimal(rat_val.p) / Decimal(rat_val.q)
                s = str(d_val.normalize())
                if 'E' in s or 'e' in s:
                    s = '{:f}'.format(d_val)
                return s.replace('.', ',')
    
        while True:
            N = random.choice([36, 40, 44, 48])
            f1 = randint(3, 6)
            f3 = randint(10, 15)
            f5 = randint(4, 8)
            f6 = randint(2, 5)
            
            x_val = randint(5, f3 - 1)
            y_val = N - (f1 + x_val + f3 + f5 + f6)
            
            if 4 <= y_val < f3:
                tong_sach = 1 * f1 + 2 * x_val + 3 * f3 + 4 * y_val + 5 * f5 + 6 * f6
                tb_rat = Rational(tong_sach, N)
                if (tb_rat * 100).q == 1:
                    # Xây dựng mảng đầy đủ để tính Q3 chính xác
                    full_arr = [1]*f1 + [2]*x_val + [3]*f3 + [4]*y_val + [5]*f5 + [6]*f6
                    mid2 = N // 2
                    nua_phai = full_arr[mid2:]
                    m = len(nua_phai) # m chẵn vì N chia hết cho 4
                    idx1 = m // 2 - 1
                    idx2 = m // 2
                    v1 = nua_phai[idx1]
                    v2 = nua_phai[idx2]
                    q3_rat = Rational(v1 + v2, 2)
                    if (q3_rat * 10).q == 1:
                        break
    
        tb_str = fmt_dec(tb_rat)
        kq_str = fmt_dec(q3_rat)
        
        tong_f_da_biet = f1 + f3 + f5 + f6
        tong_xy = N - tong_f_da_biet
        tong_sach_da_biet = 1 * f1 + 3 * f3 + 5 * f5 + 6 * f6
        tong_2x4y = tong_sach - tong_sach_da_biet
        tong_x2y = tong_2x4y // 2
        
        pos1 = mid2 + idx1 + 1
        pos2 = mid2 + idx2 + 1
        
        c1 = f1
        c2 = f1 + x_val
        c3 = c2 + f3
        c4 = c3 + y_val
        c5 = c4 + f5
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Bảng tần số thống kê số lượng sách mượn trong học kỳ I của $%s$ sinh viên một lớp đại học như sau:
    \\begin{center}
    \\begin{tabular}{|l|c|c|c|c|c|c|}
    \\hline
    \\textbf{Số cuốn sách} & $1$ & $2$ & $3$ & $4$ & $5$ & $6$ \\\\
    \\hline
    \\textbf{Số sinh viên} & $%s$ & $x$ & $%s$ & $y$ & $%s$ & $%s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Biết rằng mốt của mẫu số liệu là $3$ và số sách mượn trung bình của mỗi sinh viên là $%s$ cuốn. Tứ phân vị thứ ba ($Q_3$) của mẫu số liệu bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục).'''
                         %(str(N), str(f1), str(f3), str(f5), str(f6), tb_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì lớp có tất cả $%s$ sinh viên nên ta có phương trình: \\\\
                   $%s + x + %s + y + %s + %s = %s \\Leftrightarrow x + y = %s \\quad (1)$. \\\\
                   Vì số sách mượn trung bình của mỗi sinh viên là $%s$ cuốn nên ta có phương trình: \\\\
                   $\\dfrac{1 \\cdot %s + 2x + 3 \\cdot %s + 4y + 5 \\cdot %s + 6 \\cdot %s}{%s} = %s$ \\\\
                   $\\Leftrightarrow %s + 2x + 4y = %s \\Leftrightarrow 2x + 4y = %s \\Leftrightarrow x + 2y = %s \\quad (2)$. \\\\
                   Từ $(1)$ và $(2)$, ta có hệ phương trình: \\\\
                   $\\left\\{\\begin{aligned} x + y &= %s \\\\ x + 2y &= %s \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} x &= %s \\\\ y &= %s \\end{aligned}\\right.$ (thỏa mãn điều kiện $3$ là mốt duy nhất vì tần số của $3$ là $%s$ lớn nhất). \\\\
                   Khi sắp xếp $%s$ giá trị của mẫu số liệu theo thứ tự không giảm: \\\\
                   - Các giá trị từ thứ $1$ đến thứ $%s$ bằng $1$; \\\\
                   - Các giá trị từ thứ $%s$ đến thứ $%s$ bằng $2$; \\\\
                   - Các giá trị từ thứ $%s$ đến thứ $%s$ bằng $3$; \\\\
                   - Các giá trị từ thứ $%s$ đến thứ $%s$ bằng $4$; \\\\
                   - Các giá trị từ thứ $%s$ đến thứ $%s$ bằng $5$; \\\\
                   - Các giá trị từ thứ $%s$ đến thứ $%s$ bằng $6$. \\\\
                   Vì mẫu có $n = %s$ giá trị nên nửa số liệu bên phải $Q_2$ gồm $%s$ giá trị (từ vị trí thứ $%s$ đến thứ $%s$). Do đó, tứ phân vị thứ ba $Q_3$ là trung bình cộng của hai giá trị ở vị trí thứ $%s$ và thứ $%s$ của mẫu: \\\\
                   $Q_3 = \\dfrac{x_{%s} + x_{%s}}{2} = \\dfrac{%s + %s}{2} = %s$.'''
                   %(str(N),
                     str(f1), str(f3), str(f5), str(f6), str(N), str(tong_xy),
                     tb_str,
                     str(f1), str(f3), str(f5), str(f6), str(N), tb_str,
                     str(tong_sach_da_biet), str(tong_sach), str(tong_2x4y), str(tong_x2y),
                     str(tong_xy), str(tong_x2y), str(x_val), str(y_val), str(f3),
                     str(N),
                     str(c1),
                     str(c1 + 1), str(c2),
                     str(c2 + 1), str(c3),
                     str(c3 + 1), str(c4),
                     str(c4 + 1), str(c5),
                     str(c5 + 1), str(N),
                     str(N), str(m), str(mid2 + 1), str(N), str(pos1), str(pos2),
                     str(pos1), str(pos2), str(v1), str(v2), kq_str
                   ))
        
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+
    str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n')
    return content

