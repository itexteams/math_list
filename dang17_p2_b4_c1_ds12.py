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


def bt_dang17_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Các số liệu được fix cứng do yêu cầu chỉ random số trong câu hỏi, không random hình
            a_val = -1
            b_val = 0
            c_val = 3
            d_val = 0

            tikz_graph = '''\\begin{center}
            \\begin{tikzpicture}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.8]
            \\draw[->] (-2.5,0) -- (3,0) node[below] {$x$};
            \\draw[->] (0,-3) -- (0,3) node[left] {$y$};
            \\node[below left] at (0,0) {$O$};
            \\foreach \\x in {-2,-1,1,2} \\draw (\\x,0.05) -- (\\x,-0.05);
            \\foreach \\y in {-2,-1,1,2} \\draw (0.05,\\y) -- (-0.05,\\y);
            \\node[above left] at (-0.9,0) {$-1$};
            \\node[below right] at (0.9,0) {$1$};
            \\node[left] at (0,2) {$2$};
            \\node[right] at (0,-2) {$-2$};
            \\draw[line width=1pt, domain=-2.1:2.1, samples=100] plot (\\x, {-\\x*\\x*\\x + 3*\\x});
            \\draw[dashed] (-1,0) -- (-1,-2) -- (0,-2);
            \\draw[dashed] (1,0) -- (1,2) -- (0,2);
            \\fill (-1,-2) circle (1.5pt);
            \\fill (1,2) circle (1.5pt);
            \\fill (0,0) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}'''

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=f(x)=ax^3+bx^2+cx+d$ với $(a,b,c,d \\in \\mathbb{R})$ có tập xác định trên $\\mathbb{R}$ và có đồ thị như hình vẽ dưới đây.
            %s''' % (tikz_graph))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            num_cuc_tri = 2
            num_cuc_tri_sai = random.choice([1, 3, 4])
            nb_da_1_d = '\\True Đồ thị hàm số đã cho có $2$ điểm cực trị'
            nb_da_1_s = 'Đồ thị hàm số đã cho có $%s$ điểm cực trị' % num_cuc_tri_sai

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Dựa vào đồ thị, hàm số có một điểm cực đại và một điểm cực tiểu nên đồ thị hàm số có $2$ điểm cực trị.''')

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
            th_da_1_d = '\\True Hàm số đã cho đồng biến trên khoảng $\\left(-1; 1\\right)$'
            th_da_1_s = 'Hàm số đã cho nghịch biến trên khoảng $\\left(-1; 1\\right)$'

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Dựa vào đồ thị, trên khoảng $\\left(-1; 1\\right)$ đồ thị hàm số đi lên từ trái sang phải nên hàm số đồng biến trên khoảng $\\left(-1; 1\\right)$.''')

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
            false_points = ["(1; 2)", "(-1; -2)", "(0; 2)", "(2; 0)"]
            false_pt = random.choice(false_points)

            vd_da_1_d = '\\True Điểm $O(0; 0)$ là tâm đối xứng đồ thị hàm số $y=f(x)$'
            vd_da_1_s = 'Điểm $I%s$ là tâm đối xứng đồ thị hàm số $y=f(x)$' % false_pt

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Hàm số đa thức bậc ba luôn nhận điểm uốn làm tâm đối xứng. \\\\
            Dựa vào đồ thị, điểm uốn là trung điểm của hai điểm cực trị $(-1; -2)$ và $(1; 2)$, tức là điểm $O(0; 0)$. \\\\
            Vậy $O(0; 0)$ là tâm đối xứng của đồ thị hàm số.''')

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
            expr_list = [
                ("a+b+c+d", 2),
                ("2a+b-c+d", -5),
                ("a-b+c-d", 2),
                ("a+2b+3c+d", 8)
            ]
            expr_str, val_true = random.choice(expr_list)
            val_false = val_true + random.choice([-2, -1, 1, 2, 3])

            vdc_da_1_d = '\\True $%s=%s$' % (expr_str, val_true)
            vdc_da_1_s = '$%s=%s$' % (expr_str, val_false)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Dựa vào đồ thị hàm số, ta có: \\\\
            Đồ thị đi qua gốc tọa độ $O(0; 0)$ nên $d = 0$. \\\\
            Đồ thị hàm số đạt cực tiểu tại $(-1; -2)$ và cực đại tại $(1; 2)$ nên ta có hệ phương trình: \\\\
            $\\left\\{\\begin{matrix} f(-1) = -a + b - c = -2 \\\\ f(1) = a + b + c = 2 \\\\ f'(1) = 3a + 2b + c = 0 \\end{matrix}\\right.$ \\\\
            $\\Rightarrow \\left\\{\\begin{matrix} 2b = 0 \\\\ a + c = 2 \\\\ 3a + c = 0 \\end{matrix}\\right. \\Leftrightarrow \\left\\{\\begin{matrix} b = 0 \\\\ a = -1 \\\\ c = 3 \\end{matrix}\\right.$. \\\\
            Vậy $a = -1, b = 0, c = 3, d = 0$. \\\\
            Suy ra $%s = %s$.''' % (expr_str, val_true))

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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

