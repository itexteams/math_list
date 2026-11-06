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


def bt_dang29_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số (đổi dấu chấm thành phẩy, bỏ đuôi .0)
            def fmt(val):
                if isinstance(val, (int, float)) and abs(val - round(val)) < 1e-9:
                    return str(int(round(val)))
                res = str(round(val, 1)).replace('.', ',')
                return res

            # Khai báo biến ngẫu nhiên
            t1 = random.randint(2, 4)
            v_max = random.choice([6, 8, 10])
            v_min = random.choice([2, 4])
            while v_min >= v_max:
                v_min = v_max - 2
            a = (v_max + v_min) // 2
            b = (v_max - v_min) // 2

            dt_c = random.randint(3, 5)
            t2 = t1 + dt_c
            k = random.randint(2, 4)
            t3 = t2 + k
            t4 = t3 + k

            valid_tx = [t for t in range(t2 + 1, t4) if t != t3]
            t_x = random.choice(valid_tx)

            # Tính toán các giá trị
            S1 = 0.5 * t1 * v_max
            S2 = (t2 - t1) * v_max
            S3 = a * (t4 - t2)
            S_total = S1 + S2 + S3

            S_d = S1 + S2 + a * (t_x - t2) + (b * k / math.pi) * math.sin(math.pi / k * (t_x - t2))
            S_d_rounded = round(S_d, 1)

            # Vẽ hình TikZ
            tikz = ('''\\begin{center}
            \\begin{tikzpicture}[>=latex, xscale=0.8, yscale=0.6, line width=1pt]
            \\draw[->] (-1,0) -- (%s,0) node[above] {$t$};
            \\draw[->] (0,-1) -- (0,%s) node[right] {$v$};
            \\node[below left] at (0,0) {$O$};
            \\draw[blue] (0,0) -- (%s,%s) -- (%s,%s);
            \\draw[red, domain=%s:%s, samples=100] plot (\\x, {%s + %s*cos(180/%s*(\\x - %s))});
            \\draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s);
            \\draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s);
            \\draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s);
            \\draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s);
            \\draw[dashed] (0,%s) node[left] {$%s$} -- (%s,%s);
            \\draw[dashed] (0,%s) node[left] {$%s$} -- (%s,%s);
            \\fill (0,0) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}''' % (
                t4 + 1.5, v_max + 1.5,
                t1, v_max, t2, v_max,
                t2, t4, a, b, k, t2,
                t1, t1, t1, v_max,
                t2, t2, t2, v_max,
                t3, t3, t3, v_min,
                t4, t4, t4, v_max,
                v_min, v_min, t3, v_min,
                v_max, v_max, t4, v_max,
                t1, v_max, t2, v_max, t3, v_min, t4, v_max
            ))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một vật bắt đầu chuyển động trên trục $Ox$ với đồ thị vận tốc theo thời gian $v(t)$ được mô tả như hình vẽ dưới đây. Biết rằng từ giây thứ $%s$ đến giây thứ $%s$ thì đồ thị có dạng hình sin và vận tốc của vật được biểu diễn bởi phương trình $v(t) = a + b \\cos\\left[ \\frac{\\pi}{%s}(t - %s) \\right]$.
            %s''' % (t2, t4, k, t2, tikz))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Quãng đường vật đi được trong $%s$ giây đầu tiên là $%s$ m' % (t1, fmt(S1))
            nb_da_1_s = 'Quãng đường vật đi được trong $%s$ giây đầu tiên là $%s$ m' % (t1, fmt(S1 + random.choice([1, 2, 3])))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Quãng đường đi được trong $%s$ giây đầu: $S = \\frac{1}{2} \\cdot %s \\cdot %s = %s$ m.''' % (t1, t1, v_max, fmt(S1)))

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
            th_da_1_d = '\\True Biểu thức vận tốc của vật trong khoảng thời gian $t \\in [%s;%s]$ là $v(t) = %s + %s \\cos\\left[ \\frac{\\pi}{%s}(t - %s) \\right]$' % (t2, t4, a, b, k, t2)
            th_da_1_s = 'Biểu thức vận tốc của vật trong khoảng thời gian $t \\in [%s;%s]$ là $v(t) = %s + %s \\cos\\left[ \\frac{\\pi}{%s}(t - %s) \\right]$' % (t2, t4, b, a, k, t2)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $\\begin{cases} v(%s) = %s \\\\ v(%s) = %s \\end{cases} \\Leftrightarrow \\begin{cases} a + b \\cos 0 = %s \\\\ a + b \\cos \\pi = %s \\end{cases} \\Leftrightarrow \\begin{cases} a + b = %s \\\\ a - b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$ \\\\ Suy ra $v(t) = %s + %s \\cos\\left[ \\frac{\\pi}{%s}(t - %s) \\right]$.''' % (t2, v_max, t3, v_min, v_max, v_min, v_max, v_min, a, b, a, b, k, t2))

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
            vd_da_1_d = '\\True Tổng quãng đường vật đi được trong $%s$ giây là $%s$ m' % (t4, fmt(S_total))
            vd_da_1_s = 'Tổng quãng đường vật đi được trong $%s$ giây là $%s$ m' % (t4, fmt(S_total + random.choice([2, 5, 8])))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tổng quãng đường đi được trong $%s$ giây là:\\\\ $S = %s + %s \\cdot %s + \\int_{%s}^{%s} \\left( %s + %s \\cos\\left[ \\frac{\\pi}{%s}(t - %s) \\right] \\right) \\mathrm{d}t = %s$ (m).''' % (t4, fmt(S1), v_max, (t2 - t1), t2, t4, a, b, k, t2, fmt(S_total)))

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
            vdc_da_1_d = '\\True Quãng đường vật đi được trong $%s$ giây đầu tiên là $%s$ m (Kết quả làm tròn đến hàng phần mười)' % (t_x, fmt(S_d_rounded))
            vdc_da_1_s = 'Quãng đường vật đi được trong $%s$ giây đầu tiên là $%s$ m (Kết quả làm tròn đến hàng phần mười)' % (t_x, fmt(S_d_rounded + random.choice([-1.5, 1.5, 2.5])))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Quãng đường đi được trong $%s$ giây đầu tiên là: \\\\ $S = %s + %s \\cdot %s + \\int_{%s}^{%s} \\left( %s + %s \\cos\\left[ \\frac{\\pi}{%s}(t - %s) \\right] \\right) \\mathrm{d}t \\approx %s$ (m).''' % (t_x, fmt(S1), v_max, (t2 - t1), t2, t_x, a, b, k, t2, fmt(S_d_rounded)))

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
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

