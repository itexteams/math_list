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

def bt_dang19_p2_b2_c3_ds10(self):
    def format_dec(val):
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    # Điểm số cố định từ 5 đến 10
    scores = [5, 6, 7, 8, 9, 10]
    n_total = 30
    
    # Random các tần số f5, f6, a (tại 7), f8, b (tại 9), f10
    # Điều kiện:
    # - Tổng tần số = 30
    # - Tổng điểm chia hết cho 3 để điểm trung bình (chia 30) có 1 chữ số thập phân đẹp
    # - f8 là tần số lớn nhất duy nhất (mốt là 8)
    # - Trung vị của 30 học sinh (trung bình cộng phần tử thứ 15 và 16) bằng 8 (tức f5 + f6 + a < 15 và f5 + f6 + a + f8 >= 16)
    while True:
        f5 = random.randint(2, 4)
        f6 = random.randint(3, 6)
        a_val = random.randint(4, 7)
        f8 = random.randint(8, 11)
        b_val = random.randint(3, 7)
        f10 = n_total - (f5 + f6 + a_val + f8 + b_val)
        
        if 2 <= f10 <= 5:
            freqs = [f5, f6, a_val, f8, b_val, f10]
            # Kiểm tra f8 là lớn nhất duy nhất
            if f8 == max(freqs) and freqs.count(f8) == 1:
                # Kiểm tra phần tử thứ 15 và 16 đều rơi vào điểm 8
                if f5 + f6 + a_val <= 14 and f5 + f6 + a_val + f8 >= 16:
                    tong_diem = 5 * f5 + 6 * f6 + 7 * a_val + 8 * f8 + 9 * b_val + 10 * f10
                    if tong_diem % 3 == 0:
                        break
    
    sum_ab = a_val + b_val
    mean_dec = Decimal(str(tong_diem)) / Decimal(str(n_total))
    mean_str = format_dec(mean_dec)
    
    # Các hằng số trong hệ phương trình:
    # a + b = sum_ab
    # 7a + 9b = tong_diem - (5*f5 + 6*f6 + 8*f8 + 10*f10)
    const_known = 5 * f5 + 6 * f6 + 8 * f8 + 10 * f10
    rhs_eq2 = tong_diem - const_known
    
    # Giá trị nhiễu
    wrong_sum_ab = sum_ab + random.choice([-1, 1])
    wrong_a = b_val
    wrong_b = a_val
    wrong_med = '7,5'
    wrong_mode = 7 if a_val >= b_val else 9
    
    # Bảng tần số tabular
    bang_tan_so = (
        '\\begin{center}\n'
        '\\begin{tabular}{|l|c|c|c|c|c|c|}\n'
        '\\hline\n'
        '\\textbf{Điểm số ($x_i$)} & $5$ & $6$ & $7$ & $8$ & $9$ & $10$ \\\\\n'
        '\\hline\n'
        '\\textbf{Tần số ($n_i$)} & $%s$ & $%s$ & $a$ & $%s$ & $b$ & $%s$ \\\\\n'
        '\\hline\n'
        '\\end{tabular}\n'
        '\\end{center}'
    ) % (f5, f6, f8, f10)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho bảng tần số điểm kiểm tra $15$ phút của $30$ học sinh lớp $10\\text{B}$: %s Biết điểm trung bình của cả lớp là $%s$.''' % (bang_tan_so, mean_str))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Ta có phương trình $a + b = %s$' % (sum_ab)
    nb_da_1_s = 'Ta có phương trình $a + b = %s$' % (wrong_sum_ab)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    sum_known_freq = f5 + f6 + f8 + f10
    loigiai_nb_1 = ('''Vì cả lớp có $30$ học sinh nên tổng các tần số bằng $30$: $%s + %s + a + %s + b + %s = 30 \\Leftrightarrow a + b + %s = 30 \\Leftrightarrow a + b = %s$.''' % (f5, f6, f8, f10, sum_known_freq, sum_ab))
    
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
    th_da_1_d = '\\True Giá trị của $a = %s$ và $b = %s$' % (a_val, b_val)
    th_da_1_s = 'Giá trị của $a = %s$ và $b = %s$' % (wrong_a, wrong_b)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Vì điểm trung bình của cả lớp là $%s$ nên ta có: $\\dfrac{5 \\cdot %s + 6 \\cdot %s + 7a + 8 \\cdot %s + 9b + 10 \\cdot %s}{30} = %s \\Leftrightarrow %s + 7a + 9b = %s \\Leftrightarrow 7a + 9b = %s$. \\\\ Kết hợp với $a + b = %s$, ta giải hệ phương trình $\\begin{cases} a + b = %s \\\\ 7a + 9b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$.''' % (mean_str, f5, f6, f8, f10, mean_str, const_known, tong_diem, rhs_eq2, sum_ab, sum_ab, rhs_eq2, a_val, b_val))
    
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
    vd_da_1_d = '\\True Trung vị của mẫu số liệu là $8$'
    vd_da_1_s = 'Trung vị của mẫu số liệu là $%s$' % (wrong_med)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    cum_7 = f5 + f6 + a_val
    cum_8 = cum_7 + f8
    loigiai_vd_1 = ('''Cỡ mẫu $n = 30$ là số chẵn nên khi sắp xếp điểm số theo thứ tự không giảm, trung vị là trung bình cộng của giá trị thứ $15$ và giá trị thứ $16$. \\\\ Theo bảng tần số hoàn chỉnh, số học sinh đạt điểm từ $5$ đến $7$ là $%s + %s + %s = %s$ học sinh, và số học sinh đạt điểm từ $5$ đến $8$ là $%s + %s = %s$ học sinh. \\\\ Suy ra giá trị thứ $15$ và thứ $16$ đều bằng $8$. Vậy trung vị của mẫu số liệu là $M_e = \\dfrac{8 + 8}{2} = 8$.''' % (f5, f6, a_val, cum_7, cum_7, f8, cum_8))
    
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
    vdc_da_1_d = '\\True Mốt của mẫu số liệu là $8$'
    vdc_da_1_s = 'Mốt của mẫu số liệu là $%s$' % (wrong_mode)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Với $a = %s$ và $b = %s$, điểm số $8$ có tần số lớn nhất trong bảng là $%s$. \\\\ Vậy mốt của mẫu số liệu là $M_o = 8$.''' % (a_val, b_val, f8))
    
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