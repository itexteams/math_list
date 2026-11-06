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


def bt_dang9_p2_b3_c4_ds11(self):
            # Khai báo biến
            # t1: mốc thời gian 1, t2: mốc thời gian 2
            t1 = 2
            t2 = 4
            p1 = random.choice([30000, 40000, 50000, 60000])
            p2 = random.choice([100000, 110000, 120000, 130000])
            p3 = random.choice([30000, 35000, 40000, 45000])

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Một bãi đậu xe ô tô đưa ra giá $T(x)$ (đồng) khi thời gian đậu xe là $x$ (giờ) như sau:
            $T(x) = \begin{cases} %s, & 0 < x \le %s \\ %s, & %s < x < %s \\ %sx, & x \ge %s \end{cases}$''' 
            % (p1, t1, p2, t1, t2, p3, t2))

            ########################################################################
            # Nhận biết: Kiểm tra giá trị tại điểm t1
            ########################################################################
            nb_da_1_d = r'\True $T(%s) = %s$' % (t1, p1)
            nb_da_1_s = r'$T(%s) = %s$' % (t1, p2)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Dựa vào công thức hàm số, khi $x=%s$ thuộc khoảng $0 < x \le %s$ nên $T(%s) = %s$.''' % (t1, t1, t1, p1)
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Giới hạn bên phải tại t2
            ########################################################################
            lim_right = p3 * t2
            th_da_1_d = r'\True $\lim_{x \to %s^+} T(x) = %s$' % (t2, lim_right)
            th_da_1_s = r'$\lim_{x \to %s^+} T(x) = %s$' % (t2, p2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''Ta có $\lim_{x \to %s^+} T(x) = \lim_{x \to %s^+} (%s x) = %s \cdot %s = %s$.''' % (t2, t2, p3, p3, t2, lim_right)
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Tính liên tục tại t2
            ########################################################################
            vd_da_1_d = r'\True Hàm số $T(x)$ không liên tục tại $x = %s$' % (t2)
            vd_da_1_s = r'Hàm số $T(x)$ liên tục tại $x = %s$' % (t2)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Vì $\lim_{x \to %s^-} T(x) = %s$ và $\lim_{x \to %s^+} T(x) = %s$. Do $%s \neq %s$ nên không tồn tại giới hạn tại $x=%s$, suy ra hàm số không liên tục tại đó.''' % (t2, p2, t2, lim_right, p2, lim_right, t2)
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Tính liên tục trên nửa khoảng
            ########################################################################
            vdc_da_1_d = r'\True Hàm số $T(x)$ liên tục trên nửa khoảng $[%s; +\infty)$' % (t2)
            vdc_da_1_s = r'Hàm số $T(x)$ không liên tục trên nửa khoảng $[%s; +\infty)$' % (t2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Khi $x > %s$, $T(x) = %sx$ là hàm đa thức nên liên tục trên $(%s; +\infty)$. Ta lại có $\lim_{x \to %s^+} T(x) = T(%s) = %s$ nên hàm số liên tục phải tại $x=%s$. Vậy hàm số liên tục trên $[%s; +\infty)$.''' % (t2, p3, t2, t2, t2, lim_right, t2, t2)
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số câu đúng từ 1 đến 3
            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Xuất kết quả theo mẫu LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n')
            return content

