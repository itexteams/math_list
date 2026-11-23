import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols, sqrt, evaluate, Subs, latex, Rational
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

def bt_dang11_p2_b2_c3_ds10(self):
    def format_dec(val):
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    def format_list_num(lst):
        return '; '.join('$' + str(v) + '$' for v in lst)
    
    # Random mẫu số liệu số ngày làm việc trong tháng của 10 công nhân có 1 mốt duy nhất
    while True:
        mode_val = random.randint(23, 27)
        mode_freq = random.choice([3, 4])
        rem_count = 10 - mode_freq
        pool = [v for v in range(19, 31) if v != mode_val]
        others = []
        counts = {}
        valid = True
        for _ in range(rem_count):
            avail = [v for v in pool if counts.get(v, 0) < mode_freq - 1]
            if not avail:
                valid = False
                break
            chosen = random.choice(avail)
            others.append(chosen)
            counts[chosen] = counts.get(chosen, 0) + 1
        if not valid:
            continue
        data = [mode_val] * mode_freq + others
        random.shuffle(data)
        sorted_data = sorted(data)
        if data != sorted_data:
            break
    
    # Tính các đặc trưng mẫu số liệu
    tong_ngay = sum(data)
    mean_dec = Decimal(str(tong_ngay)) / Decimal('10')
    mean_str = format_dec(mean_dec)
    
    # Trung vị của 10 số là trung bình cộng của số thứ 5 và số thứ 6 (index 4 và 5)
    x5 = sorted_data[4]
    x6 = sorted_data[5]
    median_dec = Decimal(str(x5 + x6)) / Decimal('2')
    median_str = format_dec(median_dec)
    
    # Chuỗi hiển thị mẫu số liệu
    str_data = format_list_num(data)
    str_sorted = format_list_num(sorted_data)
    
    # Tạo dữ liệu nhiễu cho câu a (số trung bình sai)
    wrong_mean_str = format_dec(mean_dec + Decimal('0.4'))
    
    # Tạo dữ liệu nhiễu cho câu c (trung vị sai)
    wrong_median_str = format_dec(median_dec + Decimal('1'))
    
    # Tạo dữ liệu nhiễu cho câu d (mốt sai)
    wrong_mode_val = mode_val + 1 if mode_val < 30 else mode_val - 1
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho mẫu số liệu số ngày làm việc trong tháng của $10$ công nhân: %s.''' % (str_data))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Số trung bình của mẫu số liệu là $%s$ ngày' % (mean_str)
    nb_da_1_s = 'Số trung bình của mẫu số liệu là $%s$ ngày' % (wrong_mean_str)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    tong_bieu_thuc = ' + '.join(str(v) for v in data)
    loigiai_nb_1 = ('''Số trung bình của mẫu số liệu là: $\\overline{x} = \\dfrac{%s}{10} = \\dfrac{%s}{10} = %s$ (ngày).''' % (tong_bieu_thuc, tong_ngay, mean_str))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ######################################################################## Thông hiểu ############################################
    
    # Các đáp án
    th_da_1_d = '\\True Vì cỡ mẫu là $10$ (số chẵn), trung vị là trung bình cộng của số thứ $5$ và số thứ $6$ trong dãy đã sắp xếp'
    th_da_1_s = 'Vì cỡ mẫu là $10$ (số chẵn), trung vị là trung bình cộng của số thứ $4$ và số thứ $5$ trong dãy đã sắp xếp'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Mẫu số liệu có cỡ mẫu $n = 10$ là số chẵn nên trung vị của mẫu số liệu là trung bình cộng của hai giá trị đứng ở vị trí thứ $\\dfrac{10}{2} = 5$ và thứ $\\dfrac{10}{2} + 1 = 6$ trong dãy đã sắp xếp theo thứ tự không giảm.''')
    
    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ######################################################################## Vận dụng ############################################
    
    # Các đáp án
    vd_da_1_d = '\\True Trung vị của mẫu số liệu là $%s$ ngày' % (median_str)
    vd_da_1_s = 'Trung vị của mẫu số liệu là $%s$ ngày' % (wrong_median_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Sắp xếp mẫu số liệu theo thứ tự không giảm ta được: %s. \\\\ Vì $n = 10$ là số chẵn nên trung vị của mẫu số liệu là trung bình cộng của số thứ $5$ và số thứ $6$: $M_e = \\dfrac{%s + %s}{2} = %s$ (ngày).''' % (str_sorted, x5, x6, median_str))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ######################################################################## Vận dụng cao ############################################
    
    # Các đáp án
    vdc_da_1_d = '\\True Mốt của mẫu số liệu là $%s$ ngày' % (mode_val)
    vdc_da_1_s = 'Mốt của mẫu số liệu là $%s$ ngày' % (wrong_mode_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Trong mẫu số liệu trên, giá trị $%s$ xuất hiện nhiều nhất (với tần số là $%s$). \\\\ Vậy mốt của mẫu số liệu là $M_o = %s$ ngày.''' % (mode_val, mode_freq, mode_val))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
    '\\choiceTFn \n'
    '{'+str(shuffled_answers_nb[0])+'}\n'
    '{'+str(shuffled_answers_th[0])+'}\n'
    '{'+str(shuffled_answers_vd[0])+'}\n'
    '{'+str(shuffled_answers_vdc[0])+'}\n'
    '\\loigiai{ \n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item '+str(shuffled_solutions_nb[0])+'\n'
    '\\item '+str(shuffled_solutions_th[0])+'\n'
    '\\item '+str(shuffled_solutions_vd[0])+'\n'
    '\\item '+str(shuffled_solutions_vdc[0])+'\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n \\end{minipage}\n\n')
    return content