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


def bt_dang14_p2_b3_c3_ds10(self):
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
    
    # Tạo dữ liệu ngẫu nhiên gồm 10 điểm kiểm tra đã sắp xếp tăng dần
    # Đảm bảo phương sai là một số nguyên hoặc số thập phân hữu hạn đẹp
    while True:
        min_val = random.randint(2, 4)
        data = [min_val]
        for _ in range(9):
            step = random.choice([0, 1, 1, 2])
            next_val = min(10, data[-1] + step)
            data.append(next_val)
        
        # Đảm bảo có đủ độ phân tán và giá trị lớn nhất khác giá trị nhỏ nhất
        if len(set(data)) >= 5 and data[-1] - data[0] >= 4:
            # Kiểm tra trung bình cộng và phương sai
            mean_val = Rational(sum(data), 10)
            var_val = sum((x_i - mean_val)**2 for x_i in data) / Rational(10)
            # Kiểm tra xem phương sai có phải số thập phân tối đa 2 chữ số thập phân không (mẫu số ước của 100)
            if 100 % var_val.q == 0:
                break
    
    # Tính toán các đặc trưng của mẫu số liệu
    R_val = data[-1] - data[0]
    
    # Mẫu có 10 phần tử: nửa dưới gồm 5 phần tử đầu (index 0..4), nửa trên gồm 5 phần tử sau (index 5..9)
    Q1_val = data[2]
    Q3_val = data[7]
    Q2_val = Rational(data[4] + data[5], 2)
    delta_Q = Q3_val - Q1_val
    
    # Giá trị cộng thêm ở câu d
    k_add = random.randint(1, 2)
    
    # Chuỗi hiển thị dãy số liệu
    data_str = '; \\quad '.join(str(v) for v in data)
    sum_str = ' + '.join(str(v) for v in data)
    sq_diff_str = ' + '.join('(%s - %s)^2' % (str(v), fmt_num(mean_val)) for v in data)
    
    # Giá trị sai cho các phương án
    R_wrong = R_val + random.choice([-1, 1])
    delta_Q_wrong = delta_Q + Rational(1, 2)
    var_wrong = var_val + Rational(1, 2) if var_val.q != 1 else var_val + 1
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Điểm kiểm tra $15$ phút môn Toán của $10$ học sinh tổ $1$ được ghi lại như sau:
    \\begin{center}
    $%s$
    \\end{center}''' % (data_str))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Khoảng biến thiên của mẫu số liệu trên là $%s$' % (fmt_num(R_val))
    nb_da_1_s = 'Khoảng biến thiên của mẫu số liệu trên là $%s$' % (fmt_num(R_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Trong mẫu số liệu trên, giá trị lớn nhất là $%s$ và giá trị nhỏ nhất là $%s$. \\\\
    Vậy khoảng biến thiên của mẫu số liệu trên là $R = %s - %s = %s$.''' % (str(data[-1]), str(data[0]), str(data[-1]), str(data[0]), fmt_num(R_val)))
    
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
    th_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu trên là $\\Delta_Q = %s$' % (fmt_num(delta_Q))
    th_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu trên là $\\Delta_Q = %s$' % (fmt_num(delta_Q_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Mẫu số liệu đã được sắp xếp theo thứ tự không giảm và có $n = 10$ giá trị. \\\\
    Nửa số liệu bên trái gồm $5$ giá trị: $%s; %s; %s; %s; %s$, suy ra tứ phân vị thứ nhất là $Q_1 = %s$. \\\\
    Nửa số liệu bên phải gồm $5$ giá trị: $%s; %s; %s; %s; %s$, suy ra tứ phân vị thứ ba là $Q_3 = %s$. \\\\
    Vậy khoảng tứ phân vị của mẫu số liệu trên là $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$.''' % (
        str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), fmt_num(Q1_val),
        str(data[5]), str(data[6]), str(data[7]), str(data[8]), str(data[9]), fmt_num(Q3_val),
        fmt_num(Q3_val), fmt_num(Q1_val), fmt_num(delta_Q)
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
    vd_da_1_d = '\\True Phương sai của mẫu số liệu trên bằng $%s$' % (fmt_num(var_val))
    vd_da_1_s = 'Phương sai của mẫu số liệu trên bằng $%s$' % (fmt_num(var_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Số trung bình cộng của mẫu số liệu là:
    $$\\overline{x} = \\dfrac{%s}{10} = %s.$$
    Phương sai của mẫu số liệu là:
    $$s^2 = \\dfrac{1}{10}\\left[%s\\right] = %s.$$''' % (sum_str, fmt_num(mean_val), sq_diff_str, fmt_num(var_val)))
    
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
    vdc_da_1_d = '\\True Nếu mỗi học sinh trong tổ đều được cộng thêm $%s$ điểm khuyến khích thì độ lệch chuẩn của mẫu số liệu mới không thay đổi' % (str(k_add))
    vdc_da_1_s = 'Nếu mỗi học sinh trong tổ đều được cộng thêm $%s$ điểm khuyến khích thì độ lệch chuẩn của mẫu số liệu mới tăng thêm $%s$ đơn vị' % (str(k_add), str(k_add))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Khi mỗi giá trị của mẫu số liệu đều được cộng thêm $%s$ đơn vị thì số trung bình cộng của mẫu số liệu mới cũng tăng thêm $%s$ đơn vị: $\\overline{x}' = \\overline{x} + %s$. \\\\
    Do đó độ lệch của mỗi giá trị so với số trung bình cộng không thay đổi: $(x_i + %s) - (\\overline{x} + %s) = x_i - \\overline{x}$. \\\\
    Vì vậy phương sai và độ lệch chuẩn của mẫu số liệu mới không thay đổi.''' % (str(k_add), str(k_add), str(k_add), str(k_add), str(k_add)))
    
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

