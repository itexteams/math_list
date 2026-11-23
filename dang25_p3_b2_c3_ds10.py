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


def bt_dang25_p3_b2_c3_ds10(self):
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
            n = random.choice([12, 16, 20, 24])
            tb_nham_rat = Rational(randint(110, 150), 10)
            tong_nham_rat = n * tb_nham_rat
            
            max_dung_rat = Rational(randint(180, 195), 10)
            max_nham_rat = Rational(randint(145, 170), 10)
            
            min_dung_rat = Rational(randint(40, 70), 10)
            min_nham_rat = Rational(randint(75, 100), 10)
            
            tong_dung_rat = tong_nham_rat - max_nham_rat + max_dung_rat - min_nham_rat + min_dung_rat
            tb_dung_rat = tong_dung_rat / n
            
            if tong_nham_rat.q == 1 and tong_dung_rat.q == 1 and (tb_dung_rat * 1000).q == 1 and tb_dung_rat != tb_nham_rat:
                break
    
        tb_nham_str = fmt_dec(tb_nham_rat)
        tong_nham_str = fmt_dec(tong_nham_rat)
        max_dung_str = fmt_dec(max_dung_rat)
        max_nham_str = fmt_dec(max_nham_rat)
        min_dung_str = fmt_dec(min_dung_rat)
        min_nham_str = fmt_dec(min_nham_rat)
        tong_dung_str = fmt_dec(tong_dung_rat)
        kq_str = fmt_dec(tb_dung_rat)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Điểm thi học sinh giỏi cấp trường môn Tin học của $%s$ thí sinh được thống kê thành một mẫu số liệu có số trung bình là $%s$ điểm. Ban tổ chức phát hiện điểm của thí sinh cao nhất bị nhập nhầm từ $%s$ điểm thành $%s$ điểm, và điểm của thí sinh thấp nhất bị nhập nhầm từ $%s$ điểm thành $%s$ điểm. Sau khi sửa lại cho đúng thì điểm trung bình thực tế của $%s$ thí sinh là bao nhiêu?'''
                         %(str(n), tb_nham_str, max_dung_str, max_nham_str, min_dung_str, min_nham_str, str(n)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Tổng số điểm của $%s$ thí sinh trước khi sửa lại (tính theo số liệu nhập nhầm) là: \\\\
                   $%s \\cdot %s = %s$ (điểm). \\\\
                   Tổng số điểm thực tế của $%s$ thí sinh sau khi đã sửa lại cho đúng là: \\\\
                   $%s - %s + %s - %s + %s = %s$ (điểm). \\\\
                   Vậy điểm trung bình thực tế của $%s$ thí sinh là: \\\\
                   $\\dfrac{%s}{%s} = %s$ (điểm).'''
                   %(str(n),
                     str(n), tb_nham_str, tong_nham_str,
                     str(n),
                     tong_nham_str, max_nham_str, max_dung_str, min_nham_str, min_dung_str, tong_dung_str,
                     str(n),
                     tong_dung_str, str(n), kq_str
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

