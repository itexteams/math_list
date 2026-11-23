import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational
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


def bt_dang24_p4_b2_c3_ds10(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Cỡ mẫu N là bội của 4 (16, 20, 24, 28)
        # Gọi dãy thực tế đã sắp xếp không giảm là x_1 <= x_2 <= ... <= x_N
        # Với N = 4m:
        # - Trung vị Me = (x_{2m} + x_{2m+1}) / 2 -> để Me luôn không đổi với mọi nhiễu ở k phần tử, không có phần tử nào từ vị trí 2m trở đi bị kéo xuống dưới x_{2m} hoặc từ 2m+1 trở xuống bị đẩy lên trên x_{2m+1}, và không phần tử nào trong {x_{2m}, x_{2m+1}} bị nhiễu:
        #   Số phần tử nằm hoàn toàn bên trái x_{2m} là 2m - 1; bên phải x_{2m+1} là 2m - 1.
        #   Nếu k <= 2m - 1 (tức k <= N/2 - 1), trong trường hợp xấu nhất có k phần tử ở 1 phía bị nhiễu thì vị trí 2m và 2m+1 vẫn được giữ nguyên (hoặc khi xét đảm bảo tuyệt đối với mọi vị trí nhiễu thì tối đa k = 2m - 1 phần tử ở ngoài hai vị trí chính giữa bị nhiễu).
        #   Tương tự với Q1 = (x_m + x_{m+1}) / 2 và Q3 = (x_{3m} + x_{3m+1}) / 2:
        #   Để cả Q1 và Q3 đều không bị thay đổi trong mọi tình huống nhiễu, số điểm nhiễu k không được chạm tới các vị trí m, m+1 (bên trái còn m - 1 phần tử) và 3m, 3m+1 (bên phải còn m - 1 phần tử). Do đó số lượng giá trị bị nhiễu lớn nhất có thể là k = m - 1 = N/4 - 1.
        N = random.choice([16, 20, 24, 28])
        m = N // 4
        
        me_val = random.choice([400, 420, 450, 480, 500])
        diff_q = random.choice([3, 4, 5, 6])
        q1_val = me_val - diff_q
        q3_val = me_val + diff_q
        
        pos_me_1 = N // 2
        pos_me_2 = N // 2 + 1
        k_max_me = N // 2 - 1
        
        pos_q1_1 = m
        pos_q1_2 = m + 1
        pos_q3_1 = 3 * m
        pos_q3_2 = 3 * m + 1
        k_max_dq = m - 1
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một bộ cảm biến đo nhiệt độ lò nung mỗi phút một lần trong $%s$ phút, thu được dãy số liệu có trung vị $M_e = %s^\\circ\\text{C}$, tứ phân vị $Q_1 = %s^\\circ\\text{C}$, $Q_3 = %s^\\circ\\text{C}$. Do đường truyền tín hiệu bị nhiễu, có $k$ giá trị trong mẫu bị sai lệch hoàn toàn so với thực tế (có thể nhận giá trị âm hoặc rất lớn). Hỏi số lượng giá trị bị nhiễu $k$ lớn nhất có thể là bao nhiêu để: \\\\
    a) Trung vị $M_e$ của mẫu số liệu vẫn đảm bảo không bị thay đổi so với thực tế? \\\\
    b) Khoảng tứ phân vị $\\Delta_Q$ vẫn đảm bảo không bị ảnh hưởng bởi các điểm nhiễu?'''
                         %(N, me_val, q1_val, q3_val
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Giả sử mẫu số liệu thực tế gồm $n = %s$ giá trị được sắp xếp theo thứ tự không giảm là:
    $$x_1 \\le x_2 \\le \\dots \\le x_{%s}.$$
    \\begin{enumEX}[a)]{1}
    \\item Vì cỡ mẫu $n = %s$ là số chẵn nên trung vị của mẫu số liệu được xác định bởi hai phần tử đứng ở vị trí chính giữa là $x_{%s}$ và $x_{%s}$:
    $$M_e = \\dfrac{x_{%s} + x_{%s}}{2} = %s^\\circ\\text{C}.$$
    Khi có $k$ giá trị bị nhiễu sai lệch hoàn toàn so với thực tế (nhận giá trị âm hoặc rất lớn), chúng có thể bị đẩy về đầu bên trái hoặc đầu bên phải của dãy số liệu sau khi sắp xếp lại, làm dịch chuyển thứ tự các phần tử còn lại:
    \\begin{itemize}
    \\item Nếu các điểm nhiễu rơi vào nhóm $%s$ giá trị đầu tiên ($x_1; x_2; \\dots; x_{%s}$) hoặc nhóm $%s$ giá trị cuối cùng ($x_{%s}; \\dots; x_{%s}$) và có giá trị vượt sang phía đối diện (ví dụ các số ở đầu trái bị nhiễu thành số rất lớn chuyển sang cuối bên phải, hoặc ngược lại), thì vị trí của $x_{%s}$ và $x_{%s}$ sẽ bị dịch chuyển sang trái hoặc sang phải tối đa $k$ bậc.
    \\item Để đảm bảo trung vị $M_e$ không bị thay đổi so với thực tế (ngay cả khi các phần tử xung quanh $x_{%s}, x_{%s}$ phân biệt và các điểm nhiễu nằm ở biên làm dịch chuyển thứ tự), các điểm nhiễu không được rơi vào hai vị trí chính giữa $x_{%s}, x_{%s}$ và không được làm thay đổi hai giá trị ở vị trí thứ $%s$ và thứ $%s$. Số phần tử nằm hoàn toàn bên trái $x_{%s}$ là $%s$ phần tử (từ $x_1$ đến $x_{%s}$), và số phần tử nằm hoàn toàn bên phải $x_{%s}$ cũng là $%s$ phần tử (từ $x_{%s}$ đến $x_{%s}$).
    \\item Nếu $k \\ge %s$, chẳng hạn $k = %s$ giá trị đầu tiên $x_1; x_2; \\dots; x_{%s}$ bị nhiễu thành các số rất lớn (lớn hơn $x_{%s}$) thì sau khi sắp xếp lại, hai phần tử chính giữa mới sẽ là $x_{%s}$ và $x_{%s}$, làm trung vị thay đổi.
    \\end{itemize}
    Vậy số lượng giá trị bị nhiễu $k$ lớn nhất có thể để trung vị $M_e$ vẫn đảm bảo không bị thay đổi là $k = %s$.
    \\item Với mẫu số liệu gồm $n = %s$ phần tử:
    \\begin{itemize}
    \\item Nửa số liệu bên trái gồm $%s$ phần tử đầu tiên ($x_1; x_2; \\dots; x_{%s}$), nên tứ phân vị thứ nhất được xác định bởi hai phần tử ở vị trí thứ $%s$ và thứ $%s$:
    $$Q_1 = \\dfrac{x_{%s} + x_{%s}}{2} = %s^\\circ\\text{C}.$$
    \\item Nửa số liệu bên phải gồm $%s$ phần tử cuối cùng ($x_{%s}; \\dots; x_{%s}$), nên tứ phân vị thứ ba được xác định bởi hai phần tử ở vị trí thứ $%s$ và thứ $%s$:
    $$Q_3 = \\dfrac{x_{%s} + x_{%s}}{2} = %s^\\circ\\text{C}.$$
    \\end{itemize}
    Khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$ phụ thuộc đồng thời vào cả $Q_1$ và $Q_3$ (tức là phụ thuộc vào bốn phần tử $x_{%s}, x_{%s}, x_{%s}, x_{%s}$).
    \\begin{itemize}
    \\item Số phần tử nằm bên trái $x_{%s}$ là $%s$ phần tử ($x_1; \\dots; x_{%s}$) và số phần tử nằm bên phải $x_{%s}$ cũng là $%s$ phần tử ($x_{%s}; \\dots; x_{%s}$).
    \\item Để cả $Q_1$ và $Q_3$ đều không bị dịch chuyển khỏi vị trí thứ $%s, %s$ và thứ $%s, %s$ trong mọi trường hợp nhiễu, số điểm nhiễu $k$ không được chạm tới các vị trí này, tức là $k \\le %s$.
    \\item Nếu $k \\ge %s$, chẳng hạn $k = %s$ giá trị đầu tiên $x_1; \\dots; x_{%s}$ bị nhiễu thành các số rất lớn, thì khi sắp xếp lại dãy số liệu, các vị trí xác định $Q_1$ và $Q_3$ sẽ bị đẩy sang phải thành $x_{%s}, x_{%s}$ và $x_{%s}, x_{%s}$, làm thay đổi giá trị của $Q_1, Q_3$ và kéo theo $\\Delta_Q$ bị ảnh hưởng.
    \\end{itemize}
    Vậy số lượng giá trị bị nhiễu $k$ lớn nhất có thể để khoảng tứ phân vị $\\Delta_Q$ vẫn đảm bảo không bị ảnh hưởng là $k = %s$.
    \\end{enumEX}'''
                   %(N, N,
                     N, pos_me_1, pos_me_2, pos_me_1, pos_me_2, me_val,
                     k_max_me, k_max_me, k_max_me, pos_me_2 + 1, N, pos_me_1, pos_me_2,
                     pos_me_1, pos_me_2, pos_me_1, pos_me_2, pos_me_1, pos_me_2, pos_me_1, k_max_me, k_max_me, pos_me_2, k_max_me, pos_me_2 + 1, N,
                     k_max_me + 1, k_max_me + 1, k_max_me + 1, N, pos_me_1 + k_max_me + 1, pos_me_2 + k_max_me + 1,
                     k_max_me,
                     N,
                     N // 2, N // 2, pos_q1_1, pos_q1_2, pos_q1_1, pos_q1_2, q1_val,
                     N // 2, N // 2 + 1, N, pos_q3_1, pos_q3_2, pos_q3_1, pos_q3_2, q3_val,
                     pos_q1_1, pos_q1_2, pos_q3_1, pos_q3_2,
                     pos_q1_1, k_max_dq, k_max_dq, pos_q3_2, k_max_dq, pos_q3_2 + 1, N,
                     pos_q1_1, pos_q1_2, pos_q3_1, pos_q3_2, k_max_dq,
                     k_max_dq + 1, k_max_dq + 1, k_max_dq + 1, pos_q1_1 + k_max_dq + 1, pos_q1_2 + k_max_dq + 1, pos_q3_1 + k_max_dq + 1, pos_q3_2 + k_max_dq + 1,
                     k_max_dq
                   ))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

