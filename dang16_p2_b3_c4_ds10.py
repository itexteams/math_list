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


def bt_dang16_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC 1: TẠO DỮ LIỆU NGẪU NHIÊN ---
            # 1. Tam thức a > 0, có 2 nghiệm phân biệt
            x1, x2 = random.sample(range(1, 5), 2)
            f1 = expand((x - x1) * (x - x2))
            # 2. Tam thức a < 0, có 2 nghiệm phân biệt
            x3, x4 = random.sample(range(1, 5), 2)
            f2 = expand(-(x - x3) * (x - x4))
            # 3. Tam thức a > 0, có 2 nghiệm phân biệt khác
            x5, x6 = random.sample(range(5, 9), 2)
            f3 = expand((x - x5) * (x - x6))
            # 4. Đa thức bậc 3
            c4 = random.randint(2, 5)
            f4 = c4*x**3 - x
            # 5. Tam thức a > 0, vô nghiệm (dùng cho GTNN)
            h = random.randint(1, 3)
            k = random.randint(5, 8)
            f5 = expand((x - h)**2 + k)

            # Trộn danh sách để hiển thị trong đề bài
            poly_list = [f1, f2, f3, f4, f5]
            random.shuffle(poly_list)

            # Nội dung câu hỏi
            noidungcauhoi = "Cho các đa thức: " + "; ".join([f"$y = {latex(p)}$" for p in poly_list]) + "."

            ########################################################################
            # Nhận biết
            ########################################################################
            nb_da_1_d = '\\True Có bốn tam thức bậc hai'
            nb_da_1_s = 'Có năm tam thức bậc hai'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (f"Trong các đa thức đã cho, có 4 tam thức bậc hai là ${latex(f1)}$, ${latex(f2)}$, ${latex(f3)}$, ${latex(f5)}$. "
                            f"Đa thức ${latex(f4)}$ là đa thức bậc ba.")
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = 'Có hai tam thức bậc hai không đổi dấu trên $\\mathbb{R}$'
            th_da_1_s = '\\True Chỉ có một tam thức bậc hai không đổi dấu trên $\\mathbb{R}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            delta5 = (2*h)**2 - 4*(h**2 + k)
            loigiai_th_1 = (f"Xét dấu các tam thức: \\\\ "
                            f"- ${latex(f1)}$, ${latex(f2)}$, ${latex(f3)}$ đều có $\\Delta > 0$ nên đổi dấu qua các nghiệm. \\\\ "
                            f"- ${latex(f5)}$ có $\\Delta = {delta5} < 0$ và $a=1>0$ nên luôn dương với mọi $x$. \\\\ "
                            f"Vậy chỉ có một tam thức không đổi dấu.")
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = '\\True Có hai tam thức bậc hai có bảng xét dấu như hình vẽ'
            vd_da_1_s = 'Có ba tam thức bậc hai có bảng xét dấu như hình vẽ'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (f"Bảng xét dấu có dạng $+ , 0 , - , 0 , +$ ứng với tam thức bậc hai có $a > 0$ và có hai nghiệm phân biệt. "
                            f"Trong bài có 2 tam thức thỏa mãn là ${latex(f1)}$ và ${latex(f3)}$.")
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao
            ########################################################################
            m = random.randint(2, 4)
            f_shifted = expand(f5.subs(x, x + m))
            vdc_da_1_d = f'\\True Xét tam thức bậc hai $f(x)$ có giá trị nhỏ nhất bằng ${k}$. Khi đó $f(x+{m}) = {latex(f_shifted)}$'
            vdc_da_1_s = f'Xét tam thức bậc hai $f(x)$ có giá trị nhỏ nhất bằng ${k}$. Khi đó $f(x+{m}) = {latex(f_shifted + 1)}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (f"Tam thức $f(x) = {latex(f5)}$ có đỉnh $I({h}; {k})$. Do $a=1>0$ nên GTNN bằng ${k}$. \\\\ "
                             f"Khi đó $f(x+{m}) = (x+{m})^2 - {2*h}(x+{m}) + {h**2+k} = {latex(f_shifted)}$.")
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # --- LOGIC KIỂM TRA ĐÁP ÁN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Gán lại cho list để đúng cấu trúc mẫu
            list_nb_1 = [nb_sel]; list_th_1 = [th_sel]; list_vd_1 = [vd_sel]; list_vdc_1 = [vdc_sel]

            # Bảng xét dấu dùng tabular theo yêu cầu
            bang_xet_dau = ('''\\begin{center}
            \\begin{tabular}{c|ccccccc}
            $x$ & $-\\infty$ & & $a$ & & $b$ & & $+\\infty$ \\\\ \\hline
            $f(x)$ & & $+$ & $0$ & $-$ & $0$ & $+$ & 
            \\end{tabular}
            \\end{center}''')

            # Tách list đã xáo trộn (mặc dù ở đây list chỉ có 1 phần tử đã chọn)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*list(zip(list_nb_1, list_nb_2)))
            shuffled_answers_th, shuffled_solutions_th = zip(*list(zip(list_th_1, list_th_2)))
            shuffled_answers_vd, shuffled_solutions_vd = zip(*list(zip(list_vd_1, list_vd_2)))
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*list(zip(list_vdc_1, list_vdc_2)))

            # --- XUẤT NỘI DUNG (CONTENT) ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n' +
                'Xét tính đúng, sai của các khẳng định sau: \n' +
                str(bang_xet_dau) + '\n' +
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

