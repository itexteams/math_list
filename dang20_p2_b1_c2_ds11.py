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


def bt_dang20_p2_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn tham số ngẫu nhiên dưới dạng phân số (Rational)
            E1_val = random.choice([10, 12, 15, 20])  # Điện năng phút thứ nhất (kWh)
            p_val = random.choice([75, 80, 85, 90])   # Tỷ lệ nạp thêm ở phút tiếp theo (%)

            E1 = Rational(E1_val, 1)
            p_rat = Rational(p_val, 100)
            q_rat = p_rat                              # Công bội cấp số nhân (phân số)

            # Tính toán các giá trị số hạng và tổng dưới dạng phân số
            E2 = E1 * q_rat                            # E_2
            E2_wrong = E2 + Rational(1, 2)             # Giá trị sai cho nhiễu

            E3 = E2 * q_rat                            # E_3
            S3 = E1 + E2 + E3                          # Tổng 3 phút đầu
            S3_wrong = S3 + Rational(1, 1)             # Giá trị sai cho VDC

            A_rat = E1 / (1 - q_rat)                   # Hệ số trong công thức Sn = A * [1 - q^n]
            A_wrong = E1 / q_rat                       # Giá trị sai cho VD

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khi cắm sạc ở chế độ sạc nhanh, lượng điện năng tích tụ trong bộ pin ban đầu ở phút thứ nhất là %s kWh. Trong các phút tiếp theo, do nhiệt độ pin tăng lên, điện năng nạp thêm vào pin ở mỗi phút chỉ bằng %s\\%% so với điện năng nạp thêm ở phút ngay trước đó. Gọi $E_n$ (đơn vị: kWh) là điện năng nạp thêm vào pin ở phút thứ $n$ ($n \\ge 1$).'''
                             % (latex(E1), p_val))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Điện năng nạp thêm vào pin ở phút thứ 2 là $E_2 = %s$ kWh và số hạng tổng quát của dãy số là $E_n = %s \\cdot \\left(%s\\right)^{n-1}$' % (latex(E2), latex(E1), latex(q_rat))
            nb_da_1_s = 'Điện năng nạp thêm vào pin ở phút thứ 2 là $E_2 = %s$ kWh và số hạng tổng quát của dãy số là $E_n = %s \\cdot \\left(%s\\right)^{n-1}$' % (latex(E2_wrong), latex(E1), latex(q_rat))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Điện năng nạp thêm ở phút thứ nhất là $E_1 = %s$ (kWh). \\\\
            Ở phút thứ hai, điện năng nạp thêm là $E_2 = E_1 \\cdot %s = %s \\cdot %s = %s$ (kWh). \\\\
            Dãy số $(E_n)$ là một cấp số nhân với số hạng đầu $E_1 = %s$ và công bội $q = %s$. \\\\
            Do đó, số hạng tổng quát của dãy số là $E_n = E_1 \\cdot q^{n-1} = %s \\cdot \\left(%s\\right)^{n-1}$ với mọi $n \\ge 1$.'''
                            % (latex(E1), latex(q_rat), latex(E1), latex(q_rat), latex(E2), latex(E1), latex(q_rat), latex(E1), latex(q_rat)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Dãy số $(E_n)$ là một dãy số giảm có công thức truy hồi $E_{n+1} = %s E_n$ với mọi $n \\ge 1$' % latex(q_rat)
            th_da_1_s = 'Dãy số $(E_n)$ là một dãy số tăng có công thức truy hồi $E_{n+1} = %s E_n$ với mọi $n \\ge 1$' % latex(q_rat)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Theo đề bài, điện năng nạp thêm ở phút thứ $n+1$ bằng $%s\\%%$ điện năng nạp thêm ở phút thứ $n$. \\\\
            Do đó công thức truy hồi là $E_{n+1} = %s E_n$ với mọi $n \\ge 1$. \\\\
            Vì $E_n > 0$ và $\\frac{E_{n+1}}{E_n} = %s < 1$ với mọi $n \\ge 1$ nên $E_{n+1} < E_n$ với mọi $n \\ge 1$. \\\\
            Vậy dãy số $(E_n)$ là một dãy số giảm.'''
                            % (p_val, latex(q_rat), latex(q_rat)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Công thức tính tổng điện năng $S_n$ nạp được vào pin sau $n$ phút đầu tiên là $S_n = %s \\cdot \\left[1 - \\left(%s\\right)^n\\right]$' % (latex(A_rat), latex(q_rat))
            vd_da_1_s = 'Công thức tính tổng điện năng $S_n$ nạp được vào pin sau $n$ phút đầu tiên là $S_n = %s \\cdot \\left[1 - \\left(%s\\right)^n\\right]$' % (latex(A_wrong), latex(q_rat))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Tổng điện năng nạp được vào pin sau $n$ phút đầu tiên là tổng $n$ số hạng đầu của cấp số nhân $(E_n)$: \\\\
            $S_n = E_1 + E_2 + \\dots + E_n = E_1 \\cdot \\frac{1 - q^n}{1 - q}$. \\\\
            Thay $E_1 = %s$ và $q = %s$, ta được: \\\\
            $S_n = %s \\cdot \\frac{1 - \\left(%s\\right)^n}{1 - %s} = %s \\cdot \\frac{1 - \\left(%s\\right)^n}{%s} = %s \\cdot \\left[1 - \\left(%s\\right)^n\\right]$.'''
                            % (latex(E1), latex(q_rat), latex(E1), latex(q_rat), latex(q_rat), latex(E1), latex(q_rat), latex(1 - q_rat), latex(A_rat), latex(q_rat)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tổng điện năng nạp được vào pin sau $3$ phút đầu tiên là $S_3 = %s$ kWh' % latex(S3)
            vdc_da_1_s = 'Tổng điện năng nạp được vào pin sau $3$ phút đầu tiên là $S_3 = %s$ kWh' % latex(S3_wrong)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Điện năng nạp thêm vào pin ở $3$ phút đầu tiên lần lượt là: \\\\
            Phút thứ 1: $E_1 = %s$ (kWh). \\\\
            Phút thứ 2: $E_2 = %s \\cdot %s = %s$ (kWh). \\\\
            Phút thứ 3: $E_3 = %s \\cdot %s = %s$ (kWh). \\\\
            Tổng điện năng nạp được vào pin sau $3$ phút đầu tiên là: \\\\
            $S_3 = E_1 + E_2 + E_3 = %s + %s + %s = %s$ (kWh).'''
                             % (latex(E1), latex(E1), latex(q_rat), latex(E2), latex(E2), latex(q_rat), latex(E3), latex(E1), latex(E2), latex(E3), latex(S3)))

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

