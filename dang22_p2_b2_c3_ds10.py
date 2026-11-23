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

def bt_dang22_p2_b2_c3_ds10(self):
    def format_dec(val):
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    # Điểm số cố định từ 5 đến 9
    scores = [5, 6, 7, 8, 9]
    n_total = 25
    
    # Random các tần số f5, x (tại 6), f7, y (tại 8), f9
    # Điều kiện giống bài mẫu:
    # - Tổng tần số = 25
    # - Trung vị (giá trị thứ 13 trong dãy sắp xếp không giảm) bằng 7: f5 + x < 13 và f5 + x + f7 >= 13
    # - Mẫu số liệu có hai mốt là 7 và 8: y_val == f7 và f7 > max(f5, x_val, f9)
    # - Số học sinh có điểm <= 7 là (f5 + x_val + f7) chẵn để khi cộng 0,5 điểm cho mỗi em thì điểm trung bình mới đẹp
    while True:
        f5 = random.randint(2, 4)
        x_val = random.randint(3, 6)
        f7 = random.randint(7, 9)
        y_val = f7
        f9 = n_total - (f5 + x_val + f7 + y_val)
        
        if 2 <= f9 <= 5:
            if f7 > max(f5, x_val, f9):
                if f5 + x_val <= 12 and f5 + x_val + f7 >= 13:
                    count_le_7 = f5 + x_val + f7
                    if count_le_7 % 2 == 0:
                        tong_diem = 5 * f5 + 6 * x_val + 7 * f7 + 8 * y_val + 9 * f9
                        break
    
    sum_xy = x_val + y_val
    rhs_eq2 = tong_diem - (5 * f5 + 7 * f7 + 9 * f9)
    mean_dec = Decimal(str(tong_diem)) / Decimal(str(n_total))
    mean_str = format_dec(mean_dec)
    
    # Điểm trung bình mới sau khi cộng 0,5 cho các học sinh có điểm <= trung vị (7)
    bonus_total_dec = Decimal(str(count_le_7)) * Decimal('0.5')
    new_tong_dec = Decimal(str(tong_diem)) + bonus_total_dec
    new_mean_dec = new_tong_dec / Decimal(str(n_total))
    new_mean_str = format_dec(new_mean_dec)
    bonus_total_str = format_dec(bonus_total_dec)
    new_tong_str = format_dec(new_tong_dec)
    
    # Dữ liệu nhiễu
    wrong_rhs_eq2 = rhs_eq2 + random.choice([-4, 4])
    wrong_med = 8
    wrong_new_mean_str = format_dec(mean_dec + Decimal('0.5'))
    
    # Bảng tần số tabular
    bang_tan_so = (
        '\\begin{center}\n'
        '\\begin{tabular}{|l|c|c|c|c|c|}\n'
        '\\hline\n'
        '\\textbf{Điểm số ($x_i$)} & $5$ & $6$ & $7$ & $8$ & $9$ \\\\\n'
        '\\hline\n'
        '\\textbf{Số học sinh ($n_i$)} & $%s$ & $x$ & $%s$ & $y$ & $%s$ \\\\\n'
        '\\hline\n'
        '\\end{tabular}\n'
        '\\end{center}'
    ) % (f5, f7, f9)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Bảng tần số điểm kiểm tra môn Tiếng Anh (thang điểm $10$) của một nhóm học sinh được ghi lại như sau: %s Biết rằng nhóm có tất cả $25$ học sinh và điểm trung bình của cả nhóm là $%s$.''' % (bang_tan_so, mean_str))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Ta có hệ phương trình $\\begin{cases} x + y = %s \\\\ 6x + 8y = %s \\end{cases}$' % (sum_xy, rhs_eq2)
    nb_da_1_s = 'Ta có hệ phương trình $\\begin{cases} x + y = %s \\\\ 6x + 8y = %s \\end{cases}$' % (sum_xy, wrong_rhs_eq2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    sum_known_n = f5 + f7 + f9
    sum_known_s = 5 * f5 + 7 * f7 + 9 * f9
    loigiai_nb_1 = ('''Tổng số học sinh của nhóm là $25$ nên ta có: $%s + x + %s + y + %s = 25 \\Leftrightarrow x + y + %s = 25 \\Leftrightarrow x + y = %s$. \\\\ Điểm trung bình của cả nhóm là $%s$ nên ta có: $\\dfrac{5 \\cdot %s + 6x + 7 \\cdot %s + 8y + 9 \\cdot %s}{25} = %s \\Leftrightarrow %s + 6x + 8y = %s \\Leftrightarrow 6x + 8y = %s$. \\\\ Vậy ta có hệ phương trình $\\begin{cases} x + y = %s \\\\ 6x + 8y = %s \\end{cases}$.''' % (f5, f7, f9, sum_known_n, sum_xy, mean_str, f5, f7, f9, mean_str, sum_known_s, tong_diem, rhs_eq2, sum_xy, rhs_eq2))
    
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
    th_da_1_d = '\\True Trung vị của mẫu số liệu trên là $7$'
    th_da_1_s = 'Trung vị của mẫu số liệu trên là $%s$' % (wrong_med)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    cum_6 = f5 + x_val
    loigiai_th_1 = ('''Giải hệ phương trình $\\begin{cases} x + y = %s \\\\ 6x + 8y = %s \\end{cases}$ ta được $x = %s$ và $y = %s$. \\\\ Vì cỡ mẫu $n = 25$ là số lẻ nên khi sắp xếp điểm số theo thứ tự không giảm, trung vị của mẫu số liệu là giá trị đứng ở vị trí thứ $\\dfrac{25 + 1}{2} = 13$. \\\\ Số học sinh đạt điểm từ $5$ đến $6$ là $%s + %s = %s$ học sinh, số học sinh đạt điểm từ $5$ đến $7$ là $%s + %s = %s$ học sinh. \\\\ Do đó giá trị đứng ở vị trí thứ $13$ là $7$, tức là trung vị của mẫu số liệu trên là $M_e = 7$.''' % (sum_xy, rhs_eq2, x_val, y_val, f5, x_val, cum_6, cum_6, f7, count_le_7))
    
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
    vd_da_1_d = '\\True Mẫu số liệu có hai mốt là $7$ và $8$'
    vd_da_1_s = 'Mẫu số liệu có duy nhất một mốt là $7$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Với $x = %s$ và $y = %s$, bảng tần số có hai giá trị cùng đạt tần số lớn nhất là $%s$, tương ứng với hai điểm số $7$ và $8$. \\\\ Vậy mẫu số liệu có hai mốt là $7$ và $8$.''' % (x_val, y_val, f7))
    
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
    vdc_da_1_d = '\\True Giáo viên quyết định cộng thêm $0,5$ điểm khuyến khích cho những học sinh có điểm số nhỏ hơn hoặc bằng trung vị. Khi đó, điểm trung bình mới của cả nhóm là $%s$' % (new_mean_str)
    vdc_da_1_s = 'Giáo viên quyết định cộng thêm $0,5$ điểm khuyến khích cho những học sinh có điểm số nhỏ hơn hoặc bằng trung vị. Khi đó, điểm trung bình mới của cả nhóm là $%s$' % (wrong_new_mean_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Số học sinh có điểm số nhỏ hơn hoặc bằng trung vị ($M_e = 7$) là: $%s + %s + %s = %s$ (học sinh). \\\\ Tổng số điểm được cộng thêm cho cả nhóm là: $%s \\cdot 0,5 = %s$ (điểm). \\\\ Tổng điểm mới của cả nhóm là: $%s + %s = %s$ (điểm). \\\\ Điểm trung bình mới của cả nhóm là: $\\overline{x}_{\\text{mới}} = \\dfrac{%s}{25} = %s$.''' % (f5, x_val, f7, count_le_7, count_le_7, bonus_total_str, tong_diem, bonus_total_str, new_tong_str, new_tong_str, new_mean_str))
    
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