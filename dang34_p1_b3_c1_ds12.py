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


def bt_dang34_p1_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số của đường tiệm cận xiên mục tiêu: y = m*x + n
                m = random.choice([1, 2])
                n = random.choice([-2, -1, 1, 2])

                line_asym = m*x + n
                str_line = latex(line_asym)

                # 1. Phương án đúng: y = (m*x + n) + k/(c*x + d)
                c = random.choice([1, 2])
                d = random.choice([-2, -1, 1, 2])
                k = random.choice([-3, -2, -1, 1, 2, 3])

                P_true = expand((m*x + n)*(c*x + d) + k)
                Q_true = c*x + d
                str_da = '\\frac{%s}{%s}' % (latex(P_true), latex(Q_true))

                # 2. Phương án sai 1: Bậc tử < Bậc mẫu (Có tiệm cận ngang y = 0)
                w1_num = expand(random.choice([1, 2])*x + random.choice([-2, -1, 1, 2]))
                w1_den = expand(x**2 + random.randint(1, 3))
                str_das1 = '\\frac{%s}{%s}' % (latex(w1_num), latex(w1_den))

                # 3. Phương án sai 2: Hàm vô tỷ dạng chứa căn thức bậc hai
                p_val = random.choice([-4, -2, 2, 4])
                q_val = p_val**2 // 4 + random.randint(1, 4)
                str_das2 = '\\sqrt{%s}' % latex(x**2 + p_val*x + q_val)

                # 4. Phương án sai 3: Hàm phân thức bậc 2 trên bậc 1 nhưng có tiệm cận xiên khác
                n_wrong = n + random.choice([-2, -1, 1, 2])
                while n_wrong == n:
                    n_wrong = n + random.choice([-2, -1, 1, 2])
                c3 = random.choice([1, 2])
                d3 = random.choice([-2, -1, 1, 2])
                k3 = random.choice([-2, -1, 1, 2])
                w3_num = expand((m*x + n_wrong)*(c3*x + d3) + k3)
                w3_den = c3*x + d3
                str_das3 = '\\frac{%s}{%s}' % (latex(w3_num), latex(w3_den))

                # Các đáp án trắc nghiệm
                da = '$y = %s$' % str_da
                das1 = '$y = %s$' % str_das1
                das2 = '$y = %s$' % str_das2
                das3 = '$y = %s$' % str_das3

                # Câu hỏi
                noidungcauhoi = ('''Đường thẳng $y = %s$ là tiệm cận xiên của đồ thị hàm số nào dưới đây?''' % str_line)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                str_rem = latex(k)
                str_rem_den = latex(Q_true)
                loigiai = ('''Ta xét hàm số $y = \\frac{%s}{%s}$. \\\\
            Thực hiện phép chia tử thức cho mẫu thức, ta được: \\\\
            $y = %s + \\frac{%s}{%s}$. \\\\
            Vì $\\lim\\limits_{x \\to \\pm\\infty} \\frac{%s}{%s} = 0$ nên đường thẳng $y = %s$ là tiệm cận xiên của đồ thị hàm số này. \\\\
            Các phương án còn lại đều không có tiệm cận xiên là $y = %s$.''' % (
                    latex(P_true), latex(Q_true), str_line, str_rem, str_rem_den,
                    str_rem, str_rem_den, str_line, str_line
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

