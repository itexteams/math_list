import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
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
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang11_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Hàm tìm giao điểm 2 đường thẳng a1x + b1y = c1, a2x + b2y = c2
            # Sử dụng Rational để kết quả luôn ở dạng phân số chính xác, không bị lẻ thập phân
            def solve_system(a1, b1, c1, a2, b2, c2):
                det = a1 * b2 - a2 * b1
                if det == 0:
                    return None
                x_val = Rational(c1 * b2 - c2 * b1, det)
                y_val = Rational(a1 * c2 - a2 * c1, det)
                return (x_val, y_val)

            # Random để sinh ra các hệ số sao cho miền nghiệm tạo thành một tứ giác khép kín
            while True:
                # Ta random các hệ số dựa trên mẫu
                a1 = random.randint(1, 3)
                b1 = random.randint(1, 3)
                c1 = random.randint(3, 8)

                a2 = random.randint(1, 3)
                b2 = random.randint(1, 3)
                c2 = random.randint(1, 5)

                a3 = random.randint(1, 3)
                b3 = random.randint(1, 3)
                c3 = random.randint(6, 12)

                c4 = random.randint(1, 2)

                # Các đường:
                # d1: a1*x + b1*y = c1
                # d2: a2*x - b2*y = c2
                # d3: a3*x + b3*y = c3
                # d4: x = c4

                # Giao điểm tạo thành đa giác khép kín theo thứ tự
                A = solve_system(1, 0, c4, a1, b1, c1)    # d4 & d1
                B = solve_system(a1, b1, c1, a2, -b2, c2) # d1 & d2
                C = solve_system(a2, -b2, c2, a3, b3, c3) # d2 & d3
                D = solve_system(a3, b3, c3, 1, 0, c4)    # d3 & d4

                if A and B and C and D:
                    # Điều kiện để là tứ giác: 4 đỉnh phân biệt
                    pts = [A, B, C, D]
                    if len(set(pts)) == 4:
                        # Kiểm tra xem các đỉnh có thoả mãn các BPT còn lại để là miền nghiệm bên trong không
                        condA = (a2*A[0] - b2*A[1] <= c2) and (a3*A[0] + b3*A[1] <= c3)
                        condB = (a3*B[0] + b3*B[1] <= c3) and (B[0] >= c4)
                        condC = (a1*C[0] + b1*C[1] >= c1) and (C[0] >= c4)
                        condD = (a1*D[0] + b1*D[1] >= c1) and (a2*D[0] - b2*D[1] <= c2)

                        if condA and condB and condC and condD:
                            break

            expr1 = a1*x + b1*y
            expr2 = a2*x - b2*y
            expr3 = a3*x + b3*y

            # Hàm mục tiêu F = c5*x - c6*y
            c5 = random.randint(3, 5)
            c6 = random.randint(4, 6)

            # Các đỉnh của miền nghiệm
            vertices = [A, B, C, D]
            labels = ['A', 'B', 'C', 'D']
            vertex_strs = []
            for i in range(4):
                vx, vy = vertices[i]
                vertex_strs.append(f"${labels[i]}\\left( {latex(vx)}; {latex(vy)} \\right)$")

            # Tính giá trị F tại các đỉnh
            min_F = float('inf')
            min_vx = 0
            min_vy = 0
            min_idx = -1
            for i in range(4):
                vx, vy = vertices[i]
                F_val = c5*vx - c6*vy
                if F_val < min_F:
                    min_F = F_val
                    min_vx = vx
                    min_vy = vy
                    min_idx = i

            val_vdc = min_vx**2 + min_vy**2

            # Chọn ngẫu nhiên một điểm (x0, y0) để hỏi câu thông hiểu
            while True:
                x0 = random.randint(-5, 10)
                y0 = random.randint(-5, 10)
                # Tránh điểm O để logic phong phú hơn
                if x0 != 0 or y0 != 0:
                    break

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình: $\\begin{cases} %s \\ge %s \\\\ %s \\le %s \\\\ %s \\le %s \\\\ x \\ge %s \\end{cases} \\quad (I)$.'''
                             % (latex(expr1), c1, latex(expr2), c2, latex(expr3), c3, c4))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hệ bất phương trình $(I)$ là hệ bất phương trình bậc nhất hai ẩn $x; y$'
            nb_da_1_s = 'Hệ bất phương trình $(I)$ không phải là hệ bất phương trình bậc nhất hai ẩn $x; y$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Các bất phương trình trong hệ đều là bất phương trình bậc nhất hai ẩn (hoặc một ẩn). Do đó, hệ bất phương trình $(I)$ là hệ bất phương trình bậc nhất hai ẩn $x; y$.''')

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Kiểm tra xem cặp số (x0; y0) có phải là nghiệm không
            is_sol_1 = a1*x0 + b1*y0 >= c1
            is_sol_2 = a2*x0 - b2*y0 <= c2
            is_sol_3 = a3*x0 + b3*y0 <= c3
            is_sol_4 = x0 >= c4
            is_sol = is_sol_1 and is_sol_2 and is_sol_3 and is_sol_4

            str_sol = "là" if is_sol else "không là"

            if is_sol:
                th_da_1_d = '\\True Cặp số $(x;y)=(%s;%s)$ là một nghiệm của hệ bất phương trình trên' % (x0, y0)
                th_da_1_s = 'Cặp số $(x;y)=(%s;%s)$ không là một nghiệm của hệ bất phương trình trên' % (x0, y0)
            else:
                th_da_1_d = '\\True Cặp số $(x;y)=(%s;%s)$ không là một nghiệm của hệ bất phương trình trên' % (x0, y0)
                th_da_1_s = 'Cặp số $(x;y)=(%s;%s)$ là một nghiệm của hệ bất phương trình trên' % (x0, y0)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            s1 = "\\text{đúng}" if is_sol_1 else "\\text{sai}"
            s2 = "\\text{đúng}" if is_sol_2 else "\\text{sai}"
            s3 = "\\text{đúng}" if is_sol_3 else "\\text{sai}"
            s4 = "\\text{đúng}" if is_sol_4 else "\\text{sai}"

            loigiai_th_1 = ('''Thay tọa độ $x=%s; y=%s$ vào hệ bất phương trình, ta được:\\\\
            $\\begin{cases} %s \\cdot (%s) + %s \\cdot (%s) = %s \\ge %s \\quad (%s) \\\\ %s \\cdot (%s) - %s \\cdot (%s) = %s \\le %s \\quad (%s) \\\\ %s \\cdot (%s) + %s \\cdot (%s) = %s \\le %s \\quad (%s) \\\\ %s \\ge %s \\quad (%s) \\end{cases}$\\\\
            Vậy cặp số $(x;y)=(%s;%s)$ %s một nghiệm của hệ bất phương trình trên.'''
            % (x0, y0, 
               a1, x0, b1, y0, a1*x0+b1*y0, c1, s1,
               a2, x0, b2, y0, a2*x0-b2*y0, c2, s2,
               a3, x0, b3, y0, a3*x0+b3*y0, c3, s3,
               x0, c4, s4,
               x0, y0, str_sol))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Miền nghiệm của hệ bất phương trình $(I)$ là miền tứ giác'
            vd_da_1_s = 'Miền nghiệm của hệ bất phương trình $(I)$ là miền tam giác'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Vẽ các đường thẳng $d_1: %s = %s$, $d_2: %s = %s$, $d_3: %s = %s$, $d_4: x = %s$ trên cùng một mặt phẳng tọa độ.\\\\
            Miền nghiệm của hệ bất phương trình là tứ giác $ABCD$ (kể cả biên) với các đỉnh là giao điểm của các đường thẳng:\\\\
            %s, %s, %s, %s.'''
            % (latex(expr1), c1, latex(expr2), c2, latex(expr3), c3, c4,
               vertex_strs[0], vertex_strs[1], vertex_strs[2], vertex_strs[3]))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Nếu $x=x_0; y=y_0$ là nghiệm của hệ bất phương trình sao cho $F = %sx - %sy$ đạt giá trị nhỏ nhất thì $x_0^2 + y_0^2 = %s$' % (c5, c6, latex(val_vdc))
            vdc_da_1_s = 'Nếu $x=x_0; y=y_0$ là nghiệm của hệ bất phương trình sao cho $F = %sx - %sy$ đạt giá trị nhỏ nhất thì $x_0^2 + y_0^2 = %s$' % (c5, c6, latex(val_vdc + random.randint(1, 5)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Miền nghiệm của hệ bất phương trình là tứ giác $ABCD$ với %s, %s, %s, %s.\\\\
            Ta tính giá trị của biểu thức $F(x;y) = %sx - %sy$ tại các đỉnh của tứ giác:\\\\
            $F\\left(%s;%s\\right) = %s \\cdot \\left(%s\\right) - %s \\cdot \\left(%s\\right) = %s$\\\\
            $F\\left(%s;%s\\right) = %s \\cdot \\left(%s\\right) - %s \\cdot \\left(%s\\right) = %s$\\\\
            $F\\left(%s;%s\\right) = %s \\cdot \\left(%s\\right) - %s \\cdot \\left(%s\\right) = %s$\\\\
            $F\\left(%s;%s\\right) = %s \\cdot \\left(%s\\right) - %s \\cdot \\left(%s\\right) = %s$\\\\
            Do đó, $F$ đạt giá trị nhỏ nhất bằng $%s$ tại đỉnh $%s\\left(%s;%s\\right)$.\\\\
            Suy ra $x_0 = %s; y_0 = %s \\Rightarrow x_0^2 + y_0^2 = %s$.'''
            % (vertex_strs[0], vertex_strs[1], vertex_strs[2], vertex_strs[3],
               c5, c6,
               latex(vertices[0][0]), latex(vertices[0][1]), c5, latex(vertices[0][0]), c6, latex(vertices[0][1]), latex(c5*vertices[0][0] - c6*vertices[0][1]),
               latex(vertices[1][0]), latex(vertices[1][1]), c5, latex(vertices[1][0]), c6, latex(vertices[1][1]), latex(c5*vertices[1][0] - c6*vertices[1][1]),
               latex(vertices[2][0]), latex(vertices[2][1]), c5, latex(vertices[2][0]), c6, latex(vertices[2][1]), latex(c5*vertices[2][0] - c6*vertices[2][1]),
               latex(vertices[3][0]), latex(vertices[3][1]), c5, latex(vertices[3][0]), c6, latex(vertices[3][1]), latex(c5*vertices[3][0] - c6*vertices[3][1]),
               latex(min_F), labels[min_idx], latex(min_vx), latex(min_vy),
               latex(min_vx), latex(min_vy), latex(val_vdc)))

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
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ '\n' +
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

