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


def bt_dang23_p2_b3_c3_ds10(self):
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
    
    # Khai báo biến m
    m = symbols('m', real=True)
    
    # Tạo dữ liệu ngẫu nhiên gồm 4 số tạo thành cấp số cộng: x1, x2, x3, x4 và số thứ 5 là m0
    # Ví dụ: 2, 4, 6, 8 và m0 = 10 (hoặc bước d = 1, 2, 3)
    d_step = random.choice([1, 2, 3])
    x1 = random.randint(1, 5)
    x2 = x1 + d_step
    x3 = x1 + 2 * d_step
    x4 = x1 + 3 * d_step
    m0 = x1 + 4 * d_step
    
    # Các đặc trưng khi m = m0 (mẫu gồm 5 số hạng liên tiếp của cấp số cộng công sai d_step)
    R_val = m0 - x1
    mean_m0 = x3
    var_m0 = Rational(sum((v - mean_m0)**2 for v in [x1, x2, x3, x4, m0]), 5)
    
    # Phương sai tổng quát theo tham số m:
    # s^2(m) = (4/25)*(m - mean_4)^2 + var_4
    mean_4 = Rational(x1 + x2 + x3 + x4, 4)
    var_4 = sum((v - mean_4)**2 for v in [x1, x2, x3, x4]) / Rational(4)
    # Giá trị nhỏ nhất của phương sai đạt được khi m = mean_4, bằng (4/5)*var_4
    var_min = Rational(4, 5) * var_4
    
    # Chọn một ngưỡng k_var nhỏ hơn var_min sao cho s^2 = k_var vô nghiệm
    if d_step == 1:
        k_var = 1
    elif d_step == 2:
        k_var = 4
    else:
        k_var = 9
    
    # Biểu thức phương sai rút gọn theo m
    var_expr = expand(Rational(1, 5) * sum((v - Rational(x1 + x2 + x3 + x4 + m, 5))**2 for v in [x1, x2, x3, x4, m]))
    # Dạng bình phương hoàn chỉnh: Rational(4, 25) * (m - mean_4)^2 + var_min
    a_quad = Rational(4, 25)
    
    # Giá trị sai cho các phương án
    R_wrong = R_val + random.choice([-1, 1, 2])
    var_wrong = var_m0 + random.choice([-2, 2])
    m0_wrong = m0 + random.choice([-2, -1, 1, 2])
    
    # Chuỗi hiển thị
    sq_m0_str = '(%s - %s)^2 + (%s - %s)^2 + (%s - %s)^2 + (%s - %s)^2 + (%s - %s)^2' % (
        str(x1), str(mean_m0),
        str(x2), str(mean_m0),
        str(x3), str(mean_m0),
        str(x4), str(mean_m0),
        str(m0), str(mean_m0)
    )
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho mẫu số liệu gồm $5$ số: $%s; \\quad %s; \\quad %s; \\quad %s; \\quad m$ (với $m$ là tham số thực).''' % (
        str(x1), str(x2), str(x3), str(x4)
    ))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Với $m = %s$, khoảng biến thiên của mẫu số liệu bằng $%s$' % (str(m0), str(R_val))
    nb_da_1_s = 'Với $m = %s$, khoảng biến thiên của mẫu số liệu bằng $%s$' % (str(m0), str(R_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Với $m = %s$, mẫu số liệu là: $%s; %s; %s; %s; %s$. \\\\
    Giá trị lớn nhất là $%s$ và giá trị nhỏ nhất là $%s$. \\\\
    Vậy khoảng biến thiên của mẫu số liệu bằng $R = %s - %s = %s$.''' % (
        str(m0), str(x1), str(x2), str(x3), str(x4), str(m0),
        str(m0), str(x1), str(m0), str(x1), str(R_val)
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
    th_da_1_d = '\\True Với $m = %s$, phương sai của mẫu số liệu bằng $%s$' % (str(m0), str(var_m0))
    th_da_1_s = 'Với $m = %s$, phương sai của mẫu số liệu bằng $%s$' % (str(m0), str(var_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Với $m = %s$, số trung bình của mẫu số liệu là:
    $$\\overline{x} = \\dfrac{%s + %s + %s + %s + %s}{5} = %s.$$
    Phương sai của mẫu số liệu là:
    $$s^2 = \\dfrac{1}{5}\\left[%s\\right] = %s.$$''' % (
        str(m0), str(x1), str(x2), str(x3), str(x4), str(m0), str(mean_m0),
        sq_m0_str, str(var_m0)
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
    vd_da_1_d = '\\True Để số trung bình của mẫu số liệu bằng $%s$ thì giá trị của $m$ phải bằng $%s$' % (str(mean_m0), str(m0))
    vd_da_1_s = 'Để số trung bình của mẫu số liệu bằng $%s$ thì giá trị của $m$ phải bằng $%s$' % (str(mean_m0), str(m0_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    sum_4 = x1 + x2 + x3 + x4
    loigiai_vd_1 = ('''Số trung bình của mẫu số liệu là $\\overline{x} = \\dfrac{%s + %s + %s + %s + m}{5} = \\dfrac{%s + m}{5}$. \\\\
    Theo giả thiết $\\overline{x} = %s \\Leftrightarrow \\dfrac{%s + m}{5} = %s \\Leftrightarrow %s + m = %s \\Leftrightarrow m = %s$.''' % (
        str(x1), str(x2), str(x3), str(x4), str(sum_4),
        str(mean_m0), str(sum_4), str(mean_m0), str(sum_4), str(5 * mean_m0), str(m0)
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
    vdc_da_1_d = '\\True Không tồn tại giá trị nào của $m$ để phương sai của mẫu số liệu bằng $%s$' % (str(k_var))
    vdc_da_1_s = 'Tồn tại duy nhất một giá trị của $m$ để phương sai của mẫu số liệu bằng $%s$' % (str(k_var))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có $\\overline{x} = \\dfrac{%s + m}{5}$. Phương sai của mẫu số liệu theo $m$ là:
    $$s^2 = \\dfrac{1}{5}\\left[\\left(%s - \\dfrac{%s + m}{5}\\right)^2 + \\left(%s - \\dfrac{%s + m}{5}\\right)^2 + \\left(%s - \\dfrac{%s + m}{5}\\right)^2 + \\left(%s - \\dfrac{%s + m}{5}\\right)^2 + \\left(m - \\dfrac{%s + m}{5}\\right)^2\\right] = \\dfrac{4}{25}\\left(m - %s\\right)^2 + %s.$$
    Vì $\\dfrac{4}{25}\\left(m - %s\\right)^2 \\ge 0$ với mọi $m \\in \\mathbb{R}$ nên $s^2 \\ge %s > %s$ với mọi $m \\in \\mathbb{R}$. \\\\
    Vậy không tồn tại giá trị nào của $m$ để phương sai của mẫu số liệu bằng $%s$.''' % (
        str(sum_4),
        str(x1), str(sum_4),
        str(x2), str(sum_4),
        str(x3), str(sum_4),
        str(x4), str(sum_4),
        str(sum_4),
        fmt_num(mean_4), fmt_num(var_min),
        fmt_num(mean_4), fmt_num(var_min), str(k_var),
        str(k_var)
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

