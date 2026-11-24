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


def bt_dang27_p2_b3_c3_ds10(self):
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
    
    # Tạo dữ liệu ngẫu nhiên gồm 10 phiên giá đóng cửa cổ phiếu (nghìn đồng)
    # Đảm bảo trung bình cộng là số nguyên đẹp, phương sai là số thập phân hữu hạn đẹp
    while True:
        mean_val = random.randint(20, 26)
        total_target = 10 * mean_val
        
        # Tạo 9 giá trị đầu quanh mean_val
        data = [mean_val + random.choice([-3, -2, -1, 0, 0, 1, 2, 3]) for _ in range(9)]
        last_val = total_target - sum(data)
        
        if mean_val - 4 <= last_val <= mean_val + 4:
            data.append(last_val)
            sorted_data = sorted(data)
            
            R_val = sorted_data[-1] - sorted_data[0]
            # Mẫu có 10 phần tử: nửa dưới 5 phần tử đầu (index 0..4), nửa trên 5 phần tử sau (index 5..9)
            Q1_val = sorted_data[2]
            Q3_val = sorted_data[7]
            delta_Q = Q3_val - Q1_val
            
            var_val = sum((v - Rational(mean_val))**2 for v in data) / Rational(10)
            
            if R_val >= 4 and delta_Q >= 2 and var_val > 0 and 100 % var_val.q == 0:
                raw_data = data[:]
                random.shuffle(raw_data)
                if raw_data != sorted_data:
                    break
    
    # Ngưỡng giá trị bất thường của 10 phiên đầu
    upper_fence = Q3_val + Rational(3, 2) * delta_Q
    lower_fence = Q1_val - Rational(3, 2) * delta_Q
    
    # Tạo giá trị tăng đột biến ở phiên thứ 11 lớn hơn upper_fence
    outlier_val = int(math.floor(float(upper_fence))) + random.randint(6, 12)
    
    # Các giá trị sai cho phương án
    R_wrong = R_val + random.choice([-1, 1, 2])
    Q1_wrong = Q1_val + random.choice([-1, 1])
    Q3_wrong = Q3_val + random.choice([-1, 1])
    var_wrong = var_val + Rational(1, 2) if var_val.q != 1 else var_val + 1
    
    # Chuỗi hiển thị dãy số liệu và các biểu thức tính toán
    raw_str = '; \\quad '.join(str(v) for v in raw_data)
    sorted_str = '; \\quad '.join(str(v) for v in sorted_data)
    sum_str = ' + '.join(str(v) for v in raw_data)
    sq_diff_str = ' + '.join('(%s - %s)^2' % (str(v), str(mean_val)) for v in raw_data)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Giá đóng cửa của một mã cổ phiếu (đơn vị: nghìn đồng) trong $10$ phiên giao dịch liên tiếp được ghi lại như sau:
    \\begin{center}
    $%s$
    \\end{center}''' % (raw_str))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Khoảng biến thiên giá cổ phiếu trong $10$ phiên là $%s$ nghìn đồng' % (str(R_val))
    nb_da_1_s = 'Khoảng biến thiên giá cổ phiếu trong $10$ phiên là $%s$ nghìn đồng' % (str(R_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Trong $10$ phiên giao dịch trên, giá đóng cửa cao nhất là $%s$ nghìn đồng và giá đóng cửa thấp nhất là $%s$ nghìn đồng. \\\\
    Vậy khoảng biến thiên giá cổ phiếu trong $10$ phiên là $R = %s - %s = %s$ (nghìn đồng).''' % (
        str(sorted_data[-1]), str(sorted_data[0]),
        str(sorted_data[-1]), str(sorted_data[0]), str(R_val)
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
    th_da_1_d = '\\True Tứ phân vị thứ nhất $Q_1 = %s$ và tứ phân vị thứ ba $Q_3 = %s$' % (str(Q1_val), str(Q3_val))
    th_da_1_s = 'Tứ phân vị thứ nhất $Q_1 = %s$ và tứ phân vị thứ ba $Q_3 = %s$' % (str(Q1_wrong), str(Q3_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Sắp xếp mẫu số liệu theo thứ tự không giảm ta được:
    $$%s.$$
    Nửa số liệu bên trái gồm $5$ giá trị: $%s; %s; %s; %s; %s$, suy ra tứ phân vị thứ nhất là $Q_1 = %s$. \\\\
    Nửa số liệu bên phải gồm $5$ giá trị: $%s; %s; %s; %s; %s$, suy ra tứ phân vị thứ ba là $Q_3 = %s$.''' % (
        sorted_str,
        str(sorted_data[0]), str(sorted_data[1]), str(sorted_data[2]), str(sorted_data[3]), str(sorted_data[4]), str(Q1_val),
        str(sorted_data[5]), str(sorted_data[6]), str(sorted_data[7]), str(sorted_data[8]), str(sorted_data[9]), str(Q3_val)
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
    vd_da_1_d = '\\True Phương sai của mẫu số liệu trên là $%s$' % (fmt_num(var_val))
    vd_da_1_s = 'Phương sai của mẫu số liệu trên là $%s$' % (fmt_num(var_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Giá đóng cửa trung bình của cổ phiếu trong $10$ phiên là:
    $$\\overline{x} = \\dfrac{%s}{10} = %s \\text{ (nghìn đồng)}.$$
    Phương sai của mẫu số liệu trên là:
    $$s^2 = \\dfrac{1}{10}\\left[%s\\right] = %s.$$''' % (
        sum_str, str(mean_val), sq_diff_str, fmt_num(var_val)
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
    vdc_da_1_d = '\\True Nếu trong phiên thứ $11$, giá cổ phiếu tăng đột biến lên $%s$ nghìn đồng thì giá trị $%s$ này là giá trị bất thường so với $10$ phiên trước đó' % (str(outlier_val), str(outlier_val))
    vdc_da_1_s = 'Nếu trong phiên thứ $11$, giá cổ phiếu tăng đột biến lên $%s$ nghìn đồng thì giá trị $%s$ này không phải là giá trị bất thường so với $10$ phiên trước đó' % (str(outlier_val), str(outlier_val))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Khoảng tứ phân vị của $10$ phiên trước đó là $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$. \\\\
    Ngưỡng trên để xác định giá trị bất thường là:
    $$Q_3 + 1,5 \\cdot \\Delta_Q = %s + 1,5 \\cdot %s = %s.$$
    Vì $%s > %s$ nên giá trị $%s$ là giá trị bất thường so với $10$ phiên trước đó.''' % (
        str(Q3_val), str(Q1_val), str(delta_Q),
        str(Q3_val), str(delta_Q), fmt_num(upper_fence),
        str(outlier_val), fmt_num(upper_fence), str(outlier_val)
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

