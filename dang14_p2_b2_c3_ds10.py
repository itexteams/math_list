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

def bt_dang14_p2_b2_c3_ds10(self):
    def format_dec(val):
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    # Random cỡ giày và tần số (số đôi bán được)
    start_size = random.choice([36, 37, 38])
    sizes = [start_size + i for i in range(5)]
    
    while True:
        freqs = [random.randint(3, 15) for _ in range(5)]
        n = sum(freqs)
        max_freq = max(freqs)
        # Đảm bảo cỡ mẫu n chia hết cho 20 hoặc 40 để số trung bình đẹp, và chỉ có 1 mốt duy nhất
        if n in [40, 50] and freqs.count(max_freq) == 1:
            mode_idx = freqs.index(max_freq)
            mode_val = sizes[mode_idx]
            if mode_val != max_freq:
                # Mở rộng danh sách số liệu để tìm trung vị chính xác
                expanded = []
                for s, f in zip(sizes, freqs):
                    expanded.extend([s] * f)
                idx1 = n // 2 - 1
                idx2 = n // 2
                x_mid1 = expanded[idx1]
                x_mid2 = expanded[idx2]
                # Đảm bảo trung vị khác số trung bình và khác mốt để câu hỏi phong phú
                tong_tich = sum(s * f for s, f in zip(sizes, freqs))
                mean_dec = Decimal(str(tong_tich)) / Decimal(str(n))
                median_dec = Decimal(str(x_mid1 + x_mid2)) / Decimal('2')
                if mean_dec != median_dec:
                    break
    
    mean_str = format_dec(mean_dec)
    median_str = format_dec(median_dec)
    
    # Tạo dữ liệu nhiễu
    wrong_n = n + random.choice([-4, 4])
    wrong_mean_str = format_dec(mean_dec + Decimal('0.25'))
    wrong_median_str = format_dec(median_dec + Decimal('0.5'))
    
    # Bảng tần số tabular
    bang_tan_so = (
        '\\begin{center}\n'
        '\\begin{tabular}{|l|c|c|c|c|c|}\n'
        '\\hline\n'
        '\\textbf{Cỡ giày} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\\n'
        '\\hline\n'
        '\\textbf{Số đôi bán được} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\\n'
        '\\hline\n'
        '\\end{tabular}\n'
        '\\end{center}'
    ) % (sizes[0], sizes[1], sizes[2], sizes[3], sizes[4], freqs[0], freqs[1], freqs[2], freqs[3], freqs[4])
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một cửa hàng thống kê cỡ giày bán được trong ngày qua bảng tần số sau: %s''' % (bang_tan_so))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Cỡ mẫu của bảng số liệu trên là $n = %s$' % (n)
    nb_da_1_s = 'Cỡ mẫu của bảng số liệu trên là $n = %s$' % (wrong_n)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    tong_freq_str = ' + '.join(str(f) for f in freqs)
    loigiai_nb_1 = ('''Cỡ mẫu của bảng số liệu trên là: $n = %s = %s$.''' % (tong_freq_str, n))
    
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
    th_da_1_d = '\\True Cỡ giày trung bình bán được trong ngày là $%s$' % (mean_str)
    th_da_1_s = 'Cỡ giày trung bình bán được trong ngày là $%s$' % (wrong_mean_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    tong_tich_str = ' + '.join('%s \\cdot %s' % (s, f) for s, f in zip(sizes, freqs))
    loigiai_th_1 = ('''Cỡ giày trung bình bán được trong ngày là: $\\overline{x} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s} = %s$.''' % (tong_tich_str, n, tong_tich, n, mean_str))
    
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
    vd_da_1_d = '\\True Trung vị của mẫu số liệu là $%s$' % (median_str)
    vd_da_1_s = 'Trung vị của mẫu số liệu là $%s$' % (wrong_median_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    pos1 = n // 2
    pos2 = n // 2 + 1
    loigiai_vd_1 = ('''Vì cỡ mẫu $n = %s$ là số chẵn nên khi sắp xếp mẫu số liệu theo thứ tự không giảm, trung vị là trung bình cộng của giá trị thứ $%s$ và giá trị thứ $%s$. \\\\ Quan sát bảng tần số, giá trị thứ $%s$ là $%s$ và giá trị thứ $%s$ là $%s$. \\\\ Vậy trung vị của mẫu số liệu là $M_e = \\dfrac{%s + %s}{2} = %s$.''' % (n, pos1, pos2, pos1, x_mid1, pos2, x_mid2, x_mid1, x_mid2, median_str))
    
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
    vdc_da_1_d = '\\True Mốt của mẫu số liệu là $%s$' % (mode_val)
    vdc_da_1_s = 'Mốt của mẫu số liệu là $%s$' % (max_freq)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Trong bảng tần số trên, cỡ giày $%s$ có tần số lớn nhất là $%s$. \\\\ Vậy mốt của mẫu số liệu là $M_o = %s$ (không phải là tần số $%s$).''' % (mode_val, max_freq, mode_val, max_freq))
    
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