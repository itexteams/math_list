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

def bt_dang15_p2_b2_c3_ds10(self):
    def format_dec_1(val):
        # Định dạng số thập phân với 1 chữ số sau dấu phẩy (ví dụ 11.0 -> 11,0)
        d = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        return str(d).replace('.', ',')
    
    def format_dec_clean(val):
        # Định dạng số thập phân bỏ số 0 vô nghĩa ở cuối (ví dụ 11.15 -> 11,15; 11.20 -> 11,2)
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    def format_list_dec(lst):
        return '; '.join('$' + format_dec_1(v) + '$' for v in lst)
    
    # Random mẫu số liệu thành tích chạy 100m (tính bằng giây) của 10 vận động viên nam
    # Làm việc với số nguyên phần mười (ví dụ 112 tương ứng 11,2)
    while True:
        mode_int = random.randint(108, 114)
        pool = [v for v in range(106, 120) if v != mode_int]
        others = random.sample(pool, 8)
        data_int = [mode_int, mode_int] + others
        # Đảm bảo tổng chia hết cho 10 để số trung bình đẹp (1 chữ số thập phân)
        if sum(data_int) % 10 == 0:
            sorted_int = sorted(data_int)
            if data_int != sorted_int:
                break
    
    data_dec = [Decimal(str(v)) / Decimal('10') for v in data_int]
    sorted_dec = [Decimal(str(v)) / Decimal('10') for v in sorted_int]
    
    # Tính các đặc trưng mẫu số liệu
    tong_int = sum(data_int)
    tong_dec = Decimal(str(tong_int)) / Decimal('10')
    mean_dec = tong_dec / Decimal('10')
    mean_str = format_dec_1(mean_dec)
    
    # Trung vị của 10 số là trung bình cộng của số thứ 5 và số thứ 6 (index 4 và 5)
    x5_dec = sorted_dec[4]
    x6_dec = sorted_dec[5]
    median_dec = (x5_dec + x6_dec) / Decimal('2')
    median_str = format_dec_clean(median_dec)
    
    # Mốt của mẫu số liệu
    mode_dec = Decimal(str(mode_int)) / Decimal('10')
    mode_str = format_dec_1(mode_dec)
    
    # Chuỗi hiển thị mẫu số liệu
    str_data = format_list_dec(data_dec)
    str_sorted = format_list_dec(sorted_dec)
    
    # Tạo dữ liệu nhiễu
    wrong_mean_str = format_dec_1(mean_dec + Decimal('0.2'))
    wrong_median_str = format_dec_clean(median_dec + Decimal('0.15'))
    wrong_mode_int = sorted_int[random.choice([0, 9])]
    wrong_mode_str = format_dec_1(Decimal(str(wrong_mode_int)) / Decimal('10'))
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Thành tích chạy $100\\text{ m}$ (tính bằng giây) của $10$ vận động viên nam: %s.''' % (str_data))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Thành tích trung bình của $10$ vận động viên là $%s$ giây' % (mean_str)
    nb_da_1_s = 'Thành tích trung bình của $10$ vận động viên là $%s$ giây' % (wrong_mean_str)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    tong_bieu_thuc = ' + '.join(format_dec_1(v) for v in data_dec)
    tong_str = format_dec_clean(tong_dec)
    loigiai_nb_1 = ('''Thành tích trung bình của $10$ vận động viên là: $\\overline{x} = \\dfrac{%s}{10} = \\dfrac{%s}{10} = %s$ (giây).''' % (tong_bieu_thuc, tong_str, mean_str))
    
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
    th_da_1_d = '\\True Số trung bình cộng càng nhỏ chứng tỏ nhóm vận động viên chạy càng nhanh'
    th_da_1_s = 'Số trung bình cộng càng lớn chứng tỏ nhóm vận động viên chạy càng nhanh'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Vì mẫu số liệu biểu thị thời gian hoàn thành quãng đường chạy $100\\text{ m}$ nên thời gian chạy trung bình càng ít (số trung bình cộng càng nhỏ) chứng tỏ nhóm vận động viên chạy càng nhanh.''')
    
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
    vd_da_1_d = '\\True Trung vị của mẫu số liệu trên là $%s$ giây' % (median_str)
    vd_da_1_s = 'Trung vị của mẫu số liệu trên là $%s$ giây' % (wrong_median_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    x5_str = format_dec_1(x5_dec)
    x6_str = format_dec_1(x6_dec)
    loigiai_vd_1 = ('''Sắp xếp mẫu số liệu theo thứ tự không giảm ta được: %s. \\\\ Vì cỡ mẫu $n = 10$ là số chẵn nên trung vị của mẫu số liệu là trung bình cộng của số thứ $5$ và số thứ $6$: $M_e = \\dfrac{%s + %s}{2} = %s$ (giây).''' % (str_sorted, x5_str, x6_str, median_str))
    
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
    vdc_da_1_d = '\\True Mốt của mẫu số liệu là $%s$ giây' % (mode_str)
    vdc_da_1_s = 'Mốt của mẫu số liệu là $%s$ giây' % (wrong_mode_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Trong mẫu số liệu trên, giá trị $%s$ xuất hiện nhiều nhất (với tần số bằng $2$, các giá trị còn lại đều xuất hiện $1$ lần). \\\\ Vậy mốt của mẫu số liệu là $M_o = %s$ giây.''' % (mode_str, mode_str))
    
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