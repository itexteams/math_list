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


def bt_dang26_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các giá trị: m + căn bậc 3 của n
                # m là hằng số, n là số trong căn bậc 3
                m = random.randint(1, 3) 
                n = random.randint(2, 4)
                n2 = n**2

                # Tính các hệ số dựa trên khai triển (m + n^(1/3))^4
                # (m + x)^4 = m^4 + 4*m^3*x + 6*m^2*x^2 + 4*m*x^3 + x^4
                # Với x = n^(1/3) => x^3 = n, x^4 = n*n^(1/3)
                # Biểu thức = (m^4 + 4*m*n) + (4*m^3 + n)*n^(1/3) + (6*m^2)*n^(2/3)

                a0 = m**4 + 4*m*n
                a1 = 4*m**3 + n
                a2 = 6*m**2
                kq = a1 * a2

                # Các đáp án trắc nghiệm
                da = '$a_1 a_2 = %s$' % (latex(kq))

                # Tạo danh sách các phương án sai ngẫu nhiên
                s = [
                    '$a_1 a_2 = %s$' % (latex(kq + 10)),
                    '$a_1 a_2 = %s$' % (latex(kq - 8)),
                    '$a_1 a_2 = %s$' % (latex(kq + 12)),
                    '$a_1 a_2 = %s$' % (latex(a1 + a2)),
                    '$a_1 a_2 = %s$' % (latex(a1 * a2 + 4)),
                    '$a_1 a_2 = %s$' % (latex(a1 * a2 - 6)),
                ]

                # Loại bỏ đáp án đúng nếu lỡ trùng trong danh sách phương án sai
                s = [item for item in s if item != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Biết $\\left( %s + \\sqrt[3]{%s} \\right)^4 = a_0 + a_1\\sqrt[3]{%s} + a_2\\sqrt[3]{%s}$. Tính tích $\\left( a_1 a_2 \\right)$.'''
                                 %(latex(m), latex(n), latex(n), latex(n2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Các thành phần trung gian để trình bày lời giải
                m4 = m**4
                four_m3 = 4 * (m**3)
                six_m2 = 6 * (m**2)
                four_m_n = 4 * m * n

                loigiai = ('''Ta có $\\left( %s + \\sqrt[3]{%s} \\right)^4 = %s^4 + 4 \\cdot %s^3 \\left( \\sqrt[3]{%s} \\right)^1 + 6 \\cdot %s^2 \\left( \\sqrt[3]{%s} \\right)^2 + 4 \\cdot %s^1 \\left( \\sqrt[3]{%s} \\right)^3 + \\left( \\sqrt[3]{%s} \\right)^4$\\\\
                             $= %s + %s\\sqrt[3]{%s} + %s\\sqrt[3]{%s} + %s + %s\\sqrt[3]{%s}$ \\\\
                             $= %s + %s\\sqrt[3]{%s} + %s\\sqrt[3]{%s}$. \\\\
                             Suy ra $a_1 = %s, a_2 = %s$. \\\\
                             Vậy $a_1 a_2 = %s \\cdot %s = %s$.'''
                           %(latex(m), latex(n), latex(m), latex(m), latex(n), latex(m), latex(n), latex(m), latex(n), latex(n),
                             latex(m4), latex(four_m3), latex(n), latex(six_m2), latex(n2), latex(four_m_n), latex(n), latex(n),
                             latex(a0), latex(a1), latex(n), latex(a2), latex(n2),
                             latex(a1), latex(a2), latex(a1), latex(a2), latex(kq)
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

