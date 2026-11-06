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


def bt_dang17_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng biểu thức bậc nhất ax + by
            def fmt_expr(a, b):
                res = ""
                if a == 1:
                    res += "x"
                elif a == -1:
                    res += "-x"
                elif a != 0:
                    res += "%sx" % a

                if b > 0:
                    if res != "":
                        res += " + "
                    if b == 1:
                        res += "y"
                    else:
                        res += "%sy" % b
                elif b < 0:
                    if res != "":
                        res += " - "
                    else:
                        res += "-"
                    if b == -1:
                        res += "y"
                    else:
                        res += "%sy" % (-b)
                return res

            # Khai báo biến và tạo ngẫu nhiên các hệ số
            while True:
                a1 = random.randint(1, 3)
                b1 = random.randint(1, 3)
                c1 = random.randint(3, 6)

                a2 = random.randint(1, 3)
                b2 = random.randint(1, 3)
                c2 = random.randint(4, 8)

                # Đảm bảo hai đường thẳng không trùng hoặc song song hoàn toàn
                if a1 * b2 == a2 * b1 and a1 * c2 == a2 * c1:
                    continue
                break

            expr1 = fmt_expr(a1, b1)
            expr2 = fmt_expr(a2, b2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình $\\begin{cases} %s > %s \\\\ %s > %s \\end{cases} \\quad (1)$.''' 
                            % (expr1, c1, expr2, c2))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hệ bất phương trình $(1)$ là hệ bất phương trình bậc nhất hai ẩn'
            nb_da_1_s = 'Hệ bất phương trình $(1)$ không phải là hệ bất phương trình bậc nhất hai ẩn'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Hệ bất phương trình $(1)$ gồm hai bất phương trình bậc nhất hai ẩn $x$ và $y$, do đó $(1)$ là hệ bất phương trình bậc nhất hai ẩn.''')

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
            th_da_1_d = '\\True Cặp số $(0; 0)$ không là nghiệm của bất phương trình $%s > %s$' % (expr1, c1)
            th_da_1_s = 'Cặp số $(0; 0)$ là nghiệm của bất phương trình $%s > %s$' % (expr1, c1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Thay $x = 0, y = 0$ vào bất phương trình $%s > %s$, ta được: $%s \\cdot 0 + %s \\cdot 0 = 0 > %s$ (sai). \\\\
            Do đó, cặp số $(0; 0)$ không là nghiệm của bất phương trình $%s > %s$.''' % (expr1, c1, a1, b1, c1, expr1, c1))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            x1, y1 = random.randint(2, 4), random.randint(-1, 2)
            v1 = a1 * x1 + b1 * y1
            v2 = a2 * x1 + b2 * y1
            is_sol_c = (v1 > c1) and (v2 > c2)

            if is_sol_c:
                vd_da_1_d = '\\True Cặp số $(%s; %s)$ là một nghiệm của hệ bất phương trình $(1)$' % (x1, y1)
                vd_da_1_s = 'Cặp số $(%s; %s)$ không phải là nghiệm của hệ bất phương trình $(1)$' % (x1, y1)
            else:
                vd_da_1_d = '\\True Cặp số $(%s; %s)$ không phải là nghiệm của hệ bất phương trình $(1)$' % (x1, y1)
                vd_da_1_s = 'Cặp số $(%s; %s)$ là một nghiệm của hệ bất phương trình $(1)$' % (x1, y1)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            str_c_eval1 = ">" if v1 > c1 else "\\le"
            str_c_eval2 = ">" if v2 > c2 else "\\le"
            str_c_conclusion = "là một nghiệm" if is_sol_c else "không phải là nghiệm"

            # Nội dung lời giải
            loigiai_vd_1 = ('''Thay $x = %s, y = %s$ vào từng bất phương trình trong hệ $(1)$: \\\\
            - Bất phương trình thứ nhất: $%s \\cdot (%s) + %s \\cdot (%s) = %s %s %s$. \\\\
            - Bất phương trình thứ hai: $%s \\cdot (%s) + %s \\cdot (%s) = %s %s %s$. \\\\
            Do đó, cặp số $(%s; %s)$ %s của hệ bất phương trình $(1)$.''' 
            % (x1, y1, a1, x1, b1, y1, v1, str_c_eval1, c1, a2, x1, b2, y1, v2, str_c_eval2, c2, x1, y1, str_c_conclusion))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            M = 5
            sol_list = []
            for nx in range(M):
                for ny in range(M):
                    if (a1 * nx + b1 * ny > c1) and (a2 * nx + b2 * ny > c2):
                        sol_list.append((nx, ny))

            N_sol = len(sol_list)
            N_fake = N_sol + random.choice([-2, -1, 1, 2])
            if N_fake < 0:
                N_fake = N_sol + 2

            is_d_true = random.choice([True, False])

            if is_d_true:
                vdc_da_1_d = '\\True Hệ bất phương trình $(1)$ có $%s$ nghiệm thỏa mãn $x, y$ là các số tự nhiên nhỏ hơn $%s$' % (N_sol, M)
                vdc_da_1_s = 'Hệ bất phương trình $(1)$ có $%s$ nghiệm thỏa mãn $x, y$ là các số tự nhiên nhỏ hơn $%s$' % (N_fake, M)
            else:
                vdc_da_1_d = '\\True Hệ bất phương trình $(1)$ không có $%s$ nghiệm thỏa mãn $x, y$ là các số tự nhiên nhỏ hơn $%s$' % (N_fake, M)
                vdc_da_1_s = 'Hệ bất phương trình $(1)$ có $%s$ nghiệm thỏa mãn $x, y$ là các số tự nhiên nhỏ hơn $%s$' % (N_fake, M)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            if len(sol_list) == 0:
                sol_str_detail = "Không có cặp số tự nhiên nào thỏa mãn."
            else:
                sol_str_detail = "Các cặp số $(x; y)$ thỏa mãn là: " + ", ".join(["(%s; %s)" % (p[0], p[1]) for p in sol_list]) + "."

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Vì $x, y$ là các số tự nhiên nhỏ hơn $%s$ nên $x, y \\in \\{%s\\}$. \\\\
            Thử trực tiếp các cặp số $(x; y)$ thỏa mãn cả hai bất phương trình $%s > %s$ và $%s > %s$: \\\\
            %s \\\\
            Tổng cộng có $%s$ nghiệm thỏa mãn yêu cầu bài toán.''' 
            % (M, ", ".join(str(i) for i in range(M)), expr1, c1, expr2, c2, sol_str_detail, N_sol))

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
            str(noidungcauhoi)+ '\n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

