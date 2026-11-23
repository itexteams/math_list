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

def bt_dang24_p2_b2_c3_ds10(self):
    def format_dec(val):
        s = str(val).rstrip('0').rstrip('.')
        if s == '':
            s = '0'
        return s.replace('.', ',')
    
    def format_list_num(lst):
        return '; '.join('$' + str(v) + '$' for v in lst)
    
    # Random 9 số nguyên dương tăng dần: x1 < x2 < x3 < x4 < x5 < x6 < x7 < x8 < x9
    # Điều kiện giống bài mẫu:
    # - Tổng 9 số chia hết cho 9 => số trung bình mean_val nguyên
    # - Tổng (x1 + x9) > 2 * mean_val sao cho khi xóa x1 và x9 thì số trung bình mới giảm một lượng thập phân đẹp (chia hết cho 0,25)
    # - x6 - x5 >= 2 để khi bổ sung m >= x6, trung vị mới của 10 số là (x5 + x6)/2 đẹp và m có thể nhận giá trị > x6
    # - Khi thêm hai số bằng nhau k (k thuộc N) để mẫu 11 số có số trung bình bằng đúng trung vị mới và cùng bằng x5:
    #   Tổng 11 số = 11 * x5 => 2k = 11 * x5 - sum_9. Chọn 11 * x5 - sum_9 là số lẻ dương (k = ... ,5 không thuộc N)
    while True:
        x5 = random.randint(14, 20)
        x4 = x5 - random.randint(1, 2)
        x3 = x4 - random.randint(1, 2)
        x2 = x3 - random.randint(2, 3)
        x1 = x2 - random.randint(2, 3)
        
        x6 = x5 + random.randint(2, 3)
        x7 = x6 + random.randint(2, 3)
        x8 = x7 + random.randint(2, 3)
        x9 = x8 + random.randint(3, 5)
        
        data = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
        sum_9 = sum(data)
        
        if x1 >= 4 and sum_9 % 9 == 0:
            mean_val = sum_9 // 9
            sum_7 = sum_9 - x1 - x9
            # Kiểm tra hiệu số trung bình giảm đi (mean_val - sum_7/7) đẹp (ví dụ bội của 0.25)
            diff_num = 7 * mean_val - sum_7
            if diff_num > 0 and (diff_num * 4) % 7 == 0:
                # Kiểm tra điều kiện câu d: 2k = 11 * x5 - sum_9 lẻ dương
                two_k = 11 * x5 - sum_9
                if two_k > 0 and two_k % 2 == 1:
                    break
    
    med_val = x5
    new_mean_7_dec = Decimal(str(sum_7)) / Decimal('7')
    diff_mean_dec = Decimal(str(mean_val)) - new_mean_7_dec
    new_mean_7_str = format_dec(new_mean_7_dec)
    diff_mean_str = format_dec(diff_mean_dec)
    
    # Trung vị mới của 10 số khi thêm m >= x6 là (x5 + x6)/2
    med_10_dec = Decimal(str(x5 + x6)) / Decimal('2')
    med_10_str = format_dec(med_10_dec)
    m_example = x6 + 1
    
    # Giá trị k ở câu d
    k_dec = Decimal(str(two_k)) / Decimal('2')
    k_str = format_dec(k_dec)
    
    # Chuỗi hiển thị mẫu số liệu
    str_data = format_list_num(data)
    
    # Dữ liệu nhiễu
    wrong_mean_val = mean_val + random.choice([-1, 1])
    wrong_diff_mean_str = format_dec(diff_mean_dec + Decimal('0.25'))
    wrong_m_example = x5 - 1
    wrong_k_str = format_dec(k_dec + Decimal('1'))
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho mẫu số liệu gồm $9$ số thực đã sắp xếp không giảm: %s.''' % (str_data))
    
    ######################################################################## Nhận biết ############################################
    
    # Các đáp án
    nb_da_1_d = '\\True Số trung bình và trung vị của mẫu số liệu ban đầu lần lượt là $%s$ và $%s$' % (mean_val, med_val)
    nb_da_1_s = 'Số trung bình và trung vị của mẫu số liệu ban đầu lần lượt là $%s$ và $%s$' % (wrong_mean_val, med_val)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    tong_bieu_thuc = ' + '.join(str(v) for v in data)
    loigiai_nb_1 = ('''Số trung bình của mẫu số liệu ban đầu là: $\\overline{x} = \\dfrac{%s}{9} = \\dfrac{%s}{9} = %s$. \\\\ Vì cỡ mẫu $n = 9$ là số lẻ và mẫu đã sắp xếp theo thứ tự không giảm nên trung vị là số đứng ở vị trí thứ $\\dfrac{9 + 1}{2} = 5$, tức là $M_e = %s$.''' % (tong_bieu_thuc, sum_9, mean_val, med_val))
    
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
    th_da_1_d = '\\True Nếu xóa đi đồng thời giá trị nhỏ nhất ($%s$) và giá trị lớn nhất ($%s$) thì trung vị của mẫu số liệu mới không thay đổi, còn số trung bình giảm đi $%s$' % (x1, x9, diff_mean_str)
    th_da_1_s = 'Nếu xóa đi đồng thời giá trị nhỏ nhất ($%s$) và giá trị lớn nhất ($%s$) thì trung vị của mẫu số liệu mới không thay đổi, còn số trung bình giảm đi $%s$' % (x1, x9, wrong_diff_mean_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    data_7 = data[1:8]
    str_data_7 = format_list_num(data_7)
    loigiai_th_1 = ('''Khi xóa đi giá trị nhỏ nhất ($%s$) và giá trị lớn nhất ($%s$), mẫu số liệu mới gồm $7$ số là: %s. \\\\ Trung vị mới là số đứng ở vị trí thứ $\\dfrac{7 + 1}{2} = 4$, vẫn bằng $%s$ (không thay đổi). \\\\ Số trung bình mới là $\\overline{x}_{\\text{mới}} = \\dfrac{%s - %s - %s}{7} = \\dfrac{%s}{7} = %s$. \\\\ Vậy số trung bình giảm đi là $%s - %s = %s$.''' % (x1, x9, str_data_7, med_val, sum_9, x1, x9, sum_7, new_mean_7_str, mean_val, new_mean_7_str, diff_mean_str))
    
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
    vd_da_1_d = '\\True Nếu bổ sung thêm một giá trị $m$ vào mẫu số liệu ban đầu để được mẫu mới gồm $10$ số có trung vị bằng $%s$ thì $m$ có thể nhận giá trị là $%s$' % (med_10_str, m_example)
    vd_da_1_s = 'Nếu bổ sung thêm một giá trị $m$ vào mẫu số liệu ban đầu để được mẫu mới gồm $10$ số có trung vị bằng $%s$ thì $m$ có thể nhận giá trị là $%s$' % (med_10_str, wrong_m_example)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Khi bổ sung thêm một giá trị $m$ vào mẫu số liệu ban đầu, mẫu mới có cỡ mẫu $n = 10$ là số chẵn nên trung vị mới là trung bình cộng của hai giá trị đứng ở vị trí thứ $5$ và thứ $6$ sau khi sắp xếp không giảm. \\\\ Nếu $m \\ge %s$ thì trong dãy đã sắp xếp, $5$ số đầu tiên vẫn là $%s; %s; %s; %s; %s$ và số thứ $6$ là $%s$, khi đó trung vị mới là $\\dfrac{%s + %s}{2} = %s$. \\\\ Do đó mọi giá trị $m \\ge %s$ đều thỏa mãn, đặc biệt $m$ có thể nhận giá trị là $%s$.''' % (x6, x1, x2, x3, x4, x5, x6, x5, x6, med_10_str, x6, m_example))
    
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
    vdc_da_1_d = '\\True Nếu bổ sung thêm vào mẫu số liệu ban đầu hai giá trị bằng nhau là $k$ ($k \\in \\mathbb{N}$) sao cho mẫu mới gồm $11$ số có số trung bình bằng đúng trung vị mới và cùng bằng $%s$, thì $k = %s$ (không tồn tại số tự nhiên $k$ thỏa mãn)' % (med_val, k_str)
    vdc_da_1_s = 'Nếu bổ sung thêm vào mẫu số liệu ban đầu hai giá trị bằng nhau là $k$ ($k \\in \\mathbb{N}$) sao cho mẫu mới gồm $11$ số có số trung bình bằng đúng trung vị mới và cùng bằng $%s$, thì tồn tại số tự nhiên $k = %s$ thỏa mãn' % (med_val, wrong_k_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    sum_11_target = 11 * med_val
    loigiai_vdc_1 = ('''Khi bổ sung thêm hai giá trị bằng $k$ vào mẫu số liệu ban đầu, mẫu mới có $11$ số với tổng là $%s + 2k$. \\\\ Để số trung bình của mẫu mới bằng $%s$ thì ta phải có: $\\dfrac{%s + 2k}{11} = %s \\Leftrightarrow %s + 2k = %s \\Leftrightarrow 2k = %s \\Leftrightarrow k = %s$. \\\\ Vì $%s \\notin \\mathbb{N}$ nên không tồn tại số tự nhiên $k$ thỏa mãn yêu cầu bài toán.''' % (sum_9, med_val, sum_9, med_val, sum_9, sum_11_target, two_k, k_str, k_str))
    
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