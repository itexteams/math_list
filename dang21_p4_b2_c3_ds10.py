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


def bt_dang21_p4_b2_c3_ds10(self):
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
        # Hệ số môn Toán, Lý, Hóa là 3, 2, 1 (tổng hệ số = 6)
        # Sinh ngẫu nhiên điểm Toán, điểm Lý và ngưỡng điểm trung bình yêu cầu sao cho:
        # - Điểm Toán > điểm Lý (để 3 điểm Toán đứng cuối, 2 điểm Lý đứng giữa -> vị trí 3 là Lý, vị trí 4 là Toán)
        # - Điểm Hóa tối thiểu x_min nằm trong khoảng [8.0, 10.0] và đẹp (1 chữ số thập phân)
        while True:
            ten = random.choice(["Minh", "Lan", "Hùng", "Trang", "Nam", "Vy"])
            diem_toan = Decimal(randint(84, 92)) / Decimal(10)
            diem_ly = Decimal(randint(76, 84)) / Decimal(10)
            if diem_toan <= diem_ly:
                continue
                
            diem_tb_yc = Decimal(random.choice([82, 84, 85, 86, 88])) / Decimal(10)
            
            tong_diem_yc = Decimal(6) * diem_tb_yc
            tong_toan_ly = Decimal(3) * diem_toan + Decimal(2) * diem_ly
            diem_hoa_min = tong_diem_yc - tong_toan_ly
            
            if Decimal('8.0') <= diem_hoa_min <= Decimal('10.0'):
                break
    
        diem_toan_str = format_1dec(diem_toan)
        diem_ly_str = format_1dec(diem_ly)
        diem_tb_yc_str = format_1dec(diem_tb_yc)
        
        tich_toan = Decimal(3) * diem_toan
        tich_ly = Decimal(2) * diem_ly
        tich_toan_str = format_num(tich_toan)
        tich_ly_str = format_num(tich_ly)
        tong_toan_ly_str = format_num(tong_toan_ly)
        tong_diem_yc_str = format_num(tong_diem_yc)
        diem_hoa_min_str = format_num(diem_hoa_min)
        
        # Tính trung vị của tập 6 điểm: 3 điểm Toán (T), 2 điểm Lý (L), 1 điểm Hóa (x)
        # Vì L < T:
        # - Trường hợp 1: x <= L => dãy sắp xếp: x <= L <= L <= T <= T <= T => vị trí 3 là L, vị trí 4 là T => Me = (L + T)/2
        # - Trường hợp 2: L < x < T => dãy sắp xếp: L <= L < x < T <= T <= T => vị trí 3 là x, vị trí 4 là T => Me = (x + T)/2
        # - Trường hợp 3: x >= T => dãy sắp xếp: L <= L <= T <= T <= T <= x => vị trí 3 là T, vị trí 4 là T => Me = (T + T)/2 = T
        me_th1 = (diem_ly + diem_toan) / Decimal(2)
        me_th1_str = format_num(me_th1)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một trường THPT xét học bổng dựa trên điểm trung bình $3$ môn Toán, Lý, Hóa với hệ số lần lượt là $3; 2; 1$. Bạn %s đã thi xong môn Toán được $%s$ điểm và môn Lý được $%s$ điểm. \\\\
    a) %s cần đạt ít nhất bao nhiêu điểm môn Hóa để điểm trung bình có trọng số đạt từ $%s$ điểm trở lên? \\\\
    b) Nếu nhà trường thay đổi quy chế: không dùng điểm trung bình có trọng số mà dùng \\textbf{trung vị} của tập hợp điểm số sau khi nhân bản mỗi điểm theo đúng hệ số của nó (tức là tập gồm $3$ điểm Toán, $2$ điểm Lý, $1$ điểm Hóa). Khi đó điểm môn Hóa của %s ảnh hưởng thế nào đến trung vị này? Giải thích chi tiết.'''
                         %(ten, diem_toan_str, diem_ly_str,
                           ten, diem_tb_yc_str,
                           ten
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Gọi $x$ là điểm môn Hóa của bạn %s ($0 \\le x \\le 10$). \\\\
    Điểm trung bình có trọng số của $3$ môn Toán, Lý, Hóa là:
    $$\\overline{x} = \\dfrac{3 \\cdot %s + 2 \\cdot %s + 1 \\cdot x}{3 + 2 + 1} = \\dfrac{%s + %s + x}{6} = \\dfrac{%s + x}{6}.$$
    Để điểm trung bình có trọng số đạt từ $%s$ điểm trở lên thì:
    $$\\dfrac{%s + x}{6} \\ge %s \\Leftrightarrow %s + x \\ge %s \\Leftrightarrow x \\ge %s - %s \\Leftrightarrow x \\ge %s.$$
    Vậy bạn %s cần đạt ít nhất $%s$ điểm môn Hóa.
    \\item Sau khi nhân bản mỗi điểm theo đúng hệ số của nó, ta thu được tập hợp gồm $n = 6$ điểm số bao gồm: ba điểm $%s$ (Toán), hai điểm $%s$ (Lý) và một điểm $x$ (Hóa). \\\\
    Vì cỡ mẫu $n = 6$ là số chẵn nên trung vị $M_e$ là trung bình cộng của hai giá trị đứng ở vị trí thứ $3$ và thứ $4$ sau khi sắp xếp $6$ điểm theo thứ tự không giảm. Ta xét các trường hợp của điểm môn Hóa $x$ ($0 \\le x \\le 10$):
    \\begin{itemize}
    \\item \\textbf{Trường hợp 1: $0 \\le x \\le %s$.} \\\\
    Khi đó dãy điểm sắp xếp không giảm là: $x; %s; %s; %s; %s; %s$. \\\\
    Hai giá trị đứng ở vị trí thứ $3$ và thứ $4$ lần lượt là $%s$ và $%s$, nên trung vị là:
    $$M_e = \\dfrac{%s + %s}{2} = %s.$$
    Trong trường hợp này, trung vị cố định bằng $%s$ và \\textbf{không phụ thuộc} vào điểm môn Hóa $x$.
    \\item \\textbf{Trường hợp 2: $%s < x < %s$.} \\\\
    Khi đó dãy điểm sắp xếp không giảm là: $%s; %s; x; %s; %s; %s$. \\\\
    Hai giá trị đứng ở vị trí thứ $3$ và thứ $4$ lần lượt là $x$ và $%s$, nên trung vị là:
    $$M_e = \\dfrac{x + %s}{2}.$$
    Trong trường hợp này, trung vị \\textbf{tăng tuyến tính} theo điểm môn Hóa $x$ (tăng từ lớn hơn $%s$ đến nhỏ hơn $%s$).
    \\item \\textbf{Trường hợp 3: $%s \\le x \\le 10$.} \\\\
    Khi đó dãy điểm sắp xếp không giảm là: $%s; %s; %s; %s; %s; x$. \\\\
    Hai giá trị đứng ở vị trí thứ $3$ và thứ $4$ đều bằng $%s$, nên trung vị là:
    $$M_e = \\dfrac{%s + %s}{2} = %s.$$
    Trong trường hợp này, trung vị đạt giá trị tối đa là $%s$ và \\textbf{không tăng thêm} dù điểm môn Hóa cao hơn $%s$.
    \\end{itemize}
    \\textbf{Kết luận:} Điểm môn Hóa chỉ làm thay đổi trung vị khi nằm trong khoảng $(%s; %s)$. Nếu điểm Hóa từ $%s$ trở xuống thì trung vị luôn bị giữ ở mức $%s$, còn nếu điểm Hóa từ $%s$ trở lên thì trung vị cũng chỉ đạt tối đa là $%s$ (bị chặn trên bởi điểm môn Toán).
    \\end{enumEX}'''
                   %(ten,
                     diem_toan_str, diem_ly_str, tich_toan_str, tich_ly_str, tong_toan_ly_str,
                     diem_tb_yc_str,
                     tong_toan_ly_str, diem_tb_yc_str, tong_toan_ly_str, tong_diem_yc_str, tong_diem_yc_str, tong_toan_ly_str, diem_hoa_min_str,
                     ten, diem_hoa_min_str,
                     diem_toan_str, diem_ly_str,
                     diem_ly_str,
                     diem_ly_str, diem_ly_str, diem_toan_str, diem_toan_str, diem_toan_str,
                     diem_ly_str, diem_toan_str,
                     diem_ly_str, diem_toan_str, me_th1_str,
                     me_th1_str,
                     diem_ly_str, diem_toan_str,
                     diem_ly_str, diem_ly_str, diem_toan_str, diem_toan_str, diem_toan_str,
                     diem_toan_str,
                     diem_toan_str,
                     me_th1_str, diem_toan_str,
                     diem_toan_str,
                     diem_ly_str, diem_ly_str, diem_toan_str, diem_toan_str, diem_toan_str,
                     diem_toan_str,
                     diem_toan_str, diem_toan_str, diem_toan_str,
                     diem_toan_str, diem_toan_str,
                     diem_ly_str, diem_toan_str, diem_ly_str, me_th1_str, diem_toan_str, diem_toan_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

