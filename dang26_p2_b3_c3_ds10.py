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


def bt_dang26_p2_b3_c3_ds10(self):
    def fmt_num(val):
        if isinstance(val, Rational):
            if val.q == 1:
                return str(val.p)
            else:
                f = float(val)
                s = str(round(f, 4)).rstrip('0').rstrip('.')
                return s.replace('.', ',')
        elif isinstance(val, float):
            s = str(round(val, 4)).rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return str(val)
    
    # Random số phần tử n (ví dụ 5 hoặc 6), số trung bình x_mean và phương sai s^2
    n_val = random.choice([5, 6, 8])
    x_mean = random.randint(8, 15)
    s_sq = random.choice([9, 12, 16, 20, 25])
    
    # Các đại lượng tính toán
    sum_x = n_val * x_mean
    # s^2 = (1/n) * sum(x_i^2) - (x_mean)^2 => sum(x_i^2) = n * (s^2 + x_mean^2)
    sum_x_sq = n_val * (s_sq + x_mean**2)
    
    # Khi bổ sung thêm giá trị x_{n+1} = x_mean
    n_new = n_val + 1
    var_new = Rational(n_val * s_sq, n_new)
    
    # Giá trị sai cho các phương án
    sum_x_wrong = sum_x + random.choice([-10, -5, 5, 10])
    sum_x_sq_wrong = sum_x_sq + random.choice([-20, 20, 40])
    x_mean_wrong = x_mean + random.choice([-2, -1, 1, 2])
    
    # Chuỗi liệt kê x_1, x_2, ..., x_n
    x_list_str = ', '.join('x_%s' % str(i) for i in range(1, n_val + 1))
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một mẫu số liệu gồm $%s$ giá trị $%s$ có số trung bình $\\overline{x} = %s$ và phương sai $s^2 = %s$.''' % (
        str(n_val), x_list_str, str(x_mean), str(s_sq)
    ))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Tổng các giá trị của mẫu số liệu ban đầu bằng $%s$' % (str(sum_x))
    nb_da_1_s = 'Tổng các giá trị của mẫu số liệu ban đầu bằng $%s$' % (str(sum_x_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có số trung bình cộng của mẫu số liệu ban đầu là $\\overline{x} = \\dfrac{x_1 + x_2 + \\ldots + x_%s}{%s} = %s$. \\\\
    Suy ra tổng các giá trị của mẫu số liệu ban đầu là:
    $$x_1 + x_2 + \\ldots + x_%s = %s \\cdot %s = %s.$$''' % (
        str(n_val), str(n_val), str(x_mean),
        str(n_val), str(n_val), str(x_mean), str(sum_x)
    ))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ######################################################################## Thông hiểu ###########################################
    
    # Các đáp án
    th_da_1_d = '\\True Tổng bình phương của $%s$ giá trị ban đầu bằng $%s$' % (str(n_val), str(sum_x_sq))
    th_da_1_s = 'Tổng bình phương của $%s$ giá trị ban đầu bằng $%s$' % (str(n_val), str(sum_x_sq_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Áp dụng công thức tính phương sai:
    $$s^2 = \\dfrac{1}{%s}\\left(x_1^2 + x_2^2 + \\ldots + x_%s^2\\right) - \\overline{x}^2.$$
    Suy ra tổng bình phương của $%s$ giá trị ban đầu là:
    $$x_1^2 + x_2^2 + \\ldots + x_%s^2 = %s\\left(s^2 + \\overline{x}^2\\right) = %s\\left(%s + %s^2\\right) = %s.$$''' % (
        str(n_val), str(n_val),
        str(n_val),
        str(n_val), str(n_val), str(n_val), str(s_sq), str(x_mean), str(sum_x_sq)
    ))
    
    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ######################################################################## Vận dụng ###########################################
    
    # Các đáp án
    vd_da_1_d = '\\True Nếu bổ sung thêm một giá trị $x_%s = %s$ vào mẫu số liệu trên thì số trung bình của mẫu mới vẫn bằng $%s$' % (str(n_new), str(x_mean), str(x_mean))
    vd_da_1_s = 'Nếu bổ sung thêm một giá trị $x_%s = %s$ vào mẫu số liệu trên thì số trung bình của mẫu mới bằng $%s$' % (str(n_new), str(x_mean), str(x_mean_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Khi bổ sung thêm giá trị $x_%s = %s$, số trung bình của mẫu số liệu mới gồm $%s$ giá trị là:
    $$\\overline{x}' = \\dfrac{(x_1 + x_2 + \\ldots + x_%s) + x_%s}{%s} = \\dfrac{%s + %s}{%s} = %s.$$
    Vậy số trung bình của mẫu mới vẫn bằng $%s$.''' % (
        str(n_new), str(x_mean), str(n_new),
        str(n_val), str(n_new), str(n_new), str(sum_x), str(x_mean), str(n_new), str(x_mean),
        str(x_mean)
    ))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ######################################################################## Vận dụng cao ###########################################
    
    # Các đáp án
    vdc_da_1_d = '\\True Nếu bổ sung thêm một giá trị $x_%s = %s$ vào mẫu số liệu trên thì phương sai của mẫu mới giảm đi so với ban đầu' % (str(n_new), str(x_mean))
    vdc_da_1_s = 'Nếu bổ sung thêm một giá trị $x_%s = %s$ vào mẫu số liệu trên thì phương sai của mẫu mới không thay đổi' % (str(n_new), str(x_mean))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có $\\sum_{i=1}^{%s} (x_i - \\overline{x})^2 = %s \\cdot s^2 = %s \\cdot %s = %s$. \\\\
    Khi bổ sung thêm giá trị $x_%s = %s = \\overline{x}'$, ta có $(x_%s - \\overline{x}')^2 = (%s - %s)^2 = 0$. \\\\
    Do đó phương sai của mẫu số liệu mới là:
    $$s'^2 = \\dfrac{1}{%s}\\left[\\sum_{i=1}^{%s} (x_i - \\overline{x}')^2 + (x_%s - \\overline{x}')^2\\right] = \\dfrac{%s + 0}{%s} = %s \\ne %s.$$
    Vậy phương sai của mẫu số liệu mới giảm đi so với ban đầu.''' % (
        str(n_val), str(n_val), str(n_val), str(s_sq), str(n_val * s_sq),
        str(n_new), str(x_mean), str(n_new), str(x_mean), str(x_mean),
        str(n_new), str(n_val), str(n_new), str(n_val * s_sq), str(n_new), latex(var_new), str(s_sq)
    ))
    
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
    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
    '\\choiceTFn \n'
    '{' + str(shuffled_answers_nb[0]) + '}\n'
    '{' + str(shuffled_answers_th[0]) + '}\n'
    '{' + str(shuffled_answers_vd[0]) + '}\n'
    '{' + str(shuffled_answers_vdc[0]) + '}\n'
    '\\loigiai{ \n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
    '\\item ' + str(shuffled_solutions_th[0]) + '\n'
    '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
    '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n \\end{minipage}\n\n')
    return content

