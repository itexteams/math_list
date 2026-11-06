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


def bt_dang18_p2_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn tham số ngẫu nhiên
            A = random.choice([40, 50, 60, 80, 100])      # Khối lượng tảo xanh ban đầu (kg)
            p = random.choice([10, 12, 15, 20])           # Tỷ lệ tăng trưởng mỗi tuần (%)
            r_val = 1 + p / 100.0                         # Công bội q

            p_str = str(p)
            r_str = f"{r_val:.2f}".rstrip('0').rstrip('.').replace('.', ',')

            a1 = A
            a2 = A * r_val
            a1_str = str(a1)
            a2_str = f"{a2:.2f}".rstrip('0').rstrip('.').replace('.', ',')
            a2_w_str = f"{a2 + 2.5:.2f}".rstrip('0').rstrip('.').replace('.', ',')

            M = random.choice([150, 200, 250, 300])       # Ngưỡng khối lượng vượt quá (kg)

            # Tính số tuần n_min để a_n > M
            # a_n = A * r_val**(n-1) > M <=> (n-1) * ln(r_val) > ln(M / A) <=> n - 1 > ln(M/A) / ln(r_val)
            val_ex = math.log(M / A) / math.log(r_val)
            n_min = math.floor(val_ex) + 2
            n_wrong = n_min - 1

            val_ex_str = f"{val_ex:.2f}".replace('.', ',')
            ratio_MA_str = f"{M / A:.2f}".rstrip('0').rstrip('.').replace('.', ',')

            k_weeks = random.choice([4, 5, 6])
            Sk = A * (r_val**k_weeks - 1) / (r_val - 1)
            Sk_str = f"{Sk:.2f}".replace('.', ',')
            Sk_w_str = f"{Sk + 12.5:.2f}".replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trang trại thả %s kg tảo xanh ban đầu vào hệ thống hồ nuôi sinh học. Nhờ chế độ dinh dưỡng tối ưu, sau mỗi tuần, tổng khối lượng tảo xanh thu được tăng thêm %s\\%% so với tuần ngay trước đó. Gọi $a_n$ (đơn vị: kg) là tổng khối lượng tảo xanh ở tuần thứ $n$ ($n \\ge 1$).'''
                             % (A, p_str))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Khối lượng tảo xanh ở hai tuần đầu tiên lần lượt là $a_1 = %s$ kg, $a_2 = %s$ kg và công thức tổng quát là $a_n = %s \\cdot (%s)^{n-1}$ (kg)' % (a1_str, a2_str, A, r_str)
            nb_da_1_s = 'Khối lượng tảo xanh ở hai tuần đầu tiên lần lượt là $a_1 = %s$ kg, $a_2 = %s$ kg và công thức tổng quát là $a_n = %s \\cdot (%s)^n$ (kg)' % (a1_str, a2_w_str, A, r_str)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Khối lượng tảo xanh ở tuần đầu tiên là $a_1 = %s$ (kg). \\\\
            Sau tuần thứ nhất, khối lượng tảo xanh tăng thêm %s\\%%, nên ở tuần thứ hai khối lượng tảo xanh là: \\\\
            $a_2 = %s \\cdot (1 + %s\\%%) = %s \\cdot %s = %s$ (kg). \\\\
            Dãy số $(a_n)$ là một cấp số nhân với số hạng đầu $a_1 = %s$ và công bội $q = 1 + %s\\%% = %s$. \\\\
            Do đó, công thức tổng quát của số hạng $a_n$ là $a_n = a_1 \\cdot q^{n-1} = %s \\cdot (%s)^{n-1}$ (kg).'''
                            % (a1_str, p_str, A, p_str, A, r_str, a2_str, A, p_str, r_str, A, r_str))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Dãy số $(a_n)$ là một dãy số tăng'
            th_da_1_s = 'Dãy số $(a_n)$ là một dãy số giảm'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Xét hiệu hai số hạng liên tiếp: \\\\
            $a_{n+1} - a_n = %s \\cdot (%s)^n - %s \\cdot (%s)^{n-1} = %s \\cdot (%s)^{n-1} \\cdot (%s - 1) = %s \\cdot (%s)^{n-1} \\cdot %s$. \\\\
            Vì $a_1 = %s > 0$ và %s $> 1$ nên $a_{n+1} - a_n > 0$ với mọi $n \\ge 1$. \\\\
            Vậy $(a_n)$ là một dãy số tăng.'''
                            % (A, r_str, A, r_str, A, r_str, r_str, A, r_str, str(p/100.0).replace('.', ','), A, r_str))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Kể từ tuần thứ %s thì khối lượng tảo xanh trong hồ vượt quá %s kg' % (n_min, M)
            vd_da_1_s = 'Kể từ tuần thứ %s thì khối lượng tảo xanh trong hồ vượt quá %s kg' % (n_wrong, M)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Để khối lượng tảo xanh vượt quá %s kg, ta có bất phương trình: \\\\
            $a_n > %s \\Leftrightarrow %s \\cdot (%s)^{n-1} > %s \\Leftrightarrow (%s)^{n-1} > %s$. \\\\
            Lấy logarit tự nhiên hai vế (do %s $> 1$), ta có: \\\\
            $(n - 1) \\cdot \\ln(%s) > \\ln(%s) \\Leftrightarrow n - 1 > \\frac{\\ln(%s)}{\\ln(%s)} \\approx %s \\Leftrightarrow n > %s$. \\\\
            Vì $n \\in \\mathbb{N}^*$ nên $n \\ge %s$. \\\\
            Vậy kể từ tuần thứ %s thì khối lượng tảo xanh trong hồ vượt quá %s kg.'''
                            % (M, M, A, r_str, M, r_str, ratio_MA_str, r_str, r_str, ratio_MA_str, ratio_MA_str, r_str, val_ex_str, f"{val_ex + 1:.2f}".replace('.', ','), n_min, n_min, M))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tổng khối lượng tảo xanh thu hoạch được sau %s tuần đầu tiên là khoảng %s kg' % (k_weeks, Sk_str)
            vdc_da_1_s = 'Tổng khối lượng tảo xanh thu hoạch được sau %s tuần đầu tiên là khoảng %s kg' % (k_weeks, Sk_w_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Tổng khối lượng tảo xanh thu hoạch được sau %s tuần đầu tiên là tổng của %s số hạng đầu tiên của cấp số nhân $(a_n)$: \\\\
            $S_{%s} = a_1 + a_2 + \\dots + a_{%s} = %s \\cdot \\frac{(%s)^{%s} - 1}{%s - 1} \\approx %s$ (kg).'''
                             % (k_weeks, k_weeks, k_weeks, k_weeks, A, r_str, k_weeks, r_str, Sk_str))

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

