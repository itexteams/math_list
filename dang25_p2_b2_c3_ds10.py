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

def bt_dang25_p2_b2_c3_ds10(self):
    def format_dec(val):
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    # Random dữ liệu bảng tần số tiền lương (triệu đồng/tháng) của 15 nhân viên
    # Điều kiện giống bài mẫu:
    # - Tổng tần số = 15 (ví dụ: f1=3, f2=6, f3=3, f4=2, f5=1 => 12 nhân viên có mức lương <= s3)
    # - Mức lương s1 < s2 < s3 < s4 < s5 (với s5 là mức lương đột biến của giám đốc)
    # - Tổng lương chia hết cho 3 (để chia cho 15 được số thập phân đẹp 1 chữ số sau dấu phẩy)
    # - Mức lương trung bình mean_dec nằm giữa s3 và s4 (s3 < mean_dec < s4) để có đúng 12/15 nhân viên (80%) có lương thấp hơn mức lương trung bình
    # - Giám đốc tăng lương từ s5 lên s5_new = s5 + 15 * delta_mean (delta_mean là 1 hoặc 2 triệu đồng)
    n_total = 15
    freqs = [3, 6, 3, 2, 1]
    
    while True:
        s1 = random.randint(6, 9)
        s2 = s1 + 1
        s3 = s2 + 1
        s4 = s3 + random.randint(3, 5)
        s5 = random.randint(40, 55)
        
        tong_luong = s1 * freqs[0] + s2 * freqs[1] + s3 * freqs[2] + s4 * freqs[3] + s5 * freqs[4]
        if tong_luong % 3 == 0:
            mean_dec = Decimal(str(tong_luong)) / Decimal('15')
            if Decimal(str(s3)) < mean_dec < Decimal(str(s4)):
                delta_mean = random.choice([1, 2])
                s5_new = s5 + 15 * delta_mean
                break
    
    mean_str = format_dec(mean_dec)
    count_below_mean = freqs[0] + freqs[1] + freqs[2]  # 12
    percent_below = 80  # 12 / 15 = 80%
    
    # Dữ liệu nhiễu
    wrong_mean_str = format_dec(mean_dec + Decimal('0.4'))
    wrong_count_below = 9
    wrong_percent_below = 60
    wrong_med = s3
    wrong_delta_mean = delta_mean + 1
    
    # Bảng tần số tabular
    bang_tan_so = (
        '\\begin{center}\n'
        '\\begin{tabular}{|l|c|c|c|c|c|}\n'
        '\\hline\n'
        '\\textbf{Mức lương} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\\n'
        '\\hline\n'
        '\\textbf{Số nhân viên} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\\n'
        '\\hline\n'
        '\\end{tabular}\n'
        '\\end{center}'
    ) % (s1, s2, s3, s4, s5, freqs[0], freqs[1], freqs[2], freqs[3], freqs[4])
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Tiền lương (đơn vị: triệu đồng/tháng) của $15$ nhân viên tại một văn phòng được thống kê qua bảng tần số sau: %s Ban lãnh đạo đang cân nhắc sử dụng số trung bình, trung vị hoặc mốt để công bố mức lương đại diện của văn phòng trong thông báo tuyển dụng.''' % (bang_tan_so))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Mức lương trung bình của $15$ nhân viên là $%s$ triệu đồng/tháng' % (mean_str)
    nb_da_1_s = 'Mức lương trung bình của $15$ nhân viên là $%s$ triệu đồng/tháng' % (wrong_mean_str)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Mức lương trung bình của $15$ nhân viên là: $\\overline{x} = \\dfrac{%s \\cdot %s + %s \\cdot %s + %s \\cdot %s + %s \\cdot %s + %s \\cdot %s}{15} = \\dfrac{%s}{15} = %s$ (triệu đồng/tháng).''' % (s1, freqs[0], s2, freqs[1], s3, freqs[2], s4, freqs[3], s5, freqs[4], tong_luong, mean_str))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ######################################################################## Thông hiểu ############################################
    
    # Các đáp án
    th_da_1_d = '\\True Có tới $%s$ trên $15$ nhân viên (chiếm $%s\\%%$) có mức lương thực tế thấp hơn mức lương trung bình của văn phòng' % (count_below_mean, percent_below)
    th_da_1_s = 'Có tới $%s$ trên $15$ nhân viên (chiếm $%s\\%%$) có mức lương thực tế thấp hơn mức lương trung bình của văn phòng' % (wrong_count_below, wrong_percent_below)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Vì mức lương trung bình của văn phòng là $%s$ triệu đồng/tháng nên những nhân viên có mức lương $%s$, $%s$ và $%s$ triệu đồng/tháng đều có mức lương thấp hơn mức lương trung bình. \\\\ Số nhân viên có mức lương thực tế thấp hơn mức lương trung bình là: $%s + %s + %s = %s$ (nhân viên), chiếm tỉ lệ $\\dfrac{%s}{15} \\cdot 100\\%% = %s\\%%$.''' % (mean_str, s1, s2, s3, freqs[0], freqs[1], freqs[2], count_below_mean, count_below_mean, percent_below))
    
    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ######################################################################## Vận dụng ############################################
    
    # Các đáp án
    vd_da_1_d = '\\True Trung vị và mốt của mẫu số liệu trên bằng nhau và cùng bằng $%s$ triệu đồng/tháng' % (s2)
    vd_da_1_s = 'Trung vị và mốt của mẫu số liệu trên bằng nhau và cùng bằng $%s$ triệu đồng/tháng' % (wrong_med)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    cum_2 = freqs[0] + freqs[1]
    loigiai_vd_1 = ('''Cỡ mẫu $n = 15$ là số lẻ nên khi sắp xếp mức lương theo thứ tự không giảm, trung vị của mẫu số liệu là giá trị đứng ở vị trí thứ $\\dfrac{15 + 1}{2} = 8$. \\\\ Theo bảng tần số, có $%s$ nhân viên nhận lương $%s$ triệu đồng và $%s + %s = %s$ nhân viên nhận lương từ $%s$ đến $%s$ triệu đồng nên giá trị đứng ở vị trí thứ $8$ là $%s$, suy ra trung vị $M_e = %s$. \\\\ Mặt khác, mức lương $%s$ triệu đồng có tần số lớn nhất là $%s$ nên mốt $M_o = %s$. \\\\ Vậy trung vị và mốt của mẫu số liệu trên bằng nhau và cùng bằng $%s$ triệu đồng/tháng.''' % (freqs[0], s1, freqs[0], freqs[1], cum_2, s1, s2, s2, s2, s2, freqs[1], s2, s2))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ######################################################################## Vận dụng cao ############################################
    
    # Các đáp án
    vdc_da_1_d = '\\True Nếu giám đốc (người nhận mức lương $%s$ triệu đồng) tăng lương cho chính mình lên $%s$ triệu đồng/tháng, thì số trung bình tăng thêm $%s$ triệu đồng trong khi trung vị và mốt hoàn toàn không đổi' % (s5, s5_new, delta_mean)
    vdc_da_1_s = 'Nếu giám đốc (người nhận mức lương $%s$ triệu đồng) tăng lương cho chính mình lên $%s$ triệu đồng/tháng, thì số trung bình tăng thêm $%s$ triệu đồng trong khi trung vị và mốt hoàn toàn không đổi' % (s5, s5_new, wrong_delta_mean)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    inc_salary = s5_new - s5
    loigiai_vdc_1 = ('''Khi giám đốc tăng lương từ $%s$ lên $%s$ triệu đồng/tháng thì tổng tiền lương của cả văn phòng tăng thêm $%s - %s = %s$ (triệu đồng). \\\\ Do đó mức lương trung bình của $15$ nhân viên tăng thêm $\\dfrac{%s}{15} = %s$ (triệu đồng/tháng). \\\\ Trong khi đó, vị trí của giá trị đứng thứ $8$ (trung vị $M_e = %s$) và giá trị có tần số lớn nhất (mốt $M_o = %s$) hoàn toàn không thay đổi.''' % (s5, s5_new, s5_new, s5, inc_salary, inc_salary, delta_mean, s2, s2))
    
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
    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
    '\\choiceTFn \n'
    '{'+str(shuffled_answers_nb[0])+'}\n'
    '{'+str(shuffled_answers_th[0])+'}\n'
    '{'+str(shuffled_answers_vd[0])+'}\n'
    '{'+str(shuffled_answers_vdc[0])+'}\n'
    '\\loigiai{ \n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item '+str(shuffled_solutions_nb[0])+'\n'
    '\\item '+str(shuffled_solutions_th[0])+'\n'
    '\\item '+str(shuffled_solutions_vd[0])+'\n'
    '\\item '+str(shuffled_solutions_vdc[0])+'\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n \\end{minipage}\n\n')
    return content