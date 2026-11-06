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


def bt_dang17_p2_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn tham số ngẫu nhiên
            ten = random.choice(['An', 'Bình', 'Cường', 'Dũng', 'Mai'])
            A = random.choice([10, 15, 20, 25, 30])  # Số tiền thưởng ban đầu (triệu đồng)
            p = random.choice([70, 75, 80, 85])       # Phần trăm tiền dư so với tháng trước (%)

            # Sử dụng Rational để biểu diễn công bội và hiệu dưới dạng phân số chính xác
            q_rat = Rational(p, 100)
            q_str = latex(q_rat)                      # Ví dụ: \frac{4}{5}
            p_str = str(p)

            diff_rat = q_rat - 1                     # Ví dụ: -\frac{1}{5}
            diff_str = latex(diff_rat)

            K = random.choice([1, 2, 3])              # Ngưỡng tiền dư (triệu đồng)

            # Tính toán số tháng n_min để u_n < K bằng toán học chính xác
            val_ex = math.log(K / A) / math.log(p / 100.0)
            n_min = math.floor(val_ex) + 2
            val_ex_str = f"{val_ex:.2f}".replace('.', ',')
            n_wrong = n_min - 1

            # Nội dung câu hỏi
            noidungcauhoi = ('''%s gửi một số tiền thưởng ban đầu là %s triệu đồng vào một quỹ đầu tư. Do rủi ro thị trường, từ tháng thứ hai trở đi, số tiền dư trong quỹ ở mỗi tháng chỉ bằng %s\\%% số tiền dư của tháng ngay trước đó. Gọi $u_n$ (đơn vị: triệu đồng) là số tiền dư trong quỹ ở tháng thứ $n$ ($n \\ge 1$).'''
                             % (ten, A, p_str))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Công thức tổng quát cho số hạng $u_n$ đại diện cho quỹ đầu tư dự phòng là $u_n = %s \\cdot \\left(%s\\right)^{n-1}$ (triệu đồng)' % (A, q_str)
            nb_da_1_s = 'Công thức tổng quát cho số hạng $u_n$ đại diện cho quỹ đầu tư dự phòng là $u_n = %s \\cdot \\left(%s\\right)^n$ (triệu đồng)' % (A, q_str)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Số tiền dư trong quỹ ở tháng thứ nhất là $u_1 = %s$ (triệu đồng). \\\\
            Từ tháng thứ hai trở đi, số tiền dư ở mỗi tháng bằng %s\\%% số tiền dư tháng trước nên dãy số $(u_n)$ là một cấp số nhân có số hạng đầu $u_1 = %s$ và công bội $q = %s\\%% = %s$. \\\\
            Do đó, công thức tổng quát của $u_n$ là $u_n = u_1 \\cdot q^{n-1} = %s \\cdot \\left(%s\\right)^{n-1}$ (triệu đồng).'''
                            % (A, p_str, A, p_str, q_str, A, q_str))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Dãy số $(u_n)$ là một dãy số giảm'
            th_da_1_s = 'Dãy số $(u_n)$ là một dãy số tăng'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Xét hiệu $u_{n+1} - u_n = %s \\cdot \\left(%s\\right)^n - %s \\cdot \\left(%s\\right)^{n-1} = %s \\cdot \\left(%s\\right)^{n-1} \\cdot \\left(%s - 1\\right) = %s \\cdot \\left(%s\\right)^{n-1} \\cdot \\left(%s\\right)$. \\\\
            Vì $u_1 = %s > 0$ và $0 < %s < 1$ nên $u_{n+1} - u_n < 0$ với mọi $n \\ge 1$. \\\\
            Vậy $(u_n)$ là một dãy số giảm.'''
                            % (A, q_str, A, q_str, A, q_str, q_str, A, q_str, diff_str, A, q_str))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Dãy số $(u_n)$ là dãy số bị chặn, cụ thể $0 < u_n \\le %s$ với mọi $n \\ge 1$' % A
            vd_da_1_s = 'Dãy số $(u_n)$ là dãy số bị chặn, cụ thể $0 \\le u_n < %s$ với mọi $n \\ge 1$' % A
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Vì $0 < %s < 1$ nên với mọi $n \\ge 1$, ta có $0 < \\left(%s\\right)^{n-1} \\le 1$. \\\\
            Nhân hai vế với %s $> 0$, ta được $0 < %s \\cdot \\left(%s\\right)^{n-1} \\le %s \\Leftrightarrow 0 < u_n \\le %s$ với mọi $n \\ge 1$. \\\\
            Vậy dãy số $(u_n)$ là dãy số bị chặn dưới bởi $m = 0$ và bị chặn trên bởi $M = %s$.'''
                            % (q_str, q_str, A, A, q_str, A, A, A))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Kể từ tháng thứ %s thì số tiền trong quỹ đầu tư dự phòng $u_n$ sẽ giảm xuống dưới %s triệu đồng' % (n_min, K)
            vdc_da_1_s = 'Kể từ tháng thứ %s thì số tiền trong quỹ đầu tư dự phòng $u_n$ sẽ giảm xuống dưới %s triệu đồng' % (n_wrong, K)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Để số tiền trong quỹ đầu tư dự phòng giảm xuống dưới %s triệu đồng, ta có bất phương trình: \\\\
            $u_n < %s \\Leftrightarrow %s \\cdot \\left(%s\\right)^{n-1} < %s \\Leftrightarrow \\left(%s\\right)^{n-1} < \\frac{%s}{%s}$. \\\\
            Lấy logarit tự nhiên hai vế (do $0 < %s < 1$ nên $\\ln\\left(%s\\right) < 0$), ta có: \\\\
            $(n-1) \\cdot \\ln\\left(%s\\right) < \\ln\\left(\\frac{%s}{%s}\\right) \\Leftrightarrow n - 1 > \\frac{\\ln\\left(\\frac{%s}{%s}\\right)}{\\ln\\left(%s\\right)} \\approx %s \\Leftrightarrow n > %s$. \\\\
            Vì $n \\in \\mathbb{N}^*$ nên $n \\ge %s$. \\\\
            Vậy kể từ tháng thứ %s thì số tiền trong quỹ dự phòng sẽ giảm xuống dưới %s triệu đồng.'''
                             % (K, K, A, q_str, K, q_str, K, A, q_str, q_str, q_str, K, A, K, A, q_str, val_ex_str, f"{val_ex + 1:.2f}".replace('.', ','), n_min, n_min, K))

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

