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


def bt_dang28_p2_b3_c3_ds10(self):
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
    
    # Random tham số cho mẫu A (đàn voi trưởng thành, đơn vị kg) và mẫu B (đàn chuột bạch, đơn vị g)
    # Đảm bảo CV_A < CV_B và cả hai đều là số nguyên đẹp
    while True:
        x_A = random.choice([3000, 3500, 4000, 4500, 5000])
        cv_A = random.choice([4, 5, 6, 8])
        s_A = Rational(x_A * cv_A, 100)
        
        x_B = random.choice([20, 25, 30, 40, 50])
        cv_B = random.choice([10, 12, 15, 16, 20])
        s_B = Rational(x_B * cv_B, 100)
        
        if s_A.q == 1 and s_B.q == 1 and cv_A < cv_B:
            s_A = s_A.p
            s_B = s_B.p
            break
    
    s_A_grams = s_A * 1000
    
    # Giá trị sai cho các phương án
    cv_A_wrong = cv_A + random.choice([-2, 2, 3])
    cv_B_wrong = cv_B // 10 if cv_B % 10 == 0 else cv_B - 5
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Để so sánh mức độ phân tán của hai mẫu số liệu có đơn vị đo khác nhau hoặc số trung bình chênh lệch quá lớn, người ta dùng \\textbf{hệ số biến thiên} $CV = \\dfrac{s}{\\overline{x}} \\cdot 100\\%%$ (mẫu nào có $CV$ nhỏ hơn thì đồng đều hơn). Xét hai mẫu số liệu sau:
    \\begin{itemize}
    \\item Mẫu $A$ (cân nặng của một đàn voi trưởng thành): trung bình $\\overline{x}_A = %s\\text{ kg}$, độ lệch chuẩn $s_A = %s\\text{ kg}$.
    \\item Mẫu $B$ (cân nặng của một đàn chuột bạch): trung bình $\\overline{x}_B = %s\\text{ g}$, độ lệch chuẩn $s_B = %s\\text{ g}$.
    \\end{itemize}''' % (
        str(x_A), str(s_A), str(x_B), str(s_B)
    ))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Độ lệch chuẩn của mẫu $A$ lớn hơn độ lệch chuẩn của mẫu $B$'
    nb_da_1_s = 'Độ lệch chuẩn của mẫu $A$ nhỏ hơn độ lệch chuẩn của mẫu $B$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Đổi đơn vị: $s_A = %s\\text{ kg} = %s\\text{ g}$. \\\\
    Vì $%s\\text{ g} > %s\\text{ g}$ nên độ lệch chuẩn của mẫu $A$ lớn hơn độ lệch chuẩn của mẫu $B$.''' % (
        str(s_A), str(s_A_grams), str(s_A_grams), str(s_B)
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
    th_da_1_d = '\\True Hệ số biến thiên của mẫu $A$ là $%s\\%%$' % (str(cv_A))
    th_da_1_s = 'Hệ số biến thiên của mẫu $A$ là $%s\\%%$' % (str(cv_A_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Hệ số biến thiên của mẫu $A$ là:
    $$CV_A = \\dfrac{s_A}{\\overline{x}_A} \\cdot 100\\%% = \\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%.$$''' % (
        str(s_A), str(x_A), str(cv_A)
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
    vd_da_1_d = '\\True Hệ số biến thiên của mẫu $B$ là $%s\\%%$' % (str(cv_B))
    vd_da_1_s = 'Hệ số biến thiên của mẫu $B$ là $%s\\%%$' % (str(cv_B_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Hệ số biến thiên của mẫu $B$ là:
    $$CV_B = \\dfrac{s_B}{\\overline{x}_B} \\cdot 100\\%% = \\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%.$$''' % (
        str(s_B), str(x_B), str(cv_B)
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
    vdc_da_1_d = '\\True Xét về tỉ lệ biến động tương đối, cân nặng của đàn voi đồng đều hơn đàn chuột bạch'
    vdc_da_1_s = 'Xét về tỉ lệ biến động tương đối, cân nặng của đàn chuột bạch đồng đều hơn đàn voi'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có $CV_A = %s\\%% < CV_B = %s\\%%$. \\\\
    Vì mẫu nào có hệ số biến thiên nhỏ hơn thì đồng đều hơn nên xét về tỉ lệ biến động tương đối, cân nặng của đàn voi đồng đều hơn đàn chuột bạch.''' % (
        str(cv_A), str(cv_B)
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

