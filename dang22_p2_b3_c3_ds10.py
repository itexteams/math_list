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


def bt_dang22_p2_b3_c3_ds10(self):
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
    
    # Tạo dữ liệu ngẫu nhiên gồm 8 thành tích chạy 100 m (đơn vị: giây, dùng số nguyên nhân 10 để tính chính xác)
    # Đảm bảo trung bình cộng có 1 chữ số thập phân đẹp và phương sai là số thập phân hữu hạn đẹp (tối đa 3 chữ số thập phân)
    while True:
        mean_tenths = random.randint(112, 118)
        total_tenths = 8 * mean_tenths
        
        # Tạo 7 giá trị đầu quanh mean_tenths (lệch từ -3 đến +3 phần mười giây)
        data_tenths = [mean_tenths + random.choice([-3, -2, -1, 0, 0, 1, 2, 3]) for _ in range(7)]
        last_tenths = total_tenths - sum(data_tenths)
        
        if mean_tenths - 4 <= last_tenths <= mean_tenths + 4:
            data_tenths.append(last_tenths)
            sorted_tenths = sorted(data_tenths)
            
            # Mẫu có 8 phần tử (đã sắp xếp x0..x7):
            # Nửa dưới gồm 4 phần tử đầu (index 0..3): Q1 = (x1 + x2) / 2
            # Nửa trên gồm 4 phần tử sau (index 4..7): Q3 = (x5 + x6) / 2
            Q1_val = Rational(sorted_tenths[1] + sorted_tenths[2], 20)
            Q3_val = Rational(sorted_tenths[5] + sorted_tenths[6], 20)
            delta_Q = Q3_val - Q1_val
            
            mean_val = Rational(mean_tenths, 10)
            data_rat = [Rational(v, 10) for v in data_tenths]
            sorted_rat = [Rational(v, 10) for v in sorted_tenths]
            
            var_val = sum((v - mean_val)**2 for v in data_rat) / Rational(8)
            
            # Kiểm tra điều kiện đẹp: delta_Q > 0 và mẫu số của var_val là ước của 1000
            if delta_Q > 0 and var_val > 0 and 1000 % var_val.q == 0:
                raw_rat = data_rat[:]
                random.shuffle(raw_rat)
                if raw_rat != sorted_rat:
                    break
    
    s_float = math.sqrt(float(var_val))
    low_bound = float(mean_val) - s_float
    high_bound = float(mean_val) + s_float
    
    # Đếm số vận động viên có thành tích nằm trong đoạn [mean - s; mean + s]
    count_in = sum(1 for v in sorted_rat if low_bound <= float(v) <= high_bound)
    in_vals = [fmt_num(v) for v in sorted_rat if low_bound <= float(v) <= high_bound]
    
    # Các giá trị sai cho phương án
    mean_wrong = mean_val + Rational(1, 10)
    delta_Q_wrong = delta_Q + Rational(1, 10)
    var_wrong = var_val + Rational(5, 1000)
    count_wrong = count_in + 1 if count_in < 8 else count_in - 1
    
    # Chuỗi hiển thị dãy số liệu và các biểu thức tính toán
    raw_str = '; \\quad '.join(fmt_num(v) for v in raw_rat)
    sorted_str = '; \\quad '.join(fmt_num(v) for v in sorted_rat)
    sum_str = ' + '.join(fmt_num(v) for v in raw_rat)
    sq_diff_str = ' + '.join('(%s - %s)^2' % (fmt_num(v), fmt_num(mean_val)) for v in raw_rat)
    low_str = fmt_num(round(low_bound, 3))
    high_str = fmt_num(round(high_bound, 3))
    in_vals_str = '; '.join(in_vals)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Thành tích chạy $100\\text{ m}$ (đơn vị: giây) của $8$ vận động viên trong một đợt kiểm tra là:
    \\begin{center}
    $%s$
    \\end{center}''' % (raw_str))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Thời gian chạy trung bình của $8$ vận động viên là $%s$ giây' % (fmt_num(mean_val))
    nb_da_1_s = 'Thời gian chạy trung bình của $8$ vận động viên là $%s$ giây' % (fmt_num(mean_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Thời gian chạy trung bình của $8$ vận động viên là:
    $$\\overline{x} = \\dfrac{%s}{8} = %s \\text{ (giây)}.$$''' % (
        sum_str, fmt_num(mean_val)
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
    th_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q = %s$ giây' % (fmt_num(delta_Q))
    th_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q = %s$ giây' % (fmt_num(delta_Q_wrong))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Sắp xếp mẫu số liệu theo thứ tự không giảm ta được:
    $$%s.$$
    Nửa số liệu bên trái gồm $4$ giá trị: $%s; %s; %s; %s$, suy ra tứ phân vị thứ nhất là:
    $$Q_1 = \\dfrac{%s + %s}{2} = %s.$$
    Nửa số liệu bên phải gồm $4$ giá trị: $%s; %s; %s; %s$, suy ra tứ phân vị thứ ba là:
    $$Q_3 = \\dfrac{%s + %s}{2} = %s.$$
    Vậy khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$ (giây).''' % (
        sorted_str,
        fmt_num(sorted_rat[0]), fmt_num(sorted_rat[1]), fmt_num(sorted_rat[2]), fmt_num(sorted_rat[3]),
        fmt_num(sorted_rat[1]), fmt_num(sorted_rat[2]), fmt_num(Q1_val),
        fmt_num(sorted_rat[4]), fmt_num(sorted_rat[5]), fmt_num(sorted_rat[6]), fmt_num(sorted_rat[7]),
        fmt_num(sorted_rat[5]), fmt_num(sorted_rat[6]), fmt_num(Q3_val),
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
    vd_da_1_d = '\\True Phương sai của mẫu số liệu bằng $%s$' % (fmt_num(var_val))
    vd_da_1_s = 'Phương sai của mẫu số liệu bằng $%s$' % (fmt_num(var_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Phương sai của mẫu số liệu là:
    $$s^2 = \\dfrac{1}{8}\\left[%s\\right] = %s.$$''' % (
        sq_diff_str, fmt_num(var_val)
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
    vdc_da_1_d = '\\True Có $%s$ vận động viên có thành tích chạy nằm trong đoạn $[\\overline{x} - s; \\overline{x} + s]$' % (str(count_in))
    vdc_da_1_s = 'Có $%s$ vận động viên có thành tích chạy nằm trong đoạn $[\\overline{x} - s; \\overline{x} + s]$' % (str(count_wrong))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Độ lệch chuẩn của mẫu số liệu là $s = \\sqrt{%s} \\approx %s$. \\\\
    Suy ra $[\\overline{x} - s; \\overline{x} + s] \\approx [%s; %s]$. \\\\
    Đối chiếu với mẫu số liệu đã cho, các giá trị nằm trong đoạn này là: $%s$. \\\\
    Vậy có $%s$ vận động viên có thành tích chạy nằm trong đoạn $[\\overline{x} - s; \\overline{x} + s]$.''' % (
        fmt_num(var_val), fmt_num(round(s_float, 3)),
        low_str, high_str,
        in_vals_str,
        str(count_in)
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

