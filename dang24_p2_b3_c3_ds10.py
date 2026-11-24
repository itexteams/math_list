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


def bt_dang24_p2_b3_c3_ds10(self):
    def fmt_num(val):
        if isinstance(val, Rational):
            if val.q == 1:
                return str(val.p)
            else:
                f = float(val)
                s = str(round(f, 5)).rstrip('0').rstrip('.')
                return s.replace('.', ',')
        elif isinstance(val, float):
            s = str(round(val, 5)).rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return str(val)
    
    scores = [5, 6, 7, 8, 9, 10]
    
    # Tạo dữ liệu ngẫu nhiên cho bảng tần số của hai lớp 10A và 10B (mỗi lớp 40 học sinh)
    # Đảm bảo:
    # - Điểm trung bình của hai lớp bằng nhau (và là số đẹp)
    # - Lớp 10A có điểm tập trung ở giữa (5 và 10 có tần số 0), khoảng biến thiên nhỏ hơn 10B là 2 điểm
    # - Phương sai của 10A nhỏ hơn 10B (học sinh lớp 10A học đồng đều hơn lớp 10B)
    while True:
        # Lớp 10A: tần số tại điểm 5 và 10 bằng 0; tần số tại 6, 7, 8, 9 > 0 và tổng bằng 40
        a6 = random.choice([4, 5, 6])
        a7 = random.choice([8, 10, 12])
        a8 = random.choice([12, 14, 15, 16])
        a9 = 40 - (a6 + a7 + a8)
        if a9 < 4:
            continue
        freq_A = [0, a6, a7, a8, a9, 0]
        
        # Lớp 10B: tần số tại điểm 5 và 10 dương, tần số tại 6 bằng 0 (hoặc nhỏ), tổng bằng 40
        b5 = random.choice([4, 5, 6])
        b10 = random.choice([4, 5, 6])
        b7 = random.choice([8, 10, 12])
        b8 = random.choice([8, 10, 12])
        b9 = 40 - (b5 + b7 + b8 + b10)
        if b9 < 4:
            continue
        freq_B = [b5, 0, b7, b8, b9, b10]
        
        mean_A = Rational(sum(s * f for s, f in zip(scores, freq_A)), 40)
        mean_B = Rational(sum(s * f for s, f in zip(scores, freq_B)), 40)
        
        if mean_A == mean_B and 10 % mean_A.q == 0:
            var_A = sum(f * (s - mean_A)**2 for s, f in zip(scores, freq_A)) / Rational(40)
            var_B = sum(f * (s - mean_B)**2 for s, f in zip(scores, freq_B)) / Rational(40)
            if var_A < var_B and 10000 % var_A.q == 0 and 10000 % var_B.q == 0:
                break
    
    R_A = 9 - 6
    R_B = 10 - 5
    R_diff = R_B - R_A
    
    # Giá trị sai cho các phương án
    R_diff_wrong = R_diff + random.choice([1, 2])
    var_A_wrong = var_A + Rational(1, 4)
    
    # Chuỗi hiển thị trong lời giải
    sum_A_str = ' + '.join('%s \\cdot %s' % (str(f), str(s)) for s, f in zip(scores, freq_A) if f > 0)
    sum_B_str = ' + '.join('%s \\cdot %s' % (str(f), str(s)) for s, f in zip(scores, freq_B) if f > 0)
    var_A_str = ' + '.join('%s(%s - %s)^2' % (str(f), str(s), fmt_num(mean_A)) for s, f in zip(scores, freq_A) if f > 0)
    var_B_str = ' + '.join('%s(%s - %s)^2' % (str(f), str(s), fmt_num(mean_B)) for s, f in zip(scores, freq_B) if f > 0)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Kết quả thi học kì I môn Toán của hai lớp $10A$ và $10B$ (mỗi lớp $40$ học sinh) được thống kê ở bảng sau:
    \\begin{center}
    \\begin{tabular}{|l|c|c|c|c|c|c|}
    \\hline
    \\textbf{Điểm} & $5$ & $6$ & $7$ & $8$ & $9$ & $10$ \\\\
    \\hline
    \\textbf{Lớp 10A} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\textbf{Lớp 10B} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (
        str(freq_A[0]), str(freq_A[1]), str(freq_A[2]), str(freq_A[3]), str(freq_A[4]), str(freq_A[5]),
        str(freq_B[0]), str(freq_B[1]), str(freq_B[2]), str(freq_B[3]), str(freq_B[4]), str(freq_B[5])
    ))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Điểm trung bình môn Toán của hai lớp $10A$ và $10B$ bằng nhau'
    nb_da_1_s = 'Điểm trung bình môn Toán của lớp $10A$ cao hơn lớp $10B$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Điểm trung bình môn Toán của lớp $10A$ là:
    $$\\overline{x}_A = \\dfrac{%s}{40} = %s.$$
    Điểm trung bình môn Toán của lớp $10B$ là:
    $$\\overline{x}_B = \\dfrac{%s}{40} = %s.$$
    Vậy điểm trung bình môn Toán của hai lớp $10A$ và $10B$ bằng nhau (đều bằng $%s$).''' % (
        sum_A_str, fmt_num(mean_A),
        sum_B_str, fmt_num(mean_B),
        fmt_num(mean_A)
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
    th_da_1_d = '\\True Khoảng biến thiên điểm số của lớp $10B$ lớn hơn lớp $10A$ là $%s$ điểm' % (str(R_diff))
    th_da_1_s = 'Khoảng biến thiên điểm số của lớp $10B$ lớn hơn lớp $10A$ là $%s$ điểm' % (str(R_diff_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Khoảng biến thiên điểm số của lớp $10A$ là $R_A = 9 - 6 = %s$ (điểm). \\\\
    Khoảng biến thiên điểm số của lớp $10B$ là $R_B = 10 - 5 = %s$ (điểm). \\\\
    Vậy khoảng biến thiên điểm số của lớp $10B$ lớn hơn lớp $10A$ là $%s - %s = %s$ (điểm).''' % (
        str(R_A), str(R_B), str(R_B), str(R_A), str(R_diff)
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
    vd_da_1_d = '\\True Phương sai điểm số của lớp $10A$ là $%s$' % (fmt_num(var_A))
    vd_da_1_s = 'Phương sai điểm số của lớp $10A$ là $%s$' % (fmt_num(var_A_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Phương sai điểm số của lớp $10A$ là:
    $$s_A^2 = \\dfrac{1}{40}\\left[%s\\right] = %s.$$''' % (
        var_A_str, fmt_num(var_A)
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
    vdc_da_1_d = '\\True Học sinh lớp $10A$ học đồng đều hơn học sinh lớp $10B$'
    vdc_da_1_s = 'Học sinh lớp $10B$ học đồng đều hơn học sinh lớp $10A$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Phương sai điểm số của lớp $10B$ là:
    $$s_B^2 = \\dfrac{1}{40}\\left[%s\\right] = %s.$$
    Hai lớp có cùng điểm trung bình là $%s$, nhưng phương sai điểm số của lớp $10A$ ($s_A^2 = %s$) nhỏ hơn phương sai điểm số của lớp $10B$ ($s_B^2 = %s$). \\\\
    Do đó độ lệch chuẩn điểm số của lớp $10A$ nhỏ hơn lớp $10B$, nên học sinh lớp $10A$ học đồng đều hơn học sinh lớp $10B$.''' % (
        var_B_str, fmt_num(var_B),
        fmt_num(mean_A), fmt_num(var_A), fmt_num(var_B)
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

