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


def bt_dang23_p2_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thực hiện random các số trong bài toán
            a = random.choice([1, 2])       # Hệ số của ln(x^2 + 1)
            b = randint(1, 3)              # Hằng số tự do
            m_sym = symbols('m')

            # Biểu diễn hàm số khi chưa thế m: a*ln(x^2 + 1) - m*x + b
            if a == 1:
                f_expr_latex = "\\ln(x^2 + 1) - mx + " + str(b)
            else:
                f_expr_latex = str(a) + "\\ln(x^2 + 1) - mx + " + str(b)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = %s$ có đồ thị $(C)$ với $m$ là tham số. Xét tính đúng, sai của các mệnh đề sau:''' 
                             %(f_expr_latex))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Với $m = 0$, hàm số nghịch biến trên khoảng $(-\\infty; 0)$ và đồng biến trên khoảng $(0; +\\infty)$'
            nb_da_1_s = 'Với $m = 0$, hàm số đồng biến trên khoảng $(-\\infty; 0)$ và nghịch biến trên khoảng $(0; +\\infty)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Với $m = 0$, hàm số trở thành $y = %s \\ln(x^2 + 1) + %s$.\\\\
            Đạo hàm $y\' = \\frac{%sx}{x^2+1}$.\\\\
            Xét dấu đạo hàm:\\\\
            - Với $x \\in (-\\infty; 0) \\Rightarrow y\' < 0$, suy ra hàm số nghịch biến trên khoảng $(-\\infty; 0)$.\\\\
            - Với $x \\in (0; +\\infty) \\Rightarrow y\' > 0$, suy ra hàm số đồng biến trên khoảng $(0; +\\infty)$.'''
                            %(latex(a) if a > 1 else "", latex(b), latex(2*a)))

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
            th_da_1_d = '\\True Với $m = 0$, đồ thị hàm số $(C)$ có điểm cực tiểu là $(0; %s)$' %(latex(b))
            th_da_1_s = 'Với $m = 0$, đồ thị hàm số $(C)$ có điểm cực đại là $(0; %s)$' %(latex(b))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Dựa vào kết quả xét dấu $y\'$ ở câu a, đạo hàm đổi dấu từ âm sang dương khi đi qua $x = 0$.\\\\
            Do đó, hàm số đạt cực tiểu tại $x = 0$.\\\\
            Giá trị cực tiểu là $y(0) = %s \\ln(0^2 + 1) + %s = %s$.\\\\
            Vậy đồ thị hàm số có điểm cực tiểu là $(0; %s)$.'''
                            %(latex(a) if a > 1 else "", latex(b), latex(b), latex(b)))

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
            vd_da_1_d = 'Với mọi giá trị của tham số $m$, đồ thị hàm số $(C)$ luôn có hai điểm cực trị'
            vd_da_1_s = '\\True Không phải với mọi giá trị của tham số $m$, đồ thị hàm số $(C)$ đều có hai điểm cực trị'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét đạo hàm tổng quát: $y\' = \\frac{%sx}{x^2+1} - m = \\frac{-mx^2 + %sx - m}{x^2+1}$.\\\\
            Số cực trị của hàm số phụ thuộc vào số nghiệm đơn của phương trình $y\' = 0 \\Leftrightarrow mx^2 - %sx + m = 0$.\\\\
            - Khi $m = 0$, phương trình có nghiệm duy nhất $x = 0$, đồ thị hàm số có đúng $1$ cực trị.\\\\
            Do đó khẳng định "với mọi $m$ luôn có hai cực trị" là sai.'''
                            %(latex(2*a), latex(2*a), latex(2*a)))

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
            vdc_da_1_d = '\\True Với $m \\in [ %s; +\\infty )$ thì hàm số $(C)$ luôn nghịch biến trên $\\mathbb{R}$' %(latex(a))
            vdc_da_1_s = 'Với $m \\in (-\\infty; -%s] \\cup [%s; +\\infty)$ thì hàm số $(C)$ luôn nghịch biến trên $\\mathbb{R}$' %(latex(a), latex(a))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Để hàm số nghịch biến trên $\\mathbb{R}$ thì $y\' \\le 0, \\forall x \\in \\mathbb{R}$.\\\\
            $\\Leftrightarrow \\frac{-mx^2 + %sx - m}{x^2+1} \\le 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow mx^2 - %sx + m \\ge 0, \\forall x \\in \\mathbb{R}$.\\\\
            Trường hợp 1: $m = 0 \\Rightarrow -%sx \\ge 0, \\forall x \\in \\mathbb{R}$ (không thỏa mãn).\\\\
            Trường hợp 2: $m \\ne 0$. Hệ thức thỏa mãn khi và chỉ khi:\\\\
            $\\begin{cases} m > 0 \\\\ \\Delta\' = %s - m^2 \\le 0 \\end{cases} \\Leftrightarrow \\begin{cases} m > 0 \\\\ m^2 \\ge %s \\end{cases} \\Leftrightarrow m \\ge %s$.\\\\
            Vậy giá trị $m$ cần tìm là $m \\in [ %s; +\\infty )$.'''
                             %(latex(2*a), latex(2*a), latex(2*a), latex(a**2), latex(a**2), latex(a), latex(a)))

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

