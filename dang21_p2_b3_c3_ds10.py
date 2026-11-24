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


def bt_dang21_p2_b3_c3_ds10(self):
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
    
    # Tạo dữ liệu ngẫu nhiên gồm 11 mức lương (triệu đồng) đã sắp xếp tăng dần
    # Đảm bảo:
    # - Ban đầu (11 phần tử): Q1 = x_3, Q3 = x_9
    # - Có đúng 1 giá trị bất thường lớn (lương Giám đốc x_11)
    # - Khi bỏ x_11 (còn 10 phần tử): Q1' = x_3, Q3' = x_8. Chọn x_8 < x_9 để khoảng tứ phân vị thay đổi!
    while True:
        x0 = random.randint(7, 10)
        data = [x0]
        for _ in range(9):
            step = random.choice([0, 1, 1, 2])
            data.append(data[-1] + step)
        
        # Ban đầu n = 11:
        # Trung vị Q2 = data[5]
        # Nửa dưới gồm 5 phần tử đầu (index 0..4): Q1 = data[2]
        # Nửa trên gồm 5 phần tử sau (index 6..10): Q3 = data[8]
        Q1_old = data[2]
        Q3_old = data[8]
        delta_Q_old = Q3_old - Q1_old
        
        # Sau khi bỏ phần tử cuối (n = 10):
        # Nửa dưới gồm 5 phần tử đầu (index 0..4): Q1_new = data[2]
        # Nửa trên gồm 5 phần tử sau (index 5..9): Q3_new = data[7]
        Q1_new = data[2]
        Q3_new = data[7]
        delta_Q_new = Q3_new - Q1_new
        
        if delta_Q_old >= 3 and delta_Q_new != delta_Q_old:
            upper_fence = Q3_old + Rational(3, 2) * delta_Q_old
            lower_fence = Q1_old - Rational(3, 2) * delta_Q_old
            # Đảm bảo 10 phần tử đầu đều nằm trong khoảng thông thường
            if data[0] >= lower_fence and data[9] <= upper_fence:
                outlier_val = int(math.floor(float(upper_fence))) + random.randint(10, 20)
                data.append(outlier_val)
                break
    
    R_val = data[-1] - data[0]
    
    # Giá trị sai cho các phương án
    R_wrong = R_val + random.choice([-2, -1, 1, 2])
    Q1_wrong = Q1_old + random.choice([-1, 1])
    Q3_wrong = Q3_old + random.choice([-1, 1])
    
    # Chuỗi hiển thị dãy số liệu
    data_str = '; \\quad '.join(str(v) for v in data)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Mức lương hàng tháng (đơn vị: triệu đồng) của $11$ nhân viên trong một công ty nhỏ được liệt kê theo thứ tự tăng dần:
    \\begin{center}
    $%s$
    \\end{center}''' % (data_str))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Khoảng biến thiên của mức lương là $%s$ triệu đồng' % (str(R_val))
    nb_da_1_s = 'Khoảng biến thiên của mức lương là $%s$ triệu đồng' % (str(R_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Trong mẫu số liệu trên, mức lương cao nhất là $%s$ triệu đồng và mức lương thấp nhất là $%s$ triệu đồng. \\\\
    Vậy khoảng biến thiên của mức lương là $R = %s - %s = %s$ (triệu đồng).''' % (
        str(data[-1]), str(data[0]), str(data[-1]), str(data[0]), str(R_val)
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
    th_da_1_d = '\\True Tứ phân vị thứ nhất $Q_1 = %s$ và tứ phân vị thứ ba $Q_3 = %s$' % (str(Q1_old), str(Q3_old))
    th_da_1_s = 'Tứ phân vị thứ nhất $Q_1 = %s$ và tứ phân vị thứ ba $Q_3 = %s$' % (str(Q1_wrong), str(Q3_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Mẫu số liệu đã được sắp xếp theo thứ tự không giảm và có $n = 11$ giá trị. \\\\
    Số trung vị là giá trị thứ $6$: $Q_2 = %s$. \\\\
    Nửa số liệu bên trái gồm $5$ giá trị: $%s; %s; %s; %s; %s$, suy ra tứ phân vị thứ nhất là $Q_1 = %s$. \\\\
    Nửa số liệu bên phải gồm $5$ giá trị: $%s; %s; %s; %s; %s$, suy ra tứ phân vị thứ ba là $Q_3 = %s$.''' % (
        str(data[5]),
        str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(Q1_old),
        str(data[6]), str(data[7]), str(data[8]), str(data[9]), str(data[10]), str(Q3_old)
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
    vd_da_1_d = '\\True Trong công ty này có đúng $1$ người có mức lương được coi là giá trị bất thường'
    vd_da_1_s = 'Trong công ty này có đúng $2$ người có mức lương được coi là giá trị bất thường'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$. \\\\
    Ta có:
    $$Q_1 - 1,5 \\cdot \\Delta_Q = %s - 1,5 \\cdot %s = %s;$$
    $$Q_3 + 1,5 \\cdot \\Delta_Q = %s + 1,5 \\cdot %s = %s.$$
    Trong mẫu số liệu trên, chỉ có duy nhất giá trị $%s > %s$ nên trong công ty này có đúng $1$ người có mức lương được coi là giá trị bất thường.''' % (
        str(Q3_old), str(Q1_old), str(delta_Q_old),
        str(Q1_old), str(delta_Q_old), fmt_num(lower_fence),
        str(Q3_old), str(delta_Q_old), fmt_num(upper_fence),
        str(outlier_val), fmt_num(upper_fence)
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
    vdc_da_1_d = '\\True Nếu người có mức lương $%s$ triệu đồng (Giám đốc) nghỉ việc, thì khoảng tứ phân vị của mẫu số liệu mới thay đổi so với ban đầu' % (str(outlier_val))
    vdc_da_1_s = 'Nếu người có mức lương $%s$ triệu đồng (Giám đốc) nghỉ việc, thì khoảng tứ phân vị của mẫu số liệu mới không thay đổi so với ban đầu' % (str(outlier_val))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Nếu người có mức lương $%s$ triệu đồng nghỉ việc thì mẫu số liệu mới còn $n' = 10$ giá trị:
    $$%s.$$
    Nửa số liệu bên trái gồm $5$ giá trị: $%s; %s; %s; %s; %s$, suy ra $Q'_1 = %s$. \\\\
    Nửa số liệu bên phải gồm $5$ giá trị: $%s; %s; %s; %s; %s$, suy ra $Q'_3 = %s$. \\\\
    Khoảng tứ phân vị của mẫu số liệu mới là $\\Delta'_Q = Q'_3 - Q'_1 = %s - %s = %s \\ne %s$. \\\\
    Vậy khoảng tứ phân vị của mẫu số liệu mới thay đổi so với ban đầu.''' % (
        str(outlier_val),
        '; \\quad '.join(str(v) for v in data[:10]),
        str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(Q1_new),
        str(data[5]), str(data[6]), str(data[7]), str(data[8]), str(data[9]), str(Q3_new),
        str(Q3_new), str(Q1_new), str(delta_Q_new), str(delta_Q_old)
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

