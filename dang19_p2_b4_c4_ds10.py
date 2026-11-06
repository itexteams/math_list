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


def bt_dang19_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')


            a_val = random.randint(1, 3) # Ví dụ: 1
            b_val = random.randint(a_val + 1, a_val + 4) # Ví dụ: 2


            diff = b_val - a_val
            x2_num = diff**2 + 4 * a_val * b_val
            x2_den = 8 * diff
            x2_val = Rational(x2_num, x2_den)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $\\sqrt{x(x-%s)} + \\sqrt{x(x+%s)} = 2\\sqrt{x^2}$.''' 
                             % (latex(a_val), latex(b_val)))

            ########################################################################
            # Nhận biết 
            ########################################################################
            nb_da_1_d = '\\True $x=0$ là nghiệm của phương trình'
            nb_da_1_s = '$x=0$ không là nghiệm của phương trình'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Điều kiện xác định của phương trình là: 
            $\\begin{cases} x(x-%s) \\ge 0 \\\\ x(x+%s) \\ge 0 \\\\ x^2 \\ge 0 \\end{cases} 
            \\Leftrightarrow \\begin{cases} x \\le 0 \\vee x \\ge %s \\\\ x \\le -%s \\vee x \\ge 0 \\\\ x \\in \\mathbb{R} \\end{cases} 
            \\Leftrightarrow \\left[ \\begin{aligned} & x = 0 \\\\ & x \\ge %s \\end{aligned} \\right.$. \\\\
            Với $x=0$, thay vào phương trình ta được $0+0=0$ (đúng). Vậy $x=0$ là một nghiệm của phương trình.''' 
            % (latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(a_val)))

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = '\\True Phương trình có $2$ nghiệm phân biệt'
            th_da_1_s = 'Phương trình có duy nhất $1$ nghiệm'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Với $x \\ge %s$, phương trình tương đương với: \\\\
            $\\sqrt{x}(\\sqrt{x-%s} + \\sqrt{x+%s}) = 2\\sqrt{x^2} \\Leftrightarrow \\sqrt{x}(\\sqrt{x-%s} + \\sqrt{x+%s}) = 2x$ \\\\
            Vì $x \\ge %s > 0$, chia cả hai vế cho $\\sqrt{x}$ ta được: $\\sqrt{x-%s} + \\sqrt{x+%s} = 2\\sqrt{x}$. \\\\
            Bình phương hai vế: $(x-%s) + (x+%s) + 2\\sqrt{(x-%s)(x+%s)} = 4x$ \\\\
            $\\Leftrightarrow 2\\sqrt{(x-%s)(x+%s)} = 2x - %s \\Leftrightarrow \\sqrt{(x-%s)(x+%s)} = x - %s$. \\\\
            $\\Leftrightarrow \\begin{cases} x \\ge %s \\\\ x^2 + %sx - %s = x^2 - %sx + %s \\end{cases} \\Leftrightarrow x = %s$ (thỏa mãn $x \\ge %s$). \\\\
            Vậy phương trình có hai nghiệm là $x=0$ và $x=%s$.''' 
            % (latex(a_val), latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(a_val), latex(a_val), latex(b_val),
                latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(diff),
                latex(a_val), latex(b_val), latex(Rational(diff, 2)), latex(Rational(diff, 2)),
                latex(diff), latex(a_val * b_val), latex(diff), latex(Rational(diff**2, 4)),
                latex(x2_val), latex(a_val), latex(x2_val)))

            ########################################################################
            # Vận dụng
            ########################################################################
            tong_nghiem = x2_val
            vd_da_1_d = '\\True Tổng các nghiệm của phương trình bằng $%s$' % (latex(tong_nghiem))
            vd_da_1_s = 'Tổng các nghiệm của phương trình bằng $%s$' % (latex(tong_nghiem + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Các nghiệm của phương trình là $x_1 = 0$ và $x_2 = %s$. \\\\
            Tổng các nghiệm là: $0 + %s = %s$.''' % (latex(x2_val), latex(x2_val), latex(tong_nghiem)))

            ########################################################################
            # Vận dụng cao
            ########################################################################
            nghiem_max = x2_val
            so_sanh = int(nghiem_max) + 1
            vdc_da_1_d = '\\True Nghiệm lớn nhất của phương trình nhỏ hơn $%s$' % (so_sanh)
            vdc_da_1_s = 'Nghiệm lớn nhất của phương trình lớn hơn $%s$' % (so_sanh)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Nghiệm lớn nhất của phương trình là $x = %s \\approx %s$. \\\\
            Do đó nghiệm lớn nhất nhỏ hơn $%s$.''' % (latex(x2_val), round(float(x2_val), 2), so_sanh))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    shuffled_answers = answers
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

