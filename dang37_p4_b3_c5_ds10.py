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


def bt_dang37_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số mũ n (thường chọn số lẻ để kết quả là -1 nếu a=2)
                n = 2 * randint(5, 12) + 1
                # Random giá trị cơ số a (trong hình là 2)
                a = randint(2, 3)

                # Tính giá trị biểu thức H = (1 - a)^n
                kq_val = (1 - a)**n

                # Đáp án đúng
                da = "$%s$" % (latex(kq_val))

                # Tạo các phương án sai
                s = [
                    "$%s$" % (latex((1 + a)**n)),
                    "$%s$" % (latex(-(1 + a)**n)),
                    "$1$",
                    "$-1$" if kq_val != -1 else "$%s$" % (latex(a**n))
                ]

                # Trộn các phương án
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Định dạng: H = C_n^0 - a*C_n^1 + a^2*C_n^2 - ... + a^{n-1}*C_n^{n-1} - a^n*C_n^n
                noidungcauhoi = ("Tính $H = C_{%s}^0 - %s C_{%s}^1 + %s^2 C_{%s}^2 - \\dots + %s^{%s} C_{%s}^{%s} - %s^{%s} C_{%s}^{%s}$."
                                 % (latex(n), latex(a), latex(n), latex(a), latex(n), 
                                    latex(a), latex(n-1), latex(n), latex(n-1), 
                                    latex(a), latex(n), latex(n), latex(n)))

                # Các đáp án trắc nghiệm
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ("Xét khai triển nhị thức Newton:\\\\"
                           "$\\left(1+x\\right)^{%s} = C_{%s}^0 + C_{%s}^1 x + C_{%s}^2 x^2 + \\dots + C_{%s}^{%s} x^{%s} + C_{%s}^{%s} x^{%s}$.\\\\"
                           "Chọn $x = -%s$, ta được:\\\\"
                           "$H = C_{%s}^0 + C_{%s}^1 \\left(-%s\\right) + C_{%s}^2 \\left(-%s\\right)^2 + \\dots + C_{%s}^{%s} \\left(-%s\\right)^{%s} + C_{%s}^{%s} \\left(-%s\\right)^{%s}$.\\\\"
                           "$H = C_{%s}^0 - %s C_{%s}^1 + %s^2 C_{%s}^2 - \\dots + %s^{%s} C_{%s}^{%s} - %s^{%s} C_{%s}^{%s}$.\\\\"
                           "Do đó $H = \\left(1 - %s\\right)^{%s} = \\left(-%s\\right)^{%s} = %s$."
                           % (latex(n), latex(n), latex(n), latex(n), latex(n), latex(n-1), latex(n-1), latex(n), latex(n), latex(n),
                              latex(a),
                              latex(n), latex(n), latex(a), latex(n), latex(a), latex(n), latex(n-1), latex(a), latex(n-1), latex(n), latex(n), latex(a), latex(n),
                              latex(n), latex(a), latex(n), latex(a), latex(n), latex(a), latex(n-1), latex(n), latex(n-1), latex(a), latex(n), latex(n), latex(n),
                              latex(a), latex(n), latex(a-1), latex(n), latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

