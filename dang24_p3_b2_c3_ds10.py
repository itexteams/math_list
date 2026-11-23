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


def bt_dang24_p3_b2_c3_ds10(self):
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
    
        n = 5
        while True:
            # Mẫu gồm 5 số nguyên dương đôi một khác nhau: m1 < m2 < m3 < m4 < m5
            # Q2 = m3
            # Nửa trái Q2 là m1; m2 => Q1 = (m1 + m2)/2
            # Nửa phải Q2 là m4; m5 => Q3 = (m4 + m5)/2
            # Delta_Q = Q3 - Q1 = (m4 + m5 - m1 - m2)/2 => m4 + m5 - m1 - m2 = 2 * Delta_Q
            # Tổng 5 số = 5 * tb = m1 + m2 + m3 + m4 + m5
            # Suy ra:
            # 2(m1 + m2) = 5*tb - m3 - 2*Delta_Q => m1 + m2 = (5*tb - m3 - 2*Delta_Q)/2
            # 2(m4 + m5) = 5*tb - m3 + 2*Delta_Q => m4 + m5 = (5*tb - m3 + 2*Delta_Q)/2
            # Để m5 lớn nhất có thể, ta chọn m4 nhỏ nhất có thể: m4 = m3 + 1
            # Khi đó m5_max = m4 + m5 - (m3 + 1)
            # Đồng thời cần tồn tại m1, m2 nguyên dương thỏa mãn 1 <= m1 < m2 < m3 và m1 + m2 = S12
            # Điều kiện để tồn tại 1 <= m1 < m2 <= m3 - 1 có tổng S12 là: 3 <= S12 <= 2*m3 - 3
            m3 = randint(7, 13)
            tb = randint(m3, m3 + 4)
            delta_q = randint(5, 10)
            
            tong_5 = 5 * tb
            hai_s12 = tong_5 - m3 - 2 * delta_q
            hai_s45 = tong_5 - m3 + 2 * delta_q
            
            if hai_s12 % 2 == 0 and hai_s45 % 2 == 0:
                s12 = hai_s12 // 2
                s45 = hai_s45 // 2
                if 3 <= s12 <= 2 * m3 - 3:
                    m4_min = m3 + 1
                    m5_max = s45 - m4_min
                    if m5_max > m4_min:
                        m1_ex = 1 if s12 - 1 < m3 else s12 - (m3 - 1)
                        m2_ex = s12 - m1_ex
                        if 1 <= m1_ex < m2_ex < m3:
                            break
    
        kq_str = str(m5_max)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Có $%s$ hộp quà được đánh số từ $1$ đến $%s$, khối lượng mỗi hộp (đơn vị: kg) đều là các số nguyên dương đôi một khác nhau và đã sắp xếp tăng dần: $m_1 < m_2 < m_3 < m_4 < m_5$. Biết rằng khối lượng trung bình của $%s$ hộp là $%s$ kg, trung vị là $%s$ kg và khoảng tứ phân vị $\\Delta_Q = %s$ kg. Khối lượng lớn nhất có thể có của hộp thứ $5$ ($m_5$) bằng bao nhiêu?'''
                         %(str(n), str(n), str(n), str(tb), str(m3), str(delta_q)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì mẫu số liệu gồm $n = %s$ giá trị đã được sắp xếp theo thứ tự tăng dần $m_1 < m_2 < m_3 < m_4 < m_5$ nên: \\\\
                   - Trung vị của mẫu số liệu là giá trị chính giữa, tức là $Q_2 = m_3 = %s$. \\\\
                   - Nửa số liệu bên trái $Q_2$ gồm $2$ giá trị là $m_1; m_2$ nên tứ phân vị thứ nhất là: $Q_1 = \\dfrac{m_1 + m_2}{2}$. \\\\
                   - Nửa số liệu bên phải $Q_2$ gồm $2$ giá trị là $m_4; m_5$ nên tứ phân vị thứ ba là: $Q_3 = \\dfrac{m_4 + m_5}{2}$. \\\\
                   Theo đề bài, khoảng tứ phân vị là $\\Delta_Q = %s$ nên ta có: \\\\
                   $Q_3 - Q_1 = %s \\Leftrightarrow \\dfrac{m_4 + m_5}{2} - \\dfrac{m_1 + m_2}{2} = %s \\Leftrightarrow (m_4 + m_5) - (m_1 + m_2) = %s \\quad (1)$. \\\\
                   Mặt khác, khối lượng trung bình của $%s$ hộp là $%s$ kg nên tổng khối lượng của cả $%s$ hộp là: \\\\
                   $m_1 + m_2 + m_3 + m_4 + m_5 = %s \\cdot %s = %s$. \\\\
                   Thay $m_3 = %s$ vào đẳng thức trên, ta được: \\\\
                   $(m_4 + m_5) + (m_1 + m_2) = %s - %s = %s \\quad (2)$. \\\\
                   Cộng vế theo vế của $(1)$ và $(2)$, ta suy ra: \\\\
                   $2(m_4 + m_5) = %s + %s = %s \\Leftrightarrow m_4 + m_5 = %s$ (và $m_1 + m_2 = %s$). \\\\
                   Vì khối lượng các hộp đều là các số nguyên dương và $m_3 < m_4 < m_5$ với $m_3 = %s$ nên $m_4 \\ge %s$. \\\\
                   Do đó, để $m_5$ đạt giá trị lớn nhất thì $m_4$ phải nhỏ nhất, tức là $m_4 = %s$. \\\\
                   Khi đó, khối lượng lớn nhất có thể có của hộp thứ $5$ là: \\\\
                   $m_5 = %s - %s = %s$ (kg) (chẳng hạn ứng với bộ số liệu $%s; %s; %s; %s; %s$).'''
                   %(str(n),
                     str(m3),
                     str(delta_q),
                     str(delta_q), str(delta_q), str(2 * delta_q),
                     str(n), str(tb), str(n),
                     str(n), str(tb), str(tong_5),
                     str(m3),
                     str(tong_5), str(m3), str(tong_5 - m3),
                     str(2 * delta_q), str(tong_5 - m3), str(hai_s45), str(s45), str(s12),
                     str(m3), str(m4_min),
                     str(m4_min),
                     str(s45), str(m4_min), kq_str, str(m1_ex), str(m2_ex), str(m3), str(m4_min), kq_str
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

