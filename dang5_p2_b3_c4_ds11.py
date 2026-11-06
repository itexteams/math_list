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


def bt_dang5_p2_b3_c4_ds11(self):
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Khởi tạo các giá trị ngẫu nhiên cho hàm số
            # f(x) = x^2 + ax + b  khi x <= -1
            # f(x) = cx + d        khi -1 < x < 1
            # f(x) = ex + f        khi x >= 1

            a = random.randint(-9, 9)
            b = random.randint(1, 9)
            c = random.randint(1, 9)
            d = random.randint(1, 9)
            e = random.randint(1, 9)
            f = random.randint(1, 9)

            # Các biểu thức
            f1 = x**2 + a*x + b
            f2 = c*x + d
            f3 = e*x + f

            # Tính giá trị tại các điểm biên để xét tính liên tục
            val_f1_neg1 = (-1)**2 + a*(-1) + b # f(-1) và giới hạn bên trái tại -1
            val_f2_neg1 = c*(-1) + d           # giới hạn bên phải tại -1

            val_f2_pos1 = c*(1) + d            # giới hạn bên trái tại 1
            val_f3_pos1 = e*(1) + f            # f(1) và giới hạn bên phải tại 1

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x)=\begin{cases} %s & \text{khi } x \leq -1 \\ %s & \text{khi } -1 < x < 1 \\ %s & \text{khi } x \geq 1 \end{cases}$.''' 
                             % (latex(f1), latex(f2), latex(f3)))

            ########################################################################
            # Nhận biết: Liên tục trên khoảng xác định
            ########################################################################
            x_nb = -2
            nb_da_1_d = r'\True Hàm số liên tục tại điểm $x = %s$' % x_nb
            nb_da_1_s = r'Hàm số gián đoạn tại điểm $x = %s$' % x_nb
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Vì $x = %s \in (-\infty; -1)$ nên hàm số liên tục tại điểm đó (hàm đa thức).''' % x_nb

            ########################################################################
            # Thông hiểu: Liên tục trên khoảng giữa
            ########################################################################
            x_th = 0
            th_da_1_d = r'\True Hàm số liên tục tại điểm $x = %s$' % x_th
            th_da_1_s = r'Hàm số gián đoạn tại điểm $x = %s$' % x_th
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''Vì $x = %s \in (-1; 1)$ nên hàm số liên tục tại điểm đó.''' % x_th

            ########################################################################
            # Vận dụng: Xét tính liên tục tại x = -1
            ########################################################################
            is_cont_neg1 = (val_f1_neg1 == val_f2_neg1)
            if is_cont_neg1:
                vd_da_1_d = r'\True Hàm số liên tục tại $x = -1$'
                vd_da_1_s = r'Hàm số gián đoạn tại $x = -1$'
            else:
                vd_da_1_d = r'\True Hàm số gián đoạn tại $x = -1$'
                vd_da_1_s = r'Hàm số liên tục tại $x = -1$'

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Ta có $\lim_{x \to -1^-} f(x) = f(-1) = %s$; $\lim_{x \to -1^+} f(x) = %s$. ''' 
                            % (val_f1_neg1, val_f2_neg1))
            loigiai_vd_1 += r'''Suy ra hàm số %s tại $x = -1$.''' % ("liên tục" if is_cont_neg1 else "gián đoạn")

            ########################################################################
            # Vận dụng cao: Xét tính liên tục tại x = 1
            ########################################################################
            is_cont_pos1 = (val_f2_pos1 == val_f3_pos1)
            if is_cont_pos1:
                vdc_da_1_d = r'\True Hàm số liên tục tại $x = 1$'
                vdc_da_1_s = r'Hàm số không liên tục tại $x = 1$'
            else:
                vdc_da_1_d = r'\True Hàm số không liên tục tại $x = 1$'
                vdc_da_1_s = r'Hàm số liên tục tại $x = 1$'

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Ta có $\lim_{x \to 1^-} f(x) = %s$; $\lim_{x \to 1^+} f(x) = f(1) = %s$. ''' 
                             % (val_f2_pos1, val_f3_pos1))
            loigiai_vdc_1 += r'''Suy ra hàm số %s tại $x = 1$.''' % ("liên tục" if is_cont_pos1 else "không liên tục")

            # --- Logic lọc số lượng câu đúng (1-3 câu) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + d1 + '}\n'
                '{' + d2 + '}\n'
                '{' + d3 + '}\n'
                '{' + d4 + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n')
            return content

