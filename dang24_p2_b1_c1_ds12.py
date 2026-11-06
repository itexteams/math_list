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


def bt_dang24_p2_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thực hiện ngẫu nhiên hóa cơ số a của logarit
            a = random.choice([2, 3])
            p = 2  # Giữ nguyên p = 2 để nghiệm cực trị luôn là số hữu tỉ cực đẹp x = -1 và x = -1/3

            # Hàm số gốc: y = log_a(x^3 + 2x^2 + x + 2)
            f_expr_inside = x**3 + 2*x**2 + x + 2
            f_expr_latex = "\\log_{" + str(a) + "}\\left( x^3 + 2x^2 + x + 2 \\right)"

            # Tọa độ hai điểm cực trị A, B theo cơ số a
            y_A_val = 1 / math.log(a, 2)  # log_a(2)
            y_B_val = math.log(50.0/27.0, a)  # log_a(50/27)

            # Biểu diễn LaTeX của giá trị cực trị phục vụ hiển thị trong bảng biến thiên
            y_A_latex = "1" if a == 2 else "\\log_{3} 2"
            y_B_latex = "\\log_{2} \\frac{50}{27}" if a == 2 else "\\log_{3} \\frac{50}{27}"

            # Giá trị nhỏ nhất MA + MB = AB
            AB_val = math.sqrt(4.0/9.0 + (y_A_val - y_B_val)**2)
            AB_val_str = f"{AB_val:.2f}".replace('.', ',')

            # Xác định khoảng đúng cho mệnh đề d
            if 0.5 < AB_val < 1.0:
                vdc_interval_d = "(0,5;1)"
                vdc_interval_s = "(1;1,5)"
            else:
                vdc_interval_d = "(1;1,5)"
                vdc_interval_s = "(0,5;1)"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = %s$ có đồ thị $(C)$.''' 
                             %(f_expr_latex))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hàm số có tập xác định là $\\left( -2; +\\infty \\right)$'
            nb_da_1_s = 'Hàm số có tập xác định là $\\left( 2; +\\infty \\right)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Điều kiện xác định: $x^3 + 2x^2 + x + 2 > 0 \\Leftrightarrow (x+2)(x^2 + 1) > 0 \\Leftrightarrow x > -2$.\\\\
            Vậy hàm số có tập xác định là $\\left( -2; +\\infty \\right)$.''')

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
            # Các đáp án
            th_da_1_d = 'Hàm số đồng biến trên $\\left( -1; -\\frac{1}{3} \\right)$'
            th_da_1_s = '\\True Hàm số đồng biến trên mỗi khoảng $\\left( -2; -1 \\right)$ và $\\left( -\\frac{1}{3}; +\\infty \\right)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải chứa bảng biến thiên được gạch kín hoàn toàn vùng không xác định
            loigiai_th_1 = ('''Ta có $y\' = \\frac{3x^2 + 4x + 1}{\\left( x^3 + 2x^2 + x + 2 \\right) \\ln %s}$.\\\\
            Giải $y\' = 0 \\Leftrightarrow 3x^2 + 4x + 1 = 0 \\Leftrightarrow \\left[ \\begin{aligned} &x = -1 \\\\ &x = -\\frac{1}{3} \\end{aligned} \\right. $\\\\
            Ta có bảng biến thiên:\\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, line width=1pt]
            \\usetikzlibrary{patterns}
            \\def\\w{1.5}
            \\def\\c{2.6}
            \\draw (0,0) rectangle (\\w+4*\\c, -3.5);
            \\draw (0,-1) -- (\\w+4*\\c, -1);
            \\draw (0,-2) -- (\\w+4*\\c, -2);
            \\draw (\\w,0) -- (\\w,-3.5);
            \\node at (\\w/2, -0.5) {$x$};
            \\node at (\\w/2, -1.5) {$y\'$};
            \\node at (\\w/2, -2.75) {$y$};
            \\node at (\\w+0.25*\\c, -0.5) {$-\\infty$};
            \\node at (\\w+1*\\c, -0.5) {$-2$};
            \\node at (\\w+2*\\c, -0.5) {$-1$};
            \\node at (\\w+3*\\c, -0.5) {$-\\frac{1}{3}$};
            \\node at (\\w+3.8*\\c, -0.5) {$+\\infty$};
            \\pattern[pattern=north east lines, pattern color=black] (\\w, -1) rectangle (\\w+1*\\c, -3.5);
            \\draw (\\w+1*\\c, -1) -- (\\w+1*\\c, -3.5);
            \\draw (\\w+1*\\c+0.08, -1) -- (\\w+1*\\c+0.08, -3.5);
            \\node at (\\w+1.5*\\c, -1.5) {$+$};
            \\node at (\\w+2*\\c, -1.5) {$0$};
            \\node at (\\w+2.5*\\c, -1.5) {$-$};
            \\node at (\\w+3*\\c, -1.5) {$0$};
            \\node at (\\w+3.5*\\c, -1.5) {$+$};
            \\node (A) at (\\w+1.2*\\c, -3.1) {$-\\infty$};
            \\node (B) at (\\w+2*\\c, -2.4) {$%s$};
            \\node (C) at (\\w+3*\\c, -3.1) {$%s$};
            \\node (D) at (\\w+3.8*\\c, -2.4) {$+\\infty$};
            \\draw[->] (A) -- (B);
            \\draw[->] (B) -- (C);
            \\draw[->] (C) -- (D);
            \\end{tikzpicture}
            \\end{center}
            Suy ra hàm số đồng biến trên mỗi khoảng $\\left( -2; -1 \\right)$ và $\\left( -\\frac{1}{3}; +\\infty \\right)$.'''
                            %(latex(a), y_A_latex, y_B_latex))

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
            vd_da_1_d = '\\True Đồ thị hàm số $(C)$ có hai điểm cực trị'
            vd_da_1_s = 'Đồ thị hàm số $(C)$ không có điểm cực trị'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Từ bảng biến thiên, ta thấy đạo hàm $y\'$ đổi dấu $2$ lần khi đi qua các nghiệm $x = -1$ và $x = -\\frac{1}{3}$ thuộc tập xác định.\\\\
            Do đó, đồ thị hàm số $(C)$ có đúng hai điểm cực trị.''')

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
            vdc_da_1_d = '\\True Giả sử đồ thị hàm số $(C)$ có hai điểm cực trị là $A, B$. Một điểm $M$ thay đổi trên đường thẳng $(d): 3x + y + 1 = 0$. Giá trị nhỏ nhất của biểu thức $MA + MB$ thuộc khoảng $%s$' %(vdc_interval_d)
            vdc_da_1_s = 'Giả sử đồ thị hàm số $(C)$ có hai điểm cực trị là $A, B$. Một điểm $M$ thay đổi trên đường thẳng $(d): 3x + y + 1 = 0$. Giá trị nhỏ nhất của biểu thức $MA + MB$ thuộc khoảng $%s$' %(vdc_interval_s)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Đồ thị hàm số $(C)$ có hai điểm cực trị là $A\\left(-1; \\log_{%s} 2\\right)$, $B\\left(-\\frac{1}{3}; \\log_{%s} \\frac{50}{27}\\right)$.\\\\
            Với đường thẳng $(d): 3x + y + 1 = 0$ và $2$ điểm $A, B$, ta xét biểu thức vị trí tương đối:\\\\
            $T_A = 3 \\cdot (-1) + \\log_{%s} 2 + 1 = -2 + \\log_{%s} 2$.\\\\
            $T_B = 3 \\cdot \\left(-\\frac{1}{3}\\right) + \\log_{%s} \\frac{50}{27} + 1 = \\log_{%s} \\frac{50}{27} > 0$.\\\\
            Vì $T_A \\cdot T_B < 0$ nên hai điểm $A, B$ nằm về hai phía so với đường thẳng $(d)$.\\\\
            Do đó, với mọi điểm $M \\in (d)$, ta luôn có: $MA + MB \\ge AB$.\\\\
            Dấu bằng xảy ra khi $M$ là giao điểm của đường thẳng $AB$ và đường thẳng $(d)$.\\\\
            Khi đó: $\\min (MA + MB) = AB = \\sqrt{\\frac{4}{9} + \\left( \\log_{%s} 2 - \\log_{%s} \\frac{50}{27} \\right)^2} \\approx %s$.\\\\
            Giá trị này thuộc khoảng $%s$.'''
                             %(latex(a), latex(a), latex(a), latex(a), latex(a), latex(a), latex(a), latex(a), AB_val_str, vdc_interval_d))

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

