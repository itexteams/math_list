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


def bt_dang61_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thực hiện ngẫu nhiên hóa hệ số k trong hàm cot(k*x) của đáp án đúng
                # Chọn k ngẫu nhiên từ {2, 3, 4, 5, 6} để đổi mới bài toán
                k = random.choice([2, 3, 4, 5, 6])

                # Thiết lập chuỗi hiển thị cho hàm số đúng và các bước biến đổi tương ứng
                ham_dung = 'y = \\cot %sx' % (latex(k))
                txd_dung = 'D = \\mathbb{R} \\setminus \\left\\{ \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (latex(k))
                f_am_x = 'f(-x) = \\cot(-%sx) = -\\cot %sx = -f(x)' % (latex(k), latex(k))

                # Các hàm số sai được lấy theo mẫu gốc nhưng đổi mới nhẹ hệ số nếu cần, đảm bảo giữ nguyên tính chất
                ham_sai1 = 'y = \\frac{\\sin x + 1}{\\cos x}'
                ham_sai2 = 'y = \\tan^2 x'
                ham_sai3 = 'y = |\\cot x|'

                # Câu hỏi
                noidungcauhoi = ('''Trong các hàm số sau, hàm số nào có đồ thị đối xứng qua gốc tọa độ?''')

                # Định dạng các phương án trả lời trắc nghiệm (không chứa dấu chấm ở cuối)
                da_d = ('\\True $' + str(ham_dung) + '$')
                da_s1 = '$' + str(ham_sai1) + '$'
                da_s2 = '$' + str(ham_sai2) + '$'
                da_s3 = '$' + str(ham_sai3) + '$'

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước y hệt ảnh mẫu, sử dụng %s
                loigiai = ('''Nhận xét: Hàm số lẻ có đồ thị đối xứng qua gốc tọa độ. \\\\
                           Xét hàm số $%s$. \\\\
                           Tập xác định $%s$ là tập đối xứng. Do đó $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $%s \\longrightarrow f(x)$ là hàm số lẻ $\\Rightarrow$ Chọn. \\\\
                           Xét hàm số $%s$. \\\\
                           Tập xác định $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z} \\right\\}$ là tập đối xứng. Do đó $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $f(-x) = \\frac{\\sin(-x) + 1}{\\cos(-x)} = \\frac{-\\sin x + 1}{\\cos x} \\neq \\{f(x), -f(x)\\}$. Hàm số không có tính chẵn, lẻ. \\\\
                           Xét hàm số $%s$. \\\\
                           Tập xác định $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z} \\right\\}$ là tập đối xứng. Do đó $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $f(-x) = \\tan^2(-x) = \\tan^2 x = f(x) \\longrightarrow f(x)$ là hàm số chẵn. \\\\
                           Xét hàm số $%s$. \\\\
                           Tập xác định $D = \\mathbb{R} \\setminus \\left\\{ k\\pi, k \\in \\mathbb{Z} \\right\\}$ là tập đối xứng. Do đó $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $f(-x) = |\\cot(-x)| = |\\cot x| = f(x) \\longrightarrow f(x)$ là hàm số chẵn.''' 
                           % (str(ham_dung), str(txd_dung), str(f_am_x), str(ham_sai1), str(ham_sai2), str(ham_sai3)))

            # Xuất câu trắc nghiệm đúng định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

