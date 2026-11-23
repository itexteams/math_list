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


def bt_dang8_p4_b2_c3_ds10(self):
    def format_decimal(val):
        s = str(val)
        return s.replace('.', ',')
    
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Tạo dữ liệu ngẫu nhiên đảm bảo số nhân viên tuyển thêm là số nguyên dương đẹp
        while True:
            n_cu = randint(6, 15)
            x_them = randint(2, 10)
            luong_tb_moi = Decimal(randint(38, 48)) / Decimal(10)
            chenh_lech_moi = Decimal(randint(2, 6)) / Decimal(10)
            luong_moi = luong_tb_moi - chenh_lech_moi
            
            # Tính lương trung bình cũ từ phương trình: n_cu * luong_cu + x_them * luong_moi = (n_cu + x_them) * luong_tb_moi
            tong_luong_sau = (Decimal(n_cu) + Decimal(x_them)) * luong_tb_moi
            tong_luong_moi = Decimal(x_them) * luong_moi
            tong_luong_cu = tong_luong_sau - tong_luong_moi
            
            if (tong_luong_cu * 10) % n_cu == 0:
                luong_cu = tong_luong_cu / Decimal(n_cu)
                if luong_cu > luong_tb_moi and luong_moi > 0:
                    break
    
        luong_cu_str = format_decimal(luong_cu)
        luong_moi_str = format_decimal(luong_moi)
        luong_tb_moi_str = format_decimal(luong_tb_moi)
        
        tong_luong_cu_str = format_decimal(tong_luong_cu.normalize()) if tong_luong_cu % 1 != 0 else str(int(tong_luong_cu))
        tong_luong_sau_str = format_decimal(tong_luong_sau.normalize()) if tong_luong_sau % 1 != 0 else str(int(tong_luong_sau))
        
        hieu_luong = luong_tb_moi - luong_moi
        hieu_luong_str = format_decimal(hieu_luong.normalize()) if hieu_luong % 1 != 0 else str(int(hieu_luong))
        
        chenh_lech_tong = tong_luong_cu - Decimal(n_cu) * luong_tb_moi
        chenh_lech_tong_str = format_decimal(chenh_lech_tong.normalize()) if chenh_lech_tong % 1 != 0 else str(int(chenh_lech_tong))
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một quán cà phê hiện có $%s$ nhân viên phục vụ bán thời gian với mức lương trung bình là $%s$ triệu đồng/tháng. Để đáp ứng lượng khách tăng vào dịp lễ, chủ quán dự định tuyển thêm một số nhân viên mới có mức lương khởi điểm là $%s$ triệu đồng/tháng sao cho mức lương trung bình của toàn bộ nhân viên trong quán sau khi tuyển đạt đúng $%s$ triệu đồng/tháng. Hỏi chủ quán cần tuyển thêm bao nhiêu nhân viên?'''
                         %(n_cu, luong_cu_str, luong_moi_str, luong_tb_moi_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ là số nhân viên mới mà chủ quán cần tuyển thêm ($x \\in \\mathbb{N}^*$). \\\\
    Tổng số tiền lương hiện tại của $%s$ nhân viên cũ trong một tháng là:
    $$%s \\cdot %s = %s \\text{ (triệu đồng).}$$
    Sau khi tuyển thêm $x$ nhân viên mới, tổng số nhân viên của quán là $%s + x$ (người). \\\\
    Tổng số tiền lương của toàn bộ nhân viên trong quán sau khi tuyển thêm là:
    $$%s + %s x \\text{ (triệu đồng).}$$
    Vì mức lương trung bình của toàn bộ nhân viên sau khi tuyển đạt đúng $%s$ triệu đồng/tháng nên ta có phương trình:
    $$\\dfrac{%s + %s x}{%s + x} = %s$$
    Giải phương trình trên:
    $$%s + %s x = %s(%s + x)$$
    $$%s + %s x = %s + %s x$$
    $$%s x = %s$$
    $$x = %s \\text{ (thỏa mãn điều kiện).}$$
    Vậy chủ quán cần tuyển thêm $%s$ nhân viên.'''
                   %(n_cu,
                     n_cu, luong_cu_str, tong_luong_cu_str,
                     n_cu,
                     tong_luong_cu_str, luong_moi_str,
                     luong_tb_moi_str,
                     tong_luong_cu_str, luong_moi_str, n_cu, luong_tb_moi_str,
                     tong_luong_cu_str, luong_moi_str, luong_tb_moi_str, n_cu,
                     tong_luong_cu_str, luong_moi_str, format_decimal((Decimal(n_cu) * luong_tb_moi).normalize()) if (Decimal(n_cu) * luong_tb_moi) % 1 != 0 else str(int(Decimal(n_cu) * luong_tb_moi)), luong_tb_moi_str,
                     hieu_luong_str, chenh_lech_tong_str,
                     x_them,
                     x_them
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

