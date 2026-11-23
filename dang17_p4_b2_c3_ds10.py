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


def bt_dang17_p4_b2_c3_ds10(self):
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
    
    def format_score_1dec(val):
        s = format(val, '.1f')
        return s.replace('.', ',')
    
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Sinh ngẫu nhiên dãy 14 điểm thi (bội của 0,5 từ 5,0 đến 9,5), sắp xếp không giảm
        # Đảm bảo sau khi nhân hệ số he_so và cộng uu_tien, có 1 hoặc 2 điểm vượt quá 10 (phải khống chế tối đa 10)
        # và tổng điểm mới chia hết cho 14 hoặc cho 7 để số trung bình đẹp
        while True:
            he_so = Decimal(random.choice([11, 12])) / Decimal(10)
            uu_tien = Decimal(random.choice([2, 3, 4, 5])) / Decimal(10)
            
            pool = [Decimal(k) / Decimal(2) for k in range(10, 20)] # 5.0 đến 9.5
            data = sorted([random.choice(pool) for _ in range(14)])
            # Đảm bảo điểm thấp nhất >= 5.0 và điểm cao nhất là 9.0 hoặc 9.5 để chạm trần 10
            if data[0] > Decimal('6.0') or data[-1] < Decimal('9.0'):
                continue
                
            new_data = []
            capped_count = 0
            for v in data:
                raw_v = v * he_so + uu_tien
                if raw_v > Decimal('10'):
                    new_data.append(Decimal('10'))
                    capped_count += 1
                else:
                    new_data.append(raw_v)
                    
            if capped_count >= 1 and capped_count <= 3:
                tong_moi = sum(new_data)
                # Kiểm tra để trung bình mới chia hết cho 14 (số thập phân hữu hạn 2 chữ số)
                if (tong_moi * 100) % 14 == 0:
                    break
    
        data_str = "; ".join(format_score_1dec(v) for v in data)
        he_so_str = format_num(he_so)
        uu_tien_str = format_num(uu_tien)
        
        new_data_str = "; ".join(format_num(v) for v in new_data)
        new_sum_expr = " + ".join(format_num(v) for v in new_data)
        tong_moi_str = format_num(tong_moi)
        
        tb_moi = tong_moi / Decimal(14)
        tb_moi_str = format_num(tb_moi)
        
        # Với n = 14:
        # Trung vị Me là trung bình cộng của vị trí thứ 7 (index 6) và thứ 8 (index 7)
        x7, x8 = new_data[6], new_data[7]
        me_moi = (x7 + x8) / Decimal(2)
        me_moi_str = format_num(me_moi)
        
        # Nửa số liệu bên trái gồm 7 giá trị (index 0..6) -> Q1 là vị trí thứ 4 (index 3)
        left_str = "; ".join(format_num(v) for v in new_data[:7])
        q1_moi = new_data[3]
        q1_moi_str = format_num(q1_moi)
        
        # Nửa số liệu bên phải gồm 7 giá trị (index 7..13) -> Q3 là vị trí thứ 11 (index 10)
        right_str = "; ".join(format_num(v) for v in new_data[7:])
        q3_moi = new_data[10]
        q3_moi_str = format_num(q3_moi)
        
        delta_q_moi = q3_moi - q1_moi
        delta_q_moi_str = format_num(delta_q_moi)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Điểm thi môn Vẽ mỹ thuật của $14$ thí sinh được thống kê qua dãy số liệu:
    $$%s.$$
    Do đề thi phần hình họa có độ khó cao hơn dự kiến, hội đồng chấm thi quyết định nhân hệ số $%s$ cho tất cả điểm số, sau đó cộng thêm $%s$ điểm ưu tiên khu vực cho mỗi thí sinh (điểm tối đa không vượt quá $10$). Tìm số trung bình, trung vị và khoảng tứ phân vị của bảng điểm sau khi điều chỉnh.'''
                         %(data_str, he_so_str, uu_tien_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Áp dụng quy tắc điều chỉnh $y = %s x + %s$ (nếu $y > 10$ thì lấy $y = 10$) cho từng điểm số trong mẫu số liệu ban đầu, ta được bảng điểm mới gồm $n = 14$ giá trị đã sắp xếp theo thứ tự không giảm:
    $$%s.$$
    \\begin{itemize}
    \\item Số trung bình cộng của bảng điểm sau khi điều chỉnh là:
    $$\\overline{y} = \\dfrac{%s}{14} = \\dfrac{%s}{14} = %s.$$
    \\item Vì cỡ mẫu $n = 14$ là số chẵn nên trung vị là trung bình cộng của hai giá trị đứng ở vị trí thứ $7$ và thứ $8$:
    $$M_e = \\dfrac{%s + %s}{2} = %s.$$
    \\item Nửa số liệu bên trái gồm $7$ giá trị: $%s$. Tứ phân vị thứ nhất là trung vị của nửa số liệu bên trái (giá trị ở vị trí thứ $4$):
    $$Q_1 = %s.$$
    \\item Nửa số liệu bên phải gồm $7$ giá trị: $%s$. Tứ phân vị thứ ba là trung vị của nửa số liệu bên phải (giá trị ở vị trí thứ $11$):
    $$Q_3 = %s.$$
    \\item Khoảng tứ phân vị của bảng điểm sau khi điều chỉnh là:
    $$\\Delta_Q = Q_3 - Q_1 = %s - %s = %s.$$
    \\end{itemize}'''
                   %(he_so_str, uu_tien_str,
                     new_data_str,
                     new_sum_expr, tong_moi_str, tb_moi_str,
                     format_num(x7), format_num(x8), me_moi_str,
                     left_str, q1_moi_str,
                     right_str, q3_moi_str,
                     q3_moi_str, q1_moi_str, delta_q_moi_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

