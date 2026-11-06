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


def bt_dang46_p4_b2_c6_ds10(self):
            #Khai báo biến
            # w: số quả cầu trắng, b: số quả cầu đen, k: số quả lấy ra
            w = randint(4, 6)
            b = randint(5, 7)
            k = 3
            tong = w + b

            # Tính toán các giá trị tổ hợp
            omega = binomial(tong, k)
            cw = binomial(w, k)
            cb = binomial(b, k)

            # Xác suất từng trường hợp
            p1_tu = cw
            p2_tu = cb
            tong_tu = p1_tu + p2_tu

            # Đáp án đúng dưới dạng phân số
            kq_phanso = Rational(tong_tu, omega)

            # B4: Tạo các phương án sai (không trùng đáp án đúng)
            s = set()
            while len(s) < 3:
                # Tạo các tử số ngẫu nhiên để làm phương án nhiễu
                sai_tu = randint(1, omega - 1)
                if sai_tu != tong_tu:
                    phuong_an_sai = "$%s$" % (latex(Rational(sai_tu, omega)))
                    s.add(phuong_an_sai)

            list_sai = list(s)

            # Nội dung câu hỏi
            noidungcauhoi = ("Một hộp chứa $%s$ quả cầu trắng và $%s$ quả cầu đen, lấy ngẫu nhiên $%s$ quả. Tính xác suất để $%s$ quả cùng màu."
                             % (latex(w), latex(b), latex(k), latex(k)))

            # Các đáp án
            da_d = "\\True $%s$" % (latex(kq_phanso))
            da_s1 = list_sai[0]
            da_s2 = list_sai[1]
            da_s3 = list_sai[2]

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = ("Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$. \\\\"
                       "Xác suất để $%s$ quả lấy ra cùng màu: \\\\"
                       "TH1. Ba quả lấy ra cùng màu trắng: $\\frac{C_{%s}^{%s}}{C_{%s}^{%s}} = \\frac{%s}{%s}$. \\\\"
                       "TH2. Ba quả lấy ra cùng màu đen: $\\frac{C_{%s}^{%s}}{C_{%s}^{%s}} = \\frac{%s}{%s}$. \\\\"
                       "Vậy xác suất để $%s$ quả lấy ra có cùng màu là $\\frac{C_{%s}^{%s}}{C_{%s}^{%s}} + \\frac{C_{%s}^{%s}}{C_{%s}^{%s}} = \\frac{%s}{%s} + \\frac{%s}{%s} = %s$."
                       % (latex(tong), latex(k), latex(omega),
                          latex(k),
                          latex(w), latex(k), latex(tong), latex(k), latex(cw), latex(omega),
                          latex(b), latex(k), latex(tong), latex(k), latex(cb), latex(omega),
                          latex(k),
                          latex(w), latex(k), latex(tong), latex(k),
                          latex(b), latex(k), latex(tong), latex(k),
                          latex(cw), latex(omega), latex(cb), latex(omega), latex(kq_phanso)
                          ))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

