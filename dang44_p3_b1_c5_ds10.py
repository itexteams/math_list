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


def bt_dang44_p3_b1_c5_ds10(self):
            # Khai báo biến
            # Biến n đại diện cho số lượng màu sắc (từ 5 đến 10 màu để đảm bảo logic bài toán)
            n = random.randint(5, 10)

            # B1 & B2: Tính toán lời giải chi tiết dựa trên logic đề bài
            # Trường hợp 1: AB và CD khác màu
            c1_ab = n
            c1_bc = n - 1
            c1_cd = n - 2 # Khác BC và khác AB
            c1_ad = n - 2 # Khác AB và khác CD
            c1_total = c1_ab * c1_bc * c1_cd * c1_ad

            # Trường hợp 2: AB và CD cùng màu
            c2_ab = n
            c2_bc = n - 1
            c2_cd = 1     # Cùng màu AB
            c2_ad = n - 1 # Chỉ cần khác màu (AB=CD)
            c2_total = c2_ab * c2_bc * c2_cd * c2_ad

            # Tổng số cách
            ket_qua = c1_total + c2_total

            # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            s_sai = set()
            while len(s_sai) < 3:
                # Tạo các đáp án sai bằng cách thay đổi các hệ số hoặc cộng trừ ngẫu nhiên
                sai = ket_qua + random.choice([-150, -100, -50, 50, 100, 150, 200])
                if sai > 0 and sai != ket_qua:
                    s_sai.add('$%s$' % latex(sai))

            list_sai = list(s_sai)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tô màu các cạnh của hình vuông $ABCD$ bởi $%s$ màu khác nhau sao cho mỗi cạnh được tô bởi một màu và hai cạnh kề nhau thì tô bởi hai màu khác nhau. Hỏi có bao nhiêu cách tô?'''
                             % (latex(n)))

            # Các đáp án
            da_d = ('\\True $%s$' % latex(ket_qua))
            da_s1 = list_sai[0]
            da_s2 = list_sai[1]
            da_s3 = list_sai[2]

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết (không viết tắt, trình bày y hệt ảnh mẫu)
            loigiai = ('''Trường hợp 1: Tô cạnh $AB$ và $CD$ khác màu: \\\\
                         Số cách tô cạnh $AB$: $%s$ cách. \\\\
                         Số cách tô cạnh $BC$: $%s$ cách. \\\\
                         Số cách tô cạnh $CD$: $%s$ cách. \\\\
                         Số cách tô cạnh $AD$: $%s$ cách. \\\\
                         Theo quy tắc nhân ta có: $%s \\cdot %s \\cdot %s \\cdot %s = %s$ cách tô cạnh $AB$ và $CD$ khác màu. \\\\
                         Trường hợp 2: Tô cạnh $AB$ và $CD$ cùng màu: \\\\
                         Số cách tô cạnh $AB$: $%s$ cách. \\\\
                         Số cách tô cạnh $BC$: $%s$ cách. \\\\
                         Số cách tô cạnh $CD$: $1$ cách. \\\\
                         Số cách tô cạnh $AD$: $%s$ cách. \\\\
                         Theo quy tắc nhân ta có: $%s \\cdot %s \\cdot 1 \\cdot %s = %s$ cách tô cạnh $AB$ và $CD$ cùng màu. \\\\
                         Vậy số cách tô màu thỏa đề bài là: $%s + %s = %s$ cách.'''
                       % (latex(c1_ab), latex(c1_bc), latex(c1_cd), latex(c1_ad),
                          latex(c1_ab), latex(c1_bc), latex(c1_cd), latex(c1_ad), latex(c1_total),
                          latex(c2_ab), latex(c2_bc), latex(c2_ad),
                          latex(c2_ab), latex(c2_bc), latex(c2_ad), latex(c2_total),
                          latex(c1_total), latex(c2_total), latex(ket_qua)
                          ))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(ket_qua))

            # Xuất câu trắc nghiệm (không dùng raw string r, sử dụng double backslash)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

