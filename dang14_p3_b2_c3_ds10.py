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


def bt_dang14_p3_b2_c3_ds10(self):
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
            n_all = random.choice([8, 10, 12])
            n_dau = n_all - 1
            tb_dau_rat = Rational(randint(85, 95), 10)
            tong_dau_rat = n_dau * tb_dau_rat
            
            diem_cuoi_rat = Rational(randint(90, 99), 10)
            tong_all_rat = tong_dau_rat + diem_cuoi_rat
            tb_all_rat = tong_all_rat / n_all
            
            if (tb_all_rat * 100).q == 1 and tb_all_rat > tb_dau_rat:
                break
                
        tb_dau_str = fmt_dec(tb_dau_rat)
        tong_dau_str = fmt_dec(tong_dau_rat)
        tb_all_str = fmt_dec(tb_all_rat)
        tong_all_str = fmt_dec(tong_all_rat)
        kq_str = fmt_dec(diem_cuoi_rat)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong một cuộc thi bắn súng thể thao, mỗi vận động viên bắn $%s$ phát đạn (thang điểm tối đa $10$ điểm/phát). Thành tích của xạ thủ An qua $%s$ phát đầu có điểm trung bình là $%s$ điểm. Hỏi ở phát bắn thứ $%s$, An cần đạt bao nhiêu điểm để điểm trung bình cả $%s$ phát đạt mức $%s$ điểm?'''
                         %(str(n_all), str(n_dau), tb_dau_str, str(n_all), str(n_all), tb_all_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Tổng số điểm của xạ thủ An sau $%s$ phát bắn đầu tiên là: \\\\
                   $%s \\cdot %s = %s$ (điểm). \\\\
                   Để điểm trung bình của cả $%s$ phát bắn đạt $%s$ điểm thì tổng số điểm của cả $%s$ phát phải là: \\\\
                   $%s \\cdot %s = %s$ (điểm). \\\\
                   Vậy ở phát bắn thứ $%s$, xạ thủ An cần đạt số điểm là: \\\\
                   $%s - %s = %s$ (điểm).'''
                   %(str(n_dau),
                     str(n_dau), tb_dau_str, tong_dau_str,
                     str(n_all), tb_all_str, str(n_all),
                     str(n_all), tb_all_str, tong_all_str,
                     str(n_all),
                     tong_all_str, tong_dau_str, kq_str
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

