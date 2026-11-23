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
from collections import Counter

def bt_dang9_p2_b2_c3_ds10(self):
    def lam_tron(val):
        d = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        return str(d).replace('.', ',')
    
    def format_list_num(lst):
        return '; '.join('$' + str(v) + '$' for v in lst)
    
    # Random mẫu số liệu điểm kiểm tra Toán của 9 học sinh có 1 mốt duy nhất
    while True:
        mode_val = random.randint(6, 9)
        mode_freq = random.choice([3, 4])
        rem_count = 9 - mode_freq
        pool = [v for v in range(4, 11) if v != mode_val]
        # Chọn các giá trị còn lại sao cho tần số của chúng nhỏ hơn mode_freq
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
        # Đảm bảo dãy ban đầu khác dãy đã sắp xếp
        if data != sorted_data:
            break
    
    # Tính các đặc trưng mẫu số liệu
    tong_diem = sum(data)
    mean_exact = Rational(tong_diem, 9)
    mean_val = lam_tron(float(tong_diem) / 9.0)
    median_val = sorted_data[4]
    
    # Chuỗi hiển thị mẫu số liệu
    str_data = format_list_num(data)
    str_sorted = format_list_num(sorted_data)
    
    # Tạo dữ liệu nhiễu cho câu a (đổi chỗ 2 phần tử khác nhau trong dãy đã sắp xếp)
    wrong_sorted = sorted_data.copy()
    for i in range(8):
        if wrong_sorted[i] != wrong_sorted[i+1]:
            wrong_sorted[i], wrong_sorted[i+1] = wrong_sorted[i+1], wrong_sorted[i]
            break
    str_wrong_sorted = format_list_num(wrong_sorted)
    
    # Tạo dữ liệu nhiễu cho câu b (số trung bình sai)
    d_mean = Decimal(str(float(tong_diem) / 9.0)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    wrong_mean_val = str(d_mean + Decimal('0.2')).replace('.', ',')
    
    # Tạo dữ liệu nhiễu cho câu c (trung vị sai)
    wrong_median = median_val + 1 if median_val < 10 else median_val - 1
    
    # Tạo dữ liệu nhiễu cho câu d (mốt hoặc tần số sai)
    wrong_mode_freq = mode_freq + 1
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho mẫu số liệu điểm kiểm tra Toán của $9$ học sinh: %s.''' % (str_data))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Mẫu số liệu sau khi sắp xếp theo thứ tự không giảm là: %s' % (str_sorted)
    nb_da_1_s = 'Mẫu số liệu sau khi sắp xếp theo thứ tự không giảm là: %s' % (str_wrong_sorted)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Sắp xếp mẫu số liệu theo thứ tự không giảm ta được: %s.''' % (str_sorted))
    
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
    th_da_1_d = '\\True Số trung bình của mẫu số liệu là $%s$ (làm tròn đến hàng phần chục)' % (mean_val)
    th_da_1_s = 'Số trung bình của mẫu số liệu là $%s$ (làm tròn đến hàng phần chục)' % (wrong_mean_val)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    tong_bieu_thuc = ' + '.join(str(v) for v in data)
    loigiai_th_1 = ('''Số trung bình của mẫu số liệu là: $\\overline{x} = \\dfrac{%s}{9} = \\dfrac{%s}{9} \\approx %s$.''' % (tong_bieu_thuc, tong_diem, mean_val))
    
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
    vd_da_1_d = '\\True Trung vị của mẫu số liệu là $%s$' % (median_val)
    vd_da_1_s = 'Trung vị của mẫu số liệu là $%s$' % (wrong_median)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Mẫu số liệu có cỡ mẫu $n = 9$ là số lẻ nên trung vị là số liệu đứng ở vị trí thứ $\\dfrac{9 + 1}{2} = 5$ trong dãy đã sắp xếp không giảm. \\\\ Vậy trung vị của mẫu số liệu là $M_e = %s$.''' % (median_val))
    
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
    vdc_da_1_d = '\\True Mốt của mẫu số liệu là $%s$ với tần số $%s$' % (mode_val, mode_freq)
    vdc_da_1_s = 'Mốt của mẫu số liệu là $%s$ với tần số $%s$' % (mode_val, wrong_mode_freq)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Trong mẫu số liệu trên, giá trị $%s$ xuất hiện nhiều nhất với tần số là $%s$. \\\\ Vậy mốt của mẫu số liệu là $M_o = %s$ với tần số $%s$.''' % (mode_val, mode_freq, mode_val, mode_freq))
    
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