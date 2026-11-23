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

def bt_dang23_p2_b2_c3_ds10(self):
    def format_dec(val):
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    # Random các thông số sao cho bài toán có nghiệm duy nhất giống mẫu:
    # Mẫu: mean = 8 => sum = 48; median = 7.5 => x3 + x4 = 15; mode = 6 => x2 = x3 = 6 => x4 = 9;
    # Khi đó x1 + 6 + 6 + 9 + x5 + x6 = 48 => x1 + x5 + x6 = 27.
    # Với x6 = 14 => x1 + x5 = 13. Vì 1 <= x1 <= 5 và 10 <= x5 <= 13 => chỉ có nghiệm duy nhất x1 = 3, x5 = 10 (hoặc chọn x6 sao cho x1 + x5 = 2*mode_val + 1 => x1 = mode_val - 3, x5 = mode_val + 4, điều kiện 1 <= x1 <= mode_val - 1 và x4 + 1 <= x5 <= x6 - 1).
    while True:
        mode_val = random.randint(5, 8)
        x2 = mode_val
        x3 = mode_val
        x4 = mode_val + 3
        sum_34 = x3 + x4
        med_dec = Decimal(str(sum_34)) / Decimal('2')
        
        # Chọn x1 sao cho 1 <= x1 <= mode_val - 1 (lấy x1 = mode_val - 2 hoặc mode_val - 3)
        x1 = mode_val - random.choice([2, 3])
        if x1 < 1:
            continue
        # Chọn x5 = x4 + 1 = mode_val + 4 để x5 bị chặn dưới chặt bởi x4 < x5
        x5 = x4 + 1
        # Chọn x6 = x5 + 4 để chặn trên chặt: muốn giảm x5 thì phải tăng x1 (vượt quá mode_val - 1), muốn tăng x5 thì giảm x1 (nhỏ hơn 1 hoặc nếu x1 = 1 thì không giảm được!)
        # Để duy nhất nghiệm tuyệt đối: lấy x1 = 1, x5 = x4 + 1 (thì không thể giảm x1 vì x1 >= 1, cũng không thể giảm x5 vì x5 > x4; suy ra x1 + x5 đạt giá trị nhỏ nhất duy nhất!)
        x1 = 1
        x5 = x4 + 1
        x6 = x5 + random.randint(3, 6)
        
        total_sum = x1 + x2 + x3 + x4 + x5 + x6
        if total_sum % 6 == 0:
            mean_val = total_sum // 6
            break
    
    med_str = format_dec(med_dec)
    rem_sum_15 = total_sum - (x2 + x3 + x4 + x6)
    
    # Dữ liệu nhiễu
    wrong_total_sum = total_sum + random.choice([-6, 6])
    wrong_sum_34 = sum_34 + random.choice([-2, 2])
    wrong_x5 = x5 + 1
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một mẫu số liệu gồm $6$ số nguyên dương đã được sắp xếp theo thứ tự không giảm: $$x_1 \\le x_2 \\le x_3 \\le x_4 \\le x_5 \\le x_6$$ Biết rằng số trung bình của mẫu số liệu bằng $%s$, trung vị bằng $%s$, mốt duy nhất bằng $%s$ và giá trị lớn nhất $x_6 = %s$.''' % (mean_val, med_str, mode_val, x6))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Tổng của $6$ số trong mẫu số liệu bằng $%s$' % (total_sum)
    nb_da_1_s = 'Tổng của $6$ số trong mẫu số liệu bằng $%s$' % (wrong_total_sum)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Vì số trung bình của mẫu số liệu gồm $6$ số bằng $%s$ nên tổng của $6$ số trong mẫu số liệu là: $x_1 + x_2 + x_3 + x_4 + x_5 + x_6 = 6 \\cdot %s = %s$.''' % (mean_val, mean_val, total_sum))
    
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
    th_da_1_d = '\\True Ta luôn có $x_3 + x_4 = %s$' % (sum_34)
    th_da_1_s = 'Ta luôn có $x_3 + x_4 = %s$' % (wrong_sum_34)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Cỡ mẫu $n = 6$ là số chẵn nên trung vị của mẫu số liệu đã sắp xếp không giảm là trung bình cộng của $x_3$ và $x_4$: $M_e = \\dfrac{x_3 + x_4}{2}$. \\\\ Theo đề bài, $M_e = %s \\Leftrightarrow \\dfrac{x_3 + x_4}{2} = %s \\Leftrightarrow x_3 + x_4 = %s$.''' % (med_str, med_str, sum_34))
    
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
    vd_da_1_d = '\\True Vì mốt duy nhất bằng $%s$ nên ít nhất hai trong ba số $x_1, x_2, x_3$ phải bằng $%s$' % (mode_val, mode_val)
    vd_da_1_s = 'Vì mốt duy nhất bằng $%s$ nên cả ba số $x_1, x_2, x_3$ đều phải bằng $%s$' % (mode_val, mode_val)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Vì mốt duy nhất bằng $%s$ nên giá trị $%s$ phải xuất hiện ít nhất $2$ lần trong mẫu số liệu. \\\\ Mặt khác, nếu $x_4 = %s$ thì từ $x_3 + x_4 = %s$ suy ra $x_3 = %s > %s$ (vô lí vì $x_3 \\le x_4$). Do đó $x_4 > %s$, kéo theo $%s < x_4 \\le x_5 \\le x_6$. \\\\ Vậy các giá trị bằng $%s$ chỉ có thể nằm trong ba số đầu $x_1, x_2, x_3$, tức là ít nhất hai trong ba số $x_1, x_2, x_3$ phải bằng $%s$.''' % (mode_val, mode_val, mode_val, sum_34, x4, mode_val, mode_val, mode_val, mode_val, mode_val))
    
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
    vdc_da_1_d = '\\True Có duy nhất một bộ số $(x_1; x_2; x_3; x_4; x_5; x_6)$ thỏa mãn tất cả các điều kiện trên, và khi đó $x_5 = %s$' % (x5)
    vdc_da_1_s = 'Có duy nhất một bộ số $(x_1; x_2; x_3; x_4; x_5; x_6)$ thỏa mãn tất cả các điều kiện trên, và khi đó $x_5 = %s$' % (wrong_x5)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Vì $x_1 \\le x_2 \\le x_3$ và có ít nhất hai số bằng $%s$ nên $x_2 = x_3 = %s$. \\\\ Từ $x_3 + x_4 = %s$ suy ra $x_4 = %s - %s = %s$. \\\\ Thay $x_2 = x_3 = %s$, $x_4 = %s$ và $x_6 = %s$ vào tổng $6$ số ta được: $x_1 + %s + %s + %s + x_5 + %s = %s \\Leftrightarrow x_1 + x_5 = %s$. \\\\ Vì $x_1$ là số nguyên dương nên $x_1 \\ge 1$, và vì mốt duy nhất bằng $%s$ nên $x_4 < x_5$, tức là $x_5 \\ge %s$. \\\\ Suy ra $x_1 + x_5 \\ge 1 + %s = %s$. Dấu bằng xảy ra khi và chỉ khi $x_1 = 1$ và $x_5 = %s$. \\\\ Vậy có duy nhất một bộ số thỏa mãn là $(1; %s; %s; %s; %s; %s)$, và khi đó $x_5 = %s$.''' % (mode_val, mode_val, sum_34, sum_34, mode_val, x4, mode_val, x4, x6, mode_val, mode_val, x4, x6, total_sum, rem_sum_15, mode_val, x5, x5, rem_sum_15, x5, mode_val, mode_val, x4, x5, x6, x5))
    
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