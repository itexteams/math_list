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


def bt_dang20_p2_b3_c3_ds10(self):
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
    
    # Tạo dữ liệu ngẫu nhiên gồm 7 ngày nhiệt độ trung bình (độ C)
    # Đảm bảo trung bình cộng là số nguyên đẹp và có giá trị nằm ngoài khoảng (x_mean - s; x_mean + s)
    while True:
        mean_val = random.randint(23, 28)
        total_target = 7 * mean_val
        
        data = [random.randint(mean_val - 2, mean_val + 2) for _ in range(6)]
        last_val = total_target - sum(data)
        
        if mean_val - 3 <= last_val <= mean_val + 3:
            data.append(last_val)
            R_val = max(data) - min(data)
            var_val = sum((x_i - Rational(mean_val))**2 for x_i in data) / Rational(7)
            s_float = math.sqrt(float(var_val))
            low_bound = mean_val - s_float
            high_bound = mean_val + s_float
            
            # Kiểm tra có giá trị nằm ngoài khoảng (x_mean - s; x_mean + s)
            outside_vals = [v for v in data if not (low_bound < v < high_bound)]
            if R_val >= 3 and var_val > 0 and len(outside_vals) >= 1:
                random.shuffle(data)
                break
    
    # Giá trị sai cho các phương án
    R_wrong = R_val + random.choice([-1, 1])
    var_wrong = var_val + Rational(2, 7)
    
    # Chuỗi hiển thị dãy số liệu và các biểu thức
    data_str = '; \\quad '.join(str(v) for v in data)
    sum_str = ' + '.join(str(v) for v in data)
    sq_diff_str = ' + '.join('(%s - %s)^2' % (str(v), str(mean_val)) for v in data)
    low_str = fmt_num(round(low_bound, 2))
    high_str = fmt_num(round(high_bound, 2))
    outside_str = ', '.join(str(v) for v in sorted(set(outside_vals)))
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Nhiệt độ trung bình ngày (đơn vị: $^{\\circ}\\text{C}$) tại một địa phương trong $7$ ngày của một tuần được ghi nhận là:
    \\begin{center}
    $%s$
    \\end{center}''' % (data_str))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Khoảng biến thiên của nhiệt độ trong tuần là $%s^{\\circ}\\text{C}$' % (str(R_val))
    nb_da_1_s = 'Khoảng biến thiên của nhiệt độ trong tuần là $%s^{\\circ}\\text{C}$' % (str(R_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Nhiệt độ cao nhất trong tuần là $%s^{\\circ}\\text{C}$ và nhiệt độ thấp nhất trong tuần là $%s^{\\circ}\\text{C}$. \\\\
    Vậy khoảng biến thiên của nhiệt độ trong tuần là $R = %s - %s = %s^{\\circ}\\text{C}$.''' % (
        str(max(data)), str(min(data)), str(max(data)), str(min(data)), str(R_val)
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
    th_da_1_d = '\\True Phương sai của mẫu số liệu trên là $%s$' % (latex(var_val))
    th_da_1_s = 'Phương sai của mẫu số liệu trên là $%s$' % (latex(var_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Nhiệt độ trung bình của $7$ ngày trong tuần là:
    $$\\overline{x} = \\dfrac{%s}{7} = %s \\text{ } (^{\\circ}\\text{C}).$$
    Phương sai của mẫu số liệu trên là:
    $$s^2 = \\dfrac{1}{7}\\left[%s\\right] = %s.$$''' % (
        sum_str, str(mean_val), sq_diff_str, latex(var_val)
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
    vd_da_1_d = '\\True Nếu chuyển đổi toàn bộ số liệu trên sang độ Fahrenheit theo công thức $F = 1,8C + 32$ thì độ lệch chuẩn của mẫu số liệu mới bằng $1,8 \\cdot \\sqrt{%s}$' % (latex(var_val))
    vd_da_1_s = 'Nếu chuyển đổi toàn bộ số liệu trên sang độ Fahrenheit theo công thức $F = 1,8C + 32$ thì độ lệch chuẩn của mẫu số liệu mới bằng $1,8 \\cdot \\sqrt{%s} + 32$' % (latex(var_val))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Độ lệch chuẩn của mẫu số liệu ban đầu là $s_C = \\sqrt{s^2} = \\sqrt{%s}$. \\\\
    Khi biến đổi tuyến tính $F = 1,8C + 32$, độ lệch chuẩn của mẫu số liệu mới là:
    $$s_F = |1,8| \\cdot s_C = 1,8 \\cdot \\sqrt{%s}.$$''' % (
        latex(var_val), latex(var_val)
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
    vdc_da_1_d = '\\True Không phải tất cả các ngày trong tuần đều có nhiệt độ nằm trong khoảng $(\\overline{x} - s; \\overline{x} + s)$'
    vdc_da_1_s = 'Tất cả các ngày trong tuần đều có nhiệt độ nằm trong khoảng $(\\overline{x} - s; \\overline{x} + s)$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có $\\overline{x} = %s$ và $s = \\sqrt{%s} \\approx %s$, suy ra:
    $$(\\overline{x} - s; \\overline{x} + s) \\approx (%s; %s).$$
    Trong mẫu số liệu trên, giá trị $%s$ không thuộc khoảng $(%s; %s)$ nên không phải tất cả các ngày trong tuần đều có nhiệt độ nằm trong khoảng $(\\overline{x} - s; \\overline{x} + s)$.''' % (
        str(mean_val), latex(var_val), fmt_num(round(s_float, 2)),
        low_str, high_str,
        outside_str, low_str, high_str
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

