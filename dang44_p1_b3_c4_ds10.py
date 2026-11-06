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


def bt_dang44_p1_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1: Random nghiệm của Delta' = 0 là các số nguyên để bài toán đẹp

                m1_val = random.randint(-5, -1)
                m2_val = 1 - m1_val


                a = -(m1_val * m2_val)


                m_test = m2_val
                K = 8*(m_test**3) - 6*(m_test**2) - 6*a*m_test

                m = symbols('m')

                # Kết quả cuối cùng: m <= m1_val hoặc m = m2_val
                kq_str = "m \\le %s \\text{ hoặc } m = %s" % (latex(m1_val), latex(m2_val))
                da = '$%s$' % kq_str

                # B3: Tạo các phương án sai (không trùng đáp án đúng)
                s = [
                    '$m \\le %s$' % latex(m2_val),
                    '$m \\ge %s$' % latex(m2_val),
                    '$m \\le %s$' % latex(m1_val),
                    '$m \\le %s \\text{ hoặc } m = %s$' % (latex(m1_val - 1), latex(m2_val)),
                    '$%s \\le m \\le %s$' % (latex(m1_val), latex(m2_val)),
                    '$m < %s$' % latex(m1_val)
                ]
                if da in s: s.remove(da)
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # B4: Nội dung câu hỏi
                noidungcauhoi = ('''Giá trị của tham số $m$ để phương trình $x^2 - 2mx + m + %s = 0$ có hai nghiệm $x_1, x_2$ thỏa mãn $x_1^3 + x_2^3 \\le %s$ là'''
                                 % (latex(a), latex(K)))

                # B5: Nội dung lời giải chi tiết (không viết tắt)
                # Tính toán các hệ số cho đa thức (m-m2)(8m^2 + ...)
                # f(m) = 8m^3 - 6m^2 - 6am - K. Chia cho (m - m_test)
                # 8m^3 - 6m^2 - 6am - K = (m - m2)(8m^2 + (8*m2 - 6)m + ...)
                h_b = 8 * m2_val - 6
                h_c = K // -m2_val # Vì f(m2)=0 nên chia hết

                loigiai = ('''Phương trình có nghiệm khi $\\Delta' \\ge 0 \\Leftrightarrow m^2 - (m + %s) \\ge 0 \\Leftrightarrow m^2 - m - %s \\ge 0 \\Leftrightarrow \\left[ \\begin{array}{l} m \\ge %s \\\\ m \\le %s \\end{array} \\right. \\quad (1)$.\\\\
            Theo định lý Viète ta có $\\begin{cases} x_1 + x_2 = 2m \\\\ x_1x_2 = m + %s \\end{cases}$.\\\\
            Ta có $x_1^3 + x_2^3 \\le %s \\Leftrightarrow (x_1+x_2)^3 - 3x_1x_2(x_1+x_2) \\le %s$\\\\
            $\\Leftrightarrow (2m)^3 - 3(m + %s)(2m) \\le %s \\Leftrightarrow 8m^3 - 6m^2 - %sm - %s \\le 0$\\\\
            $\\Leftrightarrow (m - %s)(8m^2 + %sm + %s) \\le 0$\\\\
            Vì $8m^2 + %sm + %s > 0$ với mọi $m$ nên bất phương trình tương đương với:\\\\
            $m - %s \\le 0 \\Leftrightarrow m \\le %s$.\\\\
            Kết hợp với điều kiện (1), ta chọn các giá trị $m$ thỏa mãn là $m \\le %s$ hoặc $m = %s$.'''
                           % (latex(a), latex(a), latex(m2_val), latex(m1_val),
                              latex(a), latex(K), latex(K),
                              latex(a), latex(K), latex(6*a), latex(K),
                              latex(m2_val), latex(h_b), latex(abs(h_c)),
                              latex(h_b), latex(abs(h_c)),
                              latex(m2_val), latex(m2_val),
                              latex(m1_val), latex(m2_val)
                              ))

            # B6: Xuất nội dung theo cấu trúc mẫu
            da_d = ('\\True ' + str(da))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

