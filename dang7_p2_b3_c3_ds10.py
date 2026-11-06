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


def bt_dang7_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Hàm chuẩn hóa số thập phân sang định dạng Việt Nam (dùng dấu phẩy)
            def format_vn(num):
                if num == int(num):
                    return str(int(num))
                return "{:.2f}".format(num).replace('.', ',').rstrip('0').rstrip(',') if '.' in "{:.2f}".format(num) else "{:.2f}".format(num).replace('.', ',')

            # Sinh dữ liệu ngẫu nhiên: 40 học sinh
            # Phần lớn tập trung ở 145-160, thêm vài giá trị đột biến (outliers) để phương sai lớn giống đề gốc
            data = [random.randint(145, 160) for _ in range(38)]
            data.append(random.randint(105, 115))  # Outlier thấp
            data.append(random.randint(165, 175))  # Outlier cao
            random.shuffle(data) # Xáo trộn ngẫu nhiên

            # Tính toán các đại lượng thống kê (Mẫu số liệu không ghép nhóm)
            n = 40
            mean_val = sum(data) / n
            max_val = max(data)
            # Tính phương sai (dùng mẫu n, theo SGK mới)
            var_val = sum((x - mean_val)**2 for x in data) / n
            std_val = math.sqrt(var_val)

            # Làm tròn 2 chữ số thập phân
            mean_val = round(mean_val, 2)
            var_val = round(var_val, 2)
            std_val = round(std_val, 2)

            # Tạo bảng LaTeX 4x10
            table_str = "\\begin{center}\n\\begin{tabular}{|" + "c|" * 10 + "}\n\\hline\n"
            for i in range(4):
                row_data = data[i*10 : (i+1)*10]
                table_str += " & ".join(map(str, row_data)) + " \\\\\n\\hline\n"
            table_str += "\\end{tabular}\n\\end{center}"

            # Nội dung câu hỏi
            noidungcauhoi = (f"Thực hành việc đo chiều cao ($cm$) của 40 học sinh nữ khối lớp 10 của một trường Trung học phổ thông, ta được kết quả như sau:\n"
                             f"{table_str}")

            ######################################################################## Nhận biết (Chiều cao trung bình) ############################################
            fake_mean = round(mean_val + random.choice([-1.5, 1.25, 0.82, -0.95]), 2)
            nb_da_1_d = f"\\True Chiều cao trung bình: $\\overline{{x}} = {format_vn(mean_val)}$ $cm$"
            nb_da_1_s = f"Chiều cao trung bình: $\\overline{{x}} = {format_vn(fake_mean)}$ $cm$"
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = f"Chiều cao trung bình: $\\overline{{x}} = {format_vn(mean_val)}$ $cm$."
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu (Giá trị lớn nhất) ############################################
            fake_max = max_val - random.randint(2, 6)
            th_da_1_d = f"\\True ${max_val}$ $cm$ là chiều cao lớn nhất"
            th_da_1_s = f"${fake_max}$ $cm$ là chiều cao lớn nhất"
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = f"Chiều cao lớn nhất trong bảng: ${max_val}$."
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng (Phương sai) ############################################
            fake_var = round(var_val + random.choice([-2.15, 1.45, 3.12, -1.88]), 2)
            vd_da_1_d = f"\\True Phương sai: $s^2 = {format_vn(var_val)}$"
            vd_da_1_s = f"Phương sai: $s^2 = {format_vn(fake_var)}$"
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = f"Phương sai: $s^2 = {format_vn(var_val)}$."
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao (Độ lệch chuẩn) ############################################
            fake_std = round(std_val + random.choice([-0.55, 0.45, 0.82, -0.63]), 2)
            vdc_da_1_d = f"\\True Độ lệch chuẩn: $s = {format_vn(std_val)}$"
            vdc_da_1_s = f"Độ lệch chuẩn: $s = {format_vn(fake_std)}$"
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = f"Độ lệch chuẩn: $s = {format_vn(std_val)}$."
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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
                       '\\end{ex}\n\\end{minipage}\n\n')
            return content

