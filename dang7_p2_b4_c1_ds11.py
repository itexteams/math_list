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


def bt_dang7_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số phạm vi xét nghiệm ở ý d (Chọn một số nguyên chẵn N để tạo khoảng (0; N*pi))
            N = random.choice([40, 44, 48, 50, 52, 56, 60])
            # Số nghiệm đúng của phương trình cos(x) = sqrt(2/3) trong khoảng (0; N*pi) là N nghiệm 
            # (Vì mỗi khoảng chu kỳ 2*pi có đúng 2 nghiệm, suy ra khoảng N*pi có (N/2)*2 = N nghiệm)
            so_nghiem_dung = N
            so_nghiem_sai = N - randint(2, 5)

            # Vẽ hình đồ thị bằng TikZ (Độ dày nét 1pt, giữ đúng hình dạng mẫu)
            hinh_tikz = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=0.8, >=stealth]
              \\draw[->] (-5,0) -- (7.5,0) node[below] {$x$};
              \\draw[->] (0,-2) -- (0,2.5) node[right] {$y$};
              \\draw[smooth, samples=200, domain=-4.8:7.0] plot (\\x, {1.5*cos(\\x r)});
              \\node[below left] at (0,0) {$O$};
              \\node[left] at (0,1.5) {$1$};
              \\node[left] at (0,-1.5) {$-1$};
              \\draw[dashed] (-3.1416,0) -- (-3.1416,-1.5) -- (0,-1.5);
              \\draw[dashed] (3.1416,0) -- (3.1416,-1.5);
              \\draw[dashed] (6.2831,0) -- (6.2831,1.5) -- (0,1.5);
              \\node[above] at (-3.1416,0) {$-\\pi$};
              \\node[above] at (3.1416,0) {$\\pi$};
              \\node[below] at (6.2831,0) {$2\\pi$};
              \\fill (0,1.5) circle (1.5pt);
            \\end{tikzpicture} \\end{center}''')

            # Nội dung câu hỏi sử dụng định dạng %s
            noidungcauhoi = ('''Cho đồ thị hàm số lượng giác $y = f(x)$ như hình vẽ. %s'''
                             %(hinh_tikz))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Giá trị f(pi) = -1
            nb_da_1_d = '\\True $f(\\pi) = -1$'
            nb_da_1_s = '$f(\\pi) = 1$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Dựa vào đồ thị hàm số, tại điểm $x = \\pi$, dóng vuông góc xuống đồ thị ta nhận được giá trị tung độ tương ứng là $y = -1$. Do đó $f(\\pi) = -1$.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Nhận diện hàm số y = cos x
            th_da_1_d = '\\True Đồ thị đã cho là đồ thị hàm số $y = \\cos x$'
            th_da_1_s = 'Đồ thị đã cho là đồ thị hàm số $y = \\sin x$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Đồ thị đi qua điểm $(0; 1)$, đạt cực tiểu tại $x = \\pi$ và $x = -\\pi$ với giá trị $y = -1$, đạt cực đại tại $x = 2\\pi$ với giá trị $y = 1$. Đây chính là hình dạng dạng sóng đặc trưng của đồ thị hàm số $y = \\cos x$.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: f(2023) + f(2024) < 2
            vd_da_1_d = '\\True $f(2023) + f(2024) < 2$'
            vd_da_1_s = 'Giá trị lớn nhất của hàm số bằng $2$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta biết tập giá trị của hàm số $y = \\cos x$ là $[-1; 1]$, nghĩa là $f(x) \\le 1$ với mọi $x \\in \\mathbb{R}$.\\\\'''
                            '''Hàm số đạt giá trị bằng $1$ khi và chỉ khi $x = k2\\pi$ ($k \\in \\mathbb{Z}$). Vì cả $2023$ và $2024$ đều không chia hết cho $2\\pi$ nên $f(2023) < 1$ và $f(2024) < 1$.\\\\'''
                            '''Cộng vế với vế ta suy ra $f(2023) + f(2024) < 2$. Khẳng định này đúng.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Số nghiệm của phương trình f(x) = sqrt(2/3) trong khoảng (0; N*pi)
            vdc_da_1_d = '\\True Phương trình $f(x) = \\sqrt{\\frac{2}{3}}$ có %s nghiệm trong khoảng $(0; %s\\pi)$' %(latex(so_nghiem_dung), latex(N))
            vdc_da_1_s = 'Phương trình $f(x) = \\sqrt{\\frac{2}{3}}$ có %s nghiệm trong khoảng $(0; %s\\pi)$' %(latex(so_nghiem_sai), latex(N))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Số nghiệm của phương trình $f(x) = \\sqrt{\\frac{2}{3}}$ trong khoảng $(0; %s\\pi)$ chính là số giao điểm giữa đồ thị hàm số $y = \\cos x$ và đường thẳng nằm ngang $y = \\sqrt{\\frac{2}{3}}$.\\\\'''
                             '''Vì $0 < \\sqrt{\\frac{2}{3}} < 1$ nên trong mỗi chu kỳ tuần hoàn một vòng tròn lượng giác có độ dài $2\\pi$, đường thẳng cắt đồ thị tại đúng $2$ điểm.\\\\'''
                             '''Khoảng $(0; %s\\pi)$ có độ dài tương ứng với $\\frac{%s}{2}$ chu kỳ, do đó tổng số giao điểm thu được là $\\frac{%s}{2} \\cdot 2 = %s$ nghiệm.'''
                             %(latex(N), latex(N), latex(N), latex(N), latex(so_nghiem_dung)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra điều kiện sinh đáp án có từ 1 đến 3 đáp án đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Thiết lập lại danh sách sau khi lọc thỏa mãn điều kiện
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

            # Xuất câu hỏi và lời giải chi tiết theo đúng định dạng mẫu
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

