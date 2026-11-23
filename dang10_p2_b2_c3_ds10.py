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

def bt_dang10_p2_b2_c3_ds10(self):
    def format_dec(val):
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    def format_list_num(lst):
        return '; '.join('$' + str(v) + '$' for v in lst)
    
    # Random mẫu số liệu tiền lương (triệu đồng/tháng) của 8 nhân viên có 1 giá trị đột biến
    while True:
        normal_vals = [random.randint(6, 13) for _ in range(7)]
        outlier_val = random.randint(22, 32)
        data = normal_vals + [outlier_val]
        random.shuffle(data)
        sorted_data = sorted(data)
        if data != sorted_data:
            break
    
    # Tính các đặc trưng mẫu số liệu
    tong_luong = sum(data)
    mean_dec = Decimal(str(tong_luong)) / Decimal('8')
    mean_str = format_dec(mean_dec)
    
    # Trung vị của 8 số là trung bình cộng của số thứ 4 và số thứ 5 (index 3 và 4)
    x4 = sorted_data[3]
    x5 = sorted_data[4]
    median_dec = Decimal(str(x4 + x5)) / Decimal('2')
    median_str = format_dec(median_dec)
    
    # Chuỗi hiển thị mẫu số liệu
    str_data = format_list_num(data)
    str_sorted = format_list_num(sorted_data)
    
    # Tạo dữ liệu nhiễu cho câu a (đổi chỗ 2 phần tử khác nhau trong dãy đã sắp xếp)
    wrong_sorted = sorted_data.copy()
    for i in range(7):
        if wrong_sorted[i] != wrong_sorted[i+1]:
            wrong_sorted[i], wrong_sorted[i+1] = wrong_sorted[i+1], wrong_sorted[i]
            break
    str_wrong_sorted = format_list_num(wrong_sorted)
    
    # Tạo dữ liệu nhiễu cho câu b (số trung bình sai)
    wrong_mean_str = format_dec(mean_dec + Decimal('0.5'))
    
    # Tạo dữ liệu nhiễu cho câu c (trung vị sai)
    wrong_median_str = format_dec(median_dec + Decimal('1'))
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho mẫu số liệu tiền lương (triệu đồng/tháng) của $8$ nhân viên trong một công ty nhỏ: %s.''' % (str_data))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Sắp xếp mẫu số liệu không giảm được: %s' % (str_sorted)
    nb_da_1_s = 'Sắp xếp mẫu số liệu không giảm được: %s' % (str_wrong_sorted)
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
    th_da_1_d = '\\True Số trung bình của mẫu số liệu là $%s$ (triệu đồng)' % (mean_str)
    th_da_1_s = 'Số trung bình của mẫu số liệu là $%s$ (triệu đồng)' % (wrong_mean_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    tong_bieu_thuc = ' + '.join(str(v) for v in data)
    loigiai_th_1 = ('''Số trung bình của mẫu số liệu là: $\\overline{x} = \\dfrac{%s}{8} = \\dfrac{%s}{8} = %s$ (triệu đồng).''' % (tong_bieu_thuc, tong_luong, mean_str))
    
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
    vd_da_1_d = '\\True Trung vị của mẫu số liệu là $%s$ (triệu đồng)' % (median_str)
    vd_da_1_s = 'Trung vị của mẫu số liệu là $%s$ (triệu đồng)' % (wrong_median_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Mẫu số liệu có cỡ mẫu $n = 8$ là số chẵn nên trung vị là trung bình cộng của hai giá trị đứng ở vị trí thứ $4$ và thứ $5$ trong dãy đã sắp xếp không giảm. \\\\ Vậy trung vị của mẫu số liệu là $M_e = \\dfrac{%s + %s}{2} = %s$ (triệu đồng).''' % (x4, x5, median_str))
    
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
    vdc_da_1_d = '\\True Trong trường hợp này, trung vị phản ánh mức lương phổ biến tốt hơn số trung bình vì có giá trị đột biến $%s$' % (outlier_val)
    vdc_da_1_s = 'Trong trường hợp này, số trung bình phản ánh mức lương phổ biến tốt hơn trung vị vì có giá trị đột biến $%s$' % (outlier_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Do trong mẫu số liệu xuất hiện giá trị bất thường (đột biến) là $%s$ làm cho số trung bình bị kéo lệch lên cao ($%s$ triệu đồng), không đại diện chính xác cho mức lương của đa số nhân viên. \\\\ Vì vậy, trung vị ($%s$ triệu đồng) phản ánh mức lương phổ biến tốt hơn số trung bình.''' % (outlier_val, mean_str, median_str))
    
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