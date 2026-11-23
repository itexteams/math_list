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


def bt_dang13_p4_b2_c3_ds10(self):
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
        # Sinh ngẫu nhiên dãy 11 số liệu không giảm, đảm bảo kết quả trung bình mới là số thập phân hữu hạn đẹp
        while True:
            # 5 số đầu nhỏ hơn trung vị (từ 2 đến 6)
            me_val = randint(7, 9)
            left_vals = sorted([randint(2, me_val - 1) for _ in range(5)])
            # 5 số sau lớn hơn hoặc bằng trung vị, trong đó có 2 hoặc 3 số từ nguong trở lên
            nguong = randint(10, 12)
            mid_right = sorted([randint(me_val, nguong - 1) for _ in range(2)])
            high_vals = sorted([nguong, randint(nguong + 1, nguong + 3), randint(nguong + 3, nguong + 6)])
            
            data = left_vals + [me_val] + mid_right + high_vals
            
            ho_tro = Decimal(random.choice([12, 15, 16, 18, 20])) / Decimal(10)
            phan_tram = random.choice([10, 15, 20])
            ty_le_con = Decimal(100 - phan_tram) / Decimal(100)
            
            # Tính dãy mới
            new_data = []
            for v in data:
                v_dec = Decimal(v)
                if v < me_val:
                    new_data.append(v_dec + ho_tro)
                elif v >= nguong:
                    new_data.append(v_dec * ty_le_con)
                else:
                    new_data.append(v_dec)
                    
            tong_moi = sum(new_data)
            # Kiểm tra để mức thưởng trung bình mới là số thập phân hữu hạn (tối đa 2 chữ số thập phân)
            if (tong_moi * 100) % 11 == 0:
                break
    
        data_str = "; ".join(str(v) for v in data)
        ho_tro_str = format_num(ho_tro)
        
        # Danh sách các mức thưởng thấp hơn trung vị (5 giá trị đầu tiên)
        low_str = "; ".join(str(v) for v in left_vals)
        low_new_vals = [Decimal(v) + ho_tro for v in left_vals]
        low_new_str = "; ".join(format_num(v) for v in low_new_vals)
        
        # Danh sách các mức thưởng từ nguong trở lên (3 giá trị cuối cùng)
        high_str = "; ".join(str(v) for v in high_vals)
        high_new_vals = [Decimal(v) * ty_le_con for v in high_vals]
        high_new_str = "; ".join(format_num(v) for v in high_new_vals)
        
        # Danh sách các mức thưởng giữ nguyên (từ trung vị đến dưới nguong)
        keep_vals = [me_val] + mid_right
        keep_str = "; ".join(str(v) for v in keep_vals)
        
        # Dãy tiền thưởng đầy đủ sau khi điều chỉnh
        new_data_str = "; ".join(format_num(v) for v in new_data)
        new_sum_expr = " + ".join(format_num(v) for v in new_data)
        tong_moi_str = format_num(tong_moi)
        
        tb_moi = tong_moi / Decimal(11)
        tb_moi_str = format_num(tb_moi)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Tiền thưởng cuối năm (đơn vị: triệu đồng) của $11$ nhân viên một chi nhánh bán lẻ được sắp xếp không giảm là:
    $$%s.$$
    Công đoàn quyết định hỗ trợ thêm $%s$ triệu đồng cho tất cả nhân viên có mức thưởng \\textbf{thấp hơn} trung vị, đồng thời khấu trừ $%s\\%%$ tiền thưởng đối với những nhân viên có mức thưởng từ $%s$ triệu đồng trở lên để đóng quỹ từ thiện. Tính mức thưởng trung bình mới của $11$ nhân viên sau khi thực hiện chính sách này.'''
                         %(data_str, ho_tro_str, phan_tram, nguong
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Mẫu số liệu gồm $n = 11$ giá trị đã được sắp xếp theo thứ tự không giảm:
    $$%s.$$
    Vì cỡ mẫu $n = 11$ là số lẻ nên trung vị của mẫu số liệu là giá trị đứng ở vị trí chính giữa (vị trí thứ $6$):
    $$M_e = %s \\text{ (triệu đồng)}.$$
    Sau khi thực hiện chính sách hỗ trợ và khấu trừ:
    \\begin{itemize}
    \\item Có $5$ nhân viên có mức thưởng thấp hơn trung vị ($%s$ triệu đồng) được hỗ trợ thêm $%s$ triệu đồng, nên mức thưởng mới của họ lần lượt là:
    $$%s \\text{ (triệu đồng)}.$$
    \\item Có $3$ nhân viên có mức thưởng từ $%s$ triệu đồng trở lên ($%s$ triệu đồng) bị khấu trừ $%s\\%%$ tiền thưởng (tức còn lại $%s\\%%$ mức thưởng ban đầu), nên mức thưởng mới của họ lần lượt là:
    $$%s \\text{ (triệu đồng)}.$$
    \\item Có $3$ nhân viên có mức thưởng từ $%s$ triệu đồng đến dưới $%s$ triệu đồng ($%s$ triệu đồng) không thuộc diện hỗ trợ hay khấu trừ nên giữ nguyên mức thưởng.
    \\end{itemize}
    Như vậy, dãy tiền thưởng mới (đơn vị: triệu đồng) của $11$ nhân viên là:
    $$%s.$$
    Mức thưởng trung bình mới của $11$ nhân viên là:
    $$\\overline{x} = \\dfrac{%s}{11} = \\dfrac{%s}{11} = %s \\text{ (triệu đồng)}.$$'''
                   %(data_str,
                     me_val,
                     low_str, ho_tro_str, low_new_str,
                     nguong, high_str, phan_tram, 100 - phan_tram, high_new_str,
                     me_val, nguong, keep_str,
                     new_data_str,
                     new_sum_expr, tong_moi_str, tb_moi_str
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

