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


def bt_dang9_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các số trong bài toán để tạo ra nhiều câu hỏi khác nhau (a cố định bằng 1)
            while True:
                c = random.choice([1, 2, 3])
                b = random.choice([-3, -2, -1, 1, 2, 3])
                if b != c and b != 0:
                    break
            a = 1

            # Các tham số tiệm cận và tâm đối xứng phục vụ hình vẽ và lời giải
            x0 = -c
            y0 = -c + b

            # Hàm hỗ trợ hiển thị dấu của hệ số trong chuỗi chuẫn LaTeX
            def sign(val):
                return f"+{val}" if val > 0 else f"{val}"

            def format_minus(val):
                return f"+ {abs(val)}" if val < 0 else (f"- {val}" if val > 0 else "")

            b_str = sign(b)
            c_str = sign(c)
            minus_y0_str = format_minus(y0)

            # Phần điều chỉnh hình vẽ TikZ mở rộng không gian phía dưới để không bị thiếu hình
            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.7]
            \\clip (-6,-8) rectangle (5,5);
            \\draw[->] (-5.5,0) -- (4.5,0) node[below]{$x$};
            \\draw[->] (0,-7.5) -- (0,4.5) node[right]{$y$};
            \\draw[fill=black] (0,0) circle (1.5pt) node[below right]{$O$};
            \\draw[dashed] (%s,-8) -- (%s,5);
            \\draw[dashed, domain=-6:5] plot(\\x, {\\x%s});
            \\draw[blue, line width=1pt, domain=-6:%s, samples=100] plot(\\x, {\\x%s - 1/(\\x+%s)});
            \\draw[blue, line width=1pt, domain=%s:4.5, samples=100] plot(\\x, {\\x%s - 1/(\\x+%s)});
            \\draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
            \\draw[fill=black] (%s,%s) circle (1.5pt);
            \\node[above left] at (%s,0) {$%s$};
            \\node[left] at (0,%s) {$%s$};
            \\draw[fill=black] (0,%s) circle (1.5pt);
            \\node[above left] at (0,%s) {$%s$};
            \\end{tikzpicture}
            \\end{center}''' % (
                x0, x0,
                b_str,
                x0 - 0.05, b_str, c,
                x0 + 0.05, b_str, c,
                x0, x0, y0, y0,
                x0, y0,
                x0, x0,
                y0, y0,
                b,
                b, b
            ))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = ax+b - \\frac{1}{x+c}$ có đồ thị như hình vẽ: %s''' % (tikz_code))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đồ thị hàm số nhận đường $x = %s$ làm tiệm cận đứng và đường $y = x %s$ làm tiệm cận xiên' % (x0, b_str)
            nb_da_1_s = 'Đồ thị hàm số nhận đường $x = %s$ làm tiệm cận đứng và đường $y = -x %s$ làm tiệm cận xiên' % (x0, b_str)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Từ đồ thị ta có tiệm cận đứng là đường thẳng $x = %s$. \\\\
            Tiệm cận xiên $y=ax+b$ đi qua $A(%s; %s)$ và $B(0; %s) \\Rightarrow$ phương trình tiệm cận xiên là $y = x %s$.''' % (x0, x0, y0, b, b_str))

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
            th_da_1_d = '\\True Tâm đối xứng của đồ thị hàm số là $I(%s; %s)$' % (x0, y0)
            th_da_1_s = 'Tâm đối xứng của đồ thị hàm số là $I(%s; %s)$' % (y0, x0)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Tâm đối xứng là giao giữa hai đường tiệm cận đứng và tiệm cận xiên nên tọa độ tâm đối xứng là $I(%s; %s)$.''' % (x0, y0))

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
            sum_abc = 1 + b + c
            wrong_sum = 1 + b - c
            vd_da_1_d = '\\True $a+b+c = %s$' % (sum_abc)
            vd_da_1_s = '$a+b+c = %s$' % (wrong_sum)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tiệm cận đứng là đường thẳng $x = %s \\Rightarrow x %s = 0 \\Rightarrow c = %s$. \\\\
            Tiệm cận xiên $y = x %s \\Rightarrow a = 1; b = %s$. \\\\
            Suy ra $y = x %s - \\frac{1}{x %s}$, suy ra $a+b+c = 1 + (%s) + (%s) = %s$.''' % (x0, sign(c), c, b_str, b, b_str, sign(c), b, c, sum_abc))

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
            vdc_da_1_d = '\\True Gọi $M$ là một điểm bất kỳ thuộc đồ thị hàm số thì giá trị nhỏ nhất của $IM$ bằng $\\sqrt{2\\sqrt{2}-2}$'
            vdc_da_1_s = 'Gọi $M$ là một điểm bất kỳ thuộc đồ thị hàm số thì giá trị nhỏ nhất của $IM$ bằng $2(\\sqrt{2}-1)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải (Sử dụng dấu phẩy cho số thập phân theo quy định)
            x_val_str = f"{0.8409 - c:.4f}".replace('.', ',')

            loigiai_vdc_1 = ('''Độ dài $IM = \\sqrt{ (x %s)^2 + \\left[ \\left( x %s - \\frac{1}{x %s} \\right) %s \\right]^2 }$. \\\\
            $\\left. \\frac{d}{dx} \\left( \\sqrt{ (x %s)^2 + \\left[ \\left( x %s - \\frac{1}{x %s} \\right) %s \\right]^2 } \\right) \\right|_{x=x} \\xrightarrow{Shift+Solve} x = %s \\to Sto A$. \\\\
            Suy ra $IM = \\sqrt{ (A %s)^2 + \\left[ \\left( A %s - \\frac{1}{A %s} \\right) %s \\right]^2 } \\approx 0,9101 \\neq 2(\\sqrt{2}-1)$.''' % (
                sign(c), b_str, sign(c), minus_y0_str,
                sign(c), b_str, sign(c), minus_y0_str, x_val_str,
                sign(c), b_str, sign(c), minus_y0_str
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

