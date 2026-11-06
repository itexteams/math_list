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


def bt_dang16_p4_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x = symbols('x') 

                # --- Thông số được Random ---
                # Độ cao ban đầu (H)
                H_list = [50, 80, 100, 120, 200]
                H = random.choice(H_list)
                # Mẫu số của công bội (q_val > 1)
                q_val_list = [2, 3, 4, 5]
                q_val = random.choice(q_val_list)

                # --- Tính toán các giá trị phụ thuộc ---
                q_frac = Rational(1, q_val) # Công bội q
                h1_val = Rational(H, q_val) # Độ cao lần nảy thứ nhất
                # Tổng quãng đường vô hạn S = H * (q_val + 1) / (q_val - 1)
                tong_sn = Rational(H * (q_val + 1), q_val - 1)
                Sigma_val = Rational(H, q_val - 1) # Tổng cấp số nhân lùi vô hạn Sigma = H * q / (1-q) = H / (q_val - 1)
                # Nội dung câu hỏi
                noidungcauhoi = ('''Từ độ cao $%s\\text{ m}$, ta thả một quả bóng cao su xuống đất. Giả sử sau mỗi lần chạm đất, quả bóng này nảy lên một độ cao bằng $\\frac{1}{%s}$ độ cao mà quả bóng đạt được trước đó. Gọi $h_n$ là độ cao quả bóng đạt được ở lần nảy thứ $n$.\\\\'''      
                                 'a) Tìm số hạng tổng quát của dãy số $\\left( h_n \\right)$ \\\\ \n'
                                 'b) Tính giới hạn của dãy số $\\left( h_n \\right)$ và nêu ý nghĩa giới hạn của dãy số $\\left( h_n \\right)$ \\\\ \n'
                                 'c) Tính tổng quãng đường quả bóng di chuyển được nếu quá trình nảy tiếp tục diễn ra mãi \\\\ \n'
                                 %(latex(H), latex(q_val)
                                 ))

                # Nội dung lời giải
                loigiai = (    '\\begin{enumEX}[a)]{1} \n'
                                '\\item  Dãy số $\\left( h_n \\right)$ là cấp số nhân với $h_1 = \\frac{%s}{%s}$ và công bội $q = \\frac{1}{%s}$. \\\\'
                                'Số hạng tổng quát là $h_n = h_1 \\cdot q^{n-1} = \\frac{%s}{%s} \\cdot \\left( \\frac{1}{%s} \\right)^{n-1} = \\frac{%s}{%s^n}$. \n'
                                '\\item  Ta có $\\lim h_n = \\lim \\frac{%s}{%s^n}$. Vì $\\left| \\frac{1}{%s} \\right| < 1$, nên $\\lim \\left( \\frac{1}{%s} \\right)^n = 0$. \n'
                                'Do đó $\\lim h_n = %s \\cdot 0 = 0$.\\\\'
                                'Ý nghĩa: Độ cao quả bóng đạt được sau mỗi lần nảy ngày càng nhỏ dần về $0$.'
                                '\\item  Tổng quãng đường $S = %s + 2 \\left( h_1 + h_2 + h_3 + \\dots \\right)$. \\\\'
                                'Tổng của cấp số nhân lùi vô hạn $\\Sigma = h_1 + h_2 + h_3 + \\dots$ là $\\Sigma = \\frac{h_1}{1-q} = \\frac{\\frac{%s}{%s}}{1 - \\frac{1}{%s}} = \\frac{\\frac{%s}{%s}}{\\frac{%s-1}{%s}} = %s$. \\\\'
                                'Tổng quãng đường: $S = %s + 2 \\cdot %s = %s + %s = %s\\text{ m}$.'
                                '\\end{enumEX} \n'

                           %(latex(H), latex(q_val), latex(q_val),
                             latex(H), latex(q_val), latex(q_val), latex(H), latex(q_val),

                             latex(H), latex(q_val), latex(q_val), latex(q_val), 
                             latex(H),

                             latex(H), 
                             latex(H), latex(q_val), latex(q_val), 
                             latex(H), latex(q_val), latex(q_val), latex(q_val), 
                             latex(Sigma_val),
                             latex(H), latex(Sigma_val), latex(H), latex(2*Sigma_val), 
                             latex(tong_sn.numerator)
                           ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

