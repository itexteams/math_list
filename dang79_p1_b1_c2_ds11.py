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


def bt_dang79_p1_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tham số a trong biểu thức n(n+a). Bài gốc a = 3
                a = random.randint(2, 5)

                # Tính toán các thành phần cần thiết để đưa vào chuỗi
                # Tổng giới hạn của cấp số: 1/a * (1 + 1/2 + ... + 1/a)
                sum_str_list = []
                for i in range(1, a+1):
                    if i == 1:
                        sum_str_list.append("1")
                    else:
                        sum_str_list.append("\\frac{1}{%s}" % i)
                sum_str = " + ".join(sum_str_list)
                limit_val = sum([Rational(1, i) for i in range(1, a+1)]) * Rational(1, a)

                # Các đáp án trắc nghiệm
                da_d = '\\True Dãy số $(u_n)$ bị chặn'
                da_s1 = 'Dãy số $(u_n)$ bị chặn trên và không bị chặn dưới'
                da_s2 = 'Dãy số $(u_n)$ bị chặn dưới và không bị chặn trên'
                da_s3 = 'Dãy số $(u_n)$ không bị chặn'

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Câu hỏi
                noidungcauhoi = ('''Cho dãy số $(u_n)$, với $u_n = \\frac{1}{1.%s} + \\frac{1}{2.%s} + \\dots + \\frac{1}{n(n+%s)}$, $\\forall n = 1; 2; 3 \\dots$. Mệnh đề nào sau đây đúng?'''
                                 %(latex(1+a), latex(2+a), latex(a)))

                # Nội dung lời giải
                loigiai = ('''Ta có: $u_{n+1} - u_n = \\frac{1}{(n+1)(n+%s)} > 0$, $\\forall n \\ge 1$. Do đó, $(u_n)$ là dãy số tăng. Suy ra $(u_n)$ bị chặn dưới bởi $u_1 = \\frac{1}{%s}$.\\\\
                Mặt khác, xét số hạng tổng quát: $\\frac{1}{k(k+%s)} = \\frac{1}{%s} \\left( \\frac{1}{k} - \\frac{1}{k+%s} \\right)$.\\\\
                Khi đó:\\\\
                $u_n = \\frac{1}{%s} \\left( 1 - \\frac{1}{%s} + \\frac{1}{2} - \\frac{1}{%s} + \\dots + \\frac{1}{n} - \\frac{1}{n+%s} \\right)$\\\\
                $u_n = \\frac{1}{%s} \\left[ \\left( %s \\right) - \\left( \\frac{1}{n+1} + \\dots + \\frac{1}{n+%s} \\right) \\right] < \\frac{1}{%s} \\left( %s \\right) = %s$.\\\\
                Suy ra dãy số $(u_n)$ bị chặn trên.\\\\
                Vậy dãy số $(u_n)$ bị chặn.'''
                %(latex(a+1), latex(a+1),
                  latex(a), latex(a), latex(a),
                  latex(a), latex(1+a), latex(2+a), latex(a),
                  latex(a), str(sum_str), latex(a), latex(a), str(sum_str), latex(limit_val)))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

