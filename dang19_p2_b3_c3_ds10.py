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


def bt_dang19_p2_b3_c3_ds10(self):
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
    
    # Khai báo biến
    x_sym = symbols('x_i')
    
    # Random các tham số của mẫu số liệu X và phép biến đổi y_i = a * x_i + b
    x_mean = random.randint(8, 15)
    R_X = random.randint(6, 12)
    delta_QX = random.randint(3, min(6, R_X - 1))
    s_X = random.randint(2, 5)
    
    a_coef = random.choice([2, 3, 4])
    b_coef = random.choice([-5, -4, -3, 3, 4, 5, 6])
    
    # Biểu thức y_i
    y_expr = a_coef * x_sym + b_coef
    
    # Tính toán các đặc trưng của mẫu số liệu Y
    y_mean = a_coef * x_mean + b_coef
    R_Y = abs(a_coef) * R_X
    delta_QY = abs(a_coef) * delta_QX
    s_Y = abs(a_coef) * s_X
    var_Y = s_Y**2
    
    # Các giá trị sai gây nhiễu thường gặp
    y_mean_wrong = a_coef * x_mean
    R_Y_wrong = abs(a_coef) * R_X + b_coef
    if R_Y_wrong == R_Y:
        R_Y_wrong = R_Y + random.choice([-2, 2])
    delta_QY_wrong = abs(a_coef) * delta_QX + b_coef
    if delta_QY_wrong == delta_QY:
        delta_QY_wrong = delta_QY + random.choice([-2, 2])
    var_Y_wrong = abs(a_coef) * (s_X**2)
    
    # Định dạng chuỗi phép biến đổi y_i = a x_i + b
    if b_coef > 0:
        y_str = '%sx_i + %s' % (str(a_coef), str(b_coef))
        y_mean_calc = '%s \\cdot %s + %s = %s' % (str(a_coef), str(x_mean), str(b_coef), str(y_mean))
        R_Y_calc = '(%s x_{\\max} + %s) - (%s x_{\\min} + %s) = %s(x_{\\max} - x_{\\min}) = %s R_X = %s \\cdot %s = %s' % (
            str(a_coef), str(b_coef), str(a_coef), str(b_coef), str(a_coef), str(a_coef), str(a_coef), str(R_X), str(R_Y)
        )
    else:
        abs_b = abs(b_coef)
        y_str = '%sx_i - %s' % (str(a_coef), str(abs_b))
        y_mean_calc = '%s \\cdot %s - %s = %s' % (str(a_coef), str(x_mean), str(abs_b), str(y_mean))
        R_Y_calc = '(%s x_{\\max} - %s) - (%s x_{\\min} - %s) = %s(x_{\\max} - x_{\\min}) = %s R_X = %s \\cdot %s = %s' % (
            str(a_coef), str(abs_b), str(a_coef), str(abs_b), str(a_coef), str(a_coef), str(a_coef), str(R_X), str(R_Y)
        )
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho mẫu số liệu $X$ gồm $n$ giá trị $x_1, x_2, \\ldots, x_n$ có số trung bình $\\overline{x} = %s$, khoảng biến thiên $R_X = %s$, khoảng tứ phân vị $\\Delta_{Q_X} = %s$ và độ lệch chuẩn $s_X = %s$. Xét mẫu số liệu $Y$ gồm các giá trị $y_i = %s$ với mọi $i = 1, 2, \\ldots, n$.''' % (
        str(x_mean), str(R_X), str(delta_QX), str(s_X), y_str
    ))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Số trung bình của mẫu số liệu $Y$ là $\\overline{y} = %s$' % (str(y_mean))
    nb_da_1_s = 'Số trung bình của mẫu số liệu $Y$ là $\\overline{y} = %s$' % (str(y_mean_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Vì $y_i = %s$ với mọi $i = 1, 2, \\ldots, n$ nên số trung bình của mẫu số liệu $Y$ là:
    $$\\overline{y} = %s\\overline{x} %s %s = %s.$$''' % (
        y_str,
        str(a_coef), '+' if b_coef > 0 else '-', str(abs(b_coef)),
        y_mean_calc
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
    th_da_1_d = '\\True Khoảng biến thiên của mẫu số liệu $Y$ là $R_Y = %s$' % (str(R_Y))
    th_da_1_s = 'Khoảng biến thiên của mẫu số liệu $Y$ là $R_Y = %s$' % (str(R_Y_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Do $a = %s > 0$ nên giá trị lớn nhất và giá trị nhỏ nhất của mẫu số liệu $Y$ lần lượt là $y_{\\max} = %s x_{\\max} %s %s$ và $y_{\\min} = %s x_{\\min} %s %s$. \\\\
    Vậy khoảng biến thiên của mẫu số liệu $Y$ là:
    $$R_Y = y_{\\max} - y_{\\min} = %s.$$''' % (
        str(a_coef),
        str(a_coef), '+' if b_coef > 0 else '-', str(abs(b_coef)),
        str(a_coef), '+' if b_coef > 0 else '-', str(abs(b_coef)),
        R_Y_calc
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
    vd_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu $Y$ là $\\Delta_{Q_Y} = %s$' % (str(delta_QY))
    vd_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu $Y$ là $\\Delta_{Q_Y} = %s$' % (str(delta_QY_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Do $a = %s > 0$ nên tứ phân vị thứ nhất và tứ phân vị thứ ba của mẫu số liệu $Y$ lần lượt là $Q_{1Y} = %s Q_{1X} %s %s$ và $Q_{3Y} = %s Q_{3X} %s %s$. \\\\
    Suy ra khoảng tứ phân vị của mẫu số liệu $Y$ là:
    $$\\Delta_{Q_Y} = Q_{3Y} - Q_{1Y} = %s(Q_{3X} - Q_{1X}) = %s \\Delta_{Q_X} = %s \\cdot %s = %s.$$''' % (
        str(a_coef),
        str(a_coef), '+' if b_coef > 0 else '-', str(abs(b_coef)),
        str(a_coef), '+' if b_coef > 0 else '-', str(abs(b_coef)),
        str(a_coef), str(a_coef), str(a_coef), str(delta_QX), str(delta_QY)
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
    vdc_da_1_d = '\\True Phương sai của mẫu số liệu $Y$ là $s_Y^2 = %s$' % (str(var_Y))
    vdc_da_1_s = 'Phương sai của mẫu số liệu $Y$ là $s_Y^2 = %s$' % (str(var_Y_wrong))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có $y_i - \\overline{y} = (%s) - (%s\\overline{x} %s %s) = %s(x_i - \\overline{x})$ với mọi $i = 1, 2, \\ldots, n$. \\\\
    Do đó phương sai của mẫu số liệu $Y$ là:
    $$s_Y^2 = \\dfrac{1}{n}\\sum_{i=1}^{n} (y_i - \\overline{y})^2 = \\dfrac{1}{n}\\sum_{i=1}^{n} %s^2 (x_i - \\overline{x})^2 = %s^2 s_X^2 = %s \\cdot %s^2 = %s.$$''' % (
        y_str,
        str(a_coef), '+' if b_coef > 0 else '-', str(abs(b_coef)),
        str(a_coef),
        str(a_coef), str(a_coef), str(a_coef**2), str(s_X), str(var_Y)
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

