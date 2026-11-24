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
from decimal import Decimal, ROUND_HALF_UP


def bt_dang15_p2_b3_c3_ds10(self):
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
    
    def round_2_dec(val_float):
        d = Decimal(str(val_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return str(d).replace('.', ',')
    
    # Tạo dữ liệu ngẫu nhiên gồm 12 thời gian sử dụng bóng đèn LED (đã sắp xếp không giảm)
    # Trong đó phần tử cuối cùng là giá trị bất thường lớn hơn Q3 + 1.5 * Delta_Q
    while True:
        start_val = random.randint(110, 118) * 10
        data = [start_val]
        for _ in range(10):
            step = random.choice([0, 10, 10, 20, 30])
            data.append(data[-1] + step)
        
        # Tính tứ phân vị cho mẫu 12 phần tử (nửa dưới 6 phần tử đầu, nửa trên 6 phần tử sau)
        # Q1 là trung bình cộng của data[2] và data[3]
        # Q3 là trung bình cộng của data[8] và data[9]
        Q1_val = Rational(data[2] + data[3], 2)
        Q3_val = Rational(data[8] + data[9], 2)
        delta_Q = Q3_val - Q1_val
        
        if delta_Q >= 40:
            upper_fence = Q3_val + Rational(3, 2) * delta_Q
            lower_fence = Q1_val - Rational(3, 2) * delta_Q
            # Đảm bảo 11 phần tử đầu không có giá trị bất thường
            if data[0] >= lower_fence and data[10] <= upper_fence:
                # Tạo phần tử thứ 12 là giá trị bất thường lớn hơn ngưỡng trên
                outlier_min = int(math.floor(float(upper_fence) / 10.0) + 2) * 10
                outlier_val = outlier_min + random.randint(1, 5) * 10
                data.append(outlier_val)
                break
    
    # Các đại lượng thống kê của mẫu số liệu
    mean_val = Rational(sum(data), 12)
    var_val = sum((x_i - mean_val)**2 for x_i in data) / Rational(12)
    std_float = math.sqrt(float(var_val))
    std_str = round_2_dec(std_float)
    
    # Giá trị sai cho độ lệch chuẩn (lệch một lượng nhỏ)
    std_wrong_float = std_float + random.choice([-2.15, 2.35, 3.12])
    std_wrong_str = round_2_dec(std_wrong_float)
    
    # Khoảng biến thiên ban đầu và sau khi loại bỏ giá trị lớn nhất
    R_old = data[-1] - data[0]
    R_new = data[-2] - data[0]
    R_diff = R_old - R_new
    R_diff_wrong = R_diff + random.choice([-20, 20, 30])
    
    # Giá trị sai cho khoảng tứ phân vị
    delta_Q_wrong = delta_Q + random.choice([-10, 10, 20])
    
    # Chuỗi hiển thị dãy số liệu và các biểu thức tính toán
    data_str = '; \\quad '.join(str(v) for v in data)
    sum_str = ' + '.join(str(v) for v in data)
    mean_tex = latex(mean_val) if mean_val.q != 1 else str(mean_val.p)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Thời gian sử dụng (tính theo giờ) của một lô $12$ bóng đèn LED được kiểm tra và cho kết quả:
    \\begin{center}
    $%s$
    \\end{center}''' % (data_str))
    
    ######################################################################## Nhận biết ###########################################
    
    # Các đáp án
    nb_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu trên là $\\Delta_Q = %s$' % (fmt_num(delta_Q))
    nb_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu trên là $\\Delta_Q = %s$' % (fmt_num(delta_Q_wrong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Mẫu số liệu đã được sắp xếp theo thứ tự không giảm và có $n = 12$ giá trị. \\\\
    Nửa số liệu bên trái gồm $6$ giá trị: $%s; %s; %s; %s; %s; %s$, suy ra tứ phân vị thứ nhất là $Q_1 = \\dfrac{%s + %s}{2} = %s$. \\\\
    Nửa số liệu bên phải gồm $6$ giá trị: $%s; %s; %s; %s; %s; %s$, suy ra tứ phân vị thứ ba là $Q_3 = \\dfrac{%s + %s}{2} = %s$. \\\\
    Vậy khoảng tứ phân vị của mẫu số liệu trên là $\\Delta_Q = Q_3 - Q_1 = %s - %s = %s$.''' % (
        str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
        str(data[2]), str(data[3]), fmt_num(Q1_val),
        str(data[6]), str(data[7]), str(data[8]), str(data[9]), str(data[10]), str(data[11]),
        str(data[8]), str(data[9]), fmt_num(Q3_val),
        fmt_num(Q3_val), fmt_num(Q1_val), fmt_num(delta_Q)
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
    th_da_1_d = '\\True Mẫu số liệu trên có đúng một giá trị bất thường là $%s$' % (str(outlier_val))
    th_da_1_s = 'Mẫu số liệu trên không có giá trị bất thường nào'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Ta có:
    $$Q_1 - 1,5 \\cdot \\Delta_Q = %s - 1,5 \\cdot %s = %s;$$
    $$Q_3 + 1,5 \\cdot \\Delta_Q = %s + 1,5 \\cdot %s = %s.$$
    Trong mẫu số liệu trên, giá trị $%s > %s$ nên $%s$ là giá trị bất thường của mẫu số liệu.''' % (
        fmt_num(Q1_val), fmt_num(delta_Q), fmt_num(lower_fence),
        fmt_num(Q3_val), fmt_num(delta_Q), fmt_num(upper_fence),
        str(outlier_val), fmt_num(upper_fence), str(outlier_val)
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
    vd_da_1_d = '\\True Nếu loại bỏ giá trị $%s$ khỏi mẫu số liệu thì khoảng biến thiên giảm đi $%s$ giờ' % (str(outlier_val), str(R_diff))
    vd_da_1_s = 'Nếu loại bỏ giá trị $%s$ khỏi mẫu số liệu thì khoảng biến thiên giảm đi $%s$ giờ' % (str(outlier_val), str(R_diff_wrong))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Khoảng biến thiên của mẫu số liệu ban đầu là $R = %s - %s = %s$ (giờ). \\\\
    Khi loại bỏ giá trị $%s$, mẫu số liệu mới có giá trị lớn nhất là $%s$ và giá trị nhỏ nhất là $%s$, nên khoảng biến thiên mới là $R' = %s - %s = %s$ (giờ). \\\\
    Vậy khoảng biến thiên giảm đi $%s - %s = %s$ (giờ).''' % (
        str(data[-1]), str(data[0]), str(R_old),
        str(outlier_val), str(data[-2]), str(data[0]), str(data[-2]), str(data[0]), str(R_new),
        str(R_old), str(R_new), str(R_diff)
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
    vdc_da_1_d = '\\True Độ lệch chuẩn của mẫu số liệu ban đầu xấp xỉ $%s$ giờ (làm tròn đến hàng phần trăm)' % (std_str)
    vdc_da_1_s = 'Độ lệch chuẩn của mẫu số liệu ban đầu xấp xỉ $%s$ giờ (làm tròn đến hàng phần trăm)' % (std_wrong_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Số trung bình cộng của mẫu số liệu ban đầu là:
    $$\\overline{x} = \\dfrac{%s}{12} = %s.$$
    Phương sai của mẫu số liệu ban đầu là:
    $$s^2 = \\dfrac{1}{12}\\sum_{i=1}^{12} (x_i - \\overline{x})^2 = %s.$$
    Độ lệch chuẩn của mẫu số liệu ban đầu là:
    $$s = \\sqrt{s^2} = \\sqrt{%s} \\approx %s \\text{ (giờ)}.$$''' % (
        sum_str, mean_tex, latex(var_val), latex(var_val), std_str
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

