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


def bt_dang11_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')


            list_n = [4, 7] 
            n = random.choice(list_n)
            m = 2

            # Tính toán tập nghiệm để tự động hóa lời giải
            sol_can = solve(sqrt(m*x**2 + n) - (x + 2), x)
            # Tập nghiệm đầy đủ bao gồm x=2 và các nghiệm từ phương trình căn
            tap_nghiem = sorted(list(set([2] + sol_can)))
            so_nghiem = len(tap_nghiem)
            tong_nghiem = sum(tap_nghiem)
            tat_ca_chan = all(val % 2 == 0 for val in tap_nghiem)

            # Nội dung câu hỏi (Không dùng tiền tố r ở phần content theo yêu cầu)
            noidungcauhoi = 'Cho phương trình $(x-2)\\sqrt{%s x^2 + %s} = x^2 - 4$.' % (latex(m), latex(n))

            ########################################################################
            # Nhận biết (Câu a)
            ########################################################################
            nb_da_1_d = '\\True Điều kiện xác định của phương trình là $x \\in \\mathbb{R}$'
            nb_da_1_s = 'Điều kiện $x \\geq 2$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = 'Biểu thức trong căn là $%s x^2 + %s$. Vì $x^2 \\geq 0$ nên $%s x^2 + %s > 0$ với mọi $x \\in \\mathbb{R}$. Vậy điều kiện $x \\geq 2$ là sai.' % (latex(m), latex(n), latex(m), latex(n))

            ########################################################################
            # Thông hiểu (Câu b)
            ########################################################################
            th_da_1_d = '\\True Phương trình có %s nghiệm' % (so_nghiem)
            th_da_1_s = 'Phương trình có %s nghiệm' % (so_nghiem + 1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = 'Phương trình tương đương với:\\\\ $(x-2)\\sqrt{%sx^2+%s} = (x-2)(x+2) \\Leftrightarrow (x-2)\\left[\\sqrt{%sx^2+%s} - (x+2)\\right] = 0$. \\\\ ' \
                           '+ TH1: $x-2=0 \\Leftrightarrow x=2$. \\\\ ' \
                           '+ TH2: $\\sqrt{%sx^2+%s} = x+2 \\Leftrightarrow \\begin{cases} x \\geq -2 \\\\ %sx^2+%s = (x+2)^2 \\end{cases} \\Leftrightarrow x \\in %s$. \\\\ ' \
                           'Vậy tập nghiệm $S = %s$.' % (m, n, m, n, m, n, m, n, latex(sol_can), latex(tap_nghiem))

            ########################################################################
            # Vận dụng (Câu c)
            ########################################################################
            vd_da_1_d = '\\True Tổng các nghiệm của phương trình bằng %s' % (latex(tong_nghiem))
            vd_da_1_s = 'Tổng các nghiệm của phương trình bằng %s' % (latex(tong_nghiem + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = 'Dựa vào tập nghiệm $S = %s$, ta có tổng các nghiệm là: %s. ' % (latex(tap_nghiem), ' + '.join(map(str, tap_nghiem)) + ' = ' + str(tong_nghiem))

            ########################################################################
            # Vận dụng cao (Câu d)
            ########################################################################
            if tat_ca_chan:
                vdc_da_1_d = '\\True Các nghiệm của phương trình là các số chẵn'
                vdc_da_1_s = 'Phương trình có nghiệm là số lẻ'
            else:
                vdc_da_1_d = '\\True Phương trình có nghiệm là số lẻ'
                vdc_da_1_s = 'Các nghiệm của phương trình đều là các số chẵn'

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = 'Các nghiệm của phương trình là $x \\in %s$. Ta kiểm tra tính chẵn lẻ của các nghiệm này để đưa ra kết luận.' % (latex(tap_nghiem))

            # --- Phần logic xuất bản ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

