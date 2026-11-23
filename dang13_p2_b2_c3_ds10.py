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

def bt_dang13_p2_b2_c3_ds10(self):
    def format_list_num(lst):
        return '; '.join('$' + str(v) + '$' for v in lst)
    
    # Random mẫu số liệu số cuốn sách đọc được trong năm của 11 bạn
    # Điều kiện: tổng chia hết cho 11, chỉ có 1 giá trị xuất hiện 2 lần (mốt duy nhất), 9 giá trị còn lại xuất hiện 1 lần
    while True:
        mode_val = random.randint(3, 7)
        pool = [v for v in range(1, 16) if v != mode_val]
        others = random.sample(pool, 9)
        data = [mode_val, mode_val] + others
        if sum(data) % 11 == 0:
            sorted_data = sorted(data)
            # Chọn giá trị thêm vào cho câu d là một giá trị khác mode_val đã có trong mẫu (để tần số tăng từ 1 lên 2)
            second_mode = sorted_data[5]
            if second_mode != mode_val and data != sorted_data:
                break
    
    # Tính các đặc trưng mẫu số liệu
    tong_sach = sum(data)
    mean_val = tong_sach // 11
    median_val = sorted_data[5]
    
    # Hai mốt khi thêm second_mode
    modes_sorted = sorted([mode_val, second_mode])
    m1_str, m2_str = str(modes_sorted[0]), str(modes_sorted[1])
    
    # Chuỗi hiển thị mẫu số liệu
    str_data = format_list_num(data)
    str_sorted = format_list_num(sorted_data)
    
    # Tạo dữ liệu nhiễu cho câu a (số trung bình sai)
    wrong_mean_val = mean_val + random.choice([-1, 1])
    
    # Tạo dữ liệu nhiễu cho câu b (trung vị sai)
    wrong_median_val = sorted_data[random.choice([4, 6])]
    
    # Tạo dữ liệu nhiễu cho câu c (mốt sai)
    wrong_mode_val = second_mode
    
    # Tạo dữ liệu nhiễu cho câu d (thêm giá trị mới chưa từng xuất hiện nên tần số chỉ là 1, mẫu vẫn chỉ có 1 mốt)
    unused_vals = [v for v in range(1, 16) if v not in data]
    new_val_single = random.choice(unused_vals)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho mẫu số liệu số cuốn sách đọc được trong năm của $11$ bạn: %s.''' % (str_data))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Số trung bình của mẫu số liệu là $%s$ cuốn' % (mean_val)
    nb_da_1_s = 'Số trung bình của mẫu số liệu là $%s$ cuốn' % (wrong_mean_val)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    tong_bieu_thuc = ' + '.join(str(v) for v in data)
    loigiai_nb_1 = ('''Số trung bình của mẫu số liệu là: $\\overline{x} = \\dfrac{%s}{11} = \\dfrac{%s}{11} = %s$ (cuốn).''' % (tong_bieu_thuc, tong_sach, mean_val))
    
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
    th_da_1_d = '\\True Trung vị của mẫu số liệu là $%s$ cuốn' % (median_val)
    th_da_1_s = 'Trung vị của mẫu số liệu là $%s$ cuốn' % (wrong_median_val)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Sắp xếp mẫu số liệu theo thứ tự không giảm ta được: %s. \\\\ Vì cỡ mẫu $n = 11$ là số lẻ nên trung vị của mẫu số liệu là giá trị đứng ở vị trí thứ $\\dfrac{11 + 1}{2} = 6$ trong dãy đã sắp xếp. \\\\ Vậy trung vị của mẫu số liệu là $M_e = %s$ cuốn.''' % (str_sorted, median_val))
    
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
    vd_da_1_d = '\\True Mẫu số liệu có duy nhất một mốt là $%s$' % (mode_val)
    vd_da_1_s = 'Mẫu số liệu có duy nhất một mốt là $%s$' % (wrong_mode_val)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Trong mẫu số liệu ban đầu, chỉ có giá trị $%s$ xuất hiện $2$ lần, các giá trị còn lại đều chỉ xuất hiện $1$ lần. \\\\ Vậy mẫu số liệu có duy nhất một mốt là $M_o = %s$.''' % (mode_val, mode_val))
    
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
    vdc_da_1_d = '\\True Nếu thêm một bạn đọc được $%s$ cuốn sách nữa, mẫu số liệu mới có hai mốt là $%s$ và $%s$' % (second_mode, m1_str, m2_str)
    vdc_da_1_s = 'Nếu thêm một bạn đọc được $%s$ cuốn sách nữa, mẫu số liệu mới có hai mốt là $%s$ và $%s$' % (new_val_single, mode_val, new_val_single)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    if vdc_da_1 == vdc_da_1_d:
        loigiai_vdc_1 = ('''Khi thêm một bạn đọc được $%s$ cuốn sách nữa thì trong mẫu số liệu mới có hai giá trị cùng xuất hiện nhiều nhất với tần số bằng $2$ là $%s$ và $%s$. \\\\ Do đó mẫu số liệu mới có hai mốt là $%s$ và $%s$.''' % (second_mode, m1_str, m2_str, m1_str, m2_str))
    else:
        loigiai_vdc_1 = ('''Khi thêm một bạn đọc được $%s$ cuốn sách nữa thì giá trị $%s$ mới chỉ xuất hiện $1$ lần, trong khi giá trị $%s$ xuất hiện $2$ lần. \\\\ Do đó mẫu số liệu mới vẫn chỉ có duy nhất một mốt là $%s$.''' % (new_val_single, new_val_single, mode_val, mode_val))
    
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
    
    # Cập nhật lại lời giải vdc tương ứng với lựa chọn cuối cùng
    if vdc_da_1 == vdc_da_1_d:
        loigiai_vdc_1 = ('''Khi thêm một bạn đọc được $%s$ cuốn sách nữa thì trong mẫu số liệu mới có hai giá trị cùng xuất hiện nhiều nhất với tần số bằng $2$ là $%s$ và $%s$. \\\\ Do đó mẫu số liệu mới có hai mốt là $%s$ và $%s$.''' % (second_mode, m1_str, m2_str, m1_str, m2_str))
    else:
        loigiai_vdc_1 = ('''Khi thêm một bạn đọc được $%s$ cuốn sách nữa thì giá trị $%s$ mới chỉ xuất hiện $1$ lần, trong khi giá trị $%s$ xuất hiện $2$ lần. \\\\ Do đó mẫu số liệu mới vẫn chỉ có duy nhất một mốt là $%s$.''' % (new_val_single, new_val_single, mode_val, mode_val))
    list_vdc_2 = [loigiai_vdc_1]
    
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